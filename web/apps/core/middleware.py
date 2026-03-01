from typing import Any
from .navigation import MENU


class SidebarMenuMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        user = request.user

        request.sidebar_menu = []

        if not user.is_authenticated:
            return self.get_response(request)
        user_perms = user.get_all_permissions()

        def has_permissions(item):
            perm = item.get('perm')
            return user.is_superuser or perm is None or perm in user_perms
        
        filtered_menu = []

        for item in MENU:
            if item.get('children'):
                filtered_children = [
                    child for child in item['children'] if has_permissions(child)
                ]

                if filtered_children:
                    filtered_menu.append({
                        **item,
                        'children': filtered_children
                    })
            else:
                if has_permissions(item):
                    filtered_menu.append(item)
        
        # Função para marcar itens ativos
        def mark_active(menu_items, current_path):
            for item in menu_items:
                if 'children' in item:
                    has_active_child = mark_active(item['children'], current_path)
                    item['active'] = has_active_child
                else:
                    # Para itens sem filhos, verifica se o path corresponde exatamente
                    item['active'] = current_path == item['url']
        
        mark_active(filtered_menu, request.path_info)
        request.sidebar_menu = filtered_menu
        return self.get_response(request)

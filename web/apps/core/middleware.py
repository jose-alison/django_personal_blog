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
        request.sidebar_menu = filtered_menu
        return self.get_response(request)

from django.conf import settings

def blog_info(request):
    return {
        'blog_name': settings.BLOG_NAME
    }

def sidebar_menu(request):
    return {
        'sidebar_menu': getattr(request, 'sidebar_menu', [])
    }
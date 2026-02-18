MENU = [
    {
        "name": "Home",
        "url": "/",
        "icon": "home",
        "perm": None,
    },
    {
        "name": "Users",
        "children": [
            {
                "name": "List Users",
                "url": "/users/",
                "icon": "users",
                "perm": "users.view_user",
            },
            {
                "name": "Create User",
                "url": "/users/new/",
                "icon": "user-plus",
                "perm": "users.add_user",
            },
        ],
    },
]

import flet
menu_items = [
    {"name": "Home", "icon": flet.icons.HOME,"url":"/"},
    {"name": "Settings", "icon":flet.icons.SETTINGS,"url":"/settings"},
    {"name":"Logout","icon":flet.icons.LOGOUT,"url":"/logout"}
    # Add more menu items as needed
]

if __name__=='__main__':
    for item in menu_items:
        print(item['url'])
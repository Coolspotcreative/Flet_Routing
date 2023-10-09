import flet
from Template.sidebar_items import menu_items




class Navbar(flet.UserControl):
    def build(self):
        navbar = flet.Container(
            bgcolor='white',
            height=50,
            expand=True,
            content=flet.ResponsiveRow(
                controls=[
                    flet.Column(
                        col=10,
                        controls=[
                            flet.Container(
                                bgcolor='red',
                                expand=True,
                            ),
                        ]
                    ),
                    flet.Column(
                        col=2,
                        controls=[
                            flet.ResponsiveRow(
                                controls=[
                                    flet.Container(col=4,alignment=flet.alignment.center,margin=flet.margin.only(top=10),content=flet.Icon(
                                        flet.icons.NOTIFICATIONS,
                                        size=30,
                                        color='blue'
                                    )),
                                    flet.Container(col=4,alignment=flet.alignment.center,margin=flet.margin.only(top=10),content=flet.Icon(
                                        flet.icons.WECHAT,
                                        size=30,
                                        color='blue'
                                    )),
                                    flet.Container(col=4,alignment=flet.alignment.center,margin=flet.margin.only(top=10),content=flet.Icon(
                                        flet.icons.PERSON,
                                        size=30,
                                        color='blue',
                                    ))
                                ]
                            )
                        ]
                    )
                ]
            ),
        )
        return navbar
    
            

        
class Sidebar(flet.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page=page
        self.menu_items = menu_items
    def on_hover(self,e):
        e.control.bgcolor = "blue" if e.data == "true" else "transparent"
        e.control.update()
    def clicked(self,e,url):
        self.page.go(url)
        print(url+ ' was clicked')
    def generate_sidebar(self):
        sidebar_items = []
        for item in self.menu_items:
            url=item['url']
            print(url)
            sidebar_item = flet.Column(
                col=12,
                spacing=0,
                expand=True,
                controls=[
                    flet.Container(
                        on_hover=self.on_hover,
                        on_click=lambda e, url=url: self.clicked(e, url),

                        height=75,
                        content=flet.Container(
                            padding=flet.padding.only(top=25),
                            expand=True,
                            content=flet.ResponsiveRow(
                                controls=[
                                    flet.Column(
                                        col={"sm": 12, "md": 4, "xl": 4},
                                        controls=[
                                            flet.Container(
                                                alignment=flet.alignment.center_right,
                                                content=flet.Icon(
                                                    item["icon"],
                                                    size=25,
                                                    color='white'
                                                )
                                            )
                                        ]
                                    ),
                                    flet.Column(
                                        col={"sm": 12, "md": 8, "xl": 8},
                                        controls=[
                                            flet.Container(
                                                alignment=flet.alignment.center_left,
                                                content=flet.Text(value=item["name"], size=14, color='white')
                                            )
                                        ]
                                    )
                                ]
                            )
                        )
                    ),
                ]
            )


            sidebar_items.append(sidebar_item)
        return sidebar_items  # Return the list of sidebar items
        
    def build(self):
        generated_sidebar_items=self.generate_sidebar()
        sidebar = flet.ResponsiveRow(
            controls=[
                # Branding top left corner
                flet.Container(
                    border=flet.border.only(right=flet.BorderSide(width=2,color='white')),
                    expand=True,
                    content=flet.Column(
                        col=12,
                        expand=True,
                        controls=[
                            # Divider under branding
                            flet.ResponsiveRow(
                                vertical_alignment=flet.CrossAxisAlignment.CENTER,
                                controls=[
                                    flet.Container(
                                        margin=flet.margin.only(top=10,bottom=0),
                                        padding=flet.padding.only(left=10,right=10),
                                        content=flet.Image(src='../assets/logo.png')
                                    )
                                    # Sidebar menu items container
                                    # Use a for loop to add generated_sidebar_items
                                ] + generated_sidebar_items  # Add the generated sidebar items directly
                            )
                        ]
                    )
                )
            ]
        )

        return sidebar
    
class ProgressRing:
    def build(slef):
        progress_ring=flet.Column(
            alignment='center',
            controls=[
                flet.Text("Indeterminate cicrular progress", style="headlineSmall",text_align='center'),
                flet.Column(
                    [flet.ProgressRing(), flet.Text("I'm going to run for ages...")],
                    horizontal_alignment=flet.CrossAxisAlignment.CENTER,
                )
            ]
        )
        return progress_ring
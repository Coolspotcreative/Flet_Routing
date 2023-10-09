import flet
import Widgets.components
def main(page:flet.Page):
    sidebar=Widgets.components.Sidebar(page)
    page.title='Routing Test'
    def route_change(route):
        page.views.clear()
        page.views.append(
            flet.View(
                "/",
                [
                    flet.ResponsiveRow(
                        expand=True,
                        controls=[
                            flet.Column(
                                col=1.4,
                                controls=[
                                    flet.Container(expand=True,bgcolor=flet.colors.BLUE_GREY_900,content=sidebar)
                                ]
                            ),

                            
                        ],
                    )
                ]
            )
        )
        if page.route =='/settings':
            page.clear()
            page.views.append(
                flet.View(
                    '/settings',
                    [
                        flet.ResponsiveRow(
                        expand=True,
                        controls=[
                            flet.Column(
                                col=1.4,
                                controls=[
                                    flet.Container(expand=True,bgcolor=flet.colors.BLUE_GREY_900,content=sidebar)
                                ]
                            ),
                            flet.Column(
                                col=10.6,
                                controls=[
                                    flet.Text('Settings Page')
                                ]
                            )
                        ],
                    )

                    ]
                )
            )
            page.update()
    def view_pop(view):
        top_view=page.views[-1]
        page.go(top_view.route)
    page.on_route_change=route_change
    page.on_view_pop=view_pop
    page.go(page.route)
flet.app(target=main)

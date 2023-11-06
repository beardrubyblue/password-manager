import flet as ft


class Home(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.bgcolor = '#fff'
        self.expand = True
        self.alignment = ft.alignment.center
        self.content = ft.Container(
            alignment=ft.alignment.center,
            on_click=lambda _: page.go('/login'),
            bgcolor='white',
            content=ft.Text(
                value='Get Started',
                size=20,
                color='black'
            )
        )

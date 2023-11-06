import flet as ft
from pages.home import Home
from pages.login import Login


class Main(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        page.padding = 0
        self.page = page
        self.init()

    def init(self,):
        self.page.on_route_change = self.on_route_change
        self.page.go('/')
        # token = self.load_token()
        # if authenticate_token(token):
        #     self.page.go('/me')
        # else:
        #     self.page.go('/login')

    def on_route_change(self, route):
        new_page = {
            "/": Home,
            "/login": Login,
            # "/signup": Signup,
            # "/me": Dashboard,
            # "/forgotpassword": ForgotPassword

        }[self.page.route](self.page)

        self.page.views.clear()
        self.page.views.append(
            ft.View(route, [new_page])
        )


ft.app(target=Main, view=ft.AppView.WEB_BROWSER)

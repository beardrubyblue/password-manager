import flet as ft
from utils.validation import Validator


class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        page.padding = 0
        self.validator = Validator()
        self.alignment = ft.alignment.center
        self.expand = True
        self.bgcolor = '#4e73df'

        self.email_box = ft.Container(
            content=ft.TextField(
                border=ft.InputBorder.NONE,
                content_padding=ft.padding.only(
                    top=0, bottom=0, right=20, left=20),
                hint_style=ft.TextStyle(
                    size=12, color='#858796'
                ),
                hint_text='Enter email address...',
                cursor_color='#858796',
                text_style=ft.TextStyle(
                    size=14,
                    color='black',
                ),

            ),
        )
        self.content = ft.Column(
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    width=500,
                    padding=40,
                    bgcolor='white',
                    content=ft.Column(

                        controls=[
                            ft.Row([ft.Text(value="Welcome", size=16, color='black')], alignment=ft.MainAxisAlignment.CENTER),
                            self.email_box
                        ]

                    )

                )
            ]
        )
        # self.email_box = ft.Container(
        #     content=ft.TextField(
        #         border=ft.InputBorder.NONE,
        #         content_padding=ft.padding.only(
        #             top=0, bottom=0, right=20, left=20),
        #         hint_style=ft.TextStyle(
        #             size=12, color='#858796'
        #         ),
        #         hint_text='Enter email address...',
        #         cursor_color='#858796',
        #         text_style=ft.TextStyle(
        #             size=14,
        #             color='black',
        #         ),
        #
        #     ),
        #     border=ft.border.all(width=1, color='#bdcbf4'),
        #     border_radius=30
        # )
        #
        # self.password_box = ft.Container(
        #     content=ft.TextField(
        #         border=ft.InputBorder.NONE,
        #         content_padding=ft.padding.only(
        #             top=0, bottom=0, right=20, left=20),
        #         hint_style=ft.TextStyle(
        #             size=12, color='#858796'
        #         ),
        #         text_style=ft.TextStyle(
        #             size=14,
        #             color='black',
        #         ),
        #         hint_text='Password',
        #         cursor_color='#858796',
        #         password=True,
        #
        #
        #     ),
        #     border=ft.border.all(width=1, color='#bdcbf4'),
        #     border_radius=30
        # )
        #
        # self.content = ft.Column(
        #     alignment=ft.alignment.center,
        #     horizontal_alignment=ft.alignment.center,
        #     controls=[
        #         ft.Container(
        #             width=500,
        #             border_radius=12,
        #             padding=40,
        #             bgcolor='white',
        #             content=ft.Column(
        #                 horizontal_alignment=ft.alignment.center,
        #                 controls=[
        #                     ft.Text(
        #                         value="Welcome Back!",
        #                         size=16,
        #                         color='black',
        #                         text_align=ft.alignment.center
        #                     ),
        #
        #                     self.email_box,
        #
        #                     self.password_box,
        #                     ft.Container(height=0),
        #
        #                     ft.Container(
        #                         alignment=ft.alignment.center,
        #                         bgcolor='#4e73df',
        #                         height=40,
        #                         border_radius=30,
        #                         content=ft.Text(
        #                             value='Login'
        #                         ),
        #                     ),
        #                     ft.Container(height=0),
        #                     ft.Container(
        #                         content=ft.Text(
        #                             value='Forgot Password?',
        #                             color='#4e73df',
        #                             size=12
        #                         ),
        #
        #                     ),
        #                     ft.Container(
        #                         content=ft.Text(
        #                             value='Create New Account',
        #                             color='#4e73df',
        #                             size=12
        #                         ),
        #                         on_click=lambda _: self.page.go('/signup')
        #                         # on_click=lambda _: (
        #                         #     setattr(self.page, 'data', self.email_box.content.value), self.page.go('/signup'))
        #
        #                     )
        #                 ]
        #             )
        #         )
        #
        #     ]
        # )

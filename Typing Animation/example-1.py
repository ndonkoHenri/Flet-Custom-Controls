# typing animation example 1


import threading
import flet as ft
from main import TypingAnimation
import logging
logging.basicConfig(level=logging.DEBUG)

def main(page: ft.Page):
    page.title = "Typing Animation Ex 1"
    page.theme_mode = "dark"
    page.appbar = ft.AppBar(
        title=ft.Text("Typing Indicator Example 1"),
        bgcolor='blue',
        color="white",
        center_title=True
    )
    page.window_width, page.window_height = 445, 500
    page.window_always_on_top = True

    typing_anim_1 = TypingAnimation(bubble_size=7, spacing=2, alignment=ft.MainAxisAlignment.END)
    typing_anim_2 = TypingAnimation(bubble_size=7, spacing=2, alignment=ft.MainAxisAlignment.END)

    avatar_1 = ft.Stack(
            [
                ft.CircleAvatar(
                    foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4"
                ),
                ft.Container(
                    content=typing_anim_1,
                    alignment=ft.alignment.bottom_right,
                ),
            ],
            width=40,
            height=40,
        )

    avatar_2 = ft.Stack(
            [
                ft.CircleAvatar(
                    foreground_image_url="https://avatars.githubusercontent.com/u/98978078?v=4"
                ),
                ft.Container(
                    content=typing_anim_2,
                    alignment=ft.alignment.bottom_right,
                ),
            ],
            width=40,
            height=40,
        )

    page.add(
        ft.Row(
            [
                avatar_1, avatar_2
            ]
        )
    )

    # threading here is necessary, because of the while loop used in the TypingAnimation.animate function
    threading.Thread(target=typing_anim_1.animate, daemon=True, name="typing-anim1").start()
    threading.Thread(target=typing_anim_2.animate, daemon=True, name="typing-anim2").start()


ft.app(target=main)

# Typing animation example 2
# Tried to mimic this flutter example: https://docs.flutter.dev/cookbook/effects/typing-indicator

import threading

import flet as ft
from main import TypingAnimation


class FakeMessage(ft.Container):
    """A class to serve as (fake)message in the chat logs. """

    def __init__(self, is_big):
        super().__init__(bgcolor="white", border_radius=8)
        self.height = 128 if is_big else 36  # a flag indicating if this message container is big


def main(page: ft.Page):
    page.window_always_on_top = True
    page.title = "Typing Animation Ex 2"
    page.theme_mode = "dark"

    page.appbar = ft.AppBar(
        title=ft.Text("Typing Indicator"),
        bgcolor='blue',
        color="white",
        center_title=True
    )
    page.window_width, page.window_height = 347.0, 593.0

    def switch_change(e):
        # switch the content of the animation_switcher
        animation_switcher.current.content = empty_container if animation_switcher.current.content == main_container else main_container
        page.update()

    type_anim = TypingAnimation(alignment="center")

    main_container = ft.Container(
        type_anim,
        bgcolor=ft.colors.SURFACE_VARIANT,
        width=85,
        height=44,
        border_radius=ft.BorderRadius(20, 20, 00, 20),
        padding=ft.Padding(2, 2, 2, 2),
        alignment=ft.alignment.center,
    )
    empty_container = ft.Container(
        type_anim,
        width=0,
        height=0,
        bgcolor="yellow"
    )
    animation_switcher = ft.Ref[ft.AnimatedSwitcher]()

    page.add(
        ft.ListView(
            [FakeMessage(True if idx % 2 != 0 else False) for idx, i in enumerate(range(8), 1)],
            padding=ft.Padding(top=8, bottom=8, left=100, right=0),
            spacing=10,
            expand=True,
        ),
        ft.AnimatedSwitcher(
            main_container,
            ref=animation_switcher,
            switch_in_curve=ft.AnimationCurve.EASE_OUT_BACK,
            switch_out_curve=ft.AnimationCurve.EASE_IN_BACK,
            duration=500,
            reverse_duration=800,
            transition=ft.AnimatedSwitcherTransition.SCALE
        ),

        ft.Container(
            content=ft.Switch(
                value=True,
                on_change=switch_change,
            ),
            bgcolor=ft.colors.SURFACE_VARIANT,
            padding=16,
            alignment=ft.alignment.center,
        )
    )
    # threading here is necessary, because of the while loop used in the TypingAnimation.animate function
    threading.Thread(target=type_anim.animate, daemon=True, name="typing-anim3").start()


ft.app(target=main)

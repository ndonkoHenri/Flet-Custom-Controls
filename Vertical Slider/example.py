# this example tries to mimic this flutter example: https://flutterawesome.com/flutter-vertical-slider-widget-to-customize-the-appearance-of-the-slider/
import flet as ft
from vertical_slider import VerticalSlider


def main(page: ft.Page):
    page.title = "Vertical Slider Example"
    page.theme_mode = "light"
    page.window_width = 390
    page.window_height = 400
    page.theme = ft.Theme(visual_density=ft.ThemeVisualDensity.ADAPTIVEPLATFORMDENSITY)

    page.add(
        ft.Container(
            content=ft.Row(
                controls=[
                    VerticalSlider(
                        value=50,
                        label="%{value}",
                        slider_width=80,
                        text_style=ft.TextStyle(color=ft.colors.WHITE, size=24),
                        active_track_color=ft.colors.PRIMARY,
                        inactive_track_color=ft.colors.PRIMARY_CONTAINER
                    ),
                    VerticalSlider(
                        value=40,
                        label="%{value}",
                        slider_width=80,
                        round_to=0,
                        text_style=ft.TextStyle(color=ft.colors.WHITE, size=24),
                        active_track_color=ft.colors.AMBER,
                        inactive_track_color=ft.colors.AMBER_100
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=35
            ),
            alignment=ft.alignment.center,
            expand=True
        )
    )


ft.app(target=main)

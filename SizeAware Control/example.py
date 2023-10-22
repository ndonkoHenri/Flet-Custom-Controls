from size_aware_control import SizeAwareControl
import flet as ft


def main(page: ft.Page):
    def handle_resize(e: ft.canvas.CanvasResizeEvent):
        """
        The handle_resize function is a callback function that will be called when
        the control that triggered this event is resized (ex: through window resize).
        The CanvasResizeEvent object has several useful attributes:
            - control: The control that triggered the event (SizeAwareControl)
            - width: The new width of the control in pixels (after resize)
            - height: The new height of the control in pixels (after resize)
        """
        # grab the content of the SizeAwareControl
        c = e.control.content
        # grab the text in its content
        t = c.content
        # instead of e.width for example, you can use the e.control.size namedtuple (e.control.size.width or e.control.size[0])
        t.value = f"{e.width} x {e.height}"
        page.update()

    s1 = SizeAwareControl(ft.Container(content=ft.Text("W x H"), bgcolor=ft.colors.RED, alignment=ft.alignment.center), on_resize=handle_resize, expand=2)
    s2 = SizeAwareControl(ft.Container(content=ft.Text("W x H"), bgcolor=ft.colors.BLUE, alignment=ft.alignment.center), on_resize=handle_resize, expand=3)

    page.add(
        ft.Row([s1, s2], expand=True),
    )

ft.app(main)
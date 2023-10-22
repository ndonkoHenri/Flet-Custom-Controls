# SizeAwareControl
A control which can be used to track the size(width/height) of its content in real-timie.

## Example
Below is a basic example. It is also found in the `example.py` file.

```python
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
```

## Capture
A capture of the example above:

![image](https://github.com/ndonkoHenri/Flet-Custom-Controls/assets/98978078/198c49e9-0f7e-4d2a-bfb3-660d9c70d7ed)


## Properties
The size of this `SizeAwareControl` can be obtained by grabbing the `size` property. 
It is a `namedtuple` with fields `width` and `height`. 

### `content`
A child Control contained by this `SizeAwareControl`.

The default value is `None`.

### `resize_interval`
The minimum value of the slider.

The default value is `100`.

### `kwargs`
Additional keyword arguments (see Canvas properties).

## Events

### `on_resize`
Fires when the size of canvas has changed.

Event object `e` is an instance of `CanvasResizeEvent` class with the following fields:

- `control`: The control that triggered the event (SizeAwareControl)
- `width` - The new width of the control in pixels (after resize)
- `height` - The new height of the control in pixels (after resize)

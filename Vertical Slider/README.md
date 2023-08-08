# Vertical Slider

A customizable vertical slider made/drawn using the [Canvas](https://flet.dev/docs/controls/canvas).

## Capture
The following image shows two vertical sliders. The code for this is in the `example.py` file.

![image](https://github.com/ndonkoHenri/Flet-Custom-Controls/assets/98978078/c73114be-e619-42db-85c8-6686f7ed9cb0)

## Example
Below is a basic example.

```python
import flet as ft
from vertical_slider import VerticalSlider

def main(page: ft.Page):
    page.title = "Vertical Slider Example"

    def handle_slider_change(value):
        print(f"SliderValue = {value}")

    vertical_slider = VerticalSlider(on_change=handle_slider_change)

    page.add(vertical_slider)


ft.app(target=main)
```

## Properties

### `value`
The value of the slider. Must lie between `min_val` and `max_val`.

The default value is `50`.

### `min_val`
The minimum value of the slider.

The default value is `0`.

### `max_val`
The maximum value of the slider.

The default value is `100`.

### `label`
The label of the slider. If set, "`{value}`" must be present and will be replaced by the slider's value.

The default value is `"{value}%"`.

### `round_to`
The number of decimal places to round the slider's value to.

The default value is `0`.

### `inactive_track_border_radius`
The border radius of the slider's inactive track.

The default value is `ft.BorderRadius(6, 6, 6, 6)`.

### `active_track_border_radius`
The border radius of the slider's active track.

The default value is `ft.BorderRadius(0, 0, 6, 6)`.

### `slider_height`
The height of the slider.

The default value is `200`.

### `slider_width`
The width of the slider.

The default value is `60`.

### `inactive_track_color`
The color of the slider's inactive track.

The default value is `ft.colors.GREY_500`.

### `active_track_color`
The color of the slider's active track.

The default value is `ft.colors.GREY_900`.

### `text_style`
The style of the text that is displayed by default in the middle of the slider.

The default value is `ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.colors.ERROR)`.

## Events

### `on_change`
Fires when the slider's value is changed.


### Inspiration
I inspired myself from [this](https://flutterawesome.com/flutter-vertical-slider-widget-to-customize-the-appearance-of-the-slider/) flutterawesome project. 

The `example.py` file in this repo mimics the capture found on that site.


### Known Issue
I noticed that when the slider is resized, it becomes hideous. Will work on that soon and push an update.
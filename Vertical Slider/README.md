# Vertical Slider

A customizable vertical slider made/drawn using the [Canvas](https://flet.dev/docs/controls/canvas).

### Docs
The Vertical slider object is instantiated using `VerticalSlider()`. There are several paramters you could set: 

```
Args:
    value: Set the default value of the slider. Must lie between min_val and max_val.
    min_val: Set the minimum value of the slider
    max_val: Set the maximum value of the slider
    label: Set the label of the slider. "{value}" must be present and will be replaced by the slider's value.
    round_to: Round the slider's value to a certain number of decimal places
    inactive_track_border_radius: the border radius of the slider's inactive track
    active_track_border_radius: the border radius of the slider's active track
    slider_height: the height of the slider
    slider_width: the width of the slider
    inactive_track_color: the color of the slider's inactive track
    active_track_color: Set the color of the slider's active track
    text_style: Set the style of the text that is displayed by default in the middle of the slider
    on_change: Callback function to be called when the value of the slider is changed
```

Feel free to check the source code and adjust/customize these to your needs.


### Capture



### Inspiration
I inspired myself from [this](https://flutterawesome.com/flutter-vertical-slider-widget-to-customize-the-appearance-of-the-slider/) flutterawesome project. 

The `example.py` file in this repo tries mimics the capture found on that site.
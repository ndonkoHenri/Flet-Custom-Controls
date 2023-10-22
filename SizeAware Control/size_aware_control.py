from collections import namedtuple
from typing import Optional, Callable
import flet as ft
import flet.canvas as cv


class SizeAwareControl(cv.Canvas):
    def __init__(self, content: Optional[ft.Control] = None, resize_interval: int=100, on_resize: Optional[Callable]=None, **kwargs):
        """
        :param content: A child Control contained by the SizeAwareControl. Defaults to None.
        :param resize_interval: The resize interval. Defaults to 100.
        :param on_resize: The callback function for resizing. Defaults to None.
        :param kwargs: Additional keyword arguments(see Canvas properties).
        """
        super().__init__(**kwargs)
        self.content = content
        self.resize_interval = resize_interval
        self.on_resize = self.__handle_canvas_resize
        self.resize_callback = on_resize
        self.size = namedtuple("size", ["width", "height"], defaults=[0, 0])

    def __handle_canvas_resize(self, e):
        """
        Called every resize_interval when the canvas is resized.
        If a resize_callback was given, it is called.
        """
        self.size = (int(e.width), int(e.height))
        self.update()
        if self.resize_callback:
            self.resize_callback(e)
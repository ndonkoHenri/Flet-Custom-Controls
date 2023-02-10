import time
from typing import Union, Literal
import flet as ft


class TypingAnimation(ft.Row):
    def __init__(
            self,
            bubble_count: int = 3,
            bubble_size: Union[int, float] = 10,
            color_1: str = ft.colors.BLUE_GREY,
            color_2: str = ft.colors.WHITE,
            intervals: int = 0.1,
            duration: int = 1500,
            reverse_duration: int = 1500,
            is_animated: bool = False,
            opacity: Union[int, float, None] = None,
            bubble_shape: Union[ft.BoxShape, Literal["circle", "rectangle"]] = ft.BoxShape('circle'),
            **kwargs
    ):
        """
        A row containing animated bubbles.
        Use-case: Could be used for typing animations in chat apps.

        :param bubble_count: the number of bubbles/circles to display
        :param bubble_size: the size of each bubble/circle
        :param color_1: the color of the bubble/circle when not filled
        :param color_2: the color of the bubble/circle when filled
        :param intervals: the amount of seconds to sleep between bubble-updates
        :param duration: the duration of the AnimatedSwitcher
        :param reverse_duration: the reverse_duration of the AnimatedSwitcher
        :param is_animated: a flag indicating the state of the animation
        :param opacity: the opacity of the AnimatedSwitchers
        :param bubble_shape: the shape of the bubble: rectangle or circle
        :param kwargs: refers to flet.Row key-value(keyword) arguments that will be passed, ex: spacing=2

        :raises AssertionError: if bubble_count is less than 2
        """
        super().__init__(**kwargs)

        self.bubble_count = bubble_count
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_opacity = opacity
        self.intervals = intervals
        self.is_animated = is_animated
        self.shape = ft.BoxShape("circle")
        self.bubble_shape = bubble_shape

        self.bubbles_list = []
        # make sure the number of bubbles is greater than 1
        assert self.bubble_count > 1, "The bubble_count must be greater than or equal to 2."

        class CircleBubble(ft.Container):
            """A class for the bubbles."""

            def __init__(self, bubble_color: str, size=bubble_size, shape=bubble_shape):
                super().__init__()
                self.width = size
                self.height = size
                self.bgcolor = bubble_color
                assert isinstance(shape, (ft.BoxShape, str)), "bubble_shape must be of type BoxShape or str"
                self.shape = ft.BoxShape(bubble_shape) if isinstance(bubble_shape, str) else bubble_shape

        # build up bubbles depending on the bubble_count
        for i in range(int(self.bubble_count)):
            # pair
            c1 = CircleBubble(bubble_color=self.color_1)
            c2 = CircleBubble(bubble_color=self.color_2)

            # AnimatedSwitchers with the containers containing the first color
            a = ft.AnimatedSwitcher(
                c1,
                transition=ft.AnimatedSwitcherTransition.FADE,
                duration=duration,
                reverse_duration=reverse_duration,
                switch_in_curve=ft.AnimationCurve.ELASTIC_OUT,
                switch_out_curve=ft.AnimationCurve.EASE_OUT,
            )

            self.bubbles_list.append((c1, c2, a))

        # add only the AnimatedSwitchers to the list of controls
        self.controls = [j[2] for j in self.bubbles_list]

    def animate(self):
        """Starts the animation in a while loop."""

        self.is_animated = True

        while self.is_animated:
            # update(switch the content of) the bubbles one after the other, creating the Typing-Animation
            for i in self.bubbles_list:
                i[2].content = i[0] if i[2].content == i[1] else i[1]
                self.update()
                time.sleep(self.intervals)
            time.sleep(self.intervals)

        self.is_animated = False



from asciimatics.effects import RandomNoise
from asciimatics.renderers import FigletText, Rainbow, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys

from time import sleep
from sys import argv

def demo(screen):
    effects = [
        RandomNoise(screen,
                    # signal=FigletText("HAPPY NEW YEAR\n"+argv[1]), )
                    # signal=StaticRenderer(screen,
                    #                FigletText("HAPPY NEW YEAR\n     "+argv[1])))
                    signal=Rainbow(screen,
                                   FigletText("Happy  New  Year\n"+argv[1])))
    ]
    screen.play([Scene(effects, -1)], stop_on_resize=True)


print(f'\nHallo {argv[1]}')
sleep(1)
print(f'lade xmas_2022...')
sleep(1)
print(f'done!')
sleep(0.5)
print(f'hoho!')
sleep(0.5)

while True:
    try:
        Screen.wrapper(demo)
        sys.exit(0)
    except ResizeScreenError:
        pass
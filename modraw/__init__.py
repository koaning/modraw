from typing import List
from pathlib import Path
import anywidget
import traitlets


class Draw(anywidget.AnyWidget):
    """Initialize a Draw widget based on tldraw.
    """
    _esm = Path(__file__).parent / 'static' / 'draw.js'
    _css = Path(__file__).parent / 'static' / 'draw.css'
    width = traitlets.Int(800).tag(sync=True)
    height = traitlets.Int(500).tag(sync=True)
    base64 = traitlets.Unicode("").tag(sync=True)

    def __init__(self, width: int = 800, height: int = 500, **kwargs) -> None:
        super().__init__(width=width, height=height, **kwargs)

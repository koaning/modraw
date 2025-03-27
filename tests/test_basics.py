from modraw import Draw
import pytest

def test_basics_no_drawn_image():
    """Errors should be raised if no image is drawn."""
    widget = Draw()
    
    assert widget.get_base64() == ""
    with pytest.raises(ValueError):
        widget.get_pil()

from project import scroll_gesture, scroll_amount, zoom_gesture

def test_scroll_amount():
    assert scroll_amount(previous_y=None, current_y=None) == 0
    assert scroll_amount(previous_y=1, current_y=1) == 0


def test_scroll_gesture():
    assert scroll_gesture(fingers=[True, True, True, True, True]) == True
    assert scroll_gesture(fingers=[True, True, True, True, False]) == False


def test_zoom_gesture():
    assert zoom_gesture(fingers=[True, True, False, False, False]) == True
    assert zoom_gesture(fingers=[True, True, True, False, False]) == False



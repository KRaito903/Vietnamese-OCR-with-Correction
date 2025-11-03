# Các zone định nghĩa sẵn
class HTV_BOX:
    BOX_X = 1050
    BOX_Y = 50
    BOX_W = 132
    BOX_H = 60

class NEWS_BOX:
    """Ticker bar dưới cùng"""
    BOX_X = 0
    BOX_Y = 645
    BOX_W = 1280
    BOX_H = 46


# Dictionary các exclusion zones định nghĩa sẵn
EXCLUSION_ZONES = {
    'DEFAULT': [],  # Không filter
    'HTV': [
        (HTV_BOX.BOX_X, HTV_BOX.BOX_Y, HTV_BOX.BOX_W, HTV_BOX.BOX_H),
    ],
    'NEWS': [
        (NEWS_BOX.BOX_X, NEWS_BOX.BOX_Y, NEWS_BOX.BOX_W, NEWS_BOX.BOX_H),
    ],
    'NEWS_60S': [
        (HTV_BOX.BOX_X, HTV_BOX.BOX_Y, HTV_BOX.BOX_W, HTV_BOX.BOX_H),
        (NEWS_BOX.BOX_X, NEWS_BOX.BOX_Y, NEWS_BOX.BOX_W, NEWS_BOX.BOX_H),
    ],
}

# Thông số filter
FILTER_PARAMS = {
    'min_area': 100,  # Diện tích tối thiểu (pixels)
    'max_area': 50000,  # Diện tích tối đa (pixels)
    'min_aspect_ratio': 0.1,  # Tỷ lệ w/h tối thiểu
    'max_aspect_ratio': 15.0,  # Tỷ lệ w/h tối đa
}
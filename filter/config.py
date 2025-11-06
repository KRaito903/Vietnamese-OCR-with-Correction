# Các zone định nghĩa sẵn
class HTV_BOX:
    BOX_X = 1550
    BOX_Y = 0
    BOX_W = 370
    BOX_H = 180

# X,y 1.5
class REMOVE_TEXTS:
    text = ["giay", "tiep theo", "HTV", "HTV7", "HTV9", "tin chinh","tinchinh","tieptheo","chuong trinh 60","18:30","HIV"]

class NEWS_BOX:
    """Ticker bar dưới cùng"""
    BOX_X = 0
    BOX_Y = 960
    BOX_W = 1920
    BOX_H = 80

class LEFT_BOX:
    BOX_X = 0
    BOX_Y = 0
    BOX_W = 255
    BOX_H = 90

class RIGHT_BOX:
    BOX_X = 1025
    BOX_Y = 0
    BOX_W = 255
    BOX_H = 90


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
    'HTV_COOKING': [
        (LEFT_BOX.BOX_X, LEFT_BOX.BOX_Y, LEFT_BOX.BOX_W, LEFT_BOX.BOX_H),
    ],
    'COMPARE': [
        (LEFT_BOX.BOX_X, LEFT_BOX.BOX_Y, LEFT_BOX.BOX_W, LEFT_BOX.BOX_H),
        (RIGHT_BOX.BOX_X, RIGHT_BOX.BOX_Y, RIGHT_BOX.BOX_W, RIGHT_BOX.BOX_H),
    ],
    'LEFT_BOX': [
        (LEFT_BOX.BOX_X, LEFT_BOX.BOX_Y, LEFT_BOX.BOX_W, LEFT_BOX.BOX_H),
    ],
}

# Thông số filter
FILTER_PARAMS = {
    'min_area': 100,  # Diện tích tối thiểu (pixels)
    'max_area': 50000,  # Diện tích tối đa (pixels)
    'min_aspect_ratio': 0.1,  # Tỷ lệ w/h tối thiểu
    'max_aspect_ratio': 15.0,  # Tỷ lệ w/h tối đa
}
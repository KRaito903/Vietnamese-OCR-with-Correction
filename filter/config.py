# Các zone định nghĩa sẵn
class HTV_BOX:
    BOX_X = 0
    BOX_Y = 0
    BOX_W = 200
    BOX_H = 100

class NEWS_BOX:
    """Ticker bar dưới cùng"""
    BOX_X = 0
    BOX_Y = 680
    BOX_W = 1920
    BOX_H = 400

class COMPARE_BOX:
    """Logo góc trên bên phải"""
    BOX_X = 1600
    BOX_Y = 0
    BOX_W = 320
    BOX_H = 200

# Dictionary các exclusion zones định nghĩa sẵn
EXCLUSION_ZONES = {
    'DEFAULT': [],  # Không filter
    'HTV': [
        (HTV_BOX.BOX_X, HTV_BOX.BOX_Y, HTV_BOX.BOX_W, HTV_BOX.BOX_H),
    ],
    'NEWS': [
        (NEWS_BOX.BOX_X, NEWS_BOX.BOX_Y, NEWS_BOX.BOX_W, NEWS_BOX.BOX_H),
    ],
    'COMPARE': [
        (COMPARE_BOX.BOX_X, COMPARE_BOX.BOX_Y, COMPARE_BOX.BOX_W, COMPARE_BOX.BOX_H),
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
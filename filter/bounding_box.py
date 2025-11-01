import cv2
from skimage.metrics import structural_similarity as ssim

from filter.config import *

# che new và htv trên ảnh
def redact_box(image_path, x, y, w, h, color=(0, 0, 0)):
    """
    Che vùng trên ảnh bằng hình chữ nhật màu (mặc định: đen)
    
    Args:
        image_path (str): đường dẫn ảnh
        x, y (int): tọa độ góc trên bên trái
        w, h (int): chiều rộng, chiều cao box
        color (tuple): màu RGB, mặc định (0,0,0)
    
    Returns:
        img (numpy.ndarray): ảnh đã che
    """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Không thể đọc ảnh. Kiểm tra đường dẫn!")

    cv2.rectangle(img, (x, y), (x + w, y + h), color, -1)
    return img

# So sánh histogram màu trong vùng box

def compare_region_color(img1, img2, box):

    """
    img1, img2: 2 ảnh BGR
    box: (x, y, w, h)
    Trả về điểm tương đồng histogram màu trong vùng box
    1: giống hệt, -1: khác hoàn toàn
    0: không liên quan
    0.5: tương đối giống
    Lấy > 0.5 hoặc xét các ảnh đằng sau xem có trên 0.5 hay không
    """ 
    x, y, w, h = box
    region1 = cv2.cvtColor(img1[y:y+h, x:x+w], cv2.COLOR_BGR2HSV)
    region2 = cv2.cvtColor(img2[y:y+h, x:x+w], cv2.COLOR_BGR2HSV)

    # Chỉ lấy 2 kênh H và S
    hist1 = cv2.calcHist([region1], [0, 1], None, [50, 60], [0, 180, 0, 256])
    hist2 = cv2.calcHist([region2], [0, 1], None, [50, 60], [0, 180, 0, 256])

    # Chuẩn hóa để loại bỏ ảnh hưởng kích thước vùng
    cv2.normalize(hist1, hist1)
    cv2.normalize(hist2, hist2)

    # So sánh histogram bằng tương quan (CORREL)
    score = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return score

# SSIM trong vùng box

def compare_region_ssim(img1, img2, box):

    """
    img1, img2: 2 ảnh BGR
    box: (x, y, x1, y1)
    so sánh sử dụng SSIM trong vùng box
    Trả về điểm SSIM trong vùng box
    1: giống hệt, 0: khác hoàn toàn
    0.5: tương đối giống
    Lấy > 0.5
    """
    x, y, w, h = box
    region1 = cv2.cvtColor(img1[y:y+h, x:x+w], cv2.COLOR_BGR2GRAY)
    region2 = cv2.cvtColor(img2[y:y+h, x:x+w], cv2.COLOR_BGR2GRAY)
    
    score, _ = ssim(region1, region2, full=True)
    return score

# check path chứa path các video thời sự

def check_path_video_news(path_video_news):
    """
    Kiểm tra đường dẫn chứa file video thời sự
    Trả về True nếu tồn tại, False nếu không
    """
    video_list = [f"K{str(i).zfill(2)}" for i in range(1, 21)]
    video_list.append(["L21_b", "L22_b"])
    if any(code in path_video_news for code in video_list):
        return True
    else:
        return False
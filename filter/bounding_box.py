import cv2
import numpy as np

def is_box_inside_exclusion_zone(box, exclusion_zones):
    """
    Kiểm tra xem box có nằm trong exclusion zone không
    
    Args:
        box: [[x1, y1], [x2, y2]] từ PaddleOCR
        exclusion_zones: list of (x, y, w, h) zones cần loại bỏ
    
    Returns:
        bool: True nếu box nằm trong zone (cần filter)
    """
    if not exclusion_zones:
        return False
    
    box_x1, box_y1 = box[0]
    box_x2, box_y2 = box[1]
    
    for zone_x, zone_y, zone_w, zone_h in exclusion_zones:
        zone_x2 = zone_x + zone_w
        zone_y2 = zone_y + zone_h
        
        # Kiểm tra overlap (chồng lấn)
        # Nếu có bất kỳ phần nào chồng lấn thì filter
        if not (box_x2 < zone_x or box_x1 > zone_x2 or 
                box_y2 < zone_y or box_y1 > zone_y2):
            return True
    
    return False


def filter_boxes_by_zones(boxes, exclusion_zones):
    """
    Lọc bỏ các boxes nằm trong exclusion zones
    
    Args:
        boxes: list of [[x1, y1], [x2, y2]] boxes
        exclusion_zones: list of (x, y, w, h) exclusion zones
    
    Returns:
        filtered_boxes: list boxes đã được lọc
    """
    if not exclusion_zones:
        return boxes
    
    filtered = []
    for box in boxes:
        if not is_box_inside_exclusion_zone(box, exclusion_zones):
            filtered.append(box)
    
    return filtered


def filter_boxes_by_area(boxes, min_area=100, max_area=50000):
    """
    Lọc boxes theo diện tích (loại bỏ quá nhỏ hoặc quá lớn)
    """
    filtered = []
    for box in boxes:
        width = box[1][0] - box[0][0]
        height = box[1][1] - box[0][1]
        area = width * height
        
        if min_area <= area <= max_area:
            filtered.append(box)
    
    return filtered


def filter_boxes_by_aspect_ratio(boxes, min_ratio=0.1, max_ratio=15.0):
    """
    Lọc boxes theo tỷ lệ khung hình (loại bỏ hình dạng bất thường)
    """
    filtered = []
    for box in boxes:
        width = box[1][0] - box[0][0]
        height = box[1][1] - box[0][1]
        
        if height > 0:
            ratio = width / height
            if min_ratio <= ratio <= max_ratio:
                filtered.append(box)
    
    return filtered


def visualize_filtering(img_path, original_boxes, filtered_boxes, exclusion_zones, output_path):
    """
    Tạo ảnh visualization để debug
    
    Args:
        img_path: đường dẫn ảnh gốc
        original_boxes: boxes ban đầu từ PaddleOCR
        filtered_boxes: boxes sau khi filter
        exclusion_zones: list zones đã dùng
        output_path: nơi lưu ảnh visualization
    """
    img = cv2.imread(img_path)
    if img is None:
        return
    
    img_vis = img.copy()
    
    # Vẽ exclusion zones (màu đỏ, trong suốt)
    overlay = img_vis.copy()
    for x, y, w, h in exclusion_zones:
        cv2.rectangle(overlay, (x, y), (x+w, y+h), (0, 0, 255), -1)
    cv2.addWeighted(overlay, 0.3, img_vis, 0.7, 0, img_vis)
    
    # Vẽ viền exclusion zones
    for x, y, w, h in exclusion_zones:
        cv2.rectangle(img_vis, (x, y), (x+w, y+h), (0, 0, 255), 3)
        cv2.putText(img_vis, "EXCLUDED", (x+5, y+30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    # Vẽ boxes đã filter (màu xám, bị loại)
    removed_boxes = [b for b in original_boxes if b not in filtered_boxes]
    for box in removed_boxes:
        pt1 = tuple(map(int, box[0]))
        pt2 = tuple(map(int, box[1]))
        cv2.rectangle(img_vis, pt1, pt2, (128, 128, 128), 2)
        # Vẽ dấu X
        cv2.line(img_vis, pt1, pt2, (128, 128, 128), 2)
        cv2.line(img_vis, (pt1[0], pt2[1]), (pt2[0], pt1[1]), (128, 128, 128), 2)
    
    # Vẽ boxes giữ lại (màu xanh lá)
    for box in filtered_boxes:
        pt1 = tuple(map(int, box[0]))
        pt2 = tuple(map(int, box[1]))
        cv2.rectangle(img_vis, pt1, pt2, (0, 255, 0), 2)
    
    # Thêm legend
    cv2.putText(img_vis, f"Keep: {len(filtered_boxes)}", (10, 40), 
               cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
    cv2.putText(img_vis, f"Remove: {len(removed_boxes)}", (10, 80), 
               cv2.FONT_HERSHEY_SIMPLEX, 1.2, (128, 128, 128), 3)
    cv2.putText(img_vis, f"Zones: {len(exclusion_zones)}", (10, 120), 
               cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
    
    cv2.imwrite(output_path, img_vis)
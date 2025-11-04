from unidecode import unidecode
from .config import REMOVE_TEXTS
def remove_text(texts, texts_remove=REMOVE_TEXTS.text):
    """
    Xóa các từ trong texts_remove khỏi texts sau khi bỏ dấu để so sánh.
    
    Args:
        texts: list của các chuỗi cần xử lý
        texts_remove: list các chuỗi cần xóa (sau khi bỏ dấu)
    
    Returns:
        list các chuỗi sau khi đã xóa và loại bỏ chuỗi rỗng
    """
    # Chuẩn hóa texts_remove (bỏ dấu và chuyển thành lowercase)
    
    result = []
    
    for text in texts:
        # Tách các từ trong text
        # words = text.split()
        # filtered_words = []
        # print(f"Original text: {words}")
        
        # for word in words:
        #     # Bỏ dấu và lowercase để so sánh
        #     normalized_word = unidecode(word.lower())
            
        #     # Chỉ giữ lại từ nếu không nằm trong danh sách xóa
        #     if normalized_word not in texts_remove:
        #         filtered_words.append(word)
        
        # # Ghép lại thành chuỗi
        # filtered_text = " ".join(filtered_words).strip()
        normalized_text = unidecode(text.lower())
        print(f"Original text: {text} -> Normalized: {normalized_text}")
        for rem_word in texts_remove:
            print(f"  - Removing word: {rem_word}")
            if rem_word in normalized_text:
                start_word = normalized_text.find(rem_word)
                end_word = start_word + len(rem_word) + 1
                normalized_text = normalized_text[:start_word] + normalized_text[end_word:]
                text = text[:start_word] + text[end_word:]
        # Chỉ thêm vào kết quả nếu không rỗng và có độ dài > 1
        if text and len(text) > 1:
            result.append(text)
    
    return result

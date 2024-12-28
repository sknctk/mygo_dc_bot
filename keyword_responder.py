import random
import time
from fuzzywuzzy import fuzz

class KeywordResponder:
    """關鍵字與圖片回應邏輯（支持模糊匹配、隨機圖片選擇與冷卻時間）"""

    def __init__(self, keyword_to_images, threshold=80, cooldown=10):
        """
        初始化
        :param keyword_to_images: 關鍵字對應圖片列表字典
        :param threshold: 匹配域值（0-100），低於此分數不匹配
        :param cooldown: 回覆冷卻時間（秒）
        """
        self.keyword_to_images = keyword_to_images
        self.threshold = threshold
        self.cooldown = cooldown
        self.last_response_time = {}  # 記錄每個關鍵字的最後回覆時間

    def can_respond(self, keyword):
        """
        檢查是否可以回覆指定的關鍵字
        :param keyword: 關鍵字
        :return: 是否允許回覆
        """
        current_time = time.time()
        if keyword not in self.last_response_time:
            return True
        return current_time - self.last_response_time[keyword] >= self.cooldown

    def find_image(self, message_content):
        """
        檢查訊息是否模糊匹配關鍵字，並隨機返回對應圖片路徑
        :param message_content: 訊息內容
        :return: 隨機選擇的圖片路徑或 None
        """
        matched_images = []
        selected_keyword = None

        # 搜集所有符合條件的圖片
        for keyword, images in self.keyword_to_images.items():
            score = fuzz.partial_ratio(keyword, message_content)
            if score >= self.threshold and self.can_respond(keyword):  # 匹配分數需達到域值且冷卻完成
                matched_images.extend(images)
                selected_keyword = keyword

        # 如果找到匹配的圖片，隨機選擇一張返回
        if matched_images and selected_keyword:
            self.last_response_time[selected_keyword] = time.time()  # 更新最後回覆時間
            return random.choice(matched_images)

        return None  # 若無匹配圖片或冷卻未完成，返回 None

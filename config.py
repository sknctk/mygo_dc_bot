import os
from dotenv import load_dotenv

# 載入 .env 檔案
load_dotenv()

# Discord Bot Token
TOKEN = os.getenv("DISCORD_TOKEN")

# 圖片資料夾路徑
IMAGE_FOLDER = os.getenv("IMAGE_FOLDER", "images")

# 要監聽的頻道 ID（單個或多個，使用逗號分隔）
LISTEN_CHANNEL_IDS = list(map(int, os.getenv("LISTEN_CHANNEL_IDS", "").split(',')))

# 根據圖片檔名生成關鍵字對應圖片列表
def load_keyword_to_images(folder_path):
    keyword_to_images = {}
    if not os.path.exists(folder_path):
        print(f"圖片資料夾 {folder_path} 不存在！請檢查路徑設定。")
        return keyword_to_images

    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.jpg', '.png', '.jpeg')):  # 支援的圖片格式
            keyword = os.path.splitext(file_name)[0]  # 使用檔名作為關鍵字
            if keyword not in keyword_to_images:
                keyword_to_images[keyword] = []
            keyword_to_images[keyword].append(os.path.join(folder_path, file_name))
    return keyword_to_images

# 自動生成 KEYWORD_TO_IMAGES
KEYWORD_TO_IMAGES = load_keyword_to_images(IMAGE_FOLDER)

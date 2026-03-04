import requests
import os

def download_file(url, filename):
    print(f"Downloading {url} to {filename}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=20, stream=True)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Successfully downloaded {filename}")
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

# 嘗試從一些更直接的音效資源庫獲取連結
sounds = {
    "ambient.mp3": "https://assets.mixkit.co/sfx/preview/mixkit-crickets-and-insects-at-night-2508.mp3", # 蟋蟀與夜晚氛圍
    "dog.mp3": "https://assets.mixkit.co/sfx/preview/mixkit-dog-barking-twice-1.mp3", # 狗叫 (暫時替代，通常嗚咽聲較難找直接連結)
    "click.mp3": "https://assets.mixkit.co/sfx/preview/mixkit-simple-click-interface-1111.mp3" # 點擊音
}

os.makedirs("sounds", exist_ok=True)

for name, url in sounds.items():
    download_file(url, os.path.join("sounds", name))

import requests
import time

channels = [
    ("CCTV1", "http://113.15.109.216:59901/tsfile/live/0001_1.m3u8?公众号【潇雨萌萌】txiptv&playlive"),
    ("CCTV1", "http://112.99.193.34:9901/tsfile/live/1017_1.m3u8?公众号【潇雨萌萌】txiptv&playlive"),
    ("CCTV2", "http://222.169.85.8:9901/tsfile/live/0002_1.m3u8?公众号【潇雨萌萌】txiptv&playlive"),
]

headers = {"User-Agent": "Mozilla/5.0"}

def test_channel(name, url):
    try:
        start = time.time()
        response = requests.get(url, headers=headers, timeout=5, stream=True)
        end = time.time()
        duration = round(end - start, 3)

        if response.status_code == 200:
            print(f"[✓] {name} - 有效链接 - 响应时间: {duration} 秒")
        else:
            print(f"[✗] {name} - 无效链接 - 状态码: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"[✗] {name} - 请求失败: {e}")

for name, url in channels:
    test_channel(name, url)

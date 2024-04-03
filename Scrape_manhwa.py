"""import requests
req=requests.get("https://theblank.net/wp-content/uploads/WP-manga/data/manga_64fb66ad898b6/ede2b3bb6c7a91ee8e6677a4f3553358/01.jpg")
#print(req.status_code)
with open('sico.png','wb') as f:
    f.write(req.content)
"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.111 Safari/537.3'
}

url = "https://theblank.net/wp-content/uploads/WP-manga/data/manga_64fb66ad898b6/ede2b3bb6c7a91ee8e6677a4f3553358/01.jpg"
req = requests.get(url, headers=headers)

if req.status_code == 200:
    with open('siccco.png','wb') as f:
        f.write(req.content)
else:
    print("Error:", req.status_code)

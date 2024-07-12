import requests

# 서버의 URL
url = 'http://52.78.68.85:8000/api/players/'

# 추가할 플레이어 데이터
new_player = {
    "user_id": "player123",
    "nickname": "player_one",
    "highscore": 1000,
    "item": [0,0,0],
    "gold": 500,
    "email": "player@example.com"
}

# POST 요청을 통해 새로운 플레이어 데이터 전송
response = requests.post(url, json=new_player)

# 응답 확인
if response.status_code == 201:
    print('New player created successfully:', response.json())
else:
    print('Failed to create new player:', response.status_code, response.text)

import requests

# 서버의 URL
base_url = 'http://52.78.68.85:8000/api/players/'

# 수정할 플레이어의 ID
player_id = 'player1234'  # 예시로 1번 플레이어를 수정한다고 가정합니다.

# PATCH 요청으로 업데이트할 데이터
updated_data = {
    "highscore" : 5000
}

# PATCH 요청 보내기
update_url = base_url + f"{player_id}/"
response = requests.patch(update_url, json=updated_data)

# 응답 확인
if response.status_code == 200:
    print(f'Player {player_id} updated successfully:', response.json())
else:
    print(f'Failed to update player {player_id}:', response.status_code, response.text)

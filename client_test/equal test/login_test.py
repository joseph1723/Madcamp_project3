import requests
import json
# 로그인할 사용자의 정보
login_data = {
    'username': 'new_user1234',
    'password': 'password1234'
}

# 서버의 로그인 API 엔드포인트 URL
base_url = 'http://52.78.68.85:8000'
# login_url = f'{base_url}/api/login'

token_url = f'{base_url}/api/token/'

# POST 요청으로 로그인 데이터를 전송
# response = requests.post(login_url, data=login_data)

response = requests.post(token_url, data=login_data)
# 서버에서 받은 응답 코드와 데이터 처리
tokens = response.json()
print('Tokens:', tokens)

# 토큰 저장
with open('tokens.json', 'w') as f:
    json.dump(tokens, f)

if response.status_code == 200:
    print("Login successful!")

#     print(response.json())  # 서버에서 보낸 JSON 데이터 출력
#     session = requests.Session()
#     session.cookies.update(response.cookies)
#     auth_response = session.get('http://52.78.68.85:8000/api/ranks/')
#     print(auth_response.json())
elif response.status_code == 401:
    print("Invalid credentials. Please check your username and password.")
else:
    print(f"Login failed with status code {response.status_code}")



# 서버 URL 설정
# base_url = 'http://yourdomain.com'
# token_url = f'{base_url}/api/token/'

# # 로그인 요청 데이터
# login_data = {
#     'username': 'yourusername',
#     'password': 'yourpassword'
# }

# # 토큰 요청
# response = requests.post(token_url, data=login_data)
# tokens = response.json()
# print('Tokens:', tokens)

# # 토큰 저장
# with open('tokens.json', 'w') as f:
#     json.dump(tokens, f)


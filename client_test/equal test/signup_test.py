import requests

# API 엔드포인트 URL
url = 'http://localhost:8000/api/signup/'

# 회원가입에 사용할 데이터
data = {
    'username': 'new_user1234',
    'nickname':'joseph',
    'password': 'password1234',
    'password_confirm' : 'password1234',
    'email': 'new_user123@example.com',
    'first_name': 'New',
    'last_name': 'User'
}

# POST 요청 보내기
response = requests.post(url, data=data)

# 응답 확인
if response.status_code == 201:
    print('회원가입 성공!')
    print(response.json())  # 회원가입된 사용자 정보 출력
else:
    print('회원가입 실패:', response.status_code)
    print(response.json())  # 에러 메시지 출력

import requests
import json

def get_problem_list():
    url = 'http://52.78.68.85:8000/api/problems/'  # 서버의 URL을 입력하세요.

    with open('tokens.json', 'r') as f:
        tokens = json.load(f)
    headers = {
    'Authorization': f'Bearer {tokens["access"]}'
    }
        
    try:
        response = requests.get(url, headers= headers)
        response.raise_for_status()  # 응답 코드가 200이 아닌 경우 예외 발생
        problems = response.json()  # JSON 데이터를 파이썬 딕셔너리로 변환
        return problems
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    problems = get_problem_list()
    if problems:
        for problem in problems:
            print(f"num: {problem['num']}")
            print(f"Difficulty: {problem['difficulty']}")
            print("-----")

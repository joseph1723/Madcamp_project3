import requests

def get_rank_list():
    url = 'http://52.78.68.85:8000/api/ranks/'  # 서버의 URL에 맞게 변경해야 합니다.
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTP 요청이 성공적으로 처리되지 않으면 예외 발생

        rank_list = response.json()  # JSON 데이터를 Python 객체로 변환
        return rank_list
        
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

# 클라이언트 코드 실행 예시
if __name__ == '__main__':
    rank_list = get_rank_list()
    if rank_list:
        print("Rank 리스트:")
        for rank in rank_list:
            print(f"User ID: {rank['user_id']}, Score: {rank['score']}")

import requests

response = requests.get('https://api.github.com')

print("Hello, Python!")
print(response.status_code)  # 출력 예시: 200
print(response.json())       # JSON 응답 출력
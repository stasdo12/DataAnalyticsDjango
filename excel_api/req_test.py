import requests

url = 'http://127.0.0.1:8000/api/upload/'

# Определите MIME-тип для xlsx файла
files = {'file': ('test.xlsx', open('C:/Users/sante/Downloads/test.xlsx', 'rb'), 'application/vnd'
                                                                                           '.openxmlformats'
                                                                                           '-officedocument'
                                                                                           '.spreadsheetml.sheet')}

response = requests.post(url, files=files)

print(response.status_code)


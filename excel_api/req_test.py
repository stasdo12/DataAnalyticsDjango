import requests

url = 'http://127.0.0.1:8000/api/upload/'

# Определите MIME-тип для xlsx файла
files = {'file': ('sveta-04.xlsx', open('C:/Users/sante/Downloads/sveta-04.xlsx', 'rb'), 'application/vnd'
                                                                                           '.openxmlformats'
                                                                                           '-officedocument'
                                                                                           '.spreadsheetml.sheet')}

response = requests.post(url, files=files)

print(response.status_code)


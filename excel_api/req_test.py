import requests

url = 'http://127.0.0.1:8000/api/upload/'

files = {'file': ('cout_example.xlsx', open('C:/Users/sante/Downloads/cout_example.xlsx', 'rb'), 'application/vnd'
                                                                                         '.openxmlformats'
                                                                                         '-officedocument'
                                                                                         '.spreadsheetml.sheet')}

response = requests.post(url, files=files)

print(response.status_code)

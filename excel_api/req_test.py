import requests

url = 'http://127.0.0.1:8000/api/upload/'

files = {'file': ('test_ex.xlsx', open('C:/Users/sante/Downloads/test_ex.xlsx', 'rb'), 'application/vnd'
                                                                                         '.openxmlformats'
                                                                                         '-officedocument'
                                                                                         '.spreadsheetml.sheet')}

response = requests.post(url, files=files)

print(response.status_code)

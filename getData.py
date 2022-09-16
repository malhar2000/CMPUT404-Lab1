import requests

data = requests.get('https://raw.githubusercontent.com/malhar2000/CMPUT404-Lab1/master/getData.py')
print(data)
print(data.content)
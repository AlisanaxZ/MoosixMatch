import requests
data = {
    'api_token': 'a590ad1ecee0441fed52578f1f24afae',
    'return': 'apple_music,spotify',
}
files = {
    'file': open('./2158562.mp3', 'rb'),
}
result = requests.post('https://api.audd.io/', data=data, files=files)
print(result.text)

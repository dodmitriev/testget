import requests

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# это адрес по которому DJANGO отработает get
URL = 'http://a91391d8.beget.tech/get/'

client = requests.session()

condition={'search': 'открыть форму'}
r = client.get(URL, params=condition)

print(r.url)
print(r.text) # это возвращает сервер - return JsonResponse... 777




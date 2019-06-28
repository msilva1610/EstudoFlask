import requests


def teste_get():
    r = requests.get('http://localhost:5000/product/')
    print(r.json())

def teste_post():
    data = {'name': 'iPhone 6s', 'price': 699}
    r = requests.post('http://localhost:5000/product/',data=data)
    print(r.json())

def teste_get_productid(id_product):
    r = requests.get('http://localhost:5000/product/{}'.format(id_product))
    print(r.json())

teste_get()
#teste_post()
#teste_get_productid(21)
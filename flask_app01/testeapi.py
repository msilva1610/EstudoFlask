import requests
import json
import random
import time

names = []
genders = []
companies = []

def teste_get():
    r = requests.get('http://localhost:5000/cliente/')
    print(r.json())

def teste_post01(data):
    r = requests.post('http://localhost:5000/cliente/',data=data)
    print(r.json())

def teste_post():
    data = {'name': 'Maurilio Silva', 'gender': 'Masculino', 'company': 'Sky'}
    r = requests.post('http://localhost:5000/cliente/',data=data)
    print(r.json())

def teste_get_clienteid(id_product):
    r = requests.get('http://localhost:5000/cliente/{}'.format(id_product))
    print(r.json())

def lerjson():
    with open('clientes.json') as json_file:
        clientes = json.load(json_file)
        for cliente in clientes:
            names.append(cliente['name'])
            genders.append(cliente['gender'])
            companies.append(cliente['company'])

def loopPost():

    for i in (range(10000)):
        time.sleep(1)
        n = random.randint(0, len(names)-1)
        g = random.randint(0, len(genders)-1)
        c = random.randint(0, len(companies)-1)
        data = {'name': names[n], 'gender': genders[n], 'company': companies[c]} 
        teste_post01(data)
        print('loop: {}'.format(i))

#teste_get()
# teste_post()
#teste_get_clienteid(21)
print('Lendo json ...')
lerjson()
print('Iniciado loop ...')
loopPost()




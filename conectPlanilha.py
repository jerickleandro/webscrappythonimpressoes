import requests


from random import randint

import time

contador =0
while (contador < 10):
    contador = contador + 1
    valor = randint(0, 100) 
    r = requests.get("https://script.google.com/macros/s/AKfycbzPckLm1deRPLhA2OU5JGjIwNQqEQhq8kBK817hBaq2q8dHc7Cd/exec?temperatura="+str(valor))
    time.sleep(1)
    print(r.headers['content-type'])
    print(r.text)
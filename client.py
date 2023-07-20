import requests
import os
from dotenv import load_dotenv

load_dotenv()

base_url = 'http://127.0.0.1:5000/'
qr = 'qr'
add_product = 'add-product'
register = 'register'

params = {'stripe_key' : os.environ.get('stripe_secret_key')}

register = requests.post(base_url + register, params=params )
payload = {'currency' : 'usd', 'unit_amount': 1000, 'name' : 'oreo2'}
r = requests.get(base_url + add_product, params=payload)
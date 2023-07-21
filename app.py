from flask import Flask, request, send_file, current_app
import qrcode
import requests
import stripe

app = Flask(__name__)

@app.route('/')
def index():
    return "<p> Base </p>"

@app.route('/register', methods=['POST', 'GET'])
def register():
    args = request.args.to_dict()
    stripe.api_key = args['stripe_key']
    return 'OK', 200

@app.route('/add-product')
def add_product():
    args = request.args.to_dict()
    if 'name' not in args:
        return 'Bad Request', 400
    try:
        product = stripe.Product.create(name=args['name'])
        return product
    except:
        return 'Error', 500

@app.route('/create-price')
def create_price():
    args = request.args.to_dict()
    if 'currency' not in args and 'unit_amount' not in args and 'id' not in args:
        return 'Bad Request', 400
        
    currency = 'usd' if 'currency' not in args else args['currency']
    unit_amount = 1000 if 'unit_amount' not in args else args['unit_amount']
    id = args['id']
    try:
        price = stripe.Price.create(currency=currency, unit_amount=unit_amount, product=id)
        return price
    except:
        return 'Error', 500
    
@app.route('/qr/<priceid>')
def generate_qrcode(priceid):
    args = request.args.to_dict()
    # stripe token must be present
    payment_link = stripe.PaymentLink.create(line_items=[{"price": priceid, "quantity": 1}])
    payment_link_id = payment_link['id']
    url = payment_link['url']
    img = qrcode.make(url)
    img.save(f'./static/{payment_link_id}.png')
    return payment_link_id

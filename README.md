# QR-Stripe
A web service that generates QR codes for Stripe Payment Links.

# Setup
To start, you'll need to clone the repo. You can do this via GitHub Desktop or the terminal with: 
```
git clone https://github.com/alvinjz2/qr-stripe.git
```

Install any requirements using 
```
pip install -r requirements.txt
```
Create a .env file with your secret Stripe key. More info on this key can be found [here](https://stripe.com/docs/keys). The .env file should look something like this:
```
stripe_secret_key=sk_test_numbers
```

# Usage
Start the Flask app by running 
```
python -m flask run --debug

```

# Supported Features
To create payment links, you'll need to first create products. Then, create Prices for these products. Finally, payment links can be generated for prices. To see an overview of this process, see [this](https://stripe.com/docs/payment-links/api) page.
- Products can be created with the /add-product endpoint
- Prices can be created with the /create-price endpoint
- Generate a QR code for a price with the /qr/<priceid> endpoint
- View the generated QR codes with the /view/<priceid> endpoint

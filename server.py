#! /usr/bin/env python3.6
"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""

import os
from flask import Flask, render_template, redirect, request, url_for

import stripe
# This is your test secret API key.
stripe.api_key = 'sk_test_51ONgZlK2btjRP0oVdy5O9QMe9PeKY7w7mahXZAIeR3tY4Jz3kBwnQlETwzE4Sf4T39CiVuLh4jmYnzimuUTnn65J00tbWi2JGw'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

@app.route('/')
def home():
    # Render the checkout.html template
    return render_template('checkout.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/cancel')
def cancel():
    return render_template('cancel.html')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1ONgd7K2btjRP0oV1eArr2fD',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=url_for('success', _external=True),
            cancel_url=url_for('cancel', _external=True),

        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)



if __name__ == '__main__':
    app.run(host='localhost', port=4242, debug=True)
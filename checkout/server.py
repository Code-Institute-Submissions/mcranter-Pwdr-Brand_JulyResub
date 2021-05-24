# This example sets up an endpoint using the Flask framework. NON CI
# from stripe.com documentation.
import os
import stripe
import json

from flask import Flask, jsonify

app = Flask(__name__)

stripe.api_key = ('pk_test_51Igp6uAkbdkgFtr8wO7oDdioKa5VwcgRhgUm5bQo47wjY7aF4\
                  LDfs27cwvbrjRRIZAHJjyAU7smE6f8LYmN74fkD00yB5CzGPp')


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    data = json.loads(request.data)

    try:
        # See https://stripe.com/docs/api/checkout/sessions/create
        # for additional parameters to pass.
        # {CHECKOUT_SESSION_ID} is a string literal; do not change it!
        # the actual Session ID is returned in the
        # query parameter when your customer
        # is redirected to the success page.
        checkout_session = stripe.checkout.Session.create(
            success_url=(
                         'https://example.com/success.html?session_id={CHECKOUT_SESSION_ID}'),
            cancel_url='https://example.com/canceled.html',
            payment_method_types=['card'],
            mode='subscription',
            line_items=[{
                'price': data['priceId'],
                # For metered billing, do not pass quantity
                'quantity': 1
            }],
            )

            return jsonify({'sessionId': checkout_session['id']})
        except Exception as e:
            return jsonify({'error': {'message': str(e)}}), 400


@app.route('/webhook', methods=['POST'])
def webhook_received():
    webhook_secret = {{'STRIPE_WEBHOOK_SECRET'}}
    request_data = json.loads(request.data)

    if webhook_secret:
        # Retrieve the event by verifying the
        # signature using the raw body and
        # secret if webhook signing is configured.
        signature = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload=request.data,
                sig_header=signature, secret=webhook_secret)
            data = event['data']
        except Exception as e:
            return e
        # Get the type of webhook event sent -
        # used to check the status of PaymentIntents.
        event_type = event['type']
    else:
        data = request_data['data']
        event_type = request_data['type']
    data_object = data['object']

    if event_type == 'checkout.session.completed':
        # Payment is successful and the subscription is created.
        # You should provision the subscription and save the
        # customer ID to your database.
        print(data)
    elif event_type == 'invoice.paid':
        # Continue to provision the subscription as
        # payments continue to be made.
        # Store the status in your database and
        # check when a user accesses your service.
        # This approach helps you avoid hitting rate limits.
        print(data)
    elif event_type == 'invoice.payment_failed':
        # The payment failed or the customer does
        # not have a valid payment method.
        # The subscription becomes past_due.
        # Notify your customer and send them to the
        # customer portal to update their payment information.
        print(data)
    else:
        print('Unhandled event type {}'.format(event_type))

    return jsonify({'status': 'success'})

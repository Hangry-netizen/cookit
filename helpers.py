import braintree
from app import app

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id=app.config.get("BT_MERCHANT"),
        public_key=app.config.get("BT_PUBLIC"),
        private_key=app.config.get("BT_PRIVATE")
    )
)

def get_client_token():
    return gateway.client_token.generate()

def create_transaction(amount, nonce):
  return gateway.transaction.sale({
    "amount": "10.00",
    "payment_method_nonce": nonce,
    "options": {
      "submit_for_settlement": True
    }
})
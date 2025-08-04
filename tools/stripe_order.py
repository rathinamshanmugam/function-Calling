import stripe
stripe.api_key = "YOUR_STRIPE_SECRET_KEY"

def place_order(product, quantity, token):
    charge = stripe.Charge.create(
        amount=100 * quantity,  # $1 per item
        currency="usd",
        description=f"{quantity}×{product}",
        source=token
    )
    return {"status": charge.status, "id": charge.id}

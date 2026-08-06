import requests

def validate_intent(payment_id: str, key: str ):
    validate_response = requests.get(f"https://api.stripe.com/v1/payment_intents/{payment_id}",
    auth=(key, ""),
    timeout=30   
    )
    validate_response.raise_for_status()
    return validate_response.json()


def post_intent(payment_id: str, amount: int, key: str):
    post_intent_response = requests.post(f"https://api.stripe.com/v1/payment_intents/{payment_id}/increment_authorization",
    auth=(key, ""),
    data={"amount": amount, "description": "Charger not returned - non-return fee applied"},
    timeout=30
    )
    try:
        post_intent_response.raise_for_status()
    except requests.exceptions.HTTPError:
        raise RuntimeError(post_intent_response.json())

    return post_intent_response.json()
import os
import api_queries


def main():
    api_key = os.getenv("STRIPE_API_KEY")     # SET STRIPE KEY IN TERMINAL $env:STRIPE_API_KEY = "sk_live_..."
    if not api_key:
        raise RuntimeError("Missing STRIPE_API_KEY environment variable")
    payment_id = ""  # Fill in a PaymentIntent ID to retrieve, or leave empty to list recent ones
    amount = 5000  # Set a number e.g. 5000 = £50


    if amount is not None and payment_id:

        validated_response = api_queries.validate_intent(payment_id, api_key)
        if validated_response['status'] != "requires_capture":
            raise RuntimeError(
                f"{payment_id} is in state '{validated_response['status']}', expected 'requires_capture'"
                )

        updated_intent = api_queries.post_intent(payment_id, amount, api_key)
        if amount != updated_intent['amount']:
             raise RuntimeError(
                 f"Expected {amount} from API response, received {updated_intent['amount']}"
                )
        else:
            print(f"Updated PaymentIntent amount: {updated_intent['amount']}")

    else:
        raise RuntimeError("Fill in payment_id you want to target and amount to increment by")


if __name__ == "__main__":
    main()
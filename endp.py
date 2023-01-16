import json
import os
import mercadopago

def lambda_handler(event, context):

    sdk = mercadopago.SDK(os.environ["TEST_TOKEN"])
    
    payment_data = {
        "transaction_amount": float(event["transaction_amount"]),
        "token": event["token"],
        "installments": int(event["installments"]),
        "payment_method_id": event["payment_method_id"],
        "issuer_id": event["issuer_id"],
        "payer": {
            "email": event["payer"]["email"],
            "identification": {
                "type": event["payer"]["identification"]["type"], 
                "number": event["payer"]["identification"]["number"]
            },
        }
    }
    
    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]
    
    print("status =>", payment["status"])
    print("status_detail =>", payment["status_detail"])
    print("id=>", payment["id"])

    
    return {
        "statusCode": 200,
        "status": payment["status"],
        "status_detail": payment["status_detail"],
        "id": payment["id"],
        "body": payment,
    }
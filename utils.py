from kavenegar import *


def send_sms():
    try:
        api = KavenegarAPI(
            'API_key')
        params = {
            'sender': '',
            'receptor': '' ,
            'message': '',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)

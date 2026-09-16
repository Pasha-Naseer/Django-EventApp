from kavenegar import *

def send_otp_code(phone_number, code):

    try:
        api = KavenegarAPI('714E6A506A656A765A564A412B4D666F42466F42793956342B656C52394537496C2F4F70492B65554951493D')

        params = {
            'receptor': phone_number,
            'token': code,
            'template': 'SendOtpCode'
        }

        response = api.verify_lookup(params)

        return response

    except APIException as e:
        print(e)

    except HTTPException as e:
        print(e)




# from kavenegar import *
#
# KAVENEGAR_TEMPLATE = "SendOtpCode"
# def send_otp_code(phone_number, code):
#     try:
#         api = KavenegarAPI('714E6A506A656A765A564A412B4D666F42466F42793956342B656C52394537496C2F4F70492B65554951493D')
#         params = {
#             'sender': "0018018949161",
#             'receptor': phone_number,
#             'message': f"کد تایید شما {code}",
#         }
#         response = api.sms_send(params)
#     except APIException as e:
#         print(e)
#     except HTTPException as e:
#         print(e)
#
#


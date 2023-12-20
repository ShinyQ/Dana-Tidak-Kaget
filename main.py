from constant import get_phising_link, generate_data
import requests

i = 0

for _ in iter(int, 1):
    phising_link, phone_link, pin_link, otp_link = get_phising_link()
    data_phone, data_pin, data_otp = generate_data()
    
    resp_phone = requests.post(phone_link, data=data_phone)
    resp_pin = requests.post(pin_link, data=data_otp)
    resp_otp = requests.post(otp_link, data=data_pin)
    
    status = f'[{resp_phone.status_code}, {resp_pin.status_code}, {resp_otp.status_code}]'
    i += 1
    
    print(f'{i}. {phising_link}, Phone: {data_phone.get('nohp')}, Status: {status}')
    
    
    
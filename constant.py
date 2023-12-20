from helper import random_phone_number, random_single_number
import random

def generate_data():
    data_phone = {
        'nohp': random_phone_number()
    }

    data_pin = {
        'pin1': random_single_number(),
        'pin2': random_single_number(),
        'pin3': random_single_number(),
        'pin4': random_single_number(),
        'pin5': random_single_number(),
        'pin6': random_single_number(),
    }

    data_otp = {
        'otp1': random_single_number(),
        'otp2': random_single_number(),
        'otp3': random_single_number(),
        'otp4': random_single_number(),
    }
    
    return data_phone, data_pin, data_otp


def get_phising_link():
    phising_link = [
        'https://linkxzxc-dagetzz.danacareid.my.id',
        'https://linkd4gtz-ld-wb.bqx.my.id',
        'https://appdana.skom.id',
    ]
    
    link_choice = random.choice(phising_link)

    phone_link = link_choice + '/ast/req/3678fd6893fb190b400d9d618c79cf92.php'
    pin_link = link_choice + '/ast/req/2f68d4e0d386ee468cd061afc288d287.php'
    otp_link = link_choice + '/ast/req/9dd9f94bf970e28cfd0d1bbdac2879ce.php'

    return link_choice, phone_link, pin_link, otp_link
import requests
from concurrent.futures import ThreadPoolExecutor, wait
from constant import get_phising_link, generate_data, v2_link

def process_request(link, data):
    try:
        response = requests.post(link, data=data)
        status = response.status_code
    except requests.RequestException as e:
        print(f"Error during request: {e}")
        status = -1
        
    return status


def main():
    i = 0

    with ThreadPoolExecutor(max_workers=32) as executor:
        while True:
            phishing_link, phone_link, pin_link, otp_link = get_phising_link()
           
            type = 'v1'
            
            if phishing_link in v2_link:
               type = 'v2'
                
            data_phone, data_pin, data_otp = generate_data(type)

            phone = data_phone.get("nohp")
            
            if phishing_link in v2_link:
                phone = data_phone.get("phoneNumber")    
            
            futures = [
                executor.submit(process_request, phone_link, data_phone),
                executor.submit(process_request, pin_link, data_otp),
                executor.submit(process_request, otp_link, data_pin)
            ]

            wait(futures)

            resp_phone, resp_pin, resp_otp = [future.result() for future in futures]
            status = f'[{resp_phone}, {resp_pin}, {resp_otp}]'
            i += 1

            print(f'{i}. {phishing_link}, Phone: {phone}, Status: {status}')


if __name__ == "__main__":
    main()

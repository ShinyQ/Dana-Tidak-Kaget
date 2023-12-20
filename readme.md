## DANA Phishing Link Attacker

This Python script simulates a phishing attack by making concurrent HTTP requests to phishing links. It is designed to test the resilience of systems against phishing attempts, especially those involving phone number, PIN, and OTP links.

### Usage
To run the script, execute the main function in the provided main.py file:
```py
python main.py
```

### Dependencies
Make sure you have the required Python modules installed. You can install them using:
```bash
pip install requests
```
### Description
The script uses the requests library for making HTTP requests and ThreadPoolExecutor for concurrent processing. It includes a set of functions to generate phishing links and corresponding data for phone, PIN, and OTP requests. The process_request function sends a POST request to a given link with the provided data.

The main function (main) initiates the attack simulation by repeatedly fetching phishing links and generating data. It then concurrently sends requests to phone, PIN, and OTP links using a thread pool with a maximum of 32 workers. The results are printed, including the phishing link, phone number, and the status of each request.

### Customization
You can customize the script by modifying the get_phishing_link and generate_data functions in the constant.py file. Additionally, you may adjust the number of max_workers in the ThreadPoolExecutor for performance tuning.
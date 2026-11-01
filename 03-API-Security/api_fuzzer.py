import requests

# 1. Target endpoint configuration (Localhost or remote API gateway):
target_api_url = "http://localhost:8081/api/"

# 📄 Wordlist for directory and endpoint discovery (The Fuzzing Pool):
# Simulating a core automated directory fuzzing scenario inside the script:
wordlist = ["v1", "v2", "users", "admin", "login", "config", "secret_tokens"]

# 🛡️ Custom header for bug bounty and responsible disclosure tracking:
headers = {
    "X-HackerOne-Research": "ismayil_hadisov"
}

print(f"[*] API Fuzzing operation started on target: {target_api_url}...\n")

# 🔄 2. Main automation engine (The Fuzzer Loop):
for word in wordlist:
    
    # Dynamically inject the payload from the wordlist into the target URL:
    fuzz_url = f"{target_api_url}{word}"
    
    # 🛡️ Exception handling matrix:
    try:
        # Timeout set to 3 seconds to handle network latency effectively:
        response = requests.get(fuzz_url, headers=headers, timeout=3)
        
        # Checking for discovered paths (Any status code other than 404 Not Found):
        if response.status_code != 404:
            print(f"[+] DISCOVERED ENDPOINT: /{word} -> Status Code: {response.status_code}")
        else:
            # Silent pass to suppress negative noise from the terminal output:
            pass
            
    except requests.exceptions.RequestException:
        print(f"[-] Network error occurred while testing endpoint: /{word}")

print("\n[+] API FUZZING OPERATION COMPLETED SUCCESSFULLY!")



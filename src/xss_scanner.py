import requests

def check_xss(url):
    print(f"\nTesting {url} for reflected XSS...\n")

    # Basic payload variations
    payloads = [
        "<script>alert(1)</script>",
        "'><script>alert(1)</script>"
    ]

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    vulnerable = False

    for payload in payloads:
        target_url = f"{url}{payload}"
        print(f"Trying payload: {payload}")

        try:
            response = requests.get(target_url, headers=headers, timeout=5)

            # Convert to lowercase to avoid case mismatch
            if payload.lower() in response.text.lower():
                print("\nPossible reflected XSS detected!")
                print(f"Payload: {payload}")
                print(f"URL: {target_url}")
                vulnerable = True
                break

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            break

    if not vulnerable:
        print("\nNo reflected payload found.")
        

if __name__ == "__main__":
    print("Basic XSS Testing Script")
    print("Note: The URL should end with a parameter like ?q=\n")

    user_input = input("Target URL: ").strip()

    if user_input == "":
        print("You did not enter any URL.")
    else:
        check_xss(user_input)

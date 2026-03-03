import requests

def check_idor(url_pattern):
    print("\nChecking API for possible IDOR issues...")
    print(f"Pattern used: {url_pattern}\n")

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    found = False

    # Testing a small range of IDs for basic enumeration
    for user_id in range(1, 6):
        target_url = url_pattern.replace("{ID}", str(user_id))
        print(f"Trying ID: {user_id}")

        try:
            response = requests.get(target_url, headers=headers, timeout=5)

            # Basic validation: status code and response length
            if response.status_code == 200 and len(response.text) > 30:
                print(f"Possible unauthorized access to ID {user_id}")
                print(f"URL: {target_url}")
                print(f"Response preview: {response.text[:60]}...\n")
                found = True
            else:
                print(f"Access blocked or no data (Status: {response.status_code})\n")

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}\n")
            break

    if not found:
        print("No obvious IDOR behavior detected in tested range.")


if __name__ == "__main__":
    print("Basic API IDOR Test Script\n")
    print("Use {ID} in the URL where the object number changes.\n")
    
    url_input = input("Enter API pattern (example: https://site.com/users/{ID}): ").strip()

    if url_input:
        check_idor(url_input)
    else:
        print("No input provided.")

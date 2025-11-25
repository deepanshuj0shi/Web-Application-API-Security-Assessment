import requests

def check_idor(url_pattern):
    print(f"\n[+] Testing API for IDOR (Insecure Direct Object Reference)...")
    print(f"    Target Pattern: {url_pattern}")
    
    # Simulate an attacker trying IDs from 1 to 5
    # In a real attack, they might try thousands
    for user_id in range(1, 6):
        target = url_pattern.replace("{ID}", str(user_id))
        
        try:
            response = requests.get(target)
            
            # ANALYSIS:
            # If we get a 200 OK, it means we successfully accessed that object.
            # In a real secure system, trying to access another user's ID 
            # should return 403 Forbidden or 401 Unauthorized.
            if response.status_code == 200:
                print(f"  [+] Success! Accessed ID {user_id}: {target}")
                # Print a snippet of the private data found
                print(f"      Data leaked: {response.text[:50]}...")
            else:
                print(f"  [-] Access Denied for ID {user_id} (Status: {response.status_code})")
                
        except Exception as e:
            print(f"  [!] Connection error: {e}")

if __name__ == "__main__":
    # We use jsonplaceholder, a fake API for testing.
    # It acts like a vulnerable API because it lets anyone read any user.
    test_url = "https://jsonplaceholder.typicode.com/users/{ID}"
    
    check_idor(test_url)
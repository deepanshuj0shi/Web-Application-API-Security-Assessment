# Web Application & API Security Assessment Toolkit

# Project Overview
A comprehensive security assessment toolkit developed during my Infosys internship. This project translates manual penetration testing findings (originally discovered using Burp Suite and OWASP methodologies) into automated Python Proof-of-Concept (PoC) scripts.

# Features
- SQL Injection Scanner: Automates detection of Error-Based SQLi vulnerabilities in URL parameters.
- XSS Payload Tester: Verified Reflected Cross-Site Scripting (XSS) by analyzing server responses for payload reflection.
- API Access Control Tester: Simulates IDOR (Insecure Direct Object Reference) attacks to detect Broken Access Control in API endpoints.

# Technologies Used
- Python 3.x: For automation and exploit scripting.
- Requests Library: For HTTP manipulation and API interaction.
- OWASP Top 10: Testing methodology framework.
- DVWA (Damn Vulnerable Web App): Sandbox environment used for initial manual testing.

# Installation
1. Clone the repository:

   git clone [https://github.com/deepanshuj0shi/Web-Application-API-Security-Assessment.git](https://github.com/deepanshuj0shi/Web-Application-API-Security-Assessment.git)

2. Install dependencies:

pip install requests

Usage
1. SQL Injection Scan
Tests a target URL for database errors.

python src/sqli_tester.py

2. XSS Scan
Tests if a script tag is reflected in the page.

python src/xss_scanner.py

3. API IDOR Test

Iterates through user IDs to check for unauthorized data access.

python src/api_tester.py

Contact

Deepanshu Joshi

Email: deepanshujoshi212@gmail.com

LinkedIn: deepanshujoshi2
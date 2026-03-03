# Web Application & API Security Assessment Toolkit

# Project Overview
I built this project during my winter break to understand how common web vulnerabilities are detected at a practical level.
Instead of only using tools like Burp Suite or automated scanners, I wanted to manually implement basic detection logic using Python. This helped me understand how payload injection, response analysis, and object enumeration actually work behind the scenes.

The toolkit focuses on three common OWASP Top 10 issues:

Error-Based SQL Injection
Reflected Cross-Site Scripting (XSS)
Insecure Direct Object Reference (IDOR) in APIs
This project is intended for learning and testing in controlled environments only.

# Features
1. SQL Injection Tester
Injects common SQL payloads into URL parameters
Checks server responses for database error patterns
Logs potential findings into a local file
Uses basic header simulation and timeout handling

Detection Type: Error-Based SQL Injection

2. Reflected XSS Tester
Injects script payloads into input parameters
Checks if payload appears in server response
Uses multiple payload variations
Performs case-insensitive matching

Detection Type: Basic Reflected XSS

3. API IDOR Tester
Performs object ID enumeration (e.g., /users/{ID})
Checks if different IDs are accessible
Validates response status and data length
Simulates basic unauthorized access attempts

Detection Type: Basic ID Enumeration

# Technologies Used
Python 3
Requests Library
Basic HTTP header manipulation
OWASP Top 10 methodology (learning reference)

# LEARNING OUTCOME
Through this project, I gained practical understanding of:

How user input affects backend queries
How reflected payloads appear in HTTP responses
How broken access control can be detected through enumeration
How basic vulnerability detection logic works internall

# Contact

Deepanshu Joshi
Email: deepanshujoshi212@gmail.com
LinkedIn: deepanshujoshi2

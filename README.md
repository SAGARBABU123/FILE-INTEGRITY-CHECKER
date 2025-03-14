# codeTech TASK 1
This project is a simple File Integrity Checker built using Python. It calculates the SHA-256 hash of a file to verify its integrity. SHA-256 is a cryptographic hash function that generates a unique 256-bit hash value for any given file.

Features:-
✅ Accepts file path input from the user.
✅ Calculates the SHA-256 hash of the file.
✅ Displays the hash value to verify file integrity.
✅ Handles file reading errors gracefully.
✅ (Optional) Displays output in a graphical window using tkinter.
✅ (Optional) Saves the hash value to a text file (hash_output.txt) for future reference.

🏗️ How It Works:-
The program takes a file path as input.
It reads the file in chunks (to handle large files).
It computes the SHA-256 hash of the file content using the hashlib library.
The computed hash is displayed to the user.
(Optional) The hash value can be shown in a pop-up window or saved to a text file.

🛠️ Technologies Used:-
Python – Main programming language
hashlib – For SHA-256 hashing
tkinter – For graphical user interface (optional)

🙌 Contributors
GUDIPUDI SAGAR BABU – Developer

# codeTech TASK 2

📄 Project Description
🚀 Web Application Vulnerability Scanner
This project is a Python-based Web Application Vulnerability Scanner that helps identify common security weaknesses in web applications. It checks for two major vulnerabilities:

SQL Injection (SQLi)
Cross-Site Scripting (XSS)
The scanner uses Python libraries like Requests and BeautifulSoup to send HTTP requests, analyze HTML forms, and test for vulnerabilities.

🏆 Purpose
To create a security tool that helps developers and security professionals identify vulnerabilities in their web applications.
To provide a simple and effective way to test for common web application security issues.
To automate the testing process for quicker vulnerability detection.
🛠️ How It Works
✅ 1. Extract Forms from the Website
The scanner sends a GET request to the target URL using the requests library.
It parses the HTML content using BeautifulSoup.
All available forms on the page are extracted and analyzed.
✅ 2. Test for XSS Vulnerability
A JavaScript payload (<script>alert('XSS')</script>) is injected into the form fields.
The scanner submits the form using POST or GET requests.
If the payload is reflected in the server response, the site is vulnerable to XSS.
✅ 3. Test for SQL Injection Vulnerability
A malicious SQL query (' OR '1'='1) is sent to the target URL.
If the server response contains database errors or sensitive information, the site is vulnerable to SQL Injection.
✅ 4. Display Results
If a vulnerability is found, it shows a warning with the target URL.
If no vulnerability is found, it confirms that the site is safe.

🌟 Technologies Used
✅ Python
✅ Requests (for HTTP requests)
✅ BeautifulSoup (for parsing HTML)

🚀 Features
✔️ Identifies forms on a webpage
✔️ Tests for SQL Injection vulnerabilities
✔️ Tests for XSS vulnerabilities
✔️ Outputs clear and detailed results

📌 Why It’s Useful
🔐 Helps secure web applications from common attacks.
🚀 Fast and automated vulnerability scanning.
💡 Easy to extend and modify for more complex testing.

🔥 Future Improvements
✅ Add more vulnerability checks (e.g., CSRF, Directory Traversal)
✅ Improve result analysis and reporting
✅ Add support for scanning multiple pages



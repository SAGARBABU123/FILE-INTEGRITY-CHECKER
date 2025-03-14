import requests
from bs4 import BeautifulSoup

def get_forms(url):
    """Extract all form tags from the HTML content."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    forms = soup.find_all("form")
    return forms

def test_sql_injection(url):
    """Test for SQL Injection vulnerability."""
    payload = "' OR '1'='1"
    response = requests.get(f"{url}{payload}")
    if "error" in response.text.lower():
        print(f"[!] SQL Injection vulnerability detected at {url}")
    else:
        print(f"[✔] No SQL Injection vulnerability detected at {url}")

def test_xss(url):
    """Test for XSS vulnerability."""
    xss_payload = "<script>alert('XSS')</script>"
    response = requests.get(f"{url}{xss_payload}")
    if xss_payload in response.text:
        print(f"[!] XSS vulnerability detected at {url}")
    else:
        print(f"[✔] No XSS vulnerability detected at {url}")

def main():
    url = input("Enter the URL to scan: ")
    
    # Step 1: Get all forms
    print("\n[+] Searching for forms...")
    forms = get_forms(url)
    if forms:
        print(f"[+] {len(forms)} forms found!")
    else:
        print("[!] No forms found.")

    # Step 2: Test for SQL Injection
    print("\n[+] Testing for SQL Injection...")
    test_sql_injection(url)

    # Step 3: Test for XSS
    print("\n[+] Testing for XSS...")
    test_xss(url)

if __name__ == "__main__":
    main()

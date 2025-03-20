import requests
import whois
import json

def ip_lookup(ip):
url = f"http://ipwho.is/{ip}"
response = requests.get(url)
return response.json() if response.status_code == 200 else {"error": "Failed to fetch data"}

def domain_whois(domain):
try:
w = whois.whois(domain)
return w.text
except Exception as e:
return {"error": str(e)}

def subdomain_finder(domain):
url = f"https://crt.sh/?q=%25.{domain}&output=json"
response = requests.get(url)
if response.status_code == 200:
subdomains = set(entry['name_value'] for entry in response.json())
return list(subdomains)
return {"error": "Failed to fetch data"}

def user_lookup(username):
url = f"https://api.github.com/users/{username}"
response = requests.get(url)
return response.json() if response.status_code == 200 else {"error": "User not found"}

def main():
while True:
print("\nOSINT Tool:")
print("User    : Not logged in yet")
print("Owner   : Hazelnuttty")
print("Mode    : Public")
print("Premium : No\n")
print("1. IP Lookup")
print("2. Domain WHOIS")
print("3. Subdomain Finder")
print("4. User Lookup")
print("5. Exit")
choice = input("Choose an option: ")

    if choice == "1":
        ip = input("Enter IP: ")
        print(json.dumps(ip_lookup(ip), indent=4))
    elif choice == "2":
        domain = input("Enter domain: ")
        print(domain_whois(domain))
    elif choice == "3":
        domain = input("Enter domain: ")
        print(json.dumps(subdomain_finder(domain), indent=4))
    elif choice == "4":
        username = input("Enter username: ")
        print(json.dumps(user_lookup(username), indent=4))
    elif choice == "5":
        print("Follow my TikTok account!")
        break
    else:
        print("Invalid choice! Try again.")


if name == "main":
main()


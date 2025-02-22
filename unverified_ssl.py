import requests

# BAD: Ignores SSL verification
response = requests.get("https://untrusted-root.badssl.com/", verify=False)
print(response.text)

import requests
from bs4 import BeautifulSoup
import re

# Step 1: Fetch webpage content
url = 'https://free-proxy-list.net/'  # Replace with the actual URL
response = requests.get(url)
html_content = response.text
# print(html_content)

# # Step 2: Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
print(soup.prettify())

# Step 3: Extract IP addresses using regex
ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
ip_addresses = ip_pattern.findall(soup.get_text())

# Step 4: Manually count IP addresses
ip_counts = {}
for ip in ip_addresses:
    if ip in ip_counts:
        ip_counts[ip] += 1
    else:
        ip_counts[ip] = 1

# Step 5: Print IP addresses and their counts
for ip, count in ip_counts.items():
    print(f'{ip}: {count}')

# Step 6: Save to a CSV file (manually)
with open('ip_addresses.csv', 'w') as file:
    file.write('IP Address,Count\n')
    for ip, count in ip_counts.items():
        file.write(f'{ip},{count}\n')

# Step 7: Additional analysis: count unique IP addresses
unique_ips = len(ip_counts)
print(f'Total unique IP addresses: {unique_ips}')






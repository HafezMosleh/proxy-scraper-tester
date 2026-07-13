import urllib.request, re, time
print("🔍 Proxy Scraper & Tester")
print("Scraping free proxies...")
try:
    req = urllib.request.Request("https://free-proxy-list.net/", headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req, timeout=10).read().decode('utf8')
    ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+', html)
    print(f"Found {len(ips)} proxies. Testing first 5...")
    for ip in ips[:5]:
        print(f"Testing {ip}...")
        time.sleep(0.5)
except Exception as e:
    print("Error:", e)

import requests
import threading

def check_url(url):
    try:
        response = requests.get(url, allow_redirects=False, timeout=3)
        if response.status_code == 200:
            print(f"[+] {url} - {len(response.content)} bytes")
    except requests.exceptions.RequestException:
        pass

def fuzz_wordlist(url, wordlist):
    for word in wordlist:
        check_url(url + "/" + word.strip())

def fuzz_extensions(url, extensions):
    for ext in extensions:
        check_url(url + "/" + "test" + ext)

def fuzz(url, wordlist=None, extensions=None, use_headers=False, use_proxy=False):
    if use_headers:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Referer": "https://www.google.com/",
            "Cookie": "test=123;"
        }
    else:
        headers = None

    if use_proxy:
        proxies = {
            "http": "http://127.0.0.1:8080",
            "https": "https://127.0.0.1:8080"
        }
    else:
        proxies = None

    # Fuzz with wordlist
    if wordlist:
        with open(wordlist) as f:
            wordlist_lines = f.readlines()
        threads = []
        for i in range(10):
            start = i * int(len(wordlist_lines) / 10)
            end = (i + 1) * int(len(wordlist_lines) / 10)
            thread = threading.Thread(target=fuzz_wordlist, args=(url, wordlist_lines[start:end],))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

    # Fuzz with extensions
    if extensions:
        threads = []
        for ext in extensions:
            thread = threading.Thread(target=fuzz_extensions, args=(url, [ext],))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

if __name__ == '__main__':
    fuzz("https://example.com", wordlist="wordlist.txt", extensions=[".bak", ".swp"], use_headers=True, use_proxy=False)

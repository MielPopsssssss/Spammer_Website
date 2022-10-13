# Mielpopsssssss Spammer in Python

import requests
import sys
import time
import threading
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def spam_request(url, headers, data, method, proxy, timeout, delay, threads, verbose):
    if verbose:
        print("Starting to spam request to: " + url)
    if proxy:
        proxies = {"http": proxy, "https": proxy}
    else:
        proxies = None
    if method == "GET":
        data = None
    elif method == "POST":
        data = data
    else:
        print("Invalid HTTP method")
        sys.exit(1)
    if threads > 1:
        for i in range(threads):
            t = threading.Thread(target=spam_request, args=(url, headers, data, method, proxy, timeout, delay, 1, verbose))
            t.start()
    else:
        while True:
            try:
                r = requests.request(method, url, headers=headers, data=data, proxies=proxies, verify=False, timeout=timeout)
                if verbose:
                    print("Request sent to: " + url)
            except:
                if verbose:
                    print("Request failed to: " + url)
            time.sleep(delay)



if __name__ == "__main__":
    if len(sys.argv) < 8:
        print("Usage: python3 spammer.py <url> <headers> <data> <method> <proxy> <timeout> <delay> <threads> <verbose>")
        sys.exit(1)
    url = sys.argv[1]
    headers = sys.argv[2]
    data = sys.argv[3]
    method = sys.argv[4]
    proxy = sys.argv[5]
    timeout = int(sys.argv[6])
    delay = int(sys.argv[7])
    threads = int(sys.argv[8])
    verbose = sys.argv[9]
    if verbose == "True":
        verbose = True
    else:
        verbose = False
    spam_request(url, headers, data, method, proxy, timeout, delay, threads, verbose)
# Spammer_Website

How it works:

1. Import the libraries
2. Define the spam_request function
3. Check if the user wants to use a proxy
4. Check if the user wants to use multiple threads
5. Start the spamming



Instructions:

1. Install the requirements
2. Run the script
3. Enter the website URL
4. Enter the number of requests
5. Enter the number of threads (optional)
6. Enter the proxy (optional)
7. Wait for the spamming to finish
8. Enjoy ;)

## Requirements

- requests
- urllib3
- threading

## How to use it

```python
python spammer.py <url> <method> <threads> <delay> <timeout> <proxy> <verbose>
```

* exemple of use:
```bash
python3 spammer.py https://example.com GET 1 0 5 None True
python spammer.py https://example.com POST 1 0 5 None True

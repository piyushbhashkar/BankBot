# BankBot - Proxy Configuration Guide

## Problem
The application works on your MacBook but fails in the office due to proxy authentication (HTTP 407 error).

## Solution
Added proxy configuration support that works in both environments.

---

## Setup Instructions

### Step 1: Copy the new files to your project

1. Copy `proxy_config.py` to your project root directory (same level as `app.py`)

2. Replace your existing files with the updated versions:
   - `app.py`
   - `store_index.py`

### Step 2: Configure your office proxy

Open `proxy_config.py` and update these values:

```python
PROXY_ENABLED = True  # Set to False on your MacBook

PROXY_HOST = "your-proxy-server.com"  # Replace with actual proxy server
PROXY_PORT = "8080"                    # Replace with actual port
PROXY_USERNAME = "your-username"       # Your office network username
PROXY_PASSWORD = "your-password"       # Your office network password
```

**Get these details from your IT department:**
- Proxy server address (e.g., `proxy.company.com` or IP like `10.0.0.1`)
- Proxy port (commonly `8080`, `3128`, or `80`)
- Your network credentials

### Step 3: Switch between office and home

**At Office:**
```python
PROXY_ENABLED = True
```

**On MacBook (no proxy):**
```python
PROXY_ENABLED = False
```

---

## What Changed?

### 1. Added `proxy_config.py`
- Centralizes all proxy settings
- Easy to switch between office/home
- Automatically configures all HTTP requests

### 2. Updated `app.py`
Added these lines at the top:
```python
from proxy_config import setup_proxy
setup_proxy()
```

### 3. Updated `store_index.py`
Added the same proxy setup lines

---

## Testing

After configuration, test the connection:

```python
# Test script (save as test_proxy.py)
from proxy_config import setup_proxy
import requests

setup_proxy()

try:
    response = requests.get('https://www.google.com', timeout=10)
    print(f"✓ Proxy working! Status: {response.status_code}")
except Exception as e:
    print(f"✗ Proxy error: {e}")
```

---

## Troubleshooting

### Error: "407 Proxy Authentication Required"
- ✓ Verify username/password are correct
- ✓ Check if special characters in password need URL encoding
- ✓ Confirm proxy server address and port with IT

### Error: "SSL Certificate verification failed"
Your office may use SSL inspection. Add this to `proxy_config.py`:
```python
os.environ['REQUESTS_CA_BUNDLE'] = ''
os.environ['CURL_CA_BUNDLE'] = ''
```

### Still not working?
1. Contact IT to confirm proxy details
2. Ask if specific domains need whitelisting:
   - `api.openai.com`
   - `api.pinecone.io`
   - `huggingface.co`
3. Check if VPN is required

---

## Security Note

**Never commit `proxy_config.py` with your credentials to GitHub!**

Add to `.gitignore`:
```
proxy_config.py
```

Create a template instead:
```bash
cp proxy_config.py proxy_config.template.py
# Edit template to remove actual credentials
```

---

## Running the Application

Same as before:

```bash
# First time: Create index
python store_index.py

# Run the app
python app.py
```

The proxy will be automatically configured based on your `proxy_config.py` settings.

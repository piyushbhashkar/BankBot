"""
Proxy Configuration for Office Network
Replace the placeholder values with your actual office proxy details
"""
import os

# ========================================
# CONFIGURE YOUR OFFICE PROXY HERE
# ========================================
# Get these details from your IT department

PROXY_ENABLED = True  # Set to False to disable proxy (for local MacBook)

PROXY_HOST = "your-proxy-server.com"  # e.g., "proxy.company.com"
PROXY_PORT = "8080"  # e.g., "8080" or "3128"
PROXY_USERNAME = "your-username"  # Your office network username
PROXY_PASSWORD = "your-password"  # Your office network password

# ========================================
# DO NOT MODIFY BELOW THIS LINE
# ========================================

def setup_proxy():
    """
    Configure proxy settings for all HTTP/HTTPS requests
    Call this function at the start of your application
    """
    if not PROXY_ENABLED:
        print("Proxy disabled - running in local mode")
        return
    
    # Construct proxy URL with authentication
    if PROXY_USERNAME and PROXY_PASSWORD:
        proxy_url = f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{PROXY_HOST}:{PROXY_PORT}"
    else:
        proxy_url = f"http://{PROXY_HOST}:{PROXY_PORT}"
    
    # Set environment variables for proxy
    os.environ['HTTP_PROXY'] = proxy_url
    os.environ['HTTPS_PROXY'] = proxy_url
    os.environ['http_proxy'] = proxy_url
    os.environ['https_proxy'] = proxy_url
    
    print(f"Proxy configured: {PROXY_HOST}:{PROXY_PORT}")
    
    # Also set for specific libraries
    os.environ['REQUESTS_CA_BUNDLE'] = ''  # Disable SSL verification if needed
    
    return proxy_url


def get_proxy_dict():
    """
    Returns a dictionary for use with requests library
    """
    if not PROXY_ENABLED:
        return None
    
    if PROXY_USERNAME and PROXY_PASSWORD:
        proxy_url = f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{PROXY_HOST}:{PROXY_PORT}"
    else:
        proxy_url = f"http://{PROXY_HOST}:{PROXY_PORT}"
    
    return {
        'http': proxy_url,
        'https': proxy_url
    }

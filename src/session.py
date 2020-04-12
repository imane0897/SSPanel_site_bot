"""
Request session login for user and auto retry
"""
import requests
from info import base_url, email, password
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


def login():
    """Login for current user and return cookies"""

    login_url = base_url + "auth/login"
    user_info = {"email": email, "passwd": password}

    s = requests_retry_session()
    s.post(login_url, data=user_info)

    return s


def requests_retry_session(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504), session=None):
    """Retry 3 times if a request encounter problems excludes 500 errors"""

    session = session or requests.Session()
    retry = Retry(total=retries, read=retries, connect=retries,
                  backoff_factor=backoff_factor, status_forcelist=status_forcelist)
    
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    return session

import requests

def get_device_status(device_id, token):
    url = f"https://graph.microsoft.com/v1.0/devices/{device_id}"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.get(url, headers=headers).json()
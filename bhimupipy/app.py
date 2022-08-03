import json
import requests

def verify_upi(vpa):
    headers = {
        "sec-ch-ua": 'Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101.0.1210.47',
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "channel-id": "WEB_UNAUTH",
        "sec-ch-ua-platform": "Windows",
        "Origin": "https://www.airtel.in",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.airtel.in/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
    }
    try:
        req = requests.get(
            'https://paydigi.airtel.in/web/pg-service/v1/validate/vpa/' + vpa, headers=headers)
        # print(req.status_code, req.text)
        return req.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


# verify_upi("sumithemmadi@ybl")

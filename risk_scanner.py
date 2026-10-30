import os
import requests
import json

# RapidAPI Configuration
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY_HERE")
RISK_HOST = "domain-and-risk-profiler.p.rapidapi.com"  # Update host from Rapid Studio if needed

def check_domain_risk(domain):
    url = f"https://{RISK_HOST}/"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RISK_HOST
    }
    params = {"domain": domain}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            print("⚠️ Quota Exceeded! Upgrade to Pro ($29/mo) or Ultra ($99/mo) on RapidAPI.")
            return None
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return None

def main():
    target = "example.com"
    print(f"--- Running Security Risk Scan for {target} ---\n")
    
    result = check_domain_risk(target)
    if result and result.get("success"):
        print(json.dumps(result.get("data", {}), indent=2))
    else:
        print("Scan failed or returned error.")

if __name__ == "__main__":
    main()

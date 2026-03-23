import requests
import os
from dotenv import load_dotenv

def check_rate_limit():
    load_dotenv()

    url = "https://nmzkkypjourlffqrzpkq.supabase.co/functions/v1/api/v1/homebrew/spells"
    headers = {"x-api-key": os.getenv("API_KEY")}

    print("Checking rate limit...")
    try:
        # Using GET with stream=True so we only read headers efficiently
        response = requests.get(url, headers=headers, stream=True)
        
        remaining = response.headers.get("X-Ratelimit-Remaining") or response.headers.get("x-ratelimit-remaining")
        limit = response.headers.get("X-Ratelimit-Limit") or response.headers.get("x-ratelimit-limit")
        reset = response.headers.get("X-Ratelimit-Reset") or response.headers.get("x-ratelimit-reset")
        
        if remaining:
            print(f"✅ Rate Limit Remaining: {remaining}")
            if limit:
                print(f"📊 Rate Limit Max: {limit}")
            if reset:
                print(f"⏱️  Rate Limit Resets At: {reset}")
        else:
            print("⚠️ Rate Limit header not found.")
            
            # Look for alternative header variations
            rate_headers = {k: v for k, v in response.headers.items() if 'rate' in k.lower() or 'limit' in k.lower()}
            if rate_headers:
                print("\nFound alternative rate limit headers:")
                for k, v in rate_headers.items():
                    print(f"  {k}: {v}")
                    
        response.close()
            
    except Exception as e:
        print(f"Failed to check rate limit: {e}")

if __name__ == "__main__":
    check_rate_limit()

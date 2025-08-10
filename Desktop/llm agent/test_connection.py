import requests

url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_films"
print(f"Attempting to connect to: {url}")

try:
    # Use a timeout to prevent it from hanging forever
    response = requests.get(url, timeout=15)

    # Check if the request was successful (status code 200 means OK)
    if response.status_code == 200:
        print("\nSUCCESS: Connection successful!")
        print(f"Status Code: {response.status_code}")
    else:
        print(f"\nFAILURE: Connection was made, but failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    # This block will run if there's a network error, like a firewall block
    print(f"\nFAILURE: A connection error occurred. This is likely a firewall or network issue.")
    print(f"Error details: {e}")
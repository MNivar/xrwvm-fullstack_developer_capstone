# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    params = ""
    if (kwargs):
        for key, value in kwargs.items():
            params= params + key + "=" + value + "&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        # If any error occurs
        print(f"Error: {e}")
        print("Network exception occurred")


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        # Check if the response is successful
        if response.status_code == 200:
            
            try:
                # Attempt to parse JSON response
                result = response.json()
                print(f"Sentiment Analysis Result: {result}")
                return result
            except ValueError as e:
                # Handle case where response is not valid JSON
                print(f"Error parsing JSON: {e}")
                return {'sentiment': 'Unknown'}
        else:
            # Handle case where response status is not OK
            print(f"Unexpected HTTP status code: {response.status_code}")
            return {'sentiment': 'Unknown'}
    except requests.RequestException as e:
        # Handle network-related errors
        print(f"Network exception occurred: {e}")
        return {'sentiment': 'Unknown'}

# def post_review(data_dict):
#     request_url = backend_url+"/insert_review"
#     try:
#         response = requests.post(request_url,json=data_dict)
#         print(response.json())
#         return response.json()
#     except:
#         print("Network exception occurred")
def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
        
    except requests.RequestException as e:
        print(f"Network exception occurred: {e}")
        return {"status": 500, "message": "Internal server error"}

        

import requests
import logging

# Configure logging (you can adjust the logging level as needed)
logging.basicConfig(level=logging.INFO)

def generate_response(query):
    try:
        # Make the POST request to the Ollama API
        response = requests.post(OLlama_API_URL, json={'query': query})
        
        # Log the raw response content for debugging
        logging.info(f"Response Content: {response.text}")
        
        # Assuming the response is in JSON format, parse and return the 'message' content
        return response.json()['message']['content']
    
    except requests.exceptions.RequestException as e:
        # Handle other exceptions like network issues or timeout
        logging.error(f"Request Error: {e}")
        logging.error(f"Response Content: {response.text}")
        return "Sorry, there was an error processing your request."
    
    except requests.exceptions.JSONDecodeError as e:
        # Handle JSON decoding errors
        logging.error(f"JSON Decode Error: {e}")
        logging.error(f"Response Content: {response.text}")
        return "Sorry, there was an issue with the response format."

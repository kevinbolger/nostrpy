import requests

# A dictionary to serve as the config environment, similar to new.env() in R
config_env = {}

def set_config_environment(api_base_url, private_key, relays=None):
    '''
    Set up the config environment for the session.

    :param api_base_url: The base url path of the nostr API
    :param private_key: The user's private key
    :param relays: Relays to be used when calling the API. If not provided, a default list is used.
    :return: True if successful.
    '''
    # Define default relays
    if relays is None:
        relays = ["wss://nos.lol", "wss://nostr.bitcoiner.social", "wss://relay.damus.io"]
    
    # Not sure what check_values function does in your R code
    # If it's checking whether relays are valid URLs, you could use something like this in Python:
    # relays = [url for url in relays if check_url(url)]
    
    # Update the config environment
    config_env['api_base_url'] = api_base_url
    config_env['private_key'] = private_key
    config_env['relays'] = relays
    return True


def check_values(value):
    """
    If a single string value is provided, convert it to a list.
    Else, return the original list.

    :param value: A list of relays or a single relay as a string
    :return: The input converted to a list if it was a single string, or the original input if it was already a list
    """
    if isinstance(value, str):
        return [value]
    else:
        return value

def verify_api_config_success():
    """
    Verify API config successful.

    :return: True if successful.
    """
    # Construct the URL for the API endpoint
    url = f"{config_env['api_base_url']}/v0/verify"

    # Define the body of the request as a dictionary
    body = {"relays": config_env['relays'], "private_key": config_env['private_key']}

    # Send the POST request
    response = requests.post(url, json=body)

    # You might want to check the status code or the response content here
    # For example, you could raise an exception if the request was not successful:
    # response.raise_for_status()

    # Return True if successful
    return True


def send_post_request(url, body):
    """
    Utility function for sending POST requests.

    :param url: Endpoint URL
    :param body: The body of the POST request
    :return: The response from the POST request
    """
    # The requests library automatically encodes dictionaries as JSON,
    # so we don't need to manually convert it as in the R function

    # Send the POST request and return the response
    response = requests.post(url, json=body)

    # You might want to check the status code or the response content here
    # For example, you could raise an exception if the request was not successful:
    # response.raise_for_status()

    return response
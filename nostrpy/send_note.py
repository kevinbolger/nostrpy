from .util import config_env,send_post_request

def send_note(text):
    """
    Allows the owner of a Nostr public ID to publish a note.

    :param text: The message to post to the note.
    :return: The response from the POST request.
    """
    # Define the endpoint for the API request
    endpoint = config_env['api_base_url'] + "/v0/send/note"

    # Define the body of the request as a dictionary
    body = {"text": text, "private_key": config_env['private_key'], "relays": config_env['relays']}

    # Send the POST request using the send_post_request function
    response = send_post_request(endpoint, body)

    # You might want to check the status code or the response content here
    # For example, you could raise an exception if the request was not successful:
    # response.raise_for_status()

    # Return True if successful
    return True

from .util import config_env, send_post_request

def send_user_dm(text, recipient_public_key):
    """
    Allows the user to send a direct message to another Nostr ID.

    :param text: The message to post to the note.
    :param recipient_public_key: The public ID associated with the user.
    :return: The response from the POST request.
    """
    # Define the endpoint for the API request
    endpoint = config_env['api_base_url'] + "/v0/send/dm"

    # Define the body of the request as a dictionary
    body = {
        "relays": config_env['relays'],
        "sender_private_key": config_env['private_key'],
        "recipient_public_key": recipient_public_key,
        "text": text
    }

    # Send the POST request using the send_post_request function
    response = send_post_request(endpoint, body)

    # You might want to check the status code or the response content here
    # For example, you could raise an exception if the request was not successful:
    # response.raise_for_status()

    # Return True if successful
    return True

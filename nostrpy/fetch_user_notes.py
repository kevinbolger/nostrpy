from .util import config_env, send_post_request, check_values

def fetch_user_notes(authors=None, event_refs=None, pubkey_refs=None, since=None, until=None, limit=2000):
    """
    Looks up notes posted by a user.

    :param authors: List or string of npub or HEX formatted author(s)
    :param event_refs: List or string of event references
    :param pubkey_refs: List or string of pub key references
    :param since: INT of interval start
    :param until: INT of interval termination
    :param limit: INT of #notes to fetch per relay (Defaults to 2000)
    :return: Result stored in json format
    """
    authors = check_values(authors)
    event_refs = check_values(event_refs)
    pubkey_refs = check_values(pubkey_refs)

    # Define the endpoint for the API request
    endpoint = config_env['api_base_url'] + "/v0/fetch/notes"

    # Define the body of the request as a dictionary
    body = {
        "relays": config_env['relays'],
        "authors": authors,
        "event_refs": event_refs,
        "pubkey_refs": pubkey_refs,
        "since": since,
        "until": until,
        "limit": limit
    }

    # Send the POST request using the send_post_request function
    response = send_post_request(endpoint, body)

    # Parse the JSON response and store the result
    json_result = response.json()

    # Return the result
    return json_result

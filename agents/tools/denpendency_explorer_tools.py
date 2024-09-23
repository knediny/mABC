from data.trace_collect import TraceExplorer

def get_endpoint_downstream(endpoint: str) -> list:
    """
    This function retrieves the downstream endpoints of a given endpoint called by the given endpoint.

    Parameters:
    - endpoint (str): The unique identifier of the endpoint to be queried.

    Returns:
    - list: A list of strings, each representing a downstream endpoint called by the given endpoint.
    """
    traceExplorer = TraceExplorer()
    return traceExplorer.get_endpoint_downstream(endpoint)

def get_endpoint_downstream_in_range(endpoint: str, minute: str) -> list:
    """
    This function retrieves the downstream endpoints of a given endpoint called by the given endpoint.
    The time range is centered around the provided time, spanning from 15 minutes before to 5 minutes after.

    Parameters:
    - endpoint (str): The unique identifier of the endpoint to be queried.
    - minute (str): The central time point around which the statistics are to be queried, formatted as "YYYY-MM-DD HH:MM:SS". 

    Returns:
    - dict: A dictionary containing a list downstream endpoint for the given endpoint over the specified time range. 
    The dictionary consists of key-value pairs, where the key is the time point and the value is a list of downstream endpoints.
    """
    traceExplorer = TraceExplorer()
    return traceExplorer.get_endpoint_downstream_in_range(endpoint, minute)


def get_endpoint_upstream(endpoint: str) -> list:
    """
    This function retrieves the upstream endpoints of a given endpoint which calls the given endpoint.

    Parameters:
    - endpoint (str): The unique identifier of the endpoint to be queried.

    Returns:
    - list: A list of strings, each representing an upstream endpoint which calls the given endpoint.
    """
    traceExplorer = TraceExplorer()
    return traceExplorer.get_endpoint_upstream(endpoint)

def get_call_chain_for_endpoint(endpoint: str) -> list:
    """
    This function retrieves the call chain for a given endpoint, which consists of the upstream and downstream endpoints of the given endpoint.

    Parameters:
    - endpoint (str): The unique identifier of the endpoint to be queried.

    Returns:
    - dict: A dictionary containing the call chain for the given endpoint.
    The dictionary includes the following keys:
        - 'upstream' (list): A list of tuples, each representing an upstream endpoint which calls the given endpoint and the level distance from the given endpoint.
        - 'downstream' (list): A list of tuples, each representing a downstream endpoint which is called by the given endpoint and the level distance from the given endpoint.
    """
    traceExplorer = TraceExplorer()
    return traceExplorer.get_call_chain_for_endpoint(endpoint)



from data.metric_collect import MetricExplorer

# endpoint: String type, indicating the name of the API endpoint, such as "GET:/api/v1/orderservice/order/security/{checkDate}/{accountId}".
# minute: String type, following the format of "YYYY-MM-DD HH:MM", indicating the time corresponding to the statistical data. For example "2024-01-09 09:00".
# calls: Integer, indicating the number of calls to the corresponding endpoint at a given point in time.
# success_rate: Floating point type, indicating the percentage of successful requests. Calculated as (1 - Bad Requests / Total Calls) * 100.
# error_rate: Floating point type, indicating the percentage of error requests. Calculated as (error requests / total calls) * 100.
# average_duration: Float type, indicating the average response time (in milliseconds). Calculated as total response time/total number of calls.

explorer = MetricExplorer()

def query_endpoint_stats(endpoint: str, minute: str) -> dict:
    """
    This function retrieves the statistics for a specific API endpoint at a specific time.
    
    Parameters:
    - endpoint (str): The unique identifier of the API endpoint to be queried. 
    - minute (str): The specific time at which statistics are to be queried, formatted as "YYYY-MM-DD HH:MM". 
    
    Returns:
    - dict: A dictionary containing the statistical data of the specified endpoint at the specified time. 
      The dictionary includes the following keys:
        - 'calls' (int): The total number of requests made to the endpoint.
        - 'success_rate' (float): The percentage of requests that completed successfully. 
          This is calculated as (1 - Number of Bad Requests / Total Number of Calls) * 100.
        - 'error_rate' (float): The percentage of requests that resulted in an error. 
          This is calculated as (Number of Error Requests / Total Number of Calls) * 100.
        - 'average_duration' (float): The average response time of the requests in milliseconds. 
          This is calculated as (Total Response Time / Total Number of Calls).
    """
    endpoint_data = explorer.query_endpoint_stats(endpoint, minute)
    return endpoint_data

def query_endpoint_metrics_in_range(endpoint: str, minute: str) -> dict:
    """
    This function retrieves the statistics for a specific API endpoint over a specified time range. 
    The time range is centered around the provided time, spanning from 15 minutes before to 5 minutes after.
    
    Parameters:
    - endpoint (str): The unique identifier of the API endpoint to be queried. 
    - minute (str): The central time point around which the statistics are to be queried, formatted as "YYYY-MM-DD HH:MM:SS". 
    
    Returns:
    - dict: A dictionary containing aggregated statistical data for the specified endpoint over the specified time range. 
      The dictionary includes the following keys:
        - 'calls' (int): The total number of requests made to the endpoint within the time range.
        - 'success_rate' (float): The average percentage of successful requests. 
          Calculated as (1 - Number of Bad Requests / Total Number of Calls) * 100.
        - 'error_rate' (float): The average percentage of requests that resulted in an error. 
          Calculated as (Number of Error Requests / Total Number of Calls) * 100.
        - 'average_duration' (float): The average response time of the requests in milliseconds within the time range. 
          Calculated as (Total Response Time / Total Number of Calls).
        - 'timeout_rate' (float): The average percentage of requests that timed out.
          Calculated as (Number of Timeout Requests / Total Number of Calls) * 100.
    """
    endpoint_data = explorer.query_endpoint_stats_in_range(endpoint, minute)
    return endpoint_data

import json

cases_file = "historical_cases.json"  # File containing historical cases

def query_previous_cases(self, search_criteria):
    """
    Query previous cases based on the provided search criteria.
    
    Args:
        search_criteria (dict): A dictionary containing search parameters such as keywords, metrics, or other relevant information.

    Returns:
        list: A list of cases that match the search criteria.
    """
    matching_cases = []
    try:
        # Read historical cases from the file
        with open(self.cases_file, 'r') as file:
            historical_cases = json.load(file)
        
        # Search for cases that match the criteria
        for case in historical_cases:
            if self._matches_criteria(case, search_criteria):
                matching_cases.append(case)
    except FileNotFoundError:
        print(f"File {self.cases_file} not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file {self.cases_file}.")
    
    return matching_cases

def _matches_criteria(self, case, search_criteria):
    """
    Check if a case matches the provided search criteria.
    
    Args:
        case (dict): A dictionary representing a historical case.
        search_criteria (dict): A dictionary containing search parameters.

    Returns:
        bool: True if the case matches the criteria, False otherwise.
    """
    for key, value in search_criteria.items():
        # Assuming the case has attributes that can be directly compared with search criteria
        if key in case and value.lower() in case[key].lower():
            continue
        else:
            return False
    return True
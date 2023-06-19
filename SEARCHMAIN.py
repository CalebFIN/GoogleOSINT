import requests
import json
from api import check_keys
import api
from prettytable import PrettyTable


def google_search(search_term, api_key, cse_id, **kwargs):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id
    }
    params.update(kwargs)
    response = requests.get(url, params=params)
    return response.json()

def main():
    # Input search terms
    check_keys(api.api_key, api.cse_id)
    search_terms = input("Enter search terms, separated by commas-->").split(',')
    
    # Create a table
    table = PrettyTable(['Search Term', 'Title', 'Link'])
    
    for term in search_terms:
        # Perform a search for each term.
        results = google_search(term.strip(), api.api_key, api.cse_id)  

        # Check if 'items' key exists in the results
        if 'items' in results:
            # Loop over each resulting item.
            for result in results['items']:
                # Add row to the table
                table.add_row([term, result['title'], result['link']])
        else:
            print(f"No results found for search term '{term}'")
    
    # Print the table
    print(table)
    input("::")


if __name__ == "__main__":
    main()
    

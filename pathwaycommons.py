# import json
import requests

def search_by_gene(gene):
    base_url = 'http://pathwaycommons.org/pc2'  # Replace with the actual API base URL
    search_endpoint = '/search.json'
    query_params = {
        'q': gene,
        'organism': 'homo sapiens'
    }

    try:
        response = requests.get(base_url + search_endpoint, params=query_params)
        response.raise_for_status()
        search_results = response.json()


        return search_results

    except requests.exceptions.RequestException as e:
        print('An error occurred:', e)
        return None


def search_by_identifier(identifier):
    base_url = 'http://pathwaycommons.org/pc2'
    search_endpoint = '/get'
    query_params = {
        'uri': identifier,
        'format':'JSONLD'
    }
    try:
        response = requests.get(base_url + search_endpoint, params=query_params)
        response.raise_for_status()
        search_results = response.json()

        return search_results

    except requests.exceptions.RequestException as e:
        print('An error occurred:', e)
        return None

# search_results_by_identifier = search_by_identifier("EGFR")


search_results_by_gene = search_by_gene("EGFR")
search_hits = search_results_by_gene['searchHit']
for i in search_hits:
    print(i.keys())
    if i['pathway']:
        print(i['pathway'])
# print()
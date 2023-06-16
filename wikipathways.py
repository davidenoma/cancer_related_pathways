import requests
import json
def query_pathways_by_text(query):
    url = "https://webservice.wikipathways.org/findPathwaysByText"
    params = {
        "query": query,
        "species": "Homo sapiens",
        "format": "json"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Request failed with status code:", response.status_code)
        return None

# Usage example
query = "EGFR"
result = query_pathways_by_text(query)
data = json.dumps(result)

data = json.loads(data)
pathway_names = [entry['name'] for entry in data['result']]
print(pathway_names)
#Deploy a nlp word net library from NCI to capture
#pathways that are associated with "cancer" term.
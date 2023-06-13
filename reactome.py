import requests

path_to_gene_set = "/Users/davidenoma/Desktop/PhD._BMB/LONG_LAB/Projects/Pathway_TWAS"
def get_pathway_description(pathway_id):
    endpoint = 'https://reactome.org/ContentService/data/query/'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    # Specify the pathway identifier
    # Build the query payload
    query_payload = {
        'species': 'Homo sapiens',
        'query': {
            'name': pathway_id,
            'type': 'pathway'
        },
    }
    try:
        response = requests.get(endpoint+pathway_id, headers=headers, json=query_payload).json()
        description = response['disease'][0]['displayName']
    except (KeyError, IndexError):
        description = None
    return description

pathway_data = {}
with open(path_to_gene_set+"/ReactomePathways.gmt", 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                fields = line.split('\t')
                pathway_name = fields[0]
                pathway_id = fields[1]
                genes = fields[2:]

                pathway_data[pathway_name] = {
                    'pathway_id': pathway_id,
                    'genes': genes
                }
finalpathwayids = []
final_genes = []
for i in pathway_data.values():
    pathway_desc = get_pathway_description(i['pathway_id'])
    if pathway_desc == "cancer":
        finalpathwayids.append(i)
        final_genes.append(i['genes'])
        # print(i['pathway_id'], pathway_desc)
print(len(finalpathwayids),len(final_genes))
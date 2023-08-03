import requests

path_to_gene_set = ""
#This method checks if the pathway is involved in cancer with the
#reactome api
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
#looping through the gene set to obtain the pathway id, names
#and genes associated with each instance
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
print("Done looping through the geneset. Found ",len(pathway_data)," genes.")
#creating the final list of pathway ids and genes associated with cancer.


print("obtaining the pathways and genes that fall in cancer.")
for i in pathway_data.values():
    pathway_desc = get_pathway_description(i['pathway_id'])
    if pathway_desc == "cancer":
        finalpathwayids.append(i)
        final_genes.append(i['genes'])
        print(i)

print(len(finalpathwayids),len(final_genes))

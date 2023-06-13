import requests
url = 'http://rest.kegg.jp/get/hsa05200/'

# Retrieve pathway data from the API or
response = requests.get(url)
# print(response.text
pathway_data = response.text
lines = pathway_data.split('\n')
hsa_strings = [line for line in lines if line.strip().startswith('hsa')]
hsa_strings = [item.strip() for item in hsa_strings]
index_of_space = hsa_strings[1].find(" ")
hsa_ids,pathway_names = [],[]

#search for each item in the list of
for hsa_item in hsa_strings:
    hsa_ids.append(hsa_item.split(" ")[0])
    pathway_names.append(hsa_item[index_of_space:].strip())
#We will loop through all the pathway ids here
print(pathway_names)
for hsa in hsa_ids:
    # Parse the pathway data to get associated genes
    url2 = "http://rest.kegg.jp/get/"+hsa
    response = requests.get(url2)
    specific_gene = response.text
    specific_gene_lines = specific_gene.split('\n')
    print(hsa)
    #strip the leading and trailing widespaces
    specific_gene_lines = [item.strip() for item in specific_gene_lines]
    #We are going to select genes that have the KO (kegg id associated)
    genes = [line for line in specific_gene_lines if "KO:" in line]
    print(genes,len(genes))



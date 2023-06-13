path_to_gene_set = "/Users/davidenoma/Desktop/PhD._BMB/LONG_LAB/Projects/Pathway_TWAS"

#Query with the netpath genesets
# Define the gene name to search for
gene_name = "CXCL3"

# Define the file path of the TSV file
net_path_geneset = path_to_gene_set + "/NetPath_Gene_regulation_all.txt"

def get_pathway_name(gene_name):
    # Read the TSV file
    with open(net_path_geneset, 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            if columns[3] == gene_name:
                return columns[1]  # Pathway name is in column two
    return None

get_pathway_name("CXCL1")

pathway_name = get_pathway_name(gene_name)
if pathway_name:
    print(f"Pathway name for {gene_name}: {pathway_name}")
else:
    print(f"Gene name {gene_name} not found in the file.")
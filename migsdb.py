


def find_gene_pathway(dataset, gene):
    pathways = []

    with open(dataset, 'r') as file:
        for line in file:
            if line.strip():
                columns = line.split('\t')
                for column in columns:
                    if column == gene:
                        pathways.append(columns[0].rstrip())
                        break

    return pathways
#Gene set downloaded on file to be queried for genes
path_to_gene_set = "/"

# Example usage
dataset = path_to_gene_set+ "/migsdb_geneset.gmt"

gene = "EGFR"
pathways = find_gene_pathway(dataset, gene)

if pathways:
    print(f"{gene} is found in Pathway(s): {pathways}")
else:
    print(f"{gene} is not found in the dataset.")

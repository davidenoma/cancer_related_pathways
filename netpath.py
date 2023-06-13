path_to_gene_set = "/Users/davidenoma/Desktop/PhD._BMB/LONG_LAB/Projects/Pathway_TWAS"

#Query with the netpath genesets
# Define the gene name to search for
gene_name = "CXCL3"

# Define the file path of the TSV file
net_path_geneset = path_to_gene_set + "/NetPath_Gene_regulation_all.txt"

def find_pathway(gene_name):
    # Read the TSV file
    with open(net_path_geneset, "r") as file:
        lines = file.readlines()
        header = lines[0].strip().split("\t")  # Get the header row and split by tab delimiter
        gene_index = header.index("Gene name")  # Find the index of the "Gene name" column

        for line in lines[1:]:  # Skip the header row
            row = line.strip().split("\t")  # Split the line by tab delimiter
            if row[gene_index] == gene_name:
                pathway_name = row[1]  # Get the pathway name (column 2)
                print("Pathway Name:", pathway_name)
                break  # Stop searching after finding the first match
        else:
            print("Gene name not found in the TSV file.")


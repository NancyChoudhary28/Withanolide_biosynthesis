import sys

def read_chromosome_sizes(karyotype_file):
    chrm = {}
    with open(karyotype_file) as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 6 or parts[0] != "chr" or parts[1] != "-":
                continue 
            
            chromosome = parts[2]  
            try:
                size = int(parts[5])
            except ValueError:
                print(f"Invalid size for chromosome {chromosome}: {parts[5]}")
                continue
            chrm[chromosome] = size
    return chrm

def calculate_gene_density(gff_file, karyotype_file, window_size):
    """Calculates gene density across chromosomes using a given window size."""
    chrm = read_chromosome_sizes(karyotype_file)
    
    if not chrm:
        print("No valid chromosome size information found.")
        return
    
    gene_counts_per_chromosome = {}

    with open(gff_file) as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 4 and parts[2] == "gene":
                chromosome_key = parts[0]
                gene_start = int(parts[3])
                
                if chromosome_key in chrm:
                    chromosome_size = chrm[chromosome_key]
                    window_size = int(window_size)
                    num_windows = (chromosome_size + window_size - 1) // window_size
                    
                    if chromosome_key not in gene_counts_per_chromosome:
                        gene_counts_per_chromosome[chromosome_key] = [0] * num_windows
                    
                    window_index = gene_start // window_size
                    if window_index < num_windows:
                        gene_counts_per_chromosome[chromosome_key][window_index] += 1

    output_file = f'gene_density_window{window_size}.txt'
    with open(output_file, 'w') as out_f:
        for chromosome_key, gene_counts in gene_counts_per_chromosome.items():
            chromosome_size = chrm[chromosome_key]
            for i, count in enumerate(gene_counts):
                start_pos = i * window_size + 1
                end_pos = min((i + 1) * window_size, chromosome_size)
                out_f.write(f'{chromosome_key}\t{start_pos}\t{end_pos}\t{count}\n')

    print(f"Gene density data saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 gene_density.py <gff_file> <karyotype_file> <window_size>")
        sys.exit(1)
    
    gff_file = sys.argv[1]
    karyotype_file = sys.argv[2]
    window_size = int(sys.argv[3])

    calculate_gene_density(gff_file, karyotype_file, window_size)

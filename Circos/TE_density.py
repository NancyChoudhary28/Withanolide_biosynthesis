import argparse
import pandas as pd
from collections import defaultdict

def parse_karyotype(karyotype_file):
    contigs = []
    with open(karyotype_file, 'r') as f:
        for line in f:
            columns = line.strip().split()
            contigs.append(columns[2])  
    return contigs

def parse_gff3(gff3_file, contigs, so_numbers):
    filtered_entries = []
    with open(gff3_file, 'r') as f:
        for line in f:
            if line.startswith("#"):
                continue
            columns = line.strip().split("\t")
            contig = columns[0]
            if contig in contigs:
                attributes = columns[8]
                for so_num in so_numbers:
                    if f"sequence_ontology={so_num}" in attributes:
                        start = int(columns[3])
                        end = int(columns[4])
                        filtered_entries.append((contig, start, end))
                        break
    return filtered_entries

def calculate_density(entries, contigs, bin_size):
    densities = defaultdict(lambda: defaultdict(float))  # Structure: {contig: {bin_start: percentage}}

    for contig, start, end in entries:
        for position in range(start, end+1):
            bin_start = (position // bin_size) * bin_size
            densities[contig][bin_start] += 1

    for contig, bins in densities.items():
        for bin_start in bins:
            densities[contig][bin_start] = (bins[bin_start] / bin_size) * 100

    return densities

def write_output(densities, bin_size, output_file):
    with open(output_file, 'w') as f:
        for contig, bins in densities.items():
            for bin_start, percentage in sorted(bins.items()):
                bin_end = bin_start + bin_size - 1
                f.write(f"{contig}\t{bin_start}\t{bin_end}\t{percentage:.2f}\n")

def main(karyotype_file, gff3_file, so_numbers, bin_size, output_file):
    contigs = parse_karyotype(karyotype_file)

    so_numbers = so_numbers.split(",")
    entries = parse_gff3(gff3_file, contigs, so_numbers)

    densities = calculate_density(entries, contigs, bin_size)

    write_output(densities, bin_size, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate percentage of TEs in GFF3 file.")
    parser.add_argument("karyotype_file", help="Path to the karyotype file.")
    parser.add_argument("gff3_file", help="Path to the GFF3 file from EDTA.")
    parser.add_argument("so_numbers", help="Comma-separated sequence ontology numbers (e.g., SO:0002280,SO:0002281).")
    parser.add_argument("bin_size", type=int, help="Bin size for calculating density.")
    parser.add_argument("output_file", help="Output file to save the density information.")

    args = parser.parse_args()

    main(args.karyotype_file, args.gff3_file, args.so_numbers, args.bin_size, args.output_file)

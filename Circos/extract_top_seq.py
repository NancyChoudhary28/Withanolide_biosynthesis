import argparse

def extract_top_longest_sequences(assembly_file, output_file, n):
    sequences = {}
    
    # Read the input assembly file and extract sequences
    with open(assembly_file, "r") as file:
        current_sequence = ""
        current_header = ""
        for line in file:
            if line.startswith(">"):
                if current_header:  # Save the previous sequence
                    sequences[current_header] = current_sequence
                current_header = line.strip()
                current_sequence = ""
            else:
                current_sequence += line.strip()
        sequences[current_header] = current_sequence

    sorted_sequences = sorted(sequences.items(), key=lambda x: len(x[1]), reverse=True)
    top_sequences = sorted_sequences[:n]

    # Write top n sequences to the output file
    with open(output_file, "w") as outfile:
        for header, sequence in top_sequences:
            outfile.write(header + "\n")
            outfile.write(sequence + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract the top N longest sequences from a FASTA file.")

    parser.add_argument('--in', required=True, help="Path to the input assembly file (FASTA format).")
    parser.add_argument('--out', required=True, help="Path to the output file where the top N sequences will be saved.")
    parser.add_argument('--n', type=int, required=True, help="Number of top longest sequences to extract.")

    args = parser.parse_args()

    extract_top_longest_sequences(args.in, args.out, args.n)


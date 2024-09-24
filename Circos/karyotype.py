import argparse
from Bio import SeqIO

def create_circos_karyotype(fasta_file, output_file, color='RdGy-3-div-3'):
    with open(output_file, 'w') as karyotype:
        for seq_record in SeqIO.parse(fasta_file, 'fasta'):
            seq_id = seq_record.id
            seq_length = len(seq_record.seq)
            karyotype_line = f"chr - {seq_id} {seq_id} 0 {seq_length} {color}\n"
            karyotype.write(karyotype_line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Circos karyotype file from a FASTA file.")

    parser.add_argument('--input', '-i', required=True, help="Path to the input FASTA file.")
    parser.add_argument('--output', '-o', required=True, help="Path to the output karyotype file.")
    parser.add_argument('--color', '-c', default='RdGy-3-div-3', help="Color for all chromosomes/contigs. Default is RdGy-3-div-3.")

    args = parser.parse_args()

    create_circos_karyotype(args.input, args.output, args.color)

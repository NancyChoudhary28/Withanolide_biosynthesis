import argparse
import math

def read_karyotype(karyotype_file):
    contigs = set()
    with open(karyotype_file, 'r') as f:
        for line in f:
            if line.startswith('chr'):
                contig_name = line.split()[2]
                contigs.add(contig_name)
    return contigs

def process_trf(trf_file, contigs, bin_size, output_file):
    current_contig = None
    bins = {}
    
    def write_bins(contig):
        if contig in bins:
            for bin_num in sorted(bins[contig]):
                total_repeat_length = bins[contig][bin_num]
                density = total_repeat_length / bin_size
                bin_start = bin_num * bin_size
                bin_end = (bin_num + 1) * bin_size - 1
                output.write(f"{contig}\t{bin_start}\t{bin_end}\t{density}\n")
    
    def add_repeat_to_bins(contig, start, end, repeat_length):
        bin_start = start // bin_size
        bin_end = end // bin_size
        
        if bin_start == bin_end:
            if bin_start not in bins[contig]:
                bins[contig][bin_start] = 0
            bins[contig][bin_start] += repeat_length
        else:
            for bin_num in range(bin_start, bin_end + 1):
                bin_start_pos = bin_num * bin_size
                bin_end_pos = (bin_num + 1) * bin_size - 1
                
                overlap_start = max(start, bin_start_pos)
                overlap_end = min(end, bin_end_pos)
                overlap_length = overlap_end - overlap_start + 1
                
                if bin_num not in bins[contig]:
                    bins[contig][bin_num] = 0
                bins[contig][bin_num] += overlap_length
    
    with open(trf_file, 'r') as trf, open(output_file, 'w') as output:
        for line in trf:
            line = line.strip()
            if line.startswith("Sequence:"):
                if current_contig is not None:
                    write_bins(current_contig)
                current_contig = line.split()[1]
                if current_contig not in contigs:
                    current_contig = None
                    continue
                bins[current_contig] = {}

            elif current_contig and not line.startswith("Sequence:") and len(line.split()) >= 15:
                fields = line.split()
                start, end = int(fields[0]), int(fields[1])
                repeat_length = end - start + 1
                
                add_repeat_to_bins(current_contig, start, end, repeat_length)
        
        if current_contig:
            write_bins(current_contig)

def main():
    parser = argparse.ArgumentParser(description="Process TRF output and calculate tandem repeat densities in non-overlapping bins.")
    
    parser.add_argument("trf_file", help="Path to the TRF output file.")
    parser.add_argument("karyotype_file", help="Path to the karyotype file.")
    parser.add_argument("output_file", help="Path to the output file where the bin data will be written.")
    parser.add_argument("bin_size", type=int, help="Bin size to use for non-overlapping windows.")
    
    args = parser.parse_args()
    
    contigs = read_karyotype(args.karyotype_file)
    
    process_trf(args.trf_file, contigs, args.bin_size, args.output_file)

if __name__ == "__main__":
    main()

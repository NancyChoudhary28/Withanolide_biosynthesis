#!/usr/bin/python

from __future__ import division
from Bio import SeqIO
import sys
from optparse import OptionParser

def GC_content_window(s):
    gc = sum(s.count(x) for x in ['G', 'C', 'g', 'c', 'S', 's'])
    gc_content = gc / float(len(s)) if len(s) > 0 else 0
    return round(gc_content, 4)

def main():
    usage = "usage: %prog -f input.fa [-b 1000] -o output.txt"
    parser = OptionParser(usage=usage)
    parser.add_option("-f", "--file", dest="filename", help="Input Fasta format file", metavar="FASTA")
    parser.add_option("-b", "--bin", dest="BinSize", help="default:1000 Bin size for non-overlapping windows", default=1000, type='int')
    parser.add_option("-o", "--output", dest="output_file", help="Output file to write the GC content", metavar="OUTPUT")

    (options, args) = parser.parse_args()

    if not options.filename or not options.output_file:
        parser.error("Input fasta file and output file must be specified.")

    bin_size = options.BinSize
    seqobj = SeqIO.parse(options.filename, 'fasta')

    with open(options.output_file, 'w') as out_file:
        for record in seqobj:
            name = record.id
            seq = record.seq
            seq_len = len(seq)

            for i in range(0, seq_len, bin_size):
                subseq = seq[i:i + bin_size]
                gc_content = GC_content_window(subseq)
                start = i + 1 
                end = min(i + bin_size, seq_len) 
                out_file.write(f"{name}\t{start}\t{end}\t{gc_content}\n")

if __name__ == '__main__':
    main()
    sys.exit()

![Ws_circos_24_09_github](https://github.com/user-attachments/assets/77a7e889-2c45-438e-b690-810dba5d486e)
This repository includes code used in the article:   
# Phylogenomics and metabolic engineering reveal a conserved gene cluster in Solanaceae plants for withanolide biosynthesis

## Building the Circos Plot:(Withanolide_biosynthesis/Circos)

1. _extract_top_seq.py_: Extract the top _n_ longest sequences from an assembly fasta file.

    Usage:

        python3 extract_top_seq.py

        --in    <Full path to assembly fasta file>
        --out   <Full path to output text file>
        --n     <INT, number of chromosomes/contigs you want to show in the circos plot>
    
2. _karyotype.py_: Generate a Circos karyotype file from an assembly FASTA file.

    Usage:

        python3 karyotype.py

        --input,  -i  <Path to the input fasta file>
        --output, -o  <Path to the output karyotype file>
        --color,  -c  <Color for all chromosomes/contigs. Default is RdGy-3-div-3>

     If you want to change the chromosomes/contigs names on the circos plot, edit the 4th column in the output karyotype file accordingly. For circos-format color definitions, please see the documentation at 
     https://circos.ca/documentation/tutorials/configuration/colors/.

4. _gene_density.py_: Calculates gene density per chromosome/contig from a gff3 file

    Usage:

       python3 gene_density.py <gff_file> <karyotype_file> <window_size>

       gff_file         Path to the GFF file containing gene information
       karyotype_file   Path to the karyotype file (Created in the previous step) 
       window_size      The size of the windows for gene density calculation (e.g., 1000000 for 1Mb windows)
   
6. _tandem_repeat_density.py_: Parses Tandem Repeat Finder [TRF](https://github.com/Benson-Genomics-Lab/TRF) .dat output file and creates Circos format file

   Usage:

       python3 tandem_repeat_density.py <trf_outfile> <karyotype_file> <output_file> <bin_size>

       trf_outfile     Path to the TRF output file.
       karyotype_file  Path to the Circos karyotype file.
       output_file     Output file for Circos format.
       bin_size        Size of the bin for aggregation.
       -h, --help      Shows help message
       

7. _TE_density.py_: Calculates the percentage of TEs from gff3 output file of [EDTA](https://github.com/oushujun/EDTA)

   Usage:
       
       python3 TE_density.py <karyotype_file> <gff3_file> <so_numbers> <bin_size> <output_file>

       -h, --help          shows help message and exit
       karyotype_file      Path to the karyotype file.
       gff3_file           Path to the Whole-genome TE annotation ($genome.mod.EDTA.TEanno.gff3) file from EDTA.
       so_numbers          Comma-separated sequence ontology numbers (e.g., SO:0002280,SO:0002281).
       bin_size            Bin size for calculating density.
       output_file         Output file to save the density information.

      Please refer to the [TE sequence ontology file](https://github.com/NancyChoudhary28/Withanolide_biosynthesis/blob/main/TE_Sequence_ontology.txt) for the sequence ontology numbers. To display a single superfamily, use a       single ontology number (e.g., SO:0002264 for Copia-type LTR retrotransposon) .To display an entire 
      order, use multiple comma-separated sequence ontology numbers that constitute that order.  

9. _GC_density.py_: Calculate GC content of input Fasta sequence in non-overlapping windows and write to an output file

    Usage:

        python3 GC_density.py -f input.fa [-b 1000] -o output.txt

        -h, --help                    shows help message and exit
        -f FASTA, --file=FASTA        Input Fasta format file
        -b BINSIZE, --bin=BINSIZE     default:1000 Bin size for non-overlapping windows
        -o OUTPUT, --output=OUTPUT    Output file to write the GC content


12. _circos.conf_: Circos configuration file used in this study

## Building the Expression Heatmap: (Withanolide_biosynthesis/Heatmap) 
_Expression_hm.R:_ R code to plot the expression heatmap 

## Data availability
The raw sequencing data for _Withania somnifera_ is available through the European Nucleotide Archive Project **PRJEB64854**. Root gene expression raw data is available at **ERR13615536**. The genome assembly and gene annotation sequences for _W. somnifera_ are available via LeoPARD at https://leopard.tu-braunschweig.de/receive/dbbs_mods_00077979. _Physalis pruinosa_ and _P. grisea_ gene re-annotated sequences are available at https://leopard.tu-braunschweig.de/receive/dbbs_mods_00077980. Code used throughout the article is available at the GitHub repository: https://github.com/NancyChoudhary28/Withanolide_biosynthesis/

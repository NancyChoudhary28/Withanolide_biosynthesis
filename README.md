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

5. _tandem_repeat_density.py_: Calculates tandem repeat density from a TRF .dat output file

6. _EDTA_summary.py_: 

7. _TE_density.py_:

8. _GC_density.py_: Calculates GC density per chromosomes/contig from an assembly fasta file

9. _circos.conf_: Circos configuration file used in this study

## Building the Expression Heatmap: (Withanolide_biosynthesis/Heatmap) 
_Expression_hm.R:_ R code to plot the expression heatmap 

## Data availability
The raw sequencing data for _Withania somnifera_ is available through the European Nucleotide Archive Project **PRJEB64854**. Root gene expression raw data is available at **ERR13615536**. The genome assembly and gene annotation sequences for _W. somnifera_ are available via LeoPARD at https://leopard.tu-braunschweig.de/receive/dbbs_mods_00077979. _Physalis pruinosa_ and _P. grisea_ gene re-annotated sequences are available at https://leopard.tu-braunschweig.de/receive/dbbs_mods_00077980. Code used throughout the article is available at the GitHub repository: https://github.com/NancyChoudhary28/Withanolide_biosynthesis/

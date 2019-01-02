# ClustalO to VCF

Converts output from ClustalOmega alignments scripts to VCF. TO DO: Add Mutalyzer for variant description extraction.

`clustal_output` provides sample output from a clustal omega alignment. To create a VCF from it, run `clustal_to_vcf.py` to first convert it to aligned FASTA then produce a VCF. Then, run `fix_vcf.py` to fix the chromosome number and set the position offset. 

Note that producing the VCF requires that the [SNP-sites package](https://github.com/sanger-pathogens/snp-sites) be installed.

Notes:  
- To use the Mutalyzer Variant Description Extractor, you need to follow the installation instructions on their [repo](https://github.com/mutalyzer/description-extractor).  
- This means that you'll need [SWIG](www.swig.org) installed, then `pip install description-extractor`. If you run into errors about crossmapper, you can add the flag `--process-dependency-links`. 

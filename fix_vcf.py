import sys
def replace_chrom(vcf, new_chrom):
    # Split header from rest of VCF information
    header = "\n".join(vcf.split("\n")[:4]) + "\n"
    vcf_lines = vcf.split("\n")[4:]
    
    # Split into tabs and delete chromosome number
    vcf_lines = filter(lambda x: x != "", vcf_lines)
    vcf_lines = map(lambda x: x.split("\t")[1:], vcf_lines)
    
    # Function to insert the chromosome
    def insert_chrom(lst):
        lst.insert(0, str(new_chrom))
        return lst
    
    # Insert chromosome, then rebuild line of VCF file
    vcf_lines = map(insert_chrom, vcf_lines)
    vcf_lines = map(lambda x: "\t".join(x), vcf_lines)
    
    # return header with rebuilt VCF lines
    return header + "\n".join(list(vcf_lines))

def set_offset(vcf, start):
    # Split header from rest of VCF information
    header = "\n".join(vcf.split("\n")[:4]) + "\n"
    vcf_lines = vcf.split("\n")[4:]
    
    # Split into tabs 
    vcf_lines = filter(lambda x: x != "", vcf_lines)
    vcf_lines = map(lambda x: x.split("\t"), vcf_lines)
    
    # Function to add the offset
    def add_offset(lst):
        lst[1] = str(int(lst[1]) + int(start) - 24)
        return lst
    
    # Offset position, then rebuild line of VCF file
    vcf_lines = map(add_offset, vcf_lines)
    
    vcf_lines = map(lambda x: "\t".join(x), vcf_lines)
    
    # return header with rebuilt VCF lines
    return header + "\n".join(list(vcf_lines))

def fix_vcf(vcf, offset, chrom):
    vcf_offset = set_offset(vcf, offset)
    final_vcf = replace_chrom(vcf, chrom)
    return final_vcf

if __name__ == "__main__":
	# first position is file name, second is output file name, third is chrom, third is offset
    if len(sys.argv) != 5:
        print("Usage: ./fix_vcf.py <input vcf> <output vcf> <chrom #> <offset>")
        sys.exit(1)

    file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    chrom_num = sys.argv[3]
    offset = sys.argv[4]
    with open(file_name, "r") as vcf_file:
        vcf_info = vcf_file.read()
    #new_vcf = replace_chrom(vcf_info, chrom_num)
    #new_vcf = set_offset(new_vcf, offset)
    new_vcf = fix_vcf(vcf_info, offset, chrom_num)
    with open(output_file_name, "w") as f:
        f.write(new_vcf)
        f.write("\n")

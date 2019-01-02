import subprocess, sys

FASTA_OUTPUT_NAME = "clustal_fasta.tmp"
VCF_OUTPUT_NAME = "clustal.vcf"

def clustal_to_vcf(text, fasta_output = FASTA_OUTPUT_NAME, vcf_output = VCF_OUTPUT_NAME):
	# Split by FASTA entry, separating into ID and sequence
	outputs = text.split(">")[1:]
	new_seq = []
	for output in outputs:
		lines = output.split('\n')
		seq_id = lines[0]
		sequence = "".join(lines[1:])
		new_seq.append((seq_id, sequence))
	
	# 
	new_output = []
	for seq_id, sequence in new_seq:
		seq = sequence.replace('\n', '')
		
		# get rid of trailing hyphens by replacing with space, then using rstrip() function and counting difference
		old_len = len(seq)
		trail_stripped = sequence.replace('-', ' ').rstrip()
		
		num_trailing_hyphens = old_len - len(trail_stripped)

		# re-add tildas for aligned FASTA format
		padded = trail_stripped + ("~" * num_trailing_hyphens)
		
		# replace remaining spaces with . to signify SNP/INDEL
		final_seq = padded.replace(" ", ".")
		new_output.append(">{}\n{}".format(seq_id, final_seq))
	
	with open(fasta_output, 'w') as f:
		f.write('\n'.join(new_output))
		f.write('\n')
	
	proc = subprocess.Popen(['snp-sites', '-v', fasta_output, '-o', vcf_output])
	std = proc.communicate()

if __name__ == "__main__":
	with open(sys.argv[1]) as f:
		clustal_text = f.read()
	clustal_to_vcf(clustal_text)

from Bio import SeqIO
k =3
sequences =[]
seq_names = []
fasta = SeqIO.parse("graph2.fasta",'fasta')
for seq in fasta:
    sequences.append(str(seq.seq))
    seq_names.append(seq.id)
seq_dic = {seq_names[i]: sequences[i] for i in range (len(seq_names))}
result = []
for suffix_key, suffix_item in seq_dic.items():
    suffix = suffix_item[:k]
    for key, item in seq_dic.items():
        prefix = item[-k:]
        if suffix_key != key:
            if suffix == prefix:
                result.append(f"{key} {suffix_key}")
                prefix = ''
print(result)
txt_result = open("graph_output.txt", "w+")
for i in result:
    txt_result.write(i + "\n")
txt_result.close()
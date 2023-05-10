from GENIE3 import * 
import pandas as pd 

def preprocess_GEO_dataset(data_filename): 
    if data_filename.split('.')[1] == "tsv": 
        df = pd.read_csv(data_filename, sep='\t') 
        df = df.set_index("Unnamed: 0").T
        df.to_csv(data_filename.split('.')[0]+".txt", sep='\t', index=False) 


data_filename = 'GEO_dataset/GSE185047/expression.tsv' 
tf_names_file = 'GEO_dataset/GSE185047/tf_names.tsv' 

preprocess_GEO_dataset(data_filename) 
data_filename = data_filename.split('.')[0]+".txt"

data = loadtxt(data_filename, skiprows=1)
f = open(data_filename)

gene_names = f.readline()
f.close()
gene_names = gene_names.rstrip('\n').split('\t') 

tf_names = pd.read_csv(tf_names_file, sep='\t').T.values.tolist()[0]
VIM = GENIE3(data, gene_names=gene_names, regulators=tf_names) 

get_link_list(VIM, gene_names=gene_names, regulators=tf_names, file_name='ranking_test.txt') 

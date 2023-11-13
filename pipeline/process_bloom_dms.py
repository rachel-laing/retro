import pandas as pd

infile='data/raw/Bloom/single_mut_effects.txt'       # it is a txt file but still follows csv format
columns = {'site_SARS2':'Position',
           'mutation':'Mutation', 
           'bind_avg':'ACE2 Binding',
           'expr_avg':'Expression'}
df = pd.read_csv(infile, usecols=columns.keys()).rename(columns=columns)

outfile='data/processed/DMS_Mutations.tsv'
df.to_csv(outfile, sep='\t', index=False)
                                

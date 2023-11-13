import pandas as pd

infile = 'data/raw/Bloom/aamut_fitness_all.csv'
df = pd.read_csv(infile, usecols=['aa_mutation', 
                                  'aa_site',
                                  'gene',
                                  'delta_fitness'])

df = df.rename(columns={'aa_site':'Position',
                        'aa_mutation':'Mutation',
                        'gene':'Gene'})

df = df.sort_values(by='delta_fitness', ascending=False).reset_index(drop=True)
df['Rank'] = df.index

outfile = 'data/processed/Bloom_Ranked_Mutations.tsv'
df.to_csv(outfile, sep='\t', index=False)
import pandas as pd

infile = 'data/raw/EVEscape/spike_evescape_predictions.csv'
df = pd.read_csv(infile, usecols=['i', 
                                'wt', 
                                'mut',
                                'evescape',
                                'evescape_pre2020',
                                'eve', 
                                'eve_pre2020'])
df = df.rename(columns={'i':'Position'})

df['Mutation'] = df['wt'].astype(str) + df['Position'].astype(str) + df['mut'].astype(str)

df = df.sort_values(by='evescape', ascending=False).reset_index(drop=True)
df['Rank'] = df.index

outfile = 'data/processed/EVEscape_Ranked_Mutations.tsv'
df[['Mutation', 'Rank', 'Position', 
    'evescape', 'evescape_pre2020', 
    'eve', 'eve_pre2020']
   ].sort_values(by='Position'
   ).to_csv(outfile, sep='\t', index=False)
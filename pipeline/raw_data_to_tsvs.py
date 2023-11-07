"""
At https://github.com/bkotzen/sars-cov2-modeling, there are recorded results of PyR0 and BVAS runs throughout time. Aggregate those results to useful data frames and save

Assume that directory structure is:
parent
   |------retro
   |        |-----pipeline
   |        |         |----raw_data_to_tsv <YOU ARE HERE>
   |        |
   |        |-----other subdirectories
   |
   |-----sars-cov2-modeling
            |----------------<dates>
                                |-----PyR0
                                |-----BVAS
"""

import os
import re
import pandas as pd

def get_historic_run_dates(history_dir):
    date_pattern = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}')   # e.g. 2022-01-13
    dates = [d for d in os.listdir(history_dir) if re.match(date_pattern, d)]
    return dates

def add_csv_to_df(csv, df, date):
    if csv.endswith('.csv'):
        sep=','
    elif csv.endswith('.tsv'):
        sep='\t'
    else:
        assert False, 'Invalid file suffix'
        
    if os.path.isfile(csv):
        mini = pd.read_csv(csv, sep=sep)
        mini['Run date'] = date
    else:
        print(f'File does not exist: {csv}')
        mini = pd.DataFrame()
    return pd.concat([df, mini])

def generate_ranking_tables():
    history_dir = '../../sars-cov2-modeling/'
    dates = get_historic_run_dates(history_dir)
    
    # PyR0 ranking tables
    mutationRank_pyro_df = pd.DataFrame()
    strainRank_pyro_df = pd.DataFrame()
    # BVAS ranking tables
    mutationRank_bvas_df = pd.DataFrame()
    strainRank_bvas_df = pd.DataFrame()
    
    for date in dates:
        # PyR0 ranking tables
        mutationRank_pyro_df = add_csv_to_df(history_dir + date + '/PyR0/mutations.tsv', mutationRank_pyro_df, date)
        strainRank_pyro_df = add_csv_to_df(history_dir + date + '/PyR0/strains.tsv', strainRank_pyro_df, date)
        # BVAS ranking tables
        mutationRank_bvas_df = add_csv_to_df(history_dir + date + '/BVAS/allele_summary.csv', mutationRank_bvas_df, date)
        strainRank_bvas_df = add_csv_to_df(history_dir + date + '/BVAS/growth_rates_summary.csv', strainRank_bvas_df, date)
        
    return mutationRank_pyro_df, strainRank_pyro_df, mutationRank_bvas_df, strainRank_bvas_df
                                      


if __name__ == '__main__':
    # Build ranking tables
    pyro_ranked_mutations, pyro_ranked_strains, bvas_ranked_mutations, bvas_ranked_strains = generate_ranking_tables()
    
    # Save tsvs
    output_directory = '../data/processed/'
    pyro_ranked_mutations.to_csv('../data/processed/'+'PyR0_Ranked_Mutations.tsv', sep='\t', index=False)
    pyro_ranked_strains.to_csv('../data/processed/'+'PyR0_Ranked_Strains.tsv', sep='\t', index=False)
    bvas_ranked_mutations.to_csv('../data/processed/'+'BVAS_Ranked_Mutations.tsv', sep='\t', index=False)
    bvas_ranked_strains.to_csv('../data/processed/'+'BVAS_Ranked_Strains.tsv', sep='\t', index=False)
        
    
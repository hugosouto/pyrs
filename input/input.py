import pandas as pd
import polars as pl

params_lances = {
    'has_header': False, 
    'separator': '\t',
    'na_rows': 100,
    'ignore_errors': True,
    # 'on_bad_lines': 'skip', 
    # 'encoding': 'utf-8',
    # 'engine': 'c',
    # 'engine': 'python',
    # 'keep_default_na': False,
    }

df_header = pl.read_csv('dados/tbl_lances_header.csv', has_header=True)
df_lances = pl.read_csv('dados/tbl_lances.csv', **params_lances)
# df_lances_encerrados = pd.read_csv('dados/tbl_lances_encerrados.csv', **params_lances)

df_header
df_lances

df_sample = df_lances[41:44]

df
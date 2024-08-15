import pandas as pd
import csv

def join_csv_files(df1, df2, join_column):
    df_join = pd.merge(df1, df2, on=join_column, suffixes=('', '_drop'), how="inner")
    df_join = df_join[[col for col in df_join.columns if not col.endswith('_drop')]]
    return df_join

def read_csv(filepath):
    with open(filepath, 'r', newline='', encoding='latin-1') as csvfile:
        # Detecta o delimitador
        dialect = csv.Sniffer().sniff(csvfile.read(16384))
        csvfile.seek(0)
        # Lê o CSV com o delimitador detectado
        df = pd.read_csv(csvfile, delimiter=dialect.delimiter)
    return df
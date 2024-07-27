import pandas as pd

def join_csv_files(df1, df2, join_column):
    df_join = pd.merge(df1, df2, on=join_column, suffixes=('', '_drop'), how="inner")
    df_join = df_join[[col for col in df_join.columns if not col.endswith('_drop')]]
    return df_join

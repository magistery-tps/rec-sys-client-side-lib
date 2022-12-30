from scipy.sparse import  dok_matrix, csr_matrix
import logging
import pandas as pd
import logging



def seq_by_id(df, entity=None, column_id=None, column_seq=None):
    if entity:
        column_id  = f'{entity}_id'
        column_seq = f'{entity}_seq'

    return pd.Series(df[column_id].values, index=df[column_seq]).to_dict()


# DF Pipeline functions...

def normalize_column(df, source, target=None):
    if target is None:
        target = source
    df[target] = (df[source] - df[source].mean()) / df[source].std()
    return df


def min_max_scale_column(df, source, target=None):
    if target is None:
        target = source
    df[target] = (df[source]-df[source].min())/(df[source].max()-df[source].min())
    return df

def apply_fn_to_column(df, target, fn):
    df[target] = fn(df)
    return df

def clean_html_format(df, column):
    import re

    # as per recommendation from @freylis, compile once only
    CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

    def clean_html(raw_html):  return re.sub(CLEANR, '', raw_html) if raw_html else '' 

    df[column] = df[column].apply(clean_html)
    return df


def distinct_by(df, columns=[]):
    n_before = df.shape[0]
    df = df.drop_duplicates(subset=columns)
    n_after = df.shape[0]
    logging.info(f'Repeated rows by {columns} -> Count: {n_before - n_after}, Percent: {((n_before - n_after)/n_before)*100:.2f}%')
    return df



def df_to_matrix(
    df,
    x_col,
    y_col,
    value_col   = 'rating',
    progress    = 10
):
    logging.info(f'Building matrix({x_col}, {y_col})')

    matrix = dok_matrix((
        len(df[x_col].unique()),
        len(df[y_col].unique())
    ))

    n_examples = df.shape[0]
    count      = 0
    for _, row in df.iterrows():
        try:
            matrix[ int(row[x_col]), int(row[y_col]) ] = float(row[value_col])
        except IndexError as e:
            logging.error(f'Not found index matrix[{int(row[x_col])}, {int(row[y_col])}]')
            raise e

        count += 1
        if count % int(n_examples / progress) == 0:
            logging.info(f'Building matrix{matrix.shape}... {(count / n_examples) * 100:.0f}%')

    return csr_matrix(matrix)


def concat(df_a, df_b): return pd.concat([df_a, df_b], axis=0)


def save(df, path, header=True): df.to_csv(path, encoding='utf-8', index=False, header=header)


def load(path): return pd.read_csv(path)
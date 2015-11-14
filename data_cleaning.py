import pandas as pd
from scipy import stats


def find_columns_containing_nan(df, col_names):
    empty = df.apply(lambda col: pd.isnull(col))
    nan_columns = []
    for column in col_names:
        if True in empty[column].unique():
            nan_columns.append(column)
    try:
        print 'Columns containing NaNs: ', nan_columns
        return nan_columns
    except:
        print 'There are no NaNs in this dataframe'
        return None


def print_col_datatype(df, col_names):
    for column in col_names:
        print column, ':', df[column].dtype


def replace_missing_values(df, fill_method):
    if fill_method == 1:
        df.dropna(inplace=True)
    elif fill_method == 2:
        df = df.fillna("")
    elif fill_method == 3:
        df = df.fillna(df.mean())
    elif fill_method == 4:
        #the limit is how many rows forward it will fill (if there are 2 empty NaNs in a row, only the first will be replaced)
        df = df.fillna(method='pad', limit=1)
    elif fill_method == 5:
        df.dropna(axis = 1, inplace=True)
    elif fill_method == 6:
        df.interpolate(inplace=True)
    return df
    

def convert_column_to_float(df, column):
    for idx, row in enumerate(df[column]):
        try:
            df.five[idx] = float(row)
        except:
            print 'This row cannot be converted'
    return df


def locate_non_numeric_values(df, col_name):
    non_num_dict = {}
    for idx, row in df.iterrows():
        try:
            float(row['five'])
        except:
            non_num_dict[idx] = row['five']
    print non_num_dict
    return non_num_dict

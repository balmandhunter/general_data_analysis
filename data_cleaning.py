import pandas as pd
from scipy import stats
import numpy as np
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import FunctionTransformer
from sklearn.linear_model import LogisticRegression


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


def make_dummy_variables(df, columns_to_encode):
    df_dummies = pd.get_dummies(df[columns_to_encode])
    print df_dummies
    df = pd.concat([df, df_dummies], axis=1)
    df.drop(columns_to_encode, axis=1, inplace=True)
    return df


def make_poly_feat(df, features):
    transformer_log = FunctionTransformer(np.log1p)
    transformer_sq = FunctionTransformer(np.square)
    transformer_sqrt = FunctionTransformer(np.sqrt)
    for column in features:
        name = 'log_' + str(column)
        df[name] = np.transpose(transformer_log.transform(df[column]))
        name_sq = 'sq_' + str(column)
        df[name_sq] = np.transpose(transformer_sq.transform(df[column]))
        name_sqrt = 'sqrt_' + str(column)
        df[name_sqrt] = np.transpose(transformer_sqrt.transform(df[column]))
    return df


def create_interaction_feat(df, features):
    for idx, col in enumerate(features):
        i = idx + 1
        while i < 8:
            name = str(col) + '_inter_' + str(features[i])
            df[name] = df[col]*df[features[i]]
            i += 1
    return df

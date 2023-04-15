import pandas as pd
import numpy as np
from typing import Union

def peek_data(df) :
    
    print()
    print('Glance at the data : ')
    print()
    display(df.head())
    print()
    
def get_info(df) :
    
    print('Data types, dimension of the data : ')
    print()
    display(df.info())
    print()
    
def get_nans(df) :
    
    print('Missing values across variables : ')
    print()
    display(df.isnull().sum().sort_values(ascending = False))
    print()
    
    print('Missing values - % of the data : ')
    nulls_percentages = (df.isnull().sum() / len(df)) * 100
    display(nulls_percentages.round(2).sort_values(ascending = False))
    print()

def summarize_df(df : pd.DataFrame) -> None:
    
    """
    Displays the basic information about the pandas DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame.
    
    Returns
    -------
    None.
    
    """
    
    peek_data(df = df)
    get_info(df = df)
    get_nans(df = df)
    
def replace_hidden_nans(df, nan_symbol : Union[str, float, int], col_name : str) -> None :
    """
    Takes a df, an alphanumeric character representing NaNs, and the name of
    a column in that df and replaces all of the occurences of that character with NaNs.
    
    Parameters
    ----------
    df : 
    nan_symbol : 
    col_name : 
    
    Return
    ------
    None.
    """
    
    df.loc[df[col_name] == nan_symbol, col_name] = np.nan
    
def summarize_numeric_data(data : pd.DataFrame, subset = None, exclude = None) -> None:

    """
    Parameters
    ----------
    data : pandas DataFrame. The dataframe containing the data that we want to analyze.
    subset : None or list. Defaults to None. List of names of the columns that we want
                           to include in our numeric summary.
    
    exclude : None or list. Defaults to None. List of names of the columns that we want
                           to exclude from our numeric summary.
    Example
    -------
    summarize_numeric_data(df, subset = ['age', 'wave'])

      The correlation between the variables in the dataset :

            age	wave
        age	1.0	0.1
        wave	0.1	1.0

        Descriptive statistics of numeric data : 

        age	wave
        count	8283.00	8378.00
        mean	26.36	11.35
        std	3.57	6.00
        min	18.00	1.00
        25%	24.00	7.00
        50%	26.00	11.00
        75%	28.00	15.00
        max	55.00	21.00
    
    """
    
    assert (subset is None) | (exclude is None), "You should specify which columns to include or which to exclude, but not both."
    
    numeric_data = [c for c in data.columns if (data[c].dtype in ['float64', 'int64']) \
                    & (len(data[c].unique()) > 10)]
    
    relevant_data = data[numeric_data]
    
    if subset :
        relevant_data = relevant_data[subset]
    
    if exclude :
        subset = [n for n in numeric_data if n not in exclude]
        relevant_data = relevant_data[subset]
    
    print()
    print('The correlation between the variables in the dataset :')
    print()
    display(relevant_data.corr().round(2))
    print()
    print('Descriptive statistics of numeric data : ')
    print()
    display(relevant_data.describe().round(2))
    print()

def look_at_variables_values(df : pd.DataFrame, num_uniq_values = 30) -> None:

  """
  Display sample unique values from the dataset.

  Parameters
  ----------
  df : pandas DataFrame containing the data.
  num_uniq_values : int. Sets the maximum number of unique values
                         of a feature to display.

  Returns
  -------
  None
  """
  
  for c in df.columns:
    print()
    print('Unique values from {}, limited to {}'.format(c, num_uniq_values))
    print()
    col_uniq_vals = df[c].unique()
    
    if num_uniq_values > len(col_uniq_vals) :
        n = len(col_uniq_vals)
    else :
        n = num_uniq_values
    
    print(pd.Series(col_uniq_vals).sample(n = n).head(n = n))
    print()
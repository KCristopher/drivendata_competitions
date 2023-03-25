import pandas as pd
import numpy as np


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
    
    print()
    print('Glance at the data : ')
    print()
    display(df.head())
    print()
    
    print('Data types, dimension of the data : ')
    print()
    display(df.info())
    print()
    
    print('Missing values across variables : ')
    print()
    display(df.isnull().sum().sort_values(ascending = False))
    print()
    
    print('Missing values - % of the data : ')
    nulls_percentages = (df.isnull().sum() / len(df)) * 100
    display(nulls_percentages.round(2).sort_values(ascending = False))
    print()
    
def summarize_numeric_data(data : pd.DataFrame, subset = None) -> None:

    """
    Parameters
    ----------
    data : pandas DataFrame. The dataframe containing the data that we want to analyze.
    subset : None or list. Defaults to None. List of names of the columns that we want
                           to include in our numeric summary.
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
    
    numeric_data = [c for c in data.columns if (df[c].dtype in ['float64', 'int64']) \
                    & (len(df[c].unique()) > 10)]
    
    relevant_data = data[numeric_data]
    
    if subset:
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

def look_at_variables_values(df : pd.DataFrame, num_uniq_values = 66) -> None:

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
    print(set(df[c].sample(n = num_uniq_values)))
    print()
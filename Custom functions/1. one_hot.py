def one_hot(df,col):
    """
Perform one-hot encoding on the specified column of a DataFrame.

This function creates a new binary column for each unique value in the specified column.
Each binary column indicates the presence (1) or absence (0) of the corresponding unique value
in the original column. After creating these binary columns, the original column is dropped
from the DataFrame.

Parameters:
df (pd.DataFrame): The input DataFrame containing the data to be encoded.
col (str): The name of the column to be one-hot encoded.

Returns:
pd.DataFrame: The DataFrame with the original column replaced by new binary columns
representing each unique value.

Notes:
- If the original column contains a large number of unique values, this may result in a
    significant increase in the number of columns, which could impact performance.
- The function modifies the original DataFrame in place and also returns it.
"""
    #if index == True:
    for i in df[col].unique():#creating a column for each unicque value of the column
        df[i]=0 #a column with all zero
        for j in range(df.shape[0]):
            if df[col][j]==i:
                df[i][j] = 1
                #else:
                    #df[i][j] = 0
    df.drop(i,axis=1, inplace=True) #droping any one column


#note:
# this fucntion requires code improvement for better time efficiency.
# Reduce the number of encoded columns   

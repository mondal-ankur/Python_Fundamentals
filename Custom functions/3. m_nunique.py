
def m_nunique(df,max=10,min=0):
    """
    Analyze DataFrame columns based on the number of unique values.

    This function identifies columns in the DataFrame that have a number of unique values
    within the specified range [min, max]. It prints the column names, counts of unique
    values (excluding NaN), and indicates if the column contains null values. Additionally,
    it displays the frequency of each unique value in the selected columns.

    Parameters:
    df (pandas.DataFrame): The input DataFrame to analyze.
    max (int, optional): The maximum number of unique values a column can have to be included.
                         Default is 10.
    min (int, optional): The minimum number of unique values a column must have to be included.
                         Default is 0.

    Returns:
    None
    """
    bold_start = '\033[1m'
    bold_end   = '\033[0m'
    count = 0
    count_na = 0
    a=dict(df.isna().sum()) # coloumn name and its null values pair
    for i  in df.columns:
        if len(df[i].unique()) in range(min,max+1): #min and max number of unique values allowed
            count+=1
            if a[i]>0: #If there is null values in the coloumn
                count_na+=1
                print(bold_start, i,"-",len(df[i].unique())-1,bold_end,"[Has",a[i]," Null Value]" , end="\n\n") #getting total number of unique values in a coloumn
            else:
                print(bold_start, i,"-",len(df[i].unique()),bold_end, end="\n\n") 
            val=dict(df[i].value_counts()) #taking value counts of the coloumn

            # printing the unique values with its count
            for i in val.keys(): 
                print(str(i)+"("+str(val[i])+")",end="  |  ")
            print("\n\n")
            print("--"*50,"--"*50,sep="\n")

    print("||\t TOTAL", count, "COLOUMNS HERE \t||")
    print("--"*20,sep="\n")
    print("||\t AMONG THEM", count_na, "COLOUMNS WITH NULL VALUES \t||")
    print("--"*20,sep="\n")
    del a, val, count

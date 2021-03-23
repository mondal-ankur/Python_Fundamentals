def one_hot(df,col):
    #if index == True:
    for i in df[col].unique():#creating a column for each unicque value of the column
        df[i]=0 #a column with all zero
        for j in range(df.shape[0]):
            if df[col][j]==i:
                df[i][j] = 1
                #else:
                    #df[i][j] = 0
    df.drop(i,axis=1, inplace=True) #droping any one column
    return df


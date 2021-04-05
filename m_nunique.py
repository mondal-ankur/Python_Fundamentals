#df: dataset 
#min: coloumn contains 'min' numbers of unique values; default 0
#max: coloumn contains 'max' numbers of unique values; default 10
def m_nunique(df,max=10,min=0):
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

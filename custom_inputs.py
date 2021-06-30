#d: required datatype
#na: rest will be converted to na  
def cust_input(d, na=None):
    lst=input("Enter all the numbers with a space. Eg. 56 656 1 ....").split()
    lst=[i.strip() for i in lst]
    for i in range(len(lst)):
        try:
            lst[i]=d(lst[i])
        except:
            lst[i]=na
    return lst


#list(map(int, input().rstrip().split()))

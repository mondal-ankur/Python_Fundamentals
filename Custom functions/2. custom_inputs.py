from typing import Callable, Any, List
def cust_input(d, na=None):
    """
    Converts user input strings into a list of a specified data type.

    This function prompts the user to input a series of values separated by spaces,
    attempts to convert each value to the specified data type, and handles conversion
    failures by assigning a predefined 'na' value.

    Parameters:
    d (Callable[[str], Any]): A function that converts a string to the desired data type.
    na (Any, optional): The value to assign if conversion fails. Defaults to None.
    prompt (str, optional): The input prompt displayed to the user. Defaults to
                        "Enter all the numbers with a space. Eg. 56 656 1 ....".

    Returns:
    List[Any]: A list of values converted to the specified data type, with 'na' assigned
            where conversion was unsuccessful.
    """
    lst=input("Enter all the numbers with a space. Eg. 56 656 1 ....").split()
    lst=[i.strip() for i in lst]
    for i in range(len(lst)):
        try:
            lst[i]=d(lst[i])
        except:
            lst[i]=na
    return lst


#list(map(int, input().rstrip().split()))

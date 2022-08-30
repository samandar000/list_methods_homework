def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    k=0
    y=0
    i=0
    list1 = []
    list2 = []

    while i < len(fruits):
        if fruits[i]=='apple':
            list1 ==  list1.append(i)
            
        i+=1
    while k < len(fruits):
        if fruits[k] == 'apple':
            list2 == list2.append(1)
            y+=1
        k+=1
    list0 = [y]  + list1
    return   list0

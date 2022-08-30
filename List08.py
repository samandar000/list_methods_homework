def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    list1=[]
    i=0
    while i < len(fruits):
        
        if fruits[i] != 'apple':
            list1.append(fruits[i])
        
        i+=1

    return fruits
print(main(["apple", "apple", "apple", "apple", "kiwi"]))
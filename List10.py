def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    zeros = list1.count(0) 
    ones = list1.count(1)
    list0= [ones,zeros]
    
    
    return list0

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     x=0
#     y=0
#     i=0
#     while i < len(list1):
#         if list1[i] == (0):
#             list1 == list1.append(1)
#             y+=1
#         i+=1
#     while i < len(list1):
#         if list1[i] == (0):
#             list1 == list1.append(1)
#             x+=1
#         i+=1
#     return x
# print(main([0, 0, 0, 0, 1, 0, 1, 0]))

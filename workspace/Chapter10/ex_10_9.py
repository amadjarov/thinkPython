def has_dupicates(list1):
    newList = sorted(set(list1))
    
    print newList
    
has_dupicates([1,3,3,4,5,5,5,5,1,6])
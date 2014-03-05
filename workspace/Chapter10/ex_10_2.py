def capitalize_all(nestedList, newList = []):
        
        def flatlist(nestedList):
                for i in range(len(nestedList)):
                        if type(nestedList[i]) == str:
                                newList.append(nestedList[i].upper())
                        else:
                                flatlist(nestedList[i])
                return newList
 
        flatlist(nestedList)
        print newList
 
capitalize_all([["a","b","c"],["d","e","f"],["g","h","i"]])
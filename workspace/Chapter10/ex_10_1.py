def nested_sum(nestedList):
        newList = [0]
        def flatlist(nestedList):
                for i in range(len(nestedList)):
                        if type(nestedList[i]) == int:
                                newList.append(nestedList[i])
                        else:
                                flatlist(nestedList[i])
                return newList
 
        flatlist(nestedList)
        print sum(newList)
 
nested_sum([[1,2,3],[4,5,6],[7,8,9]])
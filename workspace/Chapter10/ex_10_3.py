def cumulative(nestedList):
        newList = []
        newList2 = newList + nestedList[:-1]
          
        cumulatNumber =  sum(nestedList[:-1]) + nestedList[-1]
        newList3 = [cumulatNumber]
        newList = newList2 + newList3
        print newList                  

cumulative([1,2,3,4,5,6])
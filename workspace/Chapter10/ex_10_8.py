def has_dupicates(list1):
    newList = list1[:]
    newList.sort()
    for i in range(len(newList)-1):
        if newList[i] == newList[i + 1]:
            print '+',
            print '',True
            #return
        print '.',
    print ''
    print False

print __name__
if __name__ == '__main__':
    has_dupicates([2,2,3,4,5,6,7])    
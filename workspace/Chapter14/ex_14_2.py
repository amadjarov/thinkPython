def sed(pattern, replace, file1, file2):
    """
    accept 4 arguments str1, str1 , file file
    """
    try:
        first = open(file1, 'r')
        second = open(file2, 'w')
        for line in first:
            line = line.replace(pattern, replace)
            second.write(line)
            
        first.close()
        second.close()
    except:
        print "Something is wrong"
        
            
import re
str = 'an example word:cat!!'
match = re.search(r'word:\w\w', str)
# If-statement after search() tests if it succeeded
if match:                      
    print 'found', match.group() ## 'found word:cat'
else:
    print 'did not find'
    
match = re.search(r'p\w', 'piiig')  
print match.group()

match = re.search(r'pi?', 'piiig')
print match.group()

match = re.search(r'\d\s+\d\s+\d', 'xx1 2   3xx')
print match.group()

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
    print match.group()  ## 'b@google'
    

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
print re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)







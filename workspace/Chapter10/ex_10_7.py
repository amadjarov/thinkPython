def is_anagram(t,u):
    if sorted(t) == sorted(u):
        print True
    else:
        print False
        
print is_anagram('realtor', 'rotlear')
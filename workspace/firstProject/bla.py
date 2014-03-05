#===============================================================================
# number = input("What is the number? ")
# 
# floor = 0
# while floor <= number:
#     floor = floor+1
# floor = floor-1
# 
# print "The floor of", number, "is", floor
#===============================================================================

#===============================================================================
# def euclid(a,b):
# 
#     while b:
#         a,b = b,a % b
# 
#     return a  
# euclid(4,3)
#===============================================================================

result = [1]
candidates = range(3,1000)
base = 2
product = base

while candidates:
    while product < 1000:
        if product in candidates:
            candidates.remove(product)
        product = product+base
    result.append(base)
    base = candidates[0]
    product = base
    del candidates[0]

result.append(base)
print result
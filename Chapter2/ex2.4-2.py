price =24.95
dicount = 2/5*24.95
shippingFirstCopy=3
shippingEachAdditional=0.75
copies=60
total = copies * (price-dicount) + shippingFirstCopy + (59*shippingEachAdditional)
strTotal = str(total)
print "The total whosale cost for 60 copies  is " + strTotal

class Prints(object):
    def render(self,a):
        if a == "win":
            print "wiwiwi"
        elif a == "lose":
            print "looooose"
        elif a == "sthelse":
            print "srthelse"
        
ob = Prints()
ob.render("win")
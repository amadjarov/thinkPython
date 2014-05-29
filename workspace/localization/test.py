import gettext # mod­ule for the string replacement

t = gettext.translation('localization', "./locales")
# where does get­text find the lan­guage files
 
_ = t.ugettext
# def­i­n­i­tion of strings to be translated

print "Hello world"
print "My name is: %s"
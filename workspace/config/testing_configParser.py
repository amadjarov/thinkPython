from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

print parser.get('categories', 'file_with_words')

print parser.get('shots', 'number_of_tryes')
#print parser.get("shots","number")
print parser.options("categories")

print parser.sections()

print parser.items("shots")
try:
    parser.add_section("new_section")
    parser.set("new_section", "new_option", "new_value")
    parser.set("new_section", "new_option2", "new_value2")
    parser.set("new_section", "new_option3", "new_value3")
except:
    print "error"
    
print parser.get("new_section", "new_option")
print parser.get("new_section", "new_option2")
print parser.get("new_section", "new_option3")

with open("config.ini","w+") as fp: 
    parser.write(fp)
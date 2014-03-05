import os
cwd = os.getcwd()
print cwd
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname,name)
        if os.path.isfile(path):
            print path
        else:
            walk(path)
        
walk(cwd)
os.walk
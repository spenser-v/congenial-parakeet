cat_names = [] #empty array for names to be stored in
while True:
    print("Enter the name of cat " + str(len(cat_names) + 1) + " (Or enter nothing to stop.):")
    name = input #input function that will run until it's interrupted
    if name == '': #option to break the loop
        break
    cat_names = cat_names + [name] #list concatenation
print("The cat names are:") #print after the loop is broken
for name in cat_names:
    print(' ' + name)
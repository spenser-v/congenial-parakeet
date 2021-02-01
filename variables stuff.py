#def spam():
    #eggs = 31337
#spam() #called variable is local scope, not global scope
#print(eggs) #eggs is not still defined after calling the spam function

def spamm():
    egggs = 99
    bacon()
    print(egggs) #first local eggs (spamm_eggs)

def bacon():
    ham = 101
    egggs = 0 #different local eggs (bacon_eggs)

spamm()

def spammm():
    print(eggggs)
eggggs = 42
spammm()
print(eggggs)
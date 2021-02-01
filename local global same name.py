def spam():
    eggs = "spam local"
    print(eggs) #prints spam local

def bacon():
    eggs = "bacon local"
    print(eggs) #prints bacon local
    spam()
    print(eggs) #prints bacon local

eggs = "global"
bacon() #overwrites with parameters within the called function
print(eggs) #prints "global"

#set to global
#overwrites with bacon local, prints bacon local
#overwrites with spam local, prints spam local
#returns to bacon local, prints bacon local
#returns to global, prints global
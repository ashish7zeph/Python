def spam():
    global eggs     # global eggs statement tells python, in this function, eggs refers to the global variable
    eggs = 'spam'
    
eggs = 'global'
spam()
print(eggs)

# output- spam

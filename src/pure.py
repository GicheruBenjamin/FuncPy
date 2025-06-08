# Pure functions are the ones that dont have side effects on global scope

#Impure func
x = {1, 2, 3, 4}
def inc(itr):
    return {var + 1 for var in itr}

print(inc(x)) 

#Pure func
def inc_pure():
    x = {1, 2, 3, 4}
    return {var + 1 for var in x}

print(inc_pure())

        
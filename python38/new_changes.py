# Things cover
# -> Using assignement expression to simplify some code constructs
# -> Enforcing position-only arguments in your own functions
# -> Spedifying more precise type hints
# -> Using f-string for simpler debugging

# =======================================================
# ==== The walrus in the room: Assignment Expression ====
# =======================================================

# The biggest change in python3.8 is the introduction of assignment
# expressions. They are written in new notion (:=)
# NOTE: Assignemnt expression allows you to assign and return a value
# in the same expression. Eg:
print('\nwithout using assignment operator')
walrus = False
print(walrus)

# In python 3.8, you're allowed to combine these two statements into one,
# using walrus operator:
print('\nwith using assignment operator')
print(walrus := True)

# Better use
print('\nwhile loop without walrus operator')
inputs  = list()
while True:
    current = input('Write something: ')
    if current == 'quit':
        break
    inputs.append(current)
print('INPUTS: ', inputs)

print('\nwhile loop with walrus operator')
inputs = list()
while (current := input('write something: ')) != 'quit':
    inputs.append(current)
print('INPUTS: ', inputs)

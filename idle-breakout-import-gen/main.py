import base64
import crayons

print("{}".format(crayons.blue('Idle Breakout import code generator by 3kh0')))
print("{}".format(crayons.blue('Please enter numbers for the questions.\n')))
print("{}".format(crayons.cyan('\nWhat level you want to be on?')))
level = input()

print("{}".format(crayons.green('\nHow much money do you want?')))
money = input()

print("{}".format(crayons.yellow('\nHow much gold do you want?')))

gold = input()

print("{}".format(crayons.black('\nHow many Black Boxes do you want?')))
bb = input()

print("\nHow many skillpoints do you want?")
sp = input()

print("\nGenerating....")

encode = f"{level},{money},{gold},3,0,0,0,0,0,0,0,1,1,0,43595.78,999999,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,{bb},0,0,0,1,{sp},1,0,0"
finalCode = encode.encode("UTF-8")
result = base64.b64encode(finalCode)

print("\n\nHere is your code:\n")
print(result)

print("{}".format(crayons.red('\nCopy whats INSIDE the single quotes!\n')))
print("{}".format(crayons.blue('Idle Breakout import code generator by 3kh0')))
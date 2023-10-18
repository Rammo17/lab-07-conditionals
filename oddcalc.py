firstnum = input("Give me a number, any number... ")
secondnum = input("Okay, give me another number... ")
operation = input("And what operation do you want? mul/div/mod? ")
if operation == "mul":
    [print(float(firstnum) * float(secondnum))]
elif operation == "div":
    [print(float(firstnum) / float(secondnum))]
elif operation == "mod":
    [print(float(firstnum) % float(secondnum))]
else:
        [print("INVALID OPERATION")]
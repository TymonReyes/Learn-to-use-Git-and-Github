#First I use this import option to improve my terminal (it clear automatically)
#import os
#os.system("cls")

i=0
while i != 5 :
# I used the f comand to create a litle welcome to the user
    print(f"{"-" * 50}")
    print(f"{'Welcome to the number converter':^50}")
    print(f"{"-" * 50}")

    # We have to ask to the user to insert his number.
    num=int(input("Insert your number: "))

    # I have to ask to the user, what type of number will he convert.
    print(f"{" 1 - Decimal":>15}"), print(f"{" 2 - Binario":>15}"), print(f"{" 3 - Octal  ":>15}"), print(f"{" 4 - hexadecimal":>19}"),print(f"{" 5 - Exit \n":>14}")
    format = int(input("Select the format of your number: "))
    print(f"{" 1 - Decimal":>15}"), print(f"{" 2 - Binario":>15}"), print(f"{" 3 - Octal  ":>15}"), print(f"{" 4 - hexadecimal":>19}"),print(f"{" 5 - Exit \n":>14}")
    convertion = int(input("Select the format you want to convert: "))
    
    if format == 1:
        if convertion == 1:
            print("You selected the same format, please select a different one")
        elif convertion == 2:
            print(f"Your number in Binario is: {num:b}")
        elif convertion == 3:
            print(f"Your number in Octal is: {num:o}")
        elif convertion == 4:
            print(f"Your number in Hexadecimal is: {num:x}")
        else:
            print("Invalid convertion option")

    elif format == 2:
        num=bin(num)[2:]
        if convertion == 1:
            print(f"Your number in Decimal is: {num:d}")            
        elif convertion == 2:
            print("You selected the same format, please select a different one")
        elif convertion == 3:
            print(f"Your number in Octal is: {num:o}")
        elif convertion == 4:
            print(f"Your number in Hexadecimal is: {num:x}")
        else:
            print("Invalid convertion option")

    elif format == 3:
        if convertion == 1:
            print(f"Your number in Decimal is: {num:d}")            
        elif convertion == 2:
            print(f"Your number in Binario is: {num:b}")
        elif convertion == 3:
            print("You selected the same format, please select a different one")
        elif convertion == 4:
            print(f"Your number in Hexadecimal is: {num:x}")
        else:
            print("Invalid convertion option")

    elif format == 4:
        if convertion == 1:
            print(f"Your number in Decimal is: {num:d}")            
        elif convertion == 2:
            print(f"Your number in Binario is: {num:b}")
        elif convertion == 3:
            print(f"Your number in Octal is: {num:o}")
        elif convertion == 4:
            print("You selected the same format, please select a different one")
        else:
            print("Invalid convertion option")
    elif format == 5 or convertion == 0:
        i=5
    else :
        print("Invalid option")
# 







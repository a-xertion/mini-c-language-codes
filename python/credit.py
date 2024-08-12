number = input("Number: ")

if(len(number) != 13 and len(number) != 15 and len(number) != 16):
    print("INVALID")
    exit()

# commencing Luhn's Algorithm
length = len(number)
sum = 0
for x in range(length, 0, -1):
    if((length - x) % 2 == 0):
        double = int(number[x - 1 : x])
        if(2 * double > 9): # numbers doubled > 9, sum += digits of that number doubled == -9
            double = (2 * double) - 9
            sum += double
            print(" ** " + str(double) + " ** ", end = "")
        else:
            sum += double # getting 2 * every other digit in number
            print(" * " + str(double) + " * ", end = "")
    else:
        sum += int(number[x - 1 : x]) # getting the leftover digits' sum
        print(" " + str(number[x - 1: x]) + " ", end = "")
is_valid = False
print(sum)
if(sum % 10 == 0): # Luhn's Algorithm states that if sum % 10 == 0, then credit card is valid
    is_valid = True

if(is_valid):
    if(len(number) == 15 and (number[0 : 2] == "34" or number[0 : 2] == "37")):
        print("AMEX")
    elif(len(number) == 16 and (number[0 : 2] in {"51", "52", "53", "54", "55"} )):
        print("MASTERCARD")
    elif(len(number) == 13 or len(number) == 16 and number[0 : 1] == "4"):
        print("VISA")
else:
    print("INVALID")

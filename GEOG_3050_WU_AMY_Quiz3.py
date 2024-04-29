climate = input('Enter a Climate Type: ')

temps = eval(input('Enter a list of temperatures: '))

if climate=="Tropical":
    for i in range(0,len(temps)):
        if temps[i] <= 30:
            print("F")
        else:
            print("U")

elif climate=="Continental":
    for i in range(0,len(temps)):
        if temps[i] <= 25:
            print("F")
        else:
            print("U")
else:
    for i in range(0,len(temps)):
        if temps[i] <= 18:
            print("F")
        else:
            print("U")

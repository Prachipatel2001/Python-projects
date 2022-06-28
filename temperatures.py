#A program to convert temperatures to and from c to f

temp=input("enter the temperature: ")

degree= int(temp[:-1])
convert = temp[-1]

if convert.upper() == "C":
    result = int(round((9 * degree)/ 5+ 32))
    value=  "Fahrenheit"

elif convert.upper() == "F":
    result = int(round((degree- 32) * 5 / 9))
    value= "Celsius"

else:
    print("Incorrect")
    quit()

print("the temperature in", value, "is",result, "degrees.")    

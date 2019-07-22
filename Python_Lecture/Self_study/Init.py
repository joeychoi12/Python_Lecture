monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul":  "July"
}
print(monthConversions.get("Mar", "Not a valid Key"))




def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.upper() in "AEIOU":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input('Enter:')))

try:
    number = int(input("Enter a number"))
    print(number)
except:
    print("Invalid Input")

value = 10/0


open("employees.txt","r")
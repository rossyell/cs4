# A program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message otherwise 
def computergrade(clean_number):
    # To check if out of range
    if clean_number > 1.0 or clean_number < 0.0:
        return("Bad score - number is out of range")    
    elif clean_number >= 0.9:
        return("A")
    elif clean_number >= 0.8:
        return("B")
    elif clean_number >= 0.7:
        return("C")
    elif clean_number >= 0.6:
        return("D")
    else:
        return("F")
#
#
# begin execution
number = input("Please enter a number between 0.0 and 1.0: ")
try:
    clean_number = float(number)
    x = computergrade(clean_number)
    print(x)
    print("end of grading")
except:
    print("Bad Score - Please only enter numbers")

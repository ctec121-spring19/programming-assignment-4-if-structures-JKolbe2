# Module 3
#   Programming Assignment 4
#     Prob-2.py

# <YOUR NAME>

#input: Name, wage, regulars hours, overtime hours 
#process: tax withholding, insurance withholding
#output: take home pay
def main():
    # your code goes here
    #get person's name
    name = input("enter name: ")
    #get wage rate 
    hourlywage = eval( input("enter hourly wage: "))
    #get hours
    hours = eval(input("enter hours: "))

    #calculation
    #calculate overtime
    regularhours = hours
    overtimehours = 0 
    if hours > 40:
        overtimehours = hours - 40
        regularhours = 40

    regularwages = (regularhours * hourlywage)
    overtimewages = (overtimehours * hourlywage * 1.5)
    totalwages = (regularwages + overtimewages)

    taxwithheld = totalwages * 0.20
    insurancewithheld = totalwages * 0.10
    holdings = taxwithheld + insurancewithheld
    takehomepay = totalwages - holdings

    #print outputs



    print()
    print("Name:\t\t\t\t", name)
    print()
    print("Regular wages:\t\t\t", regularwages)
    print("Overtime wages:\t\t\t", overtimewages)
    print("Total wages:\t\t\t", totalwages)
    print()
    print("Tax Withholding:\t\t", taxwithheld)
    print("Insurance Withholding:\t\t", insurancewithheld)
    print()
    print("TakeHome Pay:\t\t", takehomepay)
    print()

main()
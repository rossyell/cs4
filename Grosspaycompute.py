# Prompt the user for hours and rate per hour to compute gross pay
#Define function to compute pay
def computepay(hours, rate):
#set basic variables
    work_hours = 40.00
    loading = 1.5
    #perfrom calculation
    try:
        worked_hours = float(hours)
        basic_rate = float(rate)
        # Determine if working greater than 40 hours, determine amount over and pay
        if worked_hours > work_hours:
            overtime = worked_hours - work_hours
            overtime_pay = overtime * basic_rate * loading
            standard_pay = work_hours * basic_rate
            tot_pay = overtime_pay + standard_pay
        else:
             tot_pay = worked_hours * basic_rate
     # this function will round the result
        round(tot_pay,2)
        return tot_pay
    except:
         print("Please only enter numbers")
#
# get basic info
hours = input("Enter work Hours: ")
rate = input("Enter basic Rate/hour: ")
x = computepay(hours, rate)
print("Total pay is ", x)
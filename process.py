# the line 3 opens up the txt file and stores
# it into a variable for us to have access to it
log_file = open("um-server-01.txt")  

# the line 7 below is declaring a function called
# sales_reports passing in the open txt as it's argument
def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)

# line 8 starts a for loop to go through each line of the txt file
# line 9 removes any trailing characters from the end of each line 
# line 10 takes the first three indices of each line and sets it equal to the variable day
# line 11 check if the day is equal to a certain day
# line 12 prints all the lines that meet the conditional statement in line 11

# the line 17 is envoking the function declared above
sales_reports(log_file)

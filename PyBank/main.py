import csv

# In this challenge, you are tasked with creating a Python script for analyzing the 
# financial records of your company. You will give a set of financial data called 
# budget_data.csv found in the 'Resources' folder. The dataset is composed of 
# two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards 
# for accounting so the records are simple.)

# This Python script analyzes the records to calculate each of the following:
#
# The total number of months included in the dataset
#
# The net total amount of "Profit/Losses" over the entire period
#
# The average of the changes in "Profit/Losses" over the entire period
#
# The greatest increase in profits (date and amount) over the entire period
#
# The greatest decrease in losses (date and amount) over the entire period
#
# As an example, the analysis should look similar to the one below:
# 
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

# In addition, the analysis will both print the results to the terminal and export 
# a text file with the results.
# -----------------------------------
# 
# In this script I went down 2 paths and ended up selecting using the list functions, but
# left the homemade logic as both was working.
# 

with open("Resources/budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')

    # initialize the variables to 0 or empty for the lists
    profit_loss_month_count = 0                  # number of months
    dec = 0                                      # storage of the greatest loss between 2 months
    inc = 0                                      # storage of the greatest increase between 2 months
    previous = 0                                 # temporary storage of the previous record when looping through the months
    total_change = 0                             # total change
    total_profit_loss = 0                        # total of the profit and loss
    average_profit_loss = 0                      # storage of the average of the profit and loss change.
    

    # Strip off the header
    header = next(csv_reader)

    for row in csv_reader:

        # Use programming logic, loop through all the entries check for the greatest increase, greatest decrease
        # change.  Change is determined by taking the current entry and finding the difference from the previous 
        # month.  For the first entry ignore the change.  Also keep track of the total change, total profit and loss
        # plus the number of months being looked at. 

        # Calculate the change from the previous profit / loss.  
        change = int(row[1]) - previous

        if profit_loss_month_count == 0:

             # for the first row set the dec and inc variables to compare against
            greater_dec_proloss = row
            dec = int(row[1])
            greater_inc_proloss = row
            inc = int(row[1])
            previous = int(row[1])
            change = 0                                  # ignore the first profit / loss

        # for the other rows check to see if the profit is greater than the last max value
        elif dec > change:
            greater_dec_proloss = row
            dec = change

        # if not greater check to see if it is the least or the biggest decrease
        elif inc < change:
            greater_inc_proloss = row
            inc = change
        
        # count the number of months
        profit_loss_month_count += 1

        # sum the total profit_loss
        total_profit_loss += int(row[1])

        # keep track of the total change
        total_change += change

        # store the profit / loss for next comparison
        previous = int(row[1])

            
# calculate the average of the change which occurred between the profit_loss_months.  Since this is the 
# difference there where one less change and there by the subtraction of 1.
average_profit_loss = total_change/(profit_loss_month_count - 1)

# write the information to the file 'results'in the folder 'a'nalysis'
f = open("analysis/results.txt","w",newline='\n')
f.write("Financial Analysis \n")
f.write("-------------------------------\n")
f.write("Total Months: " + str(profit_loss_month_count) + "\n")
f.write("Total Profit / Loss: $" + str(total_profit_loss) + "\n")
f.write("Average change: $" + str(round(average_profit_loss,2)) + "\n")

f.write("Greatest Increast in Profits: " + str(greater_inc_proloss[0]) + " ($" + str(inc) + ")\n")
f.write("Greatest Decrease in Profits: " + str(greater_dec_proloss[0]) + " ($" + str(dec) + ")\n")

# close the file and then use the file to display the results to the sreen
f.close

# Print the file
f = open("analysis/results.txt","r")
file_contents = f.read()
print (file_contents)
    
f.close

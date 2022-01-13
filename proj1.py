#Christina Nguyen, 1/9/2021, puts answered data into a chart
initials = input("Enter Analyst initials:") #These are the questions
date = input("Enter Date of test:")
arsLevel = input("Enter arsenic level found:")
leadLevel = input("Enter lead level found:")
benLevel = input("Enter benzene level found:")


print("Water Analysis Report\n") #This is the chart
print("Contaminant\tResults\tUnits\tMCL" + " " *3, "Date\tAnalyst")
print("-----------\t-------\t-----\t---"+ " " *3, "----\t-------")
print("Arsenic\t\t", arsLevel, " ug/L\t10" + " " *4,date + "\t", initials)
print("Lead\t\t", leadLevel, "\tppb\t15" + " " *4, date +"\t", initials)
print("Benzene\t\t", benLevel, "\tppb\t5" + " " *5, date +"\t", initials)

#Unforunately, I didn't end up planning and went straight to coding.
#This caused me to write 20 lines of useless code.
#I started off coding a vertical design and then midway through switched to horizontial.
#I ended up testing A LOT. 
#For tests I if I were to type in a number with more than three decemial the alignment would be off. 
#Because of that I'm exspecting the user to only work with three decemial places.
#Tabing twice gave me too much space and multiplying the spaces is kind of tedious. I wish I could learn how to format faster.
#Something that I learned from this assignment is to plan before I code.

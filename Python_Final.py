#################################
#Author:        Blake Prebeck   #
#Due Date:      8/14/2021       #
#Assignment:    Final Exam      #
#################################


##################################################
#Decomposition
##################################################

#Calculate total number of cans collected
    #Data in: cans list
    #return: total cans
#Calculate average number of cans collected
    #Data in: total cans
    #return: average cans
#Calculate number of classrooms that collected above the average
    #Data in: cans array, average
    #return: Number of classes above average
#Find class with the highest number of cans collected.
    #Data in: cans array
    #return: string data of highest class
#Output Function
    #Call and output all other functions
    #Have print statements
#Main Function
    #Data: Declare cans array
    #Call Output Function


##################################################
#Program
##################################################

#Calculate total cans collected
def TotalCans(in_cans):
    #Variables
    cans_total = int(0)

    #Loop for total
    for i in range(len(in_cans)):
        cans_total = cans_total + in_cans[i]

    return cans_total

#Calculate average cans
def AverageCans(in_total):
    #Variables
    cans_average = float()

    #Calculation for average
    cans_average = in_total / 9

    return cans_average

#Calculate how many classes are above average
def AboveAverageCans(in_cans, in_average):

    #Variables
    cans_above = int(0)

    #Loop for above average
    for i in range(len(in_cans)):
        if in_cans[i] > in_average:
            cans_above = cans_above + 1
        else:
            pass

    return cans_above

#Calculate class with highest collected
def HighestCans(in_cans):

    #Variables
    cans_highest = int()
    class_highest = int()
    class_grade = str()

    #Find highest in array
    cans_highest = max(in_cans)
    class_highest = in_cans.index(cans_highest)

    #If structure for class grade
    if class_highest == 0:
        class_grade = 'Kindergarten'
    elif class_highest == 1:
        class_grade = '1st Grade'
    elif class_highest == 2:
        class_grade = '2nd Grade'
    elif class_highest == 3:
        class_grade = '3rd Grade'
    elif class_highest == 4:
        class_grade = '4th Grade'
    elif class_highest == 5:
        class_grade = '5th Grade'
    elif class_highest == 6:
        class_grade = '6th Grade'
    elif class_highest == 7:
        class_grade = '7th Grade'
    elif class_highest == 8:
        class_grade = '8th Grade'

    return class_grade

#Output function
def OutputCans(in_cans):

    #Output Total
    print('The total cans collected are:  ', TotalCans(in_cans))

    #Output Average
    print('The average cans collected are:  ', AverageCans(TotalCans(in_cans)))

    #Output Above Average
    print('There were ', AboveAverageCans(in_cans, AverageCans(TotalCans(in_cans))), 'classes above average!')

    #Output Highest Class
    print('The class with the highest collections was:  ', HighestCans(in_cans))

#Define main()
def main():

    #Declare Array
    cans = [248, 379, 189, 457, 274, 532, 279, 296, 359]

    #Call output function
    OutputCans(cans)

#Call main
main()

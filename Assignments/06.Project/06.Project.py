#Name of Files
inputfilename = "Assignments/06.Project/06.Project Input File.txt"
mergefilename = "Assignments/06.Project/06.Project Merge File.txt"
outputfilename = "Assignments/06.Project/06.Project Output File.txt"

#Keeping Count of Lines
inputrecord = 0
mergerecord = 0
outputrecord = 0

#Open Input and Merge for Reading and Output for Writing
inputfile = open(inputfilename, 'r')
mergefile = open(mergefilename, 'r')
outputfile = open(outputfilename, 'w')

#Close Input and Merge and Output Files
inputfile.close()
mergefile.close()
outputfile.close()

#printing the Count Records
print(inputrecord, "input file records")
print(mergerecord, "merge file records")
print(outputrecord, "output file records")
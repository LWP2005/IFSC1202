#Name of Files
inputfilename = "Assignments/06.Project/06.Project Input File.txt"
mergefilename = "Assignments/06.Project/06.Project Merge File.txt"
outputfilename = "Assignments/06.Project/06.Project Output File.txt"

#Keeping Count of Lines
inputrecord = 0
mergerecord = 0
outputrecord = 0

#Open Input and Merge for Reading and Output for Writing
outputfile = open(outputfilename, 'w')
inputfile = open(inputfilename, 'r')
mergefile = open(mergefilename, 'r')

#Creating Output File
inputline = inputfile.readline()
while inputline != '':
    outputfile.write(inputline)
    inputrecord += 1
    outputrecord += 1
    inputline = inputfile.readline()
    if 'This file is for testing purposes.' in inputline:
        mergeline = mergefile.readline()
        while mergeline != '':
            outputfile.write(mergeline)
            mergerecord += 1
            outputrecord += 1
            mergeline = mergefile.readline()
        outputfile.write("\n")

#Close Input and Merge and Output Files
inputfile.close()
mergefile.close()
outputfile.close()

#printing the Count Records
print(inputrecord, "input file records")
print(mergerecord, "merge file records")
print(outputrecord, "output file records")
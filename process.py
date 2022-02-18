

log_file = open("um-server-01.txt")
# to open um-server-01.txt file in this python project


def sales_reports(log_file):  # defining the function
    for line in log_file:  # starting a for loop to select a line or lines in the file
        # when it is selecting the line the .rstrip() method removesspace and trailing characters
        line = line.rstrip()
        # This selects a certain section in the line which in this case is the day
        day = line[0:3]
        if day == "Mon":  # if statement stating to print line if it contains a certain day
            print(line)


sales_reports(log_file)

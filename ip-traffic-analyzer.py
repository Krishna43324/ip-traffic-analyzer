# Name: Krishna Chinta
# Program Name: Final Coding Project
# Brief Description: This program takes a file with IP address and returns the number of records, suspect IP addresses, % of suspect IP addresses, and list of suspect IP addresses sorted by the address

records = dict()
suspects = []
def func():
    boolean = True
    while boolean:
        path = input("Enter the path and name of the input file: ")
        try:
            x = open(path,"r")
            boolean = False
        except:
            print("There is an error")
    return x
x = func()

def output():
    boolean = True
    while boolean:
        output_file = input("Enter the path and name of the output file: ")
        try:
            t = open(output_file,"w")
            boolean = False
        except:
            print("There is an error")
    t.seek(0)
    return t
output_file = output()

def output_report(records, suspects, output_file):
    dates = []
    time = []
    y = 0
    a = 0
    for line in x:
        records[y] = line
        z = line.split(" ")
        n = z[0]
        if line.startswith("168.193") or line.startswith("224.174") or line.startswith("233.012"):
            suspects.append(n)
            dates.append("" + z[1] + " " + z[2] + " " + z[3] + " " + z[4] + " " + z[5])
            a+=1
            
        y+=1
    #print(records)
    #print(suspects)
    #print(y)
    #print(a)
    suspectoutput = ""
    b = 0
    for element in suspects:
        suspectoutput += (f"IP Address  = {element}  ")
        suspectoutput += (f"Date and Time = {dates[b]}\n")
        b += 1
    numrecords = (f"The total number of records in this file are {y}.")
    numsuspects = (f"The number of suspect IP addresses are {a}.")
    percentsuspect =  (f"The percentage of suspect IP addresses are {(a/y)}.")
    listsuspects = (f"The list of suspect addresses is {suspects}.")
    report_output = (f"{numrecords} \n{numsuspects} \n{percentsuspect} \nSuspect IP Addresses \n -------------------- \n{suspectoutput }")
    
    output_file.write("Output Report\n-------------\n" + report_output)
    return report_output
print("Output Report\n-------------")
report = output_report(records, suspects, output_file)
print(report)
x.close()
output_file.close()

## Student Information
- Name: Krishna Chinta
- Email: kchinta1@umbc.edu

## Project Title
IP-Traffic-Analyzer

## Project Overview
This project contains a python script that can automate the process of manually examining logs for suspicious network traffic. By parsing a large list of IP addresses, date and time, and other fields, it calculates the total percentage of suspicious network packets and prints all suspicious IPs analyzed from the logs.

## Goal of this Project
The goal or purpose of this project is to demonstrate that a simple python script can be used and tuned to filter high-volume logs in order to extract the data that a security administrator needs to see.

## Technologies and Concepts Used
1. Python
2. Error Handling
3. File I/O
4. Data Structures (dictionaries, lists)
5. String Parsing 

## Key Features & Functionality
1. Targeted Pattern Matching: Automatically scans logs for specific high-risk IP prefixes using efficient string-matching logic.

2. Automated Security Metrics: Calculates the total record count and volume and percentage of suspicious hits.

3. Automated Report Generation: Exports all findings into a structured .txt file, including a visual separator and headers for easy reading.

## Setup:
1. Clone the repository by typing ‘git clone https://github.com/Krishna43324/ip-traffic-analyzer.git’
2. Run the script by typing ‘python ip-traffic-analyzer.py’
3. When receiving the prompt “Enter the path and name of the input file”, type testFileOfIPs.txt.
4. When receiving the prompt “Enter the path and name of the output file”, type the name of the file that you want the output to be written to. For example, you can name it output.txt.
5. The output file should be generated in the same directory that the Python script is located in. Open that file to see the output.

## Sample Input
```
python .\ip-traffic-analyzer.py
Enter the path and name of the input file: testFileOfIPs.txt
Enter the path and name of the output file: output.txt
```
## Sample Output
```
Output Report
-------------
The total number of records in this file are 103657.
The number of suspect IP addresses are 11.
The percentage of suspect IP addresses are 0.00010611922012020413.
Suspect IP Addresses
 --------------------
IP Address  = 224.174.179.128  Date and Time = Thu Jul  7 09:50:43
IP Address  = 233.012.007.208  Date and Time = Thu Jul  7 09:50:57
IP Address  = 168.193.123.124  Date and Time = Thu Jul  7 09:50:57
IP Address  = 233.012.100.137  Date and Time = Thu Jul  7 09:50:59
IP Address  = 224.174.229.191  Date and Time = Thu Jul  7 09:51:00
IP Address  = 224.174.127.229  Date and Time = Thu Jul  7 09:51:01
IP Address  = 224.174.035.037  Date and Time = Thu Jul  7 09:51:01
IP Address  = 224.174.200.210  Date and Time = Thu Jul  7 09:51:01
IP Address  = 168.193.202.160  Date and Time = Thu Jul  7 09:51:01
IP Address  = 233.012.161.124  Date and Time = Thu Jul  7 09:51:02
IP Address  = 168.193.070.208  Date and Time = Thu Jul  7 09:51:02
```

## My Role && Contribution
This project was fully designed and implemented by me. I wrote the whole Python script that provided the full functionality to read and interpret logs.

## Reflection
One of the main challenges was ensuring the program handled errors where the file path did not exist and was formatted incorrectly. A lesson learned was that aggressive testing of the program results in increased robustness of the program.

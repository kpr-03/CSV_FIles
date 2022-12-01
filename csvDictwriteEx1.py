#python program to demonstrate writing to csv file---csv Dictwriter---Dictwriter().
#importing csv module
import csv
#my data rows as dictionary objects
mydict =[ {'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
		{'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
		{'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
		{'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
		{'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
		{'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}   ]
#filed names
csvfileds=['name','branch','year','cgpa']
#name of csv file
file_name="univ2.csv"
#writing to csv file
with open(file_name,'w')as fp:
    #creating csv dictwriter object
    dictwriter=csv.DictWriter(fp,fieldnames=csvfileds)
    #writing headers(filed names)
    dictwriter.writeheader()
    # writing data rows
    dictwriter.writerows(mydict)
    print("\n CSV file created and dict data written to csv file--verify!!")
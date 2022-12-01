#program for reading the data from csv file by using csv module
import csv   # csv module contains reader(file pointer) return an object of reader class
with open("emp.csv","r")as fp:
    kpr=csv.reader(fp)     # here, kpr is an object of reader class of csv module
    for row in kpr:
        for val in row:
            print("{}".format(val),end="  ")
        print()
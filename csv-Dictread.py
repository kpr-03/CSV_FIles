#program for reading the data from csv file by using csv module
import csv  # csv module contains reader(file pointer) return an object of reader class.
with open("univ2.csv","r")as fp:
    kpr=csv.DictReader(fp) # here, kpr is an object of class'csv.DictReader' of csv module
    for record in kpr:
        for k,v in record.items():
            print("{}---->{}".format(k,v))
        print()
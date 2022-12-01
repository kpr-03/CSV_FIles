#python program to demonstrate writing to csv file---csv writer---writer().
import csv
#field names
recfields=['Names','Branch','Year','CGPA']
#data rows of csv file
rows=[['NIkhil','CSE','2','9.0'],
['utkarsh','cse','2','9.1'],
['abhishek','IT','2','9.3'],
['prem','ME','3','9.5'],
['sahil','MCE','1','7.8'],
['prateek','EP','2','9.1']]
#name of csv file
csvfilename="univ1.csv"
#writing data to csv file
with open(csvfilename,'w') as fp:
    #creating a csv writer object
    csvwriter=csv.writer(fp)
    #writing the fields
    csvwriter.writerow(recfields)
    #writing the data rows
    csvwriter.writerows(rows)
    print("\nCSV file created--verify!!!")
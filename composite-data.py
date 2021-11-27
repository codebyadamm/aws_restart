import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>",
    "model" : "<empty>",
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# REMINDER: Research f strings in Python

for key, value in myVehicle.items():
    print("{} : {}".format(key,value), '\n')
    
myInventoryList = []

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1
        else:
            print(f'vin: {row[0]} make: {1}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["vin"] = row[1]
            currentVehicle["vin"] = row[2]
            currentVehicle["vin"] = row[3]
            currentVehicle["vin"] = row[4]
            currentVehicle["vin"] = row[5]
            currentVehicle["vin"] = row[6]
            currentVehicle["vin"] = row[7]
            myInventoryList.append(currentVehicle)
            lineCount += 1
    print(f'Processed {lineCount} lines.', '\n')
            
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        #print("-----")
        # As parameter print (line 46) executes we manually insert hyphen line breaks before the parameter print re-executes as it goes down the list
        

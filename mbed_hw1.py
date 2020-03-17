# Part. 1
import csv

# Part. 2

cwb_filename = '107061106.csv'
data = []
header = []
i = 0

with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        if row["station_id"] == "C0A880" or row["station_id"] == "C0F9A0" or row["station_id"] == "C0G640" or row["station_id"] == "C0R190" or row["station_id"] == "C0X260":
            data.append(row)
            i += 1

# Part. 3

for n in range(i):
    # remove data over -99 and -999
    if data[n]["TEMP"] == "-99"or data[n]["TEMP"] == "-999":
        data[n]["TEMP"] = "None"
    n += 1

station = [[], [], [], [], []]

def classfication(temp, num):
    if (temp != 'None'):
        station[num].append(float(temp))

for n in range(i):
    if data[n]["station_id"] == "C0A880":
        classfication(data[n]["TEMP"], 0)
    elif data[n]["station_id"] == "C0F9A0":
        classfication(data[n]["TEMP"], 1)
    elif data[n]["station_id"] == "C0G640":
        classfication(data[n]["TEMP"], 2)
    elif data[n]["station_id"] == "C0R190":
        classfication(data[n]["TEMP"], 3)
    elif data[n]["station_id"] == "C0X260":
        classfication(data[n]["TEMP"], 4)

sta = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
target_data = []

for a in range(5):
    if (station[a] != []):
        maximum = max(station[a])
    else:
        maximum = 'None'
    target_data.append([sta[a], maximum])

# Part. 4 print answer
print(target_data)

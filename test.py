import csv

# Open the input file and read the data
with open('#2212211_DevA1-FM7inj-FM8-NL_10K_AS03_0p5mA_offset+73p75mV_5spm4_50rdg_100plc_230217.dat', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# Delete first unnecessary lines
data = data[32:len(data)]

# Find the indices where the field strength changes sign
sign_changes = [i for i in range(1, len(data)) if (float(data[i][0]) * float(data[i-1][0])) < 0]

# Split the data into separate columns based on the sign changes
columns = []
for i in range(len(sign_changes) - 1):
    column = [row[1] for row in data[sign_changes[i]:sign_changes[i+1]]]
    columns.append(column)

# Write the columns to a new CSV file
with open('output_file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in zip(*columns):
        writer.writerow(row)
import csv

with open('#2212211_DevA1-FM7inj-FM8-NL_10K_AS03_0p5mA_offset+73p75mV_5spm4_50rdg_100plc_230217.dat', 'r') as f:
    lines = f.readlines()

# Zmienne
sweep_number = 1
splitted_sweeps = [[], []]
mag = 0
vol = 1


# Function to find how many steps there are per cycle
def find_steps():
    a = round(splitted_sweeps[0][0])
    b = round(splitted_sweeps[0][1])
    step = abs(a - b)
    steps = 2 * (a / step)-1
    return int(abs(steps))


# Delete first unnecessary lines
lines = lines[32:len(lines)]

# Split into separate columns
i = 0
j = 0
steps_in_cycle = 999
for line in lines:
    splitted_sweeps[mag].append(float(line.split(',')[4]))
    splitted_sweeps[vol].append(float(line.split(',')[24]))

    if j == 1:
        steps_in_cycle = find_steps()

    i += 1
    j += 1

    if i == steps_in_cycle:
        i = 0
        splitted_sweeps.append([])
        splitted_sweeps.append([])

        sweep_number += 1
        mag += 2
        vol += 2

splitted_sweeps = splitted_sweeps[:-2]

# Save to CSV file
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in zip(*splitted_sweeps):
        writer.writerow(row)

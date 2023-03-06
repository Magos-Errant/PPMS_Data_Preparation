import csv
import os

# Define directory path
dir_path = "./Input"

# Load files from directory
files = os.listdir(dir_path)

for file in files:
    with open(f'./Input/{file}', 'r') as f:
        lines = f.readlines()

    #Variables
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
    steps_in_cycle = 999
    for line in lines:
        fields = line.split(',')
        if len(fields) >= 5:
            mag_value = float(fields[4])
            vol_value = float(fields[24])
            splitted_sweeps[mag].append(mag_value)
            splitted_sweeps[vol].append(vol_value)

            if len(splitted_sweeps[mag]) == 2:
                steps_in_cycle = find_steps()

            i += 1
            if i == steps_in_cycle:
                i = 0
                splitted_sweeps.append([])
                splitted_sweeps.append([])

                sweep_number += 1
                mag += 2
                vol += 2

    splitted_sweeps = splitted_sweeps[:-2]

    # Save to CSV file
    with open(f'./Output/{file[:-3]}csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in zip(*splitted_sweeps):
            writer.writerow(row)

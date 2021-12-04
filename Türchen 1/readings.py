with open("Türchen 1/readings.txt", "r") as readings_file:
  readings_content = readings_file.readlines()

larger_readings = 0

readings_ints = []

for line in readings_content:
    readings_ints.append(int(line))

for reading in readings_ints:
    next_index = readings_ints.index(reading) + 1
    next_end = readings_ints.index(reading) + 2
    for reading2 in readings_ints[next_index:next_end]:
        if reading2 > reading:
            larger_readings += 1

print(len(readings_ints))
print(larger_readings)
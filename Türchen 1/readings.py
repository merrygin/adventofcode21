with open("Türchen 1/readings.txt", "r") as readings_file:
  readings_content = readings_file.readlines()

larger_readings = 0

readings_ints = []

for line in readings_content:
    readings_ints.append(int(line))

index = 0

for reading in readings_ints:
    next_index = index + 1
    end_index = next_index +1
    print(index, next_index, end_index)
    for reading2 in readings_ints[next_index:end_index]:
        if reading2 > reading:
            larger_readings += 1
        index += 1



"""print(readings_ints)
"""
print(larger_readings)
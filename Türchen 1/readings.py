with open("Türchen 1/readings.txt", "r") as readings_file:
  readings_content = readings_file.readlines()

larger_readings = 0

readings_ints = []

for line in readings_content:
    readings_ints.append(int(line))


for reading in readings_ints[:14:1]:
    # ok, das geht nicht, weil die werte von reading öfter vorkommen... so nimmt er nicht immer den korrekten index
    next_index = readings_ints.index(reading) + 1
    end_index = next_index + 1
    print(readings_ints.index(reading))
    for reading2 in readings_ints[next_index:end_index]:
        #print(reading2, readings_ints.index(reading2))
        if reading2 > reading:
            larger_readings += 1



"""print(readings_ints)
"""
print(larger_readings)
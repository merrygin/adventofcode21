with open("Türchen 1/readings.txt", "r") as readings_file:
  readings_content = readings_file.readlines()

# prepare the counting of larger readings
larger_readings = 0
index = 0

# convert txt into list of ints
readings_ints = []
for line in readings_content:
    readings_ints.append(int(line))

# take every reading and compare to the next by slicing it out of the whole list
for reading in readings_ints:
    # use indeces as slice parameters
    next_index = index + 1
    end_index = next_index +1
    for reading2 in readings_ints[next_index:end_index]:
        if reading2 > reading:
            larger_readings += 1
        index += 1

print(larger_readings)
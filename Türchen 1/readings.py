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

print("Number of readings that is larger than the previous: " + str(larger_readings))

# set up new indeces to provide 3-pair slices; also, new count of larger measures
threestart_index = 0
threeend_index = 3
larger_threesomes = 0

# set up a loop that will continue collecting pairs of three and compare them
while True:
    A = 0
    B = 0
    # compute A and advance the indeces, also break here if end of list is reached
    for threesome_reading in readings_ints[threestart_index:threeend_index]:
        A += threesome_reading
    threestart_index += 1
    threeend_index += 1
    if threeend_index == 2001:
        break
    # compute B and compare if A is smaller than B, then count if true
    for three_some_reading2 in readings_ints[threestart_index:threeend_index]:
        B += three_some_reading2
    if B > A:
        larger_threesomes += 1

print("Number of three-pair measures that are larger than the previous three: " + str(larger_threesomes))
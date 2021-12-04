with open("Türchen 2/diving_instructions.txt", "r") as diving_file:
  diving_instructions = diving_file.readlines()

# set up coordinates and counter for good poppin'
index_counter = 0
x = 0
y = 0

while True:
    # Read next command (aka, line)
    command = diving_instructions.pop(0)
    print("Reading command {}: ".format(index_counter) + command)
    speed = 0

    # Compute speed instruction
    for each in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        if each in command:
            speed = int(each)

    # Compile command and follow it. Captain barks order!
    if "forward" in command:
        print("Advance " + str(speed) + " paces!")
        x += speed
    elif "up" in command:
        print("Rise " + str(speed) + " paces!")
        y -= speed
    elif "down" in command:
        print("Dive " + str(speed) + " paces!")
        y += speed

    # Advance counter to hit the breaks in time!
    index_counter += 1
    if index_counter == 1000:
        break

# Give our final position
print(
    "Where are we...?!\n" + 
    "We are at a depth of {} fathoms and advanced {} paces.\n".format(x, y) + 
    "Our destination coordinate is: " + str(x*y)
    )

import sys
file = open(sys.argv[1], "r", encoding = "utf-8")


try:
    for line in f:
        name = line.split(":")[0]
        university = line.split(":")[1].split(",")[0]
        department = line.split(":")[1].split(",")[1]
        print("Name: " + str(name) + "\nUniversity: " + str(university) + "\nDepartment: " + str(department))

except:
    print("\nNo record of '{}' was found!".format(name))



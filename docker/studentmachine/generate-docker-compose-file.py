#!/usr/bin/env python2
#
# This script will generate a docker-compose file and create n number of
# * private networks in1 172.20.x.0/24
# * studentmachine docker instances
# * n * m sshmachine docker instances
#
# author: Frank Gut
# version: 0.1

import sys

def prepare_header(f):
    f.write("version: '2'\r\n\r\n")
    f.write("networks:\r\n")

def write_networks(f,i):
    f.write("  studentnet%02d:\r\n" %(i,))
    f.write("    ipam:\r\n")
    f.write("      config:\r\n")
    f.write("        - subnet: 172.20.%1d.0/24\r\n" %(i,))
    f.write("\r\n")


def write_studentmachines(f,i):
    f.write("  studentmachine%02d:\r\n" %(i,))
    f.write("    image: studentmachine:latest\r\n")
    f.write("    ##build: .\r\n")
    f.write("    container_name: studentmachine%02d\r\n" %(i,))
    f.write("    environment:\r\n")
    f.write("      - TZ=Europe/Berlin\r\n")
    f.write("    ports:\r\n")
    f.write("      - \"220%02d:22\"\r\n" %(i,))
    f.write("    volumes:\r\n")
    f.write("      - /var/run/docker.sock:/var/run/docker.sock:rw\r\n")
    f.write("      - /usr/bin/docker:/usr/bin/docker:ro\r\n")
    f.write("      - /usr/local/bin/docker-compose:/usr/local/bin/docker-compose:ro\r\n")
    f.write("    networks:\r\n")
    f.write("      studentnet%02d:\r\n" %(i,))
    f.write("        ipv4_address: 172.20.%1d.100\r\n" %(i,))
    f.write("\r\n")


def write_sshmachines(f,i,sshmachinesPerGroup):
    a = 1
    while a <= sshmachinesPerGroup:
        print("Generate sshmachine%02d%02d\r" %(i,a))
        f.write("  sshmachine%02d%02d:\r\n" %(i,a))
        f.write("    image: sshmachine:latest\r\n")
        f.write("    ##build: .\r\n")
        f.write("    container_name: sshmachine%02d%02d\r\n" %(i,a))
        f.write("    environment:\r\n")
        f.write("      - TZ=Europe/Berlin\r\n")
        f.write("    networks:\r\n")
        f.write("      studentnet%02d:\r\n" %(i,))
        f.write("        ipv4_address: 172.20.%1d.%1d\r\n" %(i,a+1))
        f.write("\r\n")
        a = a + 1



def main():
    print "This script will generate our docker-compose file for the sitlecture."
    print "Opening docker-compose.yml file..."
    f = open("./docker-compose.yml", "w+")
    prepare_header(f)

    # Ask user how many groups should be created
    numberOfgropus = 0
    sshmachinesPerGroup = 0
    try:
        numberOfgropus = int(input("How many student groups (studentmachines docker containers) should be generated? \r\n Min:1, Max: 20:"))
    except ValueError:
        print("Input needs to be a whole number between 1 - 20")
    if numberOfgropus not in range(1,21):
        sys.exit("Error: Please only enter numbers between 1-20")

    try:
        sshmachinesPerGroup = int(input("How many sshmachines should be generated for each group\r\n Min:1, Max, 10:"))
    except ValueError:
        print("Input needs to be a whole number between 1 - 10")
    if sshmachinesPerGroup not in range(1,11):
        sys.exit("Error: Please only enter numbers between 1-10")


    print "Will generate " + str(numberOfgropus) + " studentmachines with " + str(
        sshmachinesPerGroup) + " sshmachines per group..."



    # Write networks
    i = 1
    while i <= numberOfgropus:
        print("Generate studentnet %02d\r" %(i,))
        write_networks(f,i)
        i = i + 1

    # Write services
    f.write("services:\r\n")

    # Write studentmachines
    i = 1
    while i <= numberOfgropus:
        print("Generate studentmachine %02d\r" %(i,))
        write_studentmachines(f,i)
        i = i + 1

    # Write sshmachines
    i = 1
    while i <= numberOfgropus:
        write_sshmachines(f,i, sshmachinesPerGroup)
        i = i + 1


    f.close()


if __name__ == "__main__":
    main()

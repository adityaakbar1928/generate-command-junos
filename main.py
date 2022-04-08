"""
Mass VLAN command generator for Junos
Generate multiple commands for:
- Add multiple vlans to multiple interfaces
- Delete multiple vlans to multiple interfaces
"""
from art import tprint
import time
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def menu():
    tprint("Aditya A.K.A El Bappo")
    print("Welcome!\n"
          "Features:\n"
          "1. Add multiple vlans to multiple interfaces (max 3 interfaces)\n"
          "2. Delete multiple vlans to multiple interfaces\n")
    opsi = int(input("Choose tools: "))
    if opsi == 1:
        addvlan()
    elif opsi == 2:
        delvlan()
    else:
        print("Invalid...Back to Menu!!")
        time.sleep(3)
        clearConsole()
        return menu()

def addvlan():
    print("You choose add multiple vlans to multiple interfaces")
    print("Enter your range VLAN, eg: First vlan is 1, and your End vlan is 40")
    vlan_range_start = int(input("First vlan is?: "))
    vlan_range_end = int(input("End vlan is?: "))
    vlans = range(vlan_range_start,vlan_range_end+1)
    print("Great, now enter how many interfaces you want to set this vlan ? eg: 1 or 2 or maximum 3")
    jumlahint = int(input("How Many: "))
    if jumlahint == 1:
        int1 = input("What interfaces? eg: ge-0/0/1:> ")
        print("Creating a Magic!")
        for x in range(len(vlans)):
            vlan = vlans[x]
            bm1 = "set interfaces "
            bm2 = " unit 0 family ethernet-switching vlan members VLAN-"
            messages = bm1+str(int1)+bm2+str(vlan)
            with open('vlans.txt', 'a') as f:
                f.write(messages)
                f.write('\n')
    elif jumlahint == 2:
        int1 = input("What the first interfaces? eg: ge-0/0/1:> ")
        int2 = input("What the second interfaces? eg: ge-0/0/1:> ")
        print("Creating a Magic!")
        for x in range(len(vlans)):
            vlan = vlans[x]
            bm1 = "set interfaces "
            bm2 = " unit 0 family ethernet-switching vlan members VLAN-"
            messages = bm1 + str(int1) + bm2 + str(vlan)
            with open('vlans.txt', 'a') as f:
                f.write(messages)
                f.write('\n')
        for x in range(len(vlans)):
            vlan = vlans[x]
            bm1 = "set interfaces "
            bm2 = " unit 0 family ethernet-switching vlan members VLAN-"
            messages2 = bm1 + str(int2) + bm2 + str(vlan)
            with open('vlans.txt', 'a') as f:
                f.write(messages2)
                f.write('\n')
    elif jumlahint == 3:
        int1 = input("What the first interfaces? eg: ge-0/0/1:> ")
        int2 = input("What the second interfaces? eg: ge-0/0/1:> ")
        int3 = input("What the third interfaces? eg: ge-0/0/1:> ")
        print("Creating a Magic!")
        for x in range(len(vlans)):
            vlan = vlans[x]
            bm1 = "set interfaces "
            bm2 = " unit 0 family ethernet-switching vlan members VLAN-"
            messages = bm1 + str(int1) + bm2 + str(vlan)
            with open('vlans.txt', 'a') as f:
                f.write(messages)
                f.write('\n')
        for x in range(len(vlans)):
            vlan = vlans[x]
            bm1 = "set interfaces "
            bm2 = " unit 0 family ethernet-switching vlan members VLAN-"
            messages2 = bm1 + str(int2) + bm2 + str(vlan)
            with open('vlans.txt', 'a') as f:
                f.write(messages2)
                f.write('\n')
        for x in range(len(vlans)):
            vlan = vlans[x]
            bm1 = "set interfaces "
            bm2 = " unit 0 family ethernet-switching vlan members VLAN-"
            messages3 = bm1 + str(int3) + bm2 + str(vlan)
            with open('vlans.txt', 'a') as f:
                f.write(messages3)
                f.write('\n')
    else:
        print("Invalid...Back to Menu!")
        time.sleep(3)
        clearConsole()
        return menu()

    print("All done! check vlans.txt file!")
    time.sleep(3)
    clearConsole()
    return menu()

def delvlan():
    print("You choose delete multiple vlans from multiple interfaces")
    print("Enter your range VLAN, eg: First vlan is 1, and your End vlan is 40")
    vlan_range_start = int(input("First vlan is?: "))
    vlan_range_end = int(input("End vlan is?: "))
    vlans = range(vlan_range_start,vlan_range_end+1)
    print("Great, now enter how many interfaces you want to delete these vlan ? eg: 1 or 2 or maximum 3")
    jumlahint = int(input("How Many: "))
    if jumlahint == 1:
        int1 = input("What interfaces? eg: ge-0/0/1:> ")
        print("Creating a Magic!")
        for x in range(len(vlans)):
            vlan = vlans[x]
            bm1 = "delete interfaces "
            bm2 = " unit 0 family ethernet-switching vlan members VLAN-"
            messages = bm1+str(int1)+bm2+str(vlan)
            with open('vlans.txt', 'a') as f:
                f.write(messages)
                f.write('\n')
    elif jumlahint == 2:
        int1 = input("What the first interfaces? eg: ge-0/0/1:> ")
        int2 = input("What the second interfaces? eg: ge-0/0/1:> ")
        print("Creating a Magic!")
        for x in range(len(vlans)):
            vlan = vlans[x]
            bm1 = "delete interfaces "
            bm2 = " unit 0 family ethernet-switching vlan members VLAN-"
            messages = bm1 + str(int1) + bm2 + str(vlan)
            with open('vlans.txt', 'a') as f:
                f.write(messages)
                f.write('\n')
        for x in range(len(vlans)):
            vlan = vlans[x]
            bm1 = "delete interfaces "
            bm2 = " unit 0 family ethernet-switching vlan members VLAN-"
            messages2 = bm1 + str(int2) + bm2 + str(vlan)
            with open('vlans.txt', 'a') as f:
                f.write(messages2)
                f.write('\n')
    elif jumlahint == 3:
        int1 = input("What the first interfaces? eg: ge-0/0/1:> ")
        int2 = input("What the second interfaces? eg: ge-0/0/1:> ")
        int3 = input("What the third interfaces? eg: ge-0/0/1:> ")
        print("Creating a Magic!")
        for x in range(len(vlans)):
            vlan = vlans[x]
            bm1 = "delete interfaces "
            bm2 = " unit 0 family ethernet-switching vlan members VLAN-"
            messages = bm1 + str(int1) + bm2 + str(vlan)
            with open('vlans.txt', 'a') as f:
                f.write(messages)
                f.write('\n')
        for x in range(len(vlans)):
            vlan = vlans[x]
            bm1 = "delete interfaces "
            bm2 = " unit 0 family ethernet-switching vlan members VLAN-"
            messages2 = bm1 + str(int2) + bm2 + str(vlan)
            with open('vlans.txt', 'a') as f:
                f.write(messages2)
                f.write('\n')
        for x in range(len(vlans)):
            vlan = vlans[x]
            bm1 = "delete interfaces "
            bm2 = " unit 0 family ethernet-switching vlan members VLAN-"
            messages3 = bm1 + str(int3) + bm2 + str(vlan)
            with open('vlans.txt', 'a') as f:
                f.write(messages3)
                f.write('\n')
    else:
        print("Invalid...Back to Menu!")
        time.sleep(3)
        clearConsole()
        return menu()

    print("All done! check vlans.txt file!")
    time.sleep(3)
    return menu()

menu()
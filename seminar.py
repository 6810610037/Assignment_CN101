# 6810610037 โกมล บุญเรือง

capacity = int(input("Capacity: "))
seats = []
waitlists = []

while True:
    command = input("Command (reg/cancel/drop/status/exit): ")
    if command == "reg":
        name = input("Name: ")
        if name not in seats:
            if capacity > len(seats):
                seats.append(name)
                free = capacity - len(seats)
                print(f"->Confirmed: {name}")
                print(f"Seats left: {free}")
                print()
            else:
                if name in seats or name in waitlists:
                    print(
                        f"-> Duplicate. {name} already registered (confirmed/waitlist)."
                    )
                    print()
                    continue
                elif capacity == len(seats):
                    waitlists.append(name)
                    print(f"-> Full. Added to waitlist: {name}")
                    print(f"Seats left: {free}")
                    print()
        else:
            print(f"-> Duplicate. '{name}' already registered (confirmed/waitlist).")
            print()
    if command == "cancel":
        name = input("Name: ")
        if name in seats:
            seats.remove(name)
            print(f"->Removed from confirmed: {name}")
            print(f"-> Moved from waitlist to confirmed: {waitlists[0]}")
            print(f"Seats left: {free}")
            seats.append(waitlists[0])
            waitlists.remove(waitlists[0])
            print(f"Confirmed: {seats}")
            print(f"Waitlist : {waitlists}")
            print()
        else:
            print(f"-> Not found in confirmed: {name}")
            print(f"Confirmed: {seats}")
            print(f"Waitlist : {waitlists}")
            print()
    if command == "drop":
        name = input("Name: ")
        if name in waitlists:
            waitlists.remove(name)
            print(f"->Removed from waitlist: {name}")
            print(f"Confirmed: {seats}")
            print(f"Waitlist : {waitlists}")
            print(f"Seats left: {free}")
            print()
        else:
            print(f"-> Not found in waitlist: Mike")
            print()
    if command == "status":
        print(f"Confirmed: {seats}")
        print(f"Waitlist : {waitlists}")
        print(f"Seats left: {free}")
        print()
    if command == "exit":
        break

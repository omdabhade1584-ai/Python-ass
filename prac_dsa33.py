
patients = []

# 1. Add Patient (Enqueue)
def enqueue():
    pid = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")

    print("1. Critical")
    print("2. Serious")
    print("3. Normal")

    priority = int(input("Enter Priority: "))

    if priority not in [1, 2, 3]:
        print("Invalid Priority!")
        return

    patient = (priority, pid, name)
    patients.append(patient)

    # Sort according to priority
    patients.sort()

    print("Patient added successfully!")


# 2. Display Next Patient
def display_next():
    if not patients:
        print("No patients waiting.")
    else:
        priority, pid, name = patients[0]

        print("\nNext Patient to be Treated")
        print("Patient ID:", pid)
        print("Patient Name:", name)
        print("Priority:", priority)


# 3. Remove Patient (Dequeue)
def dequeue():
    if not patients:
        print("No patients waiting.")
    else:
        priority, pid, name = patients.pop(0)

        print("Patient treated successfully!")
        print("Patient ID:", pid)
        print("Patient Name:", name)


# 4. Display All Patients
def display_all():
    if not patients:
        print("No patients waiting.")
    else:
        print("\nWaiting Patients (Priority Order)")

        for priority, pid, name in patients:
            print("ID:", pid,
                  "| Name:", name,
                  "| Priority:", priority)


# Main Menu
while True:
    print("\n===== HOSPITAL EMERGENCY MANAGEMENT =====")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient")
    print("4. Display All Patients")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        display_next()
    elif choice == 3:
        dequeue()
    elif choice == 4:
        display_all()
    elif choice == 5:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!")

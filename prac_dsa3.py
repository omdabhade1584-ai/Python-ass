
# Hospital Emergency Management using Priority Queue

patients = []

# 1. Add Patient (Enqueue)
def enqueue():
    pid = int(input("Enter Patient ID: "))
    name = input("Enter Patient Name: ")
    priority = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

    if priority not in [1, 2, 3]:
        print("Invalid Priority!")
        return

    patient = [priority, pid, name]
    patients.append(patient)

    patients.sort(key=lambda x: x[0])

    print("Patient added successfully!")


# 2. Display Next Patient
def display_next():
    if len(patients) == 0:
        print("No patients waiting!")
    else:
        print("\nNext Patient to be Treated:")
        print("Patient ID:", patients[0][1])
        print("Patient Name:", patients[0][2])
        print("Priority:", patients[0][0])


# 3. Remove Patient (Dequeue)
def dequeue():
    if len(patients) == 0:
        print("No patients to remove!")
    else:
        treated = patients.pop(0)

        print("\nPatient Treated Successfully!")
        print("Patient ID:", treated[1])
        print("Patient Name:", treated[2])


# 4. Display All Waiting Patients
def display_all():
    if len(patients) == 0:
        print("No patients waiting!")
    else:
        print("\nAll Waiting Patients:")

        for patient in patients:
            print("----------------------")
            print("Patient ID:", patient[1])
            print("Patient Name:", patient[2])
            print("Priority:", patient[0])


# Main Menu
while True:
    print("\n===== HOSPITAL EMERGENCY MANAGEMENT =====")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient After Treatment")
    print("4. Display All Waiting Patients")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        enqueue()

    elif choice == '2':
        display_next()

    elif choice == '3':
        dequeue()

    elif choice == '4':
        display_all()

    elif choice == '5':
        print("Exiting Hospital Management System...")
        break

    else:
        print("Invalid choice! Please try again.")

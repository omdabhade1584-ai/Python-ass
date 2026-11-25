
class Node:
    def __init__(self, patient_id, name, priority):
        self.patient_id = patient_id
        self.name = name
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    # Add patient according to priority
    def enqueue(self, patient_id, name, priority):
        new_node = Node(patient_id, name, priority)

        # If queue is empty or new patient has higher priority
        if self.front is None or priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node

        else:
            temp = self.front

            # Find the correct position
            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

        print("Patient added successfully!")


    # Display next patient
    def display_next(self):
        if self.front is None:
            print("No patients waiting.")
        else:
            print("\nNext Patient to be Treated:")
            print("Patient ID:", self.front.patient_id)
            print("Name:", self.front.name)
            print("Priority:", self.front.priority)


    # Remove patient after treatment
    def dequeue(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            temp = self.front
            print("\nPatient treated:", temp.name)
            self.front = self.front.next
            temp.next = None


    # Display all patients
    def display_all(self):
        if self.front is None:
            print("No patients waiting.")
            return

        temp = self.front

        print("\nWaiting Patients (Priority Order):")
        print("-----------------------------------")

        while temp is not None:
            print("Patient ID:", temp.patient_id)
            print("Name:", temp.name)
            print("Priority:", temp.priority)

            if temp.priority == 1:
                print("Status: Critical")
            elif temp.priority == 2:
                print("Status: Serious")
            else:
                print("Status: Normal")

            print("-----------------------------------")
            temp = temp.next


# Main Program
pq = PriorityQueue()

while True:
    print("\n===== HOSPITAL EMERGENCY MANAGEMENT =====")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient (After Treatment)")
    print("4. Display All Patients")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        priority = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

        if priority >= 1 and priority <= 3:
            pq.enqueue(patient_id, name, priority)
        else:
            print("Invalid priority! Enter 1, 2 or 3.")

    elif choice == 2:
        pq.display_next()

    elif choice == 3:
        pq.dequeue()

    elif choice == 4:
        pq.display_all()

    elif choice == 5:
        print("Exiting Hospital Management System.")
        break

    else:
        print("Invalid choice! Try again.")

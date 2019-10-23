import time


def main():

    program = True

    #test
    patient_list_queue = []

    # TEMP CODE
    print("Please do some shit")
    patient_list_queue.append(Patient(10, "Jacob"))
    patient_list_queue[0].display_patient()
    patient_list_queue.append(Patient(2, "Sarah"))
    patient_list_queue[1].display_patient()
    # TEMP CODE END

    while(program != False):

        userinput = str(input())


        # WINDOW ACTIONS CONDITIONS
        if(userinput == "Exit"):
            program = False
            return 0
        # Function Call for Sort
        if(userinput == "Sort"):
            print("are you sure?")
            print("yes or no")
            queueListSort()

#Function that will retrieve patient information and sort it into the linked list
def insertPatientIntoList(patient_list_queue, patient_name, patient_prio): #TODO
    pass
    print("Patient name: ", patient_name)
    print("\nPriority: ", patient_prio)
    update = input("\nUpdate this list? <Y/N>: ")
    while(update == "y" or update == "Y"):
        update_patient_name = input("Update patient's name: ")
        patient_list_queue[patient_name] = update_patient_name
        update_patient_prior = int(input("Update patient's priority: "))
        patient_list_queue[patient_prio] = update_patient_prior
        update = input("\nUpdate this list? <Y/N>")

    print("Update Complete...")
    return patient_list_queue

#Function that allows patient records to be accessed and manipulated in the list
def accessPatientRecord(patient_list_queue): #TODO
    pass
    patient = input("Which patient's record you wish to access: ")
    for patient_name in patient_list_queue:
        if patient_name == patient:
            patient_prio = patient_name+2
            print(patient_list_queue[patient:patient_prio])
    return patient_name, patient_prio
    insertPatientIntoList( patient_list_queue, patient_name, patient_prio)



# -------------------------------------- #
# Function that forces the values in the #
# list to sort                           #
# Usage: is to allow a mid section update#
# in a patient file                      #
# -------------------------------------- #
def queueListSort(patient_list_queue): #TODO
    pass
    accessPatientRecord(patient_list_queue)
    insertPatientIntoList(patient_list_queue, patient_name, patient_prio)
    update_list = input("Do you want to update list again? <Y/N> ")
    while update_list == "y" or update_list == "Y":
        accessPatientRecord(patient_list_queue)
        insertPatientIntoList(patient_list_queue, patient_name, patient_prio)
        update_list  = input("Do you want to update list again? <Y/N> ")
    print("List update successful...")

# ------------------------------------- #
# Function that requests a patient file #
# from the queue for the doctor then    #
# saves and closes the file             #
# ------------------------------------- #
def closePatientFile(): #TODO
    pass


# Patient Class Definition
class Patient:

    patient_count = 1

    # -------------------------------------------------------------------- #
    # Constructor Function                                                 #
    # Usage: Retrieve the critical level and paitent name from main        #
    #        Assigns a patient number and entry time upon constructor call #
    # -------------------------------------------------------------------- #
    def __init__(self, critical_level, patient_name):
        self.critical_level = critical_level
        self.patient_name = patient_name
        self.patient_entry_time = time.time()
        self.patient_number = Patient.patient_count
        Patient.patient_count += 1

    def display_patient(self):
        print("Patient Number: " + str(self.patient_number), "Patient Name: " + self.patient_name,
              "Patient Critical Level: " + str(self.critical_level), "Patient Entry Time: " + str(self.patient_entry_time))


main()

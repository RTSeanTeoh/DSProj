import time
patient_list_queue = []

def main():

    program = True


    # test
    # patient_list_queue = []



    # TEMP CODE
    print("Please do some shit")
    patient_list_queue.append(Patient(10, "Jacob"))
    patient_list_queue[0].display_patient()
    patient_list_queue.append(Patient(2, "Sarah"))
    patient_list_queue[1].display_patient()
    # TEMP CODE END

    # ------------------------- #
    # Runtime Initiation for    #
    # Program                   #
    # ------------------------- #
    while program:

        userinput = str(input())

        # WINDOW ACTIONS CONDITIONS
        if (userinput == 'Exit') or (userinput == 'exit'):
            program = False
            return 0
        # ----------------------------------------- #
        # Function Call for insertPatientIntoList() #
        # Usage: To create new patient information  #
        #        and pass it into the function to   #
        #        insert the information into the    #
        #        linked list for storage            #
        # ----------------------------------------- #
        if (userinput == 'New')or (userinput == 'new'):
            insertPatientIntoList()

        # Function Call for Sort
        if userinput == 'Sort':
            print("are you sure?")
            print("yes or no")
            queueListSort()
        # Function Call for commandlist
        if (userinput == 'help') or (userinput == 'list'):
            commandlist()

        else:
            userinput = None









# Function that will retrieve patient information and sort it into the linked list
def insertPatientIntoList(): #TODO
    new_patient = Patient(critical_level=str(input("Critical Level: ")), patient_name=str(input("Patient Name: ")))
    patient_list_queue.append(new_patient)

#Function that allows patient records to be accessed and manipulated in the list
def accessPatientRecord(): #TODO
    pass

# -------------------------------------- #
# Function that forces the values in the #
# list to sort                           #
# Usage: is to allow a mid section update#
# in a patient file                      #
# -------------------------------------- #
def queueListSort(): #TODO
    pass

# ------------------------------------- #
# Function that requests a patient file #
# from the queue for the doctor then    #
# saves and closes the file             #
# ------------------------------------- #
def closePatientFile(): #TODO
    pass

# Prints a list of available commands for the user
def commandlist():
    print("---------------------------------------------------------------")
    print("Command | Description |")
    print("--------------------------------------")
    print("| New | Enter a new patient into the queue |")
    print("| Sort | Sorts the Queue of Patients |")
    print("| Treat | Closes a Patient file for Doctors |")
    print("| Help | Show the list of Command Available |")
    print("| Exit | Close the program, Warning!Queue Data is not Saved |")
    print("--------------------------------------------------------------")

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
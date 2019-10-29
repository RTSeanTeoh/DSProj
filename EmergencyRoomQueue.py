import time
import operator

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
        if (userinput == 'New') or (userinput == 'new'):
            new_patient_insert_into_list()

        # Function Call for Sort
        if (userinput == 'Sort') or (userinput == 'sort'):
            print("Do you want to sort the queue?")
            print("Yes or No")
            userinput = str(input("Choice: "))
            if (userinput == 'Yes') or (userinput == 'yes'):
                sort_queue()
            elif (userinput == 'No') or (userinput == 'no'):
                print("Returning to Menu...")
            else:
                print("Invalid choice...")

        # Function Call for List All in Queue
        if (userinput == 'listall') or (userinput == 'listall'):
            for i in range(len(patient_list_queue)):
                patient_list_queue[i].display_patient()

        # Function Call for Function Commands List
        if (userinput == 'help') or (userinput == 'list'):
            function_call_command_list()

        userinput = None


# Function that will retrieve patient information and sort it into the linked list
def new_patient_insert_into_list():  # TODO
    new_patient = Patient(critical_level=int(input("Critical Level: ")), patient_name=str(input("Patient Name: ")))
    patient_list_queue.append(new_patient)


# Function that allows patient records to be accessed and manipulated in the list
def access_patient_pecord():  # TODO
    pass


# -------------------------------------- #
# Function that forces the values in the #
# list to sort                           #
# Usage: is to allow a mid section update#
# in a patient file                      #
# -------------------------------------- #
def sort_queue():  # TODO

    # -------------------------------------------- #
    # Complex Sort, sorting based on               #
    # Critical Level & Entry Time                  #
    # -------------------------------------------- #
    # Step 1:                                      #
    # Call upon the inbuilt python sorted function #
    # to sort the patients based on entry time     #
    # and store into entry_sort variable           #
    # -------------------------------------------- #
    # entry_sort = sorted(patient_list_queue, key=operator.attrgetter('patient_entry_time'))
    patient_list_queue.sort(key=operator.attrgetter('patient_entry_time'))


    # -------------------------------------------- #
    # Step 2:                                      #
    # Call upon the inbuilt python sorted function #
    # to sort the patients based on critical level #
    # and store into critical_sort variable        #
    # -------------------------------------------- #
    # patient_list_queue = sorted(entry_sort, key=operator.attrgetter('critical_level'))
    patient_list_queue.sort(key=operator.attrgetter('critical_level'))

# ------------------------------------- #
# Function that requests a patient file #
# from the queue for the doctor then    #
# saves and closes the file             #
# ------------------------------------- #
def close_patient_file():  # TODO
    pass


# ------------------------------------- #
# Function that prints all values inside#
# the linked list                       #
# Usage: To view all the sorted data    #
#        within the list                #
# ------------------------------------- #
def list_all_in_queue():
    pass


# Prints a list of available commands for the user
def function_call_command_list():  # TODO
    print("---------------------------------------------------------------")
    print("Command | Description |")
    print("--------------------------------------")
    print("| New | Enter a new patient into the queue |")
    print("| Sort | Sorts the Queue of Patients |")
    print("| Listall | Print a list of all patients in queue |")
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
        self.patient_entry_time_display = time.strftime("%c")
        self.patient_number = Patient.patient_count
        Patient.patient_count += 1

    def display_patient(self):
        print(" Patient Number\t\t\t: " + str(self.patient_number) + "\n",
              "Patient Name\t\t\t: " + self.patient_name + "\n",
              "Patient Critical Level\t: " + str(self.critical_level) + "\n",
              "Patient Entry Time\t\t: " + self.patient_entry_time_display + "\n")


main()

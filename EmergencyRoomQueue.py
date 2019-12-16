import time
import operator

patient_list_queue = []


def main():
    program = True

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

        # Function Call for Treat
        if (userinput == 'Treat') or (userinput == 'treat'):
            treat_patient()

        # Function Call for List All in Queue
        if (userinput == 'listall') or (userinput == 'listall'):
            list_all_in_queue()

        # Function Call for Function Commands List
        if (userinput == 'help') or (userinput == 'list'):
            function_call_command_list()

        userinput = None


# Function that will retrieve patient information and sort it into the linked list
def new_patient_insert_into_list():  # WESLY CODE
    # Call upon Patient Constructor to input new patient instance into list
    new_patient = Patient(critical_level=int(input("Critical Level: ")), patient_name=str(input("Patient Name: ")))
    patient_list_queue.append(new_patient)
    # TODO
    # Currently takes new patient and auto sorts whole list
    # Better alternative is to use slice and insert method through search and insertion
    sort_queue()

# Function that allows patient records to be accessed and manipulated in the list
def access_patient_record():  # WESLY CODE

    update = "Y"
    while update == "Y":
        decide_name = input("Which patient's record you wish to access: ")
        for patient_name in patient_list_queue:
            if patient_name == decide_name:
                temp1 = patient_list_queue[patient_name]
                temp2 = patient_list_queue[patient_name - 1]
                patient_list_queue[patient_name] = input("Update the patient's name: ")
                patient_list_queue[patient_name - 1] = int(input("Update the patient's priority: "))
                print(temp1, "\nchanged to ", patient_list_queue[patient_name])
                print(temp2, "\nchanged to ", patient_list_queue[patient_name - 1])
                final = input("\nConfirm change? <Y/N> ")
                if final == "N":
                    patient_list_queue[patient_name] = temp1
                    patient_list_queue[patient_name - 1] = temp2
        update = input("Update the list again? <Y/N> ")
    print("Update complete...")


# --------------------------------------------------------------- #
# Since the list will display as [critical level, Patient's Name] #
# The position will be changed by extracting 1 from the position  #
# of the Patient's name, if not just adding 1 from the position   #
# of the Patient's name.                                          #
# The purpose for using 2 temp value is to allow undo function    #
# --------------------------------------------------------------- #


# -------------------------------------- #
# Function that forces the values in the #
# list to sort                           #
# Usage: is to allow a mid section update#
# in a patient file                      #
# -------------------------------------- #
def sort_queue():  # SEAN CODE

    # -------------------------------------------- #
    # Complex Sort, sorting based on               #
    # Critical Level & Entry Time, python in built #
    # sort uses Timsort Method                     #
    # -------------------------------------------- #
    # Step 1:                                      #
    # Call upon the inbuilt python sort function   #
    # to sort the patients based on entry time     #
    # -------------------------------------------- #
    patient_list_queue.sort(key=operator.attrgetter('patient_entry_time'), reverse=True)

    # -------------------------------------------- #
    # Step 2:                                      #
    # Call upon the inbuilt python sort function   #
    # to sort the patients based on critical level #
    # -------------------------------------------- #
    patient_list_queue.sort(key=operator.attrgetter('critical_level'))

# ------------------------------------- #
# Function that requests a patient file #
# from the queue for the doctor then    #
# saves and closes the file             #
# ------------------------------------- #
def treat_patient():  # WESLY CODE, SEAN MODIFIED

    x = patient_list_queue.pop()
    x.display_patient()
    f = open("Patient.txt", "a")
    f.write(x.getPatientRecord())
    f.close()

# ------------------------------------------- #
# Open a new file with list of patient's name #
# Extract the value of the array list into    #
# the .txt file, showing patient's name and   #
# patient's critical level, the doctor later  #
# can request for treatment for the patient   #
# based on the critical level that just       #
# released, after extract the .txt file,      #
# the .txt file should be close               #
# ------------------------------------------- #

# ------------------------------------- #
# Function that prints all values inside#
# the linked list                       #
# Usage: To view all the sorted data    #
#        within the list                #
# ------------------------------------- #
def list_all_in_queue():  # SEAN CODE
    for i in range(len(patient_list_queue)):
        patient_list_queue[i].display_patient()


# Prints a list of available commands for the user
def function_call_command_list():  # SEAN CODE
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
class Patient:  # SEAN CODE
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

    def getPatientRecord(self):
        record_string = str(self.patient_number) + "\n" + self.patient_name + "\n"\
                       + str(self.critical_level) + "\n" + self.patient_entry_time_display + "\n"
        return record_string

main()

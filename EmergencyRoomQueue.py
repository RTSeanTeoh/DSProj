import time
import operator

patient_list_queue = []
checker = []

def main():
    program = True
    patient_count_loader()
    opening_menu()

    # ------------------------- #
    # Runtime Initiation for    #
    # Program                   #
    # ------------------------- #
    while program:

        print("User Input: ", end=' ')
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

        if (userinput == 'Retrieve') or (userinput == 'retrieve'):
            retrieve_patient_record()

        # Function Call for Treat
        if (userinput == 'Treat') or (userinput == 'treat'):
            treat_patient()

        # Function Call for List All in Queue
        if (userinput == 'Listall') or (userinput == 'listall'):
            list_all_in_queue()

        # Function Call for Function Commands List
        if (userinput == 'Help') or (userinput == 'help'):
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

# ----------------------------------------- #
# Function: To retrieve a Patient File from #
#           the Patient.txt folder          #
# Usage: Enter a patient number, then       #
#        searches the Patient.txt folder    #
#        to retrieve the Patient Record     #
def retrieve_patient_record():  # WESLY CODE
    # Take User Input for Patient Number
    print("Please Select The Patient ID Number for the Patient Record you wish to access")
    user_input = int(input("Input Patient Number: "))

    count = 0
    counter = 0
    record_list = []

    # Load all Patient Numbers into a list
    # Cuts Patient Name, Critical Level and Patient Entry Time Values
    f = open("Patient.txt", "r")
    for x in range(1, file_len("Patient.txt")):
        patient_number_check = f.readline()
        count += 1
        if count % 4 == 1:
            record_list.append(int(patient_number_check.rstrip("\n")))

    f.close()
    f = open("Patient.txt", "r")
    counter = 0

    # Compares User Input to Patient Number List
    for x in range(0, len(record_list)):
        if int(user_input) == record_list[x]:
            record = counter
            break
        counter += 1

    # Readlines to the chosen user input in Patient.txt
    for x in range(0, int(record)*4):
        f.readline()

    patient_number = f.readline().rstrip("\n")
    patient_name = f.readline().rstrip("\n")
    critical_level = f.readline().rstrip("\n")
    patient_entry_time_display = f.readline().rstrip("\n")
    f.close()

    # Prints Choice Record
    print(" Patient Number\t\t\t: " + str(patient_number) + "\n",
          "Patient Name\t\t\t: " + patient_name + "\n",
          "Patient Critical Level\t: " + str(critical_level) + "\n",
          "Patient Entry Time\t\t: " + patient_entry_time_display)

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
    print("---------------------------------------------------------------------")
    print("Command \t| Description \t\t\t\t\t\t\t\t\t\t\t|")
    print("---------------------------------------------------------------------")
    print("| New \t\t| Enter a new patient into the queue \t\t\t\t\t|")
    print("| Sort \t\t| Sorts the Queue of Patients \t\t\t\t\t\t\t|")
    print("| Listall \t| Print a list of all patients in queue \t\t\t\t|")
    print("| Treat \t| Closes a Patient file for Doctors \t\t\t\t\t|")
    print("| Retrieve \t| Retrieve a Patient file \t\t\t\t\t\t\t\t|")
    print("| Help \t\t| Show the list of Command Available \t\t\t\t\t|")
    print("| Exit \t\t| Close the program, Warning!Queue Data is not Saved  \t|")
    print("---------------------------------------------------------------------")

def patient_count_loader():

    f = open("Patient.txt", "r")
    f.seek(0)
    first_char = f.read(1)
    if first_char:
        file_length = file_len("Patient.txt")
        file_length /= 4
        Patient.patient_count = int(file_length)
    else:
        file_length = 1
        Patient.patient_count = int(file_length)
    f.close()

# File length checking Function
def file_len(fname):
    i = 0
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def opening_menu():
    print("""===============================================================================================
| WELCOME TO SW Hospital                                                                      |
| Section: Emergency Room                                                                     |
===============================================================================================""")
    function_call_command_list()


# Patient Class Definition
class Patient:  # SEAN CODE
    patient_count = 0

    # -------------------------------------------------------------------- #
    # Constructor Function                                                 #
    # Usage: Retrieve the critical level and patient name from main        #
    #        Assigns a patient number and entry time upon constructor call #
    # -------------------------------------------------------------------- #
    def __init__(self, critical_level, patient_name):
        Patient.patient_count += 1
        self.critical_level = critical_level
        self.patient_name = patient_name
        self.patient_entry_time = time.time()
        self.patient_entry_time_display = time.strftime("%c")
        self.patient_number = Patient.patient_count

    def display_patient(self):
        print(" Patient Number\t\t\t: " + str(self.patient_number) + "\n",
              "Patient Name\t\t\t: " + self.patient_name + "\n",
              "Patient Critical Level\t: " + str(self.critical_level) + "\n",
              "Patient Entry Time\t\t: " + self.patient_entry_time_display + "\n")

    def setPatientRecord(self, patient_number, critical_level, patient_name, patient_entry_time_display):
        pass
        self.patient_number = patient_number
        self.critical_level = critical_level
        self.patient_name = patient_name
        self.patient_entry_time_display = patient_entry_time_display

    def setPatientCount(self, patient_count):
        self.patient_count = patient_count

    # --------------------------------- #
    # This method is used to produce a  #
    # String to be used in file .txt    #
    # storage                           #
    # --------------------------------- #
    def getPatientRecord(self):
        record_string = str(self.patient_number) + "\n" + self.patient_name + "\n"\
                       + str(self.critical_level) + "\n" + self.patient_entry_time_display + "\n"
        return record_string

main()

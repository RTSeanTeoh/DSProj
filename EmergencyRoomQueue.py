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
def insertPatientIntoList(patient_list_queue): #TODO
    pass
    new_name = input("Patient's name: ")
    patient_list_queue.append(new_name)
    patient_list_queue.append(0)

    update = input("\nUpdate this list? <Y/N>: ")
    while(update == "y" or update == "Y"):
        new_name = input("Patient's name: ")
        patient_list_queue.append(new_name)
        patient_list_queue.append(0)
        update = input("\nUpdate this list? <Y/N>")

    print("Update Complete...")
    return patient_list_queue
#---------------------------------------------#
#The list should be show as                   #
#[(exiting data),new_name, 0}                 #
#The 0 is for later to be able to change later#
#Which do not need to use temp to keep all of #
#data                                         #
#---------------------------------------------#




#Function that allows patient records to be accessed and manipulated in the list
def accessPatientRecord(patient_list_queue): #TODO
    pass
    update = "Y"
    while(update == "Y"):
        decide_name = input("Which patient's record you wish to access: ")
        for patient_name in patient_list_queue:
            if patient_name == decide_name:
                temp1 = patient_list_queue[patient_name]
                temp2 = patient_list_queue[patient_name+1]
                patient_list_queue[patient_name] = input("Update the patient's name: ")
                patient_list_queue[patient_name+1] = int(input("Update the patient's priority: "))
                print(temp1, "\nchanged to ", patient_list_queue[patient_name])
                print(temp2, "\nchanged to ", patient_list_queue[patient_name+1])
                final = input("\nConfirm change? <Y/N> ")
                if final == "N":
                    patient_list_queue[patient_name] = temp1
                    patient_list_queue[patient_name+1] = temp2
        update = input("Update the list again? <Y/N> ")
    print("Update complete...")
#----------------------------------#
#The purpose for using 2 temp value#
#is to allow undo function         #
#----------------------------------#


# -------------------------------------- #
# Function that forces the values in the #
# list to sort                           #
# Usage: is to allow a mid section update#
# in a patient file                      #
# -------------------------------------- #
def queueListSort(patient_list_queue): #TODO
    pass


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
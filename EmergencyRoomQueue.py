import time


def main():

    program = True


    patient_list_queue = []

    print("Please do some shit")
    patient_list_queue.append(Patient(10, "Jacob"))
    patient_list_queue[0].display_patient()
    patient_list_queue.append(Patient(2, "Sarah"))
    patient_list_queue[1].display_patient()


    while(program != False):

        userinput = str(input())

        if(userinput == "Exit"):
            program = False
            return 0







#Function that will retrieve patient information and sort it into the linked list
def insertPatientIntoList(): #TODO
    pass

#Function that allows patient records to be accessed and manipulated in the list
def accessPatientRecord(): #TODO
    pass

# -------------------------------------- #
# Function that forces the values in the #
# list to sort                           #
# Usage is to allow a mid section update #
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
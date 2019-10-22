import time

class Patient:

    patient_count = 0

    # -------------------------------------------------------------------- #
    # Constructor Function                                                 #
    # Usage: Retrieve the critical level and paitent name from main        #
    #        Assigns a patient number and entry time upon constructor call #
    # -------------------------------------------------------------------- #
    def __init__(self, critical_level, patient_name):
        self.critical_level = critical_level
        self.patient_name = patient_name
        patient_entry_time = time.time()
        patient_number = Patient.patient_count
        Patient.patient_count += 1

    def display_patient(self):
        print("Patient Number: " + self.patient_number, "Patient Name: " + self.patient_name,
              "Patient Critical Level: " + self.critical_level, "Patient Entry Time: " + self.patient_entry_time)

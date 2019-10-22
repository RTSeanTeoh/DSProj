import time;

class Patient:
    def __init__(self, crit_level, patient_name, patient_number):
        self.crit_level = crit_level
        self.patient_name = patient_name
        self.patient_number = patient_number
        patient_entry_time = time.time()

import keyboard

class Clinic:
    def __init__(self):
        self.Doctors = {
            "Doc_A": {
                "Monday": ["Free", "Free", "Free", "Free"],
                "Tuesday": ["Free", "Free", "Free", "Free"],
                "Wednesday": ["Free", "Free", "Free", "Free"],
                "Thursday": ["Free", "Free", "Free", "Free"],
                "Friday": ["Free", "Free", "Free", "Free"],
                "Saturday": ["Free", "Free", "Free", "Free"],
                "Sunday": ["Booked"]
            },
            "Doc_B": {
                "Monday": ["Free", "Free", "Free", "Free"],
                "Tuesday": ["Free", "Free", "Free", "Free"],
                "Wednesday": ["Free", "Free", "Free", "Free"],
                "Thursday": ["Free", "Free", "Free", "Free"],
                "Friday": ["Free", "Free", "Free", "Free"],
                "Saturday": ["Free", "Free", "Free", "Free"],
                "Sunday": ["Booked"]
            },
            "Doc_C": {
                "Monday": ["Free", "Free", "Free", "Free"],
                "Tuesday": ["Free", "Free", "Free", "Free"],
                "Wednesday": ["Free", "Free", "Free", "Free"],
                "Thursday": ["Free", "Free", "Free", "Free"],
                "Friday": ["Free", "Free", "Free", "Free"],
                "Saturday": ["Free", "Free", "Free", "Free"],
                "Sunday": ["Booked"]
            }
        }

    def check_available_slots(self):
        DocToCheck = input("Enter Doctor Name: ")
        if DocToCheck in self.Doctors:
            DayWant = input("Enter Desired Day: ")
            if DayWant in self.Doctors[DocToCheck]:
                if DayWant == "Sunday":
                    print("Today No Slot Is Available")
                for index, slot in enumerate(self.Doctors[DocToCheck][DayWant]):
                    if slot == "Free":
                        print(f"Hour: {index}  Is: {slot}")
            else:
                print(f"Day: {DayWant} Not_Exists!")

        else:
            print("Invalid Doctor Name!")

    def check_busy_slots(self):
        DocToCheck = input("Enter Doctor Name: ")
        if DocToCheck in self.Doctors:
            DayWant = input("Enter Desired Day: ")
            if DayWant in self.Doctors[DocToCheck]:
                busy_slots = False
                for index, slot in enumerate(self.Doctors[DocToCheck][DayWant]):
                    if slot == "Booked":
                        print(f"Hour: {index}  Is: {slot}")
                        busy_slots = True
                if not busy_slots:
                    print("No slots are busy")
            else:
                print(f"Day: {DayWant} Not_Exists!")

        else:
            print("Invalid Doctor Name!")

    def book_slot(self):
        DocToCheck = input("Enter Doctor Name For Appointment: ")
        if DocToCheck in self.Doctors:
            DayWant = input("Enter Desired Day: ")
            if DayWant in self.Doctors[DocToCheck]:
                print("Slot 0 = 12 o'clock")
                print("Slot 1 = 1 o'clock")
                print("Slot 2 = 2 o'clock")
                print("Slot 3 = 3 o'clock")
                slot = int(input("Enter slot number (0-3) to book: "))
                if 0 <= slot < len(self.Doctors[DocToCheck][DayWant]):
                    if self.Doctors[DocToCheck][DayWant][slot] == "Free":
                        self.Doctors[DocToCheck][DayWant][slot] = "Booked"
                        print(f"Slot {slot} on {DayWant} has been booked")
                    else:
                        print("Slot already booked!")

                        if input("Enter 1 to exit, 2 to view free slots: ") == "2":
                            self.check_available_slots()

                        if input("Enter yes to book another slot: ").lower() == "yes":
                            self.book_slot()
                else:
                    print("Invalid slot!")
                    if input("Enter yes to book another slot: ").lower() == "yes":
                        self.book_slot()
            else:
                print(f"Day: {DayWant} Not_Exists!")
                if input("Enter yes to select another day: ").lower() == "yes":
                    self.book_slot()
        else:
            print(f"Doctor: {DocToCheck} Not_Exists!")
            if input("Enter yes to select another doctor: ").lower() == "yes":
                self.book_slot()


clinic = Clinic()

class Main:
    def __init__(self):
        while True:
            print("Choose an option:")
            print("1 : Check busy slots")
            print("2 : Check free slots")
            print("3 : Book slot")
            choice = input("Choose option: ")
            if choice == "1":
                clinic.check_busy_slots()
            elif choice == "2":
                clinic.check_available_slots()
            elif choice == "3":
                clinic.book_slot()
            else:
                print("Invalid option selected!")

            print("Press 'Esc' to exit or any other key to continue.")
            if keyboard.is_pressed('esc'):
                print("Exiting...")
                break
            else:
                input("Press Enter to continue: ")

main_obj = Main()















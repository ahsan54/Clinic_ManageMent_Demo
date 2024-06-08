from flask import Flask, render_template, request

app = Flask(__name__, template_folder='D:\\DPS\\Atm+ InfoData\\Clinic\\templates',
            static_folder='D:\\DPS\\Atm+ InfoData\\Clinic\\static')
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

    def check_available_slots(self, DocToCheck, DayWant):
        if DocToCheck in self.Doctors:
            if DayWant in self.Doctors[DocToCheck]:
                available_slots = []
                for index, slot in enumerate(self.Doctors[DocToCheck][DayWant]):
                    if slot == "Free":
                        available_slots.append(f"Hour: {index} Is: {slot}")
                if available_slots:
                    return '\n'.join(available_slots)
                else:
                    return "No available slots"
            else:
                return "Day not available"
        else:
            return "Doctor not available"

    def check_busy_slots(self, DocToCheck, DayWant):
        if DocToCheck in self.Doctors:
            if DayWant in self.Doctors[DocToCheck]:
                busy_slots = []
                for index, slot in enumerate(self.Doctors[DocToCheck][DayWant]):
                    if slot == "Booked":
                        busy_slots.append(f"Hour: {index} Is: {slot} ")
                if busy_slots:
                    return '\n'.join(busy_slots)
            else:
                return None
        else:
            return None

    def book_slot(self, DocToCheck, DayWant, slot):
        if DocToCheck in self.Doctors:
            if DayWant in self.Doctors[DocToCheck]:
                if DayWant != "Sunday":
                    if 0 <= slot < len(self.Doctors[DocToCheck][DayWant]):
                        if self.Doctors[DocToCheck][DayWant][slot] == "Free":
                            self.Doctors[DocToCheck][DayWant][slot] = "Booked"
                            return True
                        else:
                            return "Slot already booked"
                    else:
                        return "Invalid slot"
                else:
                    return "No slot available on Sunday"
        return "Invalid doctor or day"


clinic = Clinic()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/appoint')
def appoint():
    return render_template('appoint.html')

@app.route('/contact' , methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')



@app.route('/check_busy_slots', methods=['POST'])
def check_busy_slots():
    DocToCheck = request.form['doctor']
    DayWant = request.form['day']
    busy_slots = clinic.check_busy_slots(DocToCheck, DayWant)
    return f"<pre>{busy_slots}</pre>"


@app.route('/check_available_slots', methods=['POST'])
def check_available_slots():
    DocToCheck = request.form['doctor']
    DayWant = request.form['day']
    available_slots = clinic.check_available_slots(DocToCheck, DayWant)
    return f"<pre>{available_slots}</pre>"


@app.route('/book_slot', methods=['POST'])
def book_slot():
    DocToCheck = request.form['doctor']
    DayWant = request.form['day']
    slot = int(request.form['slot'])

    result = clinic.book_slot(DocToCheck, DayWant, slot)
    if result == True:
        message = f"Doctor: {DocToCheck} ==> Slot: {slot} On: {DayWant} has been booked"
    else:
        message = result

    return render_template('Appoint.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='D:\\DPS\\Atm+ InfoData\\Clinic\\templates',
            static_folder='D:\\DPS\\Atm+ InfoData\\Clinic\\static')
class Clinic:
    def __init__(self):
        self.Days = {
            "Monday": ["Free", "Free", "Free", "Free"],
            "Tuesday": ["Free", "Free", "Free", "Free"],
            "Wednesday": ["Free", "Free", "Free", "Free"],
            "Thursday": ["Free", "Free", "Free", "Free"],
            "Friday": ["Free", "Free", "Free", "Free"],
            "Saturday": ["Free", "Free", "Free", "Free"],
            "Sunday": ["Booked","Booked","Booked","Booked"]
        }

    def check_available_slots(self, day_to_check):
        if day_to_check in self.Days:
            available_slots = [index for index, slot in enumerate(self.Days[day_to_check]) if slot == "Free"]
            return available_slots
        else:
            return []

    def check_busy_slots(self, day_to_check):
        if day_to_check in self.Days:
            busy_slots = [index for index, slot in enumerate(self.Days[day_to_check]) if slot == "Booked"]
            return busy_slots
        else:
            return []

    def book_slot(self, day, slot):
        if day in self.Days:
            if self.Days[day][slot] == "Free":
                self.Days[day][slot] = "Booked"
                return True
        return False

clinic = Clinic()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_busy_slots', methods=['POST'])
def check_busy_slots():
    day_to_check = request.form['day']
    busy_slots = clinic.check_busy_slots(day_to_check)
    return render_template('index.html', busy_slots=busy_slots)

@app.route('/check_available_slots', methods=['POST'])
def check_available_slots():
    day_to_check = request.form['day']
    available_slots = clinic.check_available_slots(day_to_check)
    return render_template('index.html', available_slots=available_slots)

@app.route('/book_slot', methods=['POST'])
def book_slot():
    day = request.form['day']
    slot = int(request.form['slot'])
    if clinic.book_slot(day, slot):
        message = f"Appointment booked for {day} at {slot} o'clock."
    else:
        message = "Slot already booked."
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

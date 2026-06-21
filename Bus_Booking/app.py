from flask import Flask, render_template, request

app = Flask(__name__)

# Bus Data
buses = [
    {"id": 1,"name": "KPN Travels","source": "Chennai","destination": "Coimbatore","time": "08:00 PM","price": 750,"seats": 20},
    {"id": 2,"name": "Parveen Travels","source": "Chennai","destination": "Madurai","time": "09:00 PM","price": 800,"seats": 15},
    {"id": 3,"name": "SRM Travels","source": "Coimbatore","destination": "Chennai","time": "07:30 PM","price": 700,"seats": 18},
    {"id": 4,"name": "SRS Travels","source": "Madurai","destination": "Chennai","time": "10:00 PM","price": 850,"seats": 12},
    {"id": 5,"name": "YBM Travels","source": "Trichy","destination": "Chennai","time": "06:00 PM","price": 650,"seats": 22},
    {"id": 6,"name": "National Travels","source": "Chennai","destination": "Trichy","time": "08:30 PM","price": 650,"seats": 25},
    {"id": 7,"name": "Orange Travels","source": "Salem","destination": "Chennai","time": "09:15 PM","price": 600,"seats": 16},
    {"id": 8,"name": "Kallada Travels","source": "Chennai","destination": "Salem","time": "07:45 PM","price": 600,"seats": 20},
    {"id": 9,"name": "Vivegam Travels","source": "Erode","destination": "Chennai","time": "10:30 PM","price": 700,"seats": 14},
    {"id": 10,"name": "Rathimeena Travels","source": "Chennai","destination": "Erode","time": "08:45 PM","price": 700,"seats": 19}
]

selected_bus = {}
ticket_counter = 1001


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/search', methods=['POST'])
def search():

    source = request.form['source']
    destination = request.form['destination']

    available_buses = []

    for bus in buses:
        if (bus["source"].lower() == source.lower() and
                bus["destination"].lower() == destination.lower()):
            available_buses.append(bus)

    return render_template(
        "buses.html",
        buses=available_buses,
        source=source,
        destination=destination
    )


@app.route('/book/<int:bus_id>')
def book(bus_id):

    global selected_bus

    for bus in buses:
        if bus["id"] == bus_id:
            selected_bus = bus
            break

    return render_template(
        "passenger.html",
        bus=selected_bus
    )


@app.route('/confirm', methods=['POST'])
def confirm():

    global ticket_counter

    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    mobile = request.form['mobile']
    seats = int(request.form['seats'])

    if seats > selected_bus["seats"]:
        return f"""
        <h2>Booking Failed!</h2>
        <h3>Only {selected_bus['seats']} seats available.</h3>
        <a href='/'>Go Back</a>
        """

    total_amount = seats * selected_bus["price"]

    selected_bus["seats"] -= seats

    ticket_id = f"TKT{ticket_counter}"
    ticket_counter += 1

    return render_template(
        "confirmation.html",
        ticket_id=ticket_id,
        name=name,
        age=age,
        gender=gender,
        mobile=mobile,
        bus=selected_bus,
        seats=seats,
        total=total_amount
    )


if __name__ == '__main__':
    app.run(debug=True)

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def min_max_normalization(input, max_val, min_val):
    print(input)
    if input == None:
        return 0
    return float((input - min_val) / (max_val - min_val))


def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')


def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')

def predict():
    airline_mapping = {
        'Vistara': 1,
        'Air_India': 2,
        'Indigo': 3,
        'GO_FIRST': 4,
        'AirAsia': 5,
        'SpiceJet': 6
    }
    source_city_mapping = {
        'Delhi': 1,
        'Mumbai': 2,
        'Bangalore': 3,
        'Kolkata': 4,
        'Hyderabad': 5,
        'Chennai': 6
    }
    departure_time_mapping = {
        'Morning': 1,
        'Early_Morning': 2,
        'Evening': 3,
        'Night': 4,
        'Afternoon': 5,
        'Late_Night': 6
    }
    num_stops_mapping = {
        'one': 1,
        'zero': 2,
        'two_or_more': 3
    }
    arrival_time_mapping = {
        'Night': 1,
        'Evening': 2,
        'Morning': 3,
        'Afternoon': 4,
        'Early_Morning': 5,
        'Late_Night': 6
    }
    ticket_class_mapping = {
        'Economy': 1,
        'Business': 2
    }

    try:
        airline = airline_mapping.get(combobox_airline.get(), None)
        source_city = source_city_mapping.get(combobox_source_city.get(), None)
        departure_time = departure_time_mapping.get(combobox_departure_time.get(), None)
        num_stops = num_stops_mapping.get(combobox_num_stops.get(), None)
        arrival_time = arrival_time_mapping.get(combobox_arrival_time.get(), None)
        flight_class = ticket_class_mapping.get(combobox_ticket_class.get(), None)
        flight_code = combobox_flight_code.get()
        destination_city = combobox_destination_city.get()
        flight_duration = round(float(entry_flight_duration.get()), 2)
        days_left = int(entry_days_left.get())
        if not airline or not flight_code or not source_city or not departure_time or not num_stops or not arrival_time or not destination_city or not flight_class:
            messagebox.showerror("Input Error", "All fields must be filled!")
            return
        airline = min_max_normalization(airline, 6, 1)
        source_city = min_max_normalization(source_city, 6, 1)
        departure_time = min_max_normalization(departure_time, 6, 1)
        num_stops = min_max_normalization(num_stops, 3, 1)
        arrival_time = min_max_normalization(arrival_time, 6, 1)
        flight_class = min_max_normalization(flight_class, 2, 1)
        flight_duration = min_max_normalization(flight_duration, 49.83, 0.83)
        days_left = min_max_normalization(days_left, 49, 1)

        y = (9526.39 + -1948.22 * float(airline) + 472.71 * float(source_city) + -997.67 * float(departure_time)
             + 493.18 * float(num_stops) + -1922.56 * float(arrival_time) + 49451.36 * float(flight_class) + 7574.20 * float(flight_duration)
             + -6352.49 * days_left + -41229.79 * float(flight_class)*float(airline) + -26708.32 * float(flight_class)*float(num_stops))
        result = f"Flight price predicted: {y}"

        lbl_result.config(text=result)
    except ValueError:
        messagebox.showerror("Input Error", "Invalid datatype of input")

def reset_values():
    combobox_airline.set('')
    combobox_flight_code.set('')
    combobox_source_city.set('')
    combobox_departure_time.set('')
    combobox_num_stops.set('')
    combobox_arrival_time.set('')
    combobox_destination_city.set('')
    combobox_ticket_class.set('')

    entry_flight_duration.delete(0, 'end')
    entry_flight_duration.insert(0, "Enter value between 0.83 and 49.8")
    entry_flight_duration.config(fg='gray')

    entry_days_left.delete(0, 'end')
    entry_days_left.insert(0, "Enter value between 1 and 49")
    entry_days_left.config(fg='gray')

root = tk.Tk()
root.title("Flight Prediction Interface")
root.resizable(True, True)

root.config(bg="#f7f7f7")

lbl_title = tk.Label(root, text="Flight Prediction Interface", font=("Arial", 18, "bold"), fg="#2196F3", bg="#f7f7f7")
lbl_title.grid(row=0, column=0, columnspan=4, pady=20, padx=20, sticky="nsew")

lbl_airline = tk.Label(root, text="Airline Company:", font=("Arial", 12), bg="#f7f7f7")
lbl_airline.grid(row=1, column=0, sticky="w", padx=20, pady=10)
combobox_airline = ttk.Combobox(root, values=["Vistara", "Air_India", "Indigo", "GO_FIRST", "AirAsia", "SpiceJet"], font=("Arial", 12), state="readonly")
combobox_airline.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

lbl_flight_code = tk.Label(root, text="Flight Code:", font=("Arial", 12), bg="#f7f7f7")
lbl_flight_code.grid(row=2, column=0, sticky="w", padx=20, pady=10)
combobox_flight_code = ttk.Combobox(root, values=["UK-706", "UK-772", "UK-720", "UK-836", "UK-822"], font=("Arial", 12), state="readonly")
combobox_flight_code.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

lbl_source_city = tk.Label(root, text="Source City:", font=("Arial", 12), bg="#f7f7f7")
lbl_source_city.grid(row=3, column=0, sticky="w", padx=20, pady=10)
combobox_source_city = ttk.Combobox(root, values=["Delhi", "Mumbai", "Bangalore", "Kolkata", "Hyderabad", "Chennai"], font=("Arial", 12), state="readonly")
combobox_source_city.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

lbl_departure_time = tk.Label(root, text="Departure Time:", font=("Arial", 12), bg="#f7f7f7")
lbl_departure_time.grid(row=4, column=0, sticky="w", padx=20, pady=10)
combobox_departure_time = ttk.Combobox(root, values=["Morning", "Early_Morning", "Evening", "Night", "Afternoon", "Late_Night"], font=("Arial", 12), state="readonly")
combobox_departure_time.grid(row=4, column=1, padx=20, pady=10, sticky="ew")

lbl_num_stops = tk.Label(root, text="Number of Stops:", font=("Arial", 12), bg="#f7f7f7")
lbl_num_stops.grid(row=5, column=0, sticky="w", padx=20, pady=10)
combobox_num_stops = ttk.Combobox(root, values=["zero", "one", "two_or_more"], font=("Arial", 12), state="readonly")
combobox_num_stops.grid(row=5, column=1, padx=20, pady=10, sticky="ew")

lbl_arrival_time = tk.Label(root, text="Arrival Time:", font=("Arial", 12), bg="#f7f7f7")
lbl_arrival_time.grid(row=1, column=2, sticky="w", padx=20, pady=10)
combobox_arrival_time = ttk.Combobox(root, values=["Night", "Evening", "Morning", "Afternoon", "Early_Morning", "Late_Night"], font=("Arial", 12), state="readonly")
combobox_arrival_time.grid(row=1, column=3, padx=20, pady=10, sticky="ew")

lbl_destination_city = tk.Label(root, text="Destination City:", font=("Arial", 12), bg="#f7f7f7")
lbl_destination_city.grid(row=2, column=2, sticky="w", padx=20, pady=10)
combobox_destination_city = ttk.Combobox(root, values=["Mumbai", "Delhi", "Bangalore", "Kolkata", "Hyderabad", "Chennai"], font=("Arial", 12), state="readonly")
combobox_destination_city.grid(row=2, column=3, padx=20, pady=10, sticky="ew")

lbl_ticket_class = tk.Label(root, text="Ticket Class:", font=("Arial", 12), bg="#f7f7f7")
lbl_ticket_class.grid(row=3, column=2, sticky="w", padx=20, pady=10)
combobox_ticket_class = ttk.Combobox(root, values=["Economy", "Business"], font=("Arial", 12), state="readonly")
combobox_ticket_class.grid(row=3, column=3, padx=20, pady=10, sticky="ew")

lbl_flight_duration = tk.Label(root, text="Flight Duration (hours):", font=("Arial", 12), bg="#f7f7f7")
lbl_flight_duration.grid(row=4, column=2, sticky="w", padx=20, pady=10)
entry_flight_duration = tk.Entry(root, font=("Arial", 12))
entry_flight_duration.grid(row=4, column=3, padx=20, pady=10, sticky="ew")
entry_flight_duration.insert(0, "Suggested value from 0.83 to 49.8")
entry_flight_duration.configure(state='disabled')
duration_focus_in = entry_flight_duration.bind('<Button-1>', lambda x: on_focus_in(entry_flight_duration))
duration_focus_out = entry_flight_duration.bind(
    '<FocusOut>', lambda x: on_focus_out(entry_flight_duration, "Suggested from 0.83 to 49.8"))

lbl_days_left = tk.Label(root, text="Days Left:", font=("Arial", 12), bg="#f7f7f7")
lbl_days_left.grid(row=5, column=2, sticky="w", padx=20, pady=10)
entry_days_left = tk.Entry(root, font=("Arial", 12))
entry_days_left.grid(row=5, column=3, padx=20, pady=10, sticky="ew")
entry_days_left.insert(0, "Suggested value from 1 to 49")
entry_days_left.configure(state='disabled')
days_left_focus_in = entry_days_left.bind('<Button-1>', lambda x: on_focus_in(entry_days_left))
days_left_focus_out = entry_days_left.bind(
    '<FocusOut>', lambda x: on_focus_out(entry_days_left, "Suggested from 1 to 49"))

btn_predict = tk.Button(root, text="Predict", command=predict, font=("Arial", 12, "bold"), bg="#2196F3", fg="white", width=15, bd=2, relief="solid")
btn_predict.grid(row=6, column=0, columnspan=3, pady=20)

btn_reset = tk.Button(root, text="Reset", command=reset_values, font=("Arial", 12, "bold"), bg="gray", fg="white", width=15, bd=2, relief="solid")
btn_reset.grid(row=6, column=1, columnspan=3, pady=20)

lbl_result = tk.Label(root, text="", font=("Arial", 12), bg="#f7f7f7", anchor="w", justify="left")
lbl_result.grid(row=7, column=0, columnspan=4, pady=20, padx=20)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=3)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=2)

root.mainloop()

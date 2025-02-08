import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to calculate calories burned (extended with sets and reps)
def calories_burned(activity, duration, weight, lifted_weight=0, sets=0, reps=0):
    activity_map = {
        'running': 0.063 * weight,
        'cycling': 0.05 * weight,
        'swimming': 0.078 * weight,
        'squats': 0.1 * weight + 0.02 * lifted_weight,
        'push-ups': 0.07 * weight,
        'deadlifts': 0.08 * weight + 0.025 * lifted_weight,
        'bench_press': 0.085 * weight + 0.02 * lifted_weight,
        'pull-ups': 0.09 * weight
    }

    time_per_rep = 2  # Time per rep (in seconds)

    if activity in activity_map:
        if activity in ['squats', 'deadlifts', 'bench_press']:
            total_reps = sets * reps
            total_duration = total_reps * time_per_rep / 60  # Convert seconds to minutes
            return activity_map[activity] * total_duration  # Calories burned = rate * duration
        else:
            return activity_map[activity] * duration  # For other activities
    else:
        return 0.0  # Return 0 if invalid activity

# Function to display BMI results
def show_bmi():
    try:
        weight = float(bmi_weight_entry.get())
        height = float(bmi_height_entry.get())
        bmi = calculate_bmi(weight, height)
        bmi_result_label.config(text=f"Your BMI: {bmi:.2f}")
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        bmi_category_label.config(text=f"Category: {category}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

# Function to display calories burned result
def show_calories_burned():
    try:
        weight = float(calories_weight_entry.get())
        activity = calories_activity_var.get()
        duration = float(calories_duration_entry.get())
        lifted_weight = 0
        sets = reps = 0
        if activity in ['squats', 'deadlifts', 'bench_press']:
            lifted_weight = float(calories_lifted_weight_entry.get())
            sets = int(calories_sets_entry.get())
            reps = int(calories_reps_entry.get())
        calories = calories_burned(activity, duration, weight, lifted_weight, sets, reps)
        calories_result_label.config(text=f"Calories burned: {calories:.2f} kcal")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")

# Main window
root = tk.Tk()
root.title("Calorie and BMI Dashboard")
root.geometry("500x600")

# Create tabs for BMI and Calories Burned
tab_control = tk.Frame(root)
tab_control.pack(fill="both", expand=True)

# Tab for BMI
bmi_frame = tk.Frame(tab_control)
bmi_frame.pack(fill="both", expand=True)

bmi_weight_label = tk.Label(bmi_frame, text="Weight (kg):")
bmi_weight_label.pack()
bmi_weight_entry = tk.Entry(bmi_frame)
bmi_weight_entry.pack()

bmi_height_label = tk.Label(bmi_frame, text="Height (m):")
bmi_height_label.pack()
bmi_height_entry = tk.Entry(bmi_frame)
bmi_height_entry.pack()

bmi_button = tk.Button(bmi_frame, text="Calculate BMI", command=show_bmi)
bmi_button.pack()

bmi_result_label = tk.Label(bmi_frame, text="Your BMI: ")
bmi_result_label.pack()

bmi_category_label = tk.Label(bmi_frame, text="Category: ")
bmi_category_label.pack()

# Tab for Calories Burned
calories_frame = tk.Frame(tab_control)
calories_frame.pack(fill="both", expand=True)

calories_weight_label = tk.Label(calories_frame, text="Weight (kg):")
calories_weight_label.pack()
calories_weight_entry = tk.Entry(calories_frame)
calories_weight_entry.pack()

calories_activity_label = tk.Label(calories_frame, text="Select Activity:")
calories_activity_label.pack()

calories_activity_var = tk.StringVar()
activity_options = ["running", "cycling", "swimming", "squats", "push-ups", "deadlifts", "bench_press", "pull-ups"]
calories_activity_menu = tk.OptionMenu(calories_frame, calories_activity_var, *activity_options)
calories_activity_menu.pack()

calories_duration_label = tk.Label(calories_frame, text="Duration (minutes):")
calories_duration_label.pack()
calories_duration_entry = tk.Entry(calories_frame)
calories_duration_entry.pack()

# Fields for gym exercises
calories_lifted_weight_label = tk.Label(calories_frame, text="Lifted Weight (kg):")
calories_lifted_weight_label.pack()
calories_lifted_weight_entry = tk.Entry(calories_frame)
calories_lifted_weight_entry.pack()

calories_sets_label = tk.Label(calories_frame, text="Sets:")
calories_sets_label.pack()
calories_sets_entry = tk.Entry(calories_frame)
calories_sets_entry.pack()

calories_reps_label = tk.Label(calories_frame, text="Reps per set:")
calories_reps_label.pack()
calories_reps_entry = tk.Entry(calories_frame)
calories_reps_entry.pack()

calories_button = tk.Button(calories_frame, text="Calculate Calories Burned", command=show_calories_burned)
calories_button.pack()

calories_result_label = tk.Label(calories_frame, text="Calories burned: ")
calories_result_label.pack()

# Start the application
root.mainloop()

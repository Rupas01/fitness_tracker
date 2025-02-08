# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


# Function to calculate BMR (Basal Metabolic Rate)
def calculate_bmr(weight, height, age, gender):
    if gender.lower() == 'male':
        # Mifflin-St Jeor equation for men
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == 'female':
        # Mifflin-St Jeor equation for women
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        return "Invalid gender"
    return bmr


# Function to classify BMI category
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


# Function to estimate calories burned based on activity
def calories_burned(activity, duration, weight, lifted_weight=0, sets=0, reps=0):
    # Time per rep is estimated as 2 seconds
    time_per_rep = 2

    # Calories burned per minute for different activities (values are average estimates)
    activity_map = {
        'running': 0.063 * weight,  # 0.063 * weight (kg) per minute
        'cycling': 0.05 * weight,  # 0.05 * weight (kg) per minute
        'swimming': 0.078 * weight,  # 0.078 * weight (kg) per minute
        'squats': 0.1 * weight + 0.02 * lifted_weight,  # Adding weight lifted in squats
        'push-ups': 0.07 * weight,  # 0.07 * weight (kg) per minute
        'deadlifts': 0.08 * weight + 0.025 * lifted_weight,  # Adding weight lifted in deadlifts
        'bench_press': 0.085 * weight + 0.02 * lifted_weight,  # Adding weight lifted in bench press
        'pull-ups': 0.09 * weight  # 0.09 * weight (kg) per minute
    }

    if activity in activity_map:
        # If it's a gym activity, estimate the total duration based on sets and reps
        if activity in ['squats', 'deadlifts', 'bench_press']:
            total_reps = sets * reps
            total_duration = total_reps * time_per_rep / 60  # Total time in minutes
            return activity_map[activity] * total_duration  # Calories burned = rate * duration
        else:
            return activity_map[activity] * duration  # Calories burned for non-gym activities
    else:
        return 0.0  # Return 0.0 if the activity is invalid


# Function to calculate TDEE (Total Daily Energy Expenditure) based on activity level
def calculate_tdee(bmr, activity_level):
    activity_multipliers = {
        'sedentary': 1.2,  # little to no exercise
        'light': 1.375,  # light exercise/sports 1-3 days/week
        'moderate': 1.55,  # moderate exercise/sports 3-5 days/week
        'active': 1.725,  # hard exercise/sports 6-7 days a week
        'very_active': 1.9  # very hard exercise/physical job or training twice a day
    }

    if activity_level in activity_multipliers:
        tdee = bmr * activity_multipliers[activity_level]
        return tdee
    else:
        return "Invalid activity level"


# Function to calculate calories for weight loss and gain
def calculate_calories_for_weight(goal, tdee):
    if goal == "maintain":
        return tdee
    elif goal == "lose":
        return tdee - 500  # Target a 500 calorie deficit for weight loss
    elif goal == "gain":
        return tdee + 500  # Target a 500 calorie surplus for weight gain
    else:
        return "Invalid goal"


# Main function to get user inputs and calculate
def main():
    # User inputs for weight, height, age, and gender
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    age = int(input("Enter your age in years: "))
    gender = input("Enter your gender (male/female): ").lower()

    # BMI Calculation
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"BMI Category: {classify_bmi(bmi)}")

    # BMR Calculation (height needs to be in cm for BMR calculation)
    bmr = calculate_bmr(weight, height * 100, age, gender)  # height in cm for BMR calculation
    print(f"Your BMR is: {bmr:.2f} calories/day")

    # Get activity level from user
    activity_level = input("Enter your activity level (sedentary, light, moderate, active, very_active): ").lower()

    # Calculate TDEE based on BMR and activity level
    tdee = calculate_tdee(bmr, activity_level)
    if isinstance(tdee, str):
        print(tdee)
        return
    print(f"Your TDEE (Total Daily Energy Expenditure) is: {tdee:.2f} calories/day")

    # Get the user's goal (maintain, lose, or gain weight)
    goal = input("Enter your goal (maintain, lose, gain): ").lower()

    # Calculate the required caloric intake for the goal
    required_calories = calculate_calories_for_weight(goal, tdee)
    if isinstance(required_calories, str):
        print(required_calories)
        return
    print(f"To {goal} weight, you should consume approximately: {required_calories:.2f} calories/day")

    # Ask for activity and duration for calories burned estimation
    activity = input(
        "Enter the activity (running, cycling, swimming, squats, push-ups, deadlifts, bench_press, pull-ups): ").lower()
    duration = float(input("Enter the duration of the activity in minutes: "))

    # If the activity is a gym exercise, ask for the weight lifted and sets/reps
    if activity in ['squats', 'deadlifts', 'bench_press']:
        lifted_weight = float(input(f"Enter the weight lifted in kg for {activity}: "))
        sets = int(input(f"Enter the number of sets for {activity}: "))
        reps = int(input(f"Enter the number of reps per set for {activity}: "))
    else:
        lifted_weight = 0  # Set to 0 if it's not a gym exercise
        sets = reps = 0

    # Calories burned estimation
    calories = calories_burned(activity, duration, weight, lifted_weight, sets, reps)
    print(f"Calories burned from {activity} for {duration} minutes: {calories:.2f} kcal")


if __name__ == "__main__":
    main()

print("Welcome, thank you for using EasyFit!")
print("EasyFit is your all in one nutritional companion. You can get an estimate of your daily calories burnt(TDEE), track calories ate, and even look for healthy meal alternatives!")
print("How does a TDEE calculator work? Well, your daily calorie expenditure is dependant on many things, including weight, gender, age, height, and your general active level")
print("To begin, please input the prompted information.")
gender = input("Are you a male or female?[M or F]").upper()
while gender != "M" and gender != "F":
    print("Please enter a valid gender option")
    gender = input("Please enter M or F.")
print(gender)
age = float(input("How old are you?:"))
print(age)
weight = float(input("Please input your weight:" )) #adding in float to account for our calc later
kg_weight = weight * .45
print(str(kg_weight) + " kg")
height_feet = float(input("Please inpuut your height in feet. (Ex: 5'10 = 5)"))
height_inches = float(input("Please input your height in inches. (Ex: 5'10 = 10)"))
height_real = (height_feet * 30.48) + (height_inches * 2.54)
print(f"{height_real} meters")
print("The next step is to please indicate your activity level based off of your lifestyle.",
      "1. Sedentary: Little to no exercise + work a desk job",
      "2. Lightly Active: Light exercise 1-3 times a week.",
      "3. Moderately Active: Exercise 3-5 times a week.",
      "4. Very Active: Exercise 5-7 times a week.")
activity_level = { ##Dictionary that corresponds to a multiplier for each option
    1: 1.2,
    2: 1.375,
    3: 1.55,
    4: 1.725
}
activity_level_choice = int(input("Please select a number that most aligns with your lifestyle.(1-4)")) #Choose level
while activity_level_choice not in activity_level:
    print("Please enter a valid option.")
    activity_level_choice = int(input(("Please select a number that most aligns with your lifestyle.(1-4)")))
activity_multiplier = float(activity_level[activity_level_choice]) #Gives activity multiplier
print(f"Selected activity level corresponds to multiplier: {activity_multiplier}") #Prints the multiplier, might not be included in final product
if gender == "M":
    tdee = 88.362 + (13.397 * kg_weight) + (4.799 * height_real) - (5.677 * age)
    tdee_real = tdee * activity_multiplier
elif gender == "F":
    tdee = 447.593 + (9.247 * kg_weight) + (3.098 * height_real) - (4.330 * age)
    tdee_real = tdee * activity_multiplier
print(int(tdee_real))

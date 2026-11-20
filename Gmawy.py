import streamlit as st

st.title("GYMAWWY APP - Your Fitness Helper")
st.write("Enter your details to can help you")
#variables

weight = float(st.number_input("your weight in kg: ",min_value = 1.0 , step = 0.5))
height = float(st.number_input("your height in m: ",min_value = 1.0 , step = 0.1))
age = int(st.number_input("your age : ",min_value = 1 ,max_value = 120 , step = 1))
gender = st.selectbox("your gender: ", ["male", "female"])
goal = st.selectbox("your goal: ", ["bulking", "cutting"])
activity_level = st.selectbox("your activity level: ", ["low", "regular", "medium", "high"])


def calculate_BMI(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def calculate_BMR(weight, height, age, gender):
    if gender == "male":
        bmr = (10 * weight) + (6.25 * (height * 100)) - (5 * age) + 5
    elif gender == "female":
        bmr = (10 * weight) + (6.25 * (height * 100)) - (5 * age) - 161
    else:
        raise ValueError("Invalid gender. Please enter 'male' or 'female'.")
    return bmr

def daily_protein(weight):
    protein = weight * 1.8
    return protein

def calculate_TDEE(BMR,activity_level,goal):
    if activity_level =="low":
        tdee = BMR *1.2
    elif activity_level =="regular":
        tdee = BMR *1.375
    elif activity_level =="medium":
        tdee = BMR *1.55
    elif activity_level =="high":
        tdee = BMR *1.725
    else:
        raise ValueError("Invalid activity level. Please enter 'low', 'regular', 'medium', or 'high'.")

    if goal == "bulking":
        tdee += 400
    elif goal == "cutting":
        tdee -= 400
    else:
        raise ValueError("Invalid goal. Please enter 'bulking' or 'cutting'.")
    
    return tdee

if st.button("Calculate"):
    BMI = calculate_BMI(weight, height)
    st.write(f"Your BMI is: {BMI:.2f}") 

    BMR = calculate_BMR(weight, height, age, gender)
    st.write(f"Your BMR is: {BMR:.2f} calories/day")      
    
    protein = daily_protein(weight)
    st.write(f"Your daily protein intake should be: {protein:.2f} grams/day")

    TDEE = calculate_TDEE(BMR,activity_level,goal)
    st.write(f"Your TDEE is: {TDEE:.2f} calories/day")
        



import streamlit as st

st.title("BMI Calculator")

weight = st.slider("Select your weight in kg: ", 20, 100, 40, 1)
height = st.slider("Select your height in inches: ", 12, 84, 48, 1)

BMI = weight / (height/39.37)**2

if st.button("Calculate BMI"):
    st.success(f"Your BMI is: {BMI:.2f}.")

    if BMI < 18.5:
        st.error("You are underweight.")
    elif 18.5 <= BMI <= 24.9:
        st.success("You are normal weight.")
    elif 25 <= BMI <= 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")


st.write("### BMI Categories: ###")
st.write("Underweight: BMI less than 18.5")
st.write("Normal weight: BMI between 18.5 and 24.9")
st.write("Overweight: BMI between 25 and 29.9")
st.write("Obese: BMI 30 or greater")

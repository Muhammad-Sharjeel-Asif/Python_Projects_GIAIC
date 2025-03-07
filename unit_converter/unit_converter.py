import streamlit as st

st.title("Unit Converter")

st.write("### Convert your units with ease!")

category = st.selectbox("### Select a category to convert", ["Length", "Mass", "Time", "Speed"])

def unit_converter(category, value):
    if category == "Length":
        if from_unit == "Meter" and to_unit == "Kilometer":
            return value / 1000
        elif from_unit == "Kilometer" and to_unit == "Meter":
            return value * 1000
    
    elif category == "Mass":
        if from_unit == "Gram" and to_unit == "Kilogram":
            return value / 1000
        elif from_unit == "Kilogram" and to_unit == "Gram":
            return value * 1000
    
    elif category == "Time":
        if from_unit == "Second" and to_unit == "Minute":
            return value / 60
        elif from_unit  == "Minute" and to_unit == "Second":
            return value * 60
        elif from_unit  == "Minute" and to_unit == "Hour":
            return value / 60
        elif from_unit  == "Hour" and to_unit == "Minute":
            return value * 60
        elif from_unit  == "Second" and to_unit == "Hour":
            return value / 3600
        elif from_unit  == "Hour" and to_unit == "Second":
            return value * 3600
    
    elif category == "Speed":
        if from_unit == "Meter/Second" and to_unit == "Kilometer/Hour":
            return value * 3.6
        if from_unit == "Kilometer/Hour" and to_unit == "Meter/Second":
            return value / 3.6
        

if category == "Length":
    from_unit = st.selectbox("Select a unit to convert", ["Kilometer", "Meter"])
    to_unit = st.selectbox("Select a unit to convert", ["Meter", "Kilometer"])

elif category == "Mass":
    from_unit = st.selectbox("Select a unit to convert", ["Gram", "Kilogram"])
    to_unit = st.selectbox("Select a unit to convert", ["Kilogram", "Gram"])

elif category == "Time":
    from_unit = st.selectbox("Select a unit to convert", ["Second", "Minute", "Hour"])
    to_unit = st.selectbox("Select a unit to convert", ["Hour", "Minute", "Second"])

elif category == "Speed":
    from_unit = st.selectbox("Select the unit to convert", ["Meter/Second", "Kilometer/Hour"])
    to_unit = st.selectbox("Select the unit to convert", ["Kilometer/Hour", "Meter/Second"])

value = st.number_input("Enter the value to convert")

result = unit_converter(category, value)

if st.button("Convert"):
    if result < 0:
        st.error("Your result is too small!")
    else:
        st.success(f"The value is  {result:.3f}  {to_unit}")    
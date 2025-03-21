import streamlit as st
import re
import random
import string

if "show_generate" not in st.session_state:
    st.session_state.show_generate = False

st.title("Password Strength Meter")
st.subheader("Enter your password to check its strength")

def generate_password():
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

    return ''.join(random.choice(characters) for _ in range(12))

def password_strength(password):
    score = 0

    if(len(password) >= 8):
        score += 1
    else:
        st.warning("Password should be at least 8 characters long")
    
    if(re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)):
        score += 1
    else:
        st.warning("Password should have at least one uppercase and one lowercase letter")
    
    if(re.search(r"\d", password)):
        score += 1
    else:
        st.warning("Password should have at least one digit")
    
    if(re.search(r"[!@#$%^&*]", password)):
        score += 1 
    else:
        st.warning("Password should have at least one special character")


    if(score == 4):
        st.success("Your password is strong!")
    elif(score == 3):
        st.warning("Your password is medium. Try to make it strong.")
    else:
        st.error("Your password is weak. Try to make it strong.")

    return score

password = st.text_input("Enter your password here", type="password")

if st.button("Check Password Strength"):
    if (password):
        password_score = password_strength(password)

        if password_score < 3:
            st.session_state.show_generate = True

if st.session_state.show_generate:
    st.subheader("🔄 Generate a Strong Password")
    if st.button("Generate"):
        strong_password = generate_password()
        st.success(f"✅ Suggested Strong Password: {strong_password}")
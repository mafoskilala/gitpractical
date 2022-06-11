# import module
import streamlit as st

#Display Img:

from PIL import Image
img= Image.open("food Img.jpg")

st.image(img, width= 400)

st.title("Welcome dearly esteemed audience!")

st.header("Blood Group and Diet")

st.subheader("Compatibility and Well-being")

st.text("We are here to create awareness about your diet....")

st.success("Your Blood Group Type is which?")

if st.checkbox("Group A"):
    st.text("Group A selected")
    
if st.checkbox("Group B"):
    st.text("Group B selected")
    
if st.checkbox("Group AB"):
    st.text("Group AB selected")
    
if st.checkbox("Group O"):
    st.text("Group O selected")
    
st.success("Any discomfort when you eat certain foods?")

if st.checkbox("YES"):
    st.text("YES selected")
    
if st.checkbox("NO"):
    st.text("NO selected")
    
st.success("Which of these have you been diagnosed of or experienced recently?")

status = st.radio("Select Ailment:", ("Low Immune System", "Heart Disease", "Cancer", "Diabetes", "Chronic Fatigue", "Others"))

Ailment = st.text_input("Enter other ailments", "Type here")

if (st.button("submit")):
    result = Ailment.title()
st.text("Good to know you identified that ailment")

st.success("You are therefore advised to avoid the following foods;")

st.text_input("For Blood Group A:", "Diary, Banana, Coconut, Papaya, Fish, Refined Sugar, Refined Cabohydrate, Artificial Ingredient, Wheat, Yam, Large Meat, Potatoes")

st.text_input("For Blood Group B:", "Corn, Wheat, Buck Wheat, Lentils, Tomatoes, Peanuts, Sesame Seeds")

st.text_input("For Blood Group AB:", "Caffeine, Alcohol, Smoked Meat, Cured Meat")

st.text_input("For Blood Group O:", "Gluten, Lentils, Kidney Beans, Corn, Diary, Grain, Plenty Nuts")
    
level = st.slider("How satisfied are you with the compatibility of your Blood Group and your Diet on a scale of 5?", 1, 5)

st.subheader("Remember.... Knowledge supports well-being!")



import streamlit as st

st.header(':blue[Find the largest among the 3 given numbers(value greater than the other two])')
a = st.number_input('Insert first number')
st.write('The first number is ', a)
b = st.number_input('Insert first number')
st.write('The first number is ', b)
c = st.number_input('Insert first number')
st.write('The first number is ', c)
largest = 0

if st.button('Find the Largest one'):
    if a > b and a > c:
        largest = a
    if b > a and b > c:
        largest = b
    if c > a and c > b:
        largest = c
    st.write(largest, "is the largest of three numbers.")
else:
    st.write('Goodbye')

import streamlit as st
st. header("Calculator App")
st.subheader("Carry out your simple calculations with my web app")

def add(a,b):
    c = a + b
    return c

def subtr(a, b):
    c = a - b
    return c

def mul(a, b):
    c = a * b
    return c

def div(a,b):
    c = a/b
    return c

def rp(a,b):
    c = a**b
    return c

def sqr(a):
    c = a**0.5
    return c 

a = st.number_input("Input your fist number", step = 1)
b = st.number_input("Input your next number", step = 1)

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("Add"):
        st.write(add(a,b))
    
    if st.button ("subtract"):
        st.write(subtr(a,b))
with c2:
    if st.button ("Multiply"):
        st.write(mul(a,b))

    if st.button ("Divide"):
        st.write(div(a,b))
with c3:
    if st.button ("Power"):
        st.write(rp(a,b))

    if st.button ("sqr Root"):
        st.write(sqr(a))

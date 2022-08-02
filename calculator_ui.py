# streamlit run calculator_ui.py
import streamlit as st


c1, c2 = st.columns(2)
fnum = c1.number_input("First Value",
                    min_value=0,
                    value=50)

snum = c2.number_input("Second Value",
                    min_value=0,
                    value=50)

options = ['Add','Sub','Mul','Div']
choice = c1.radio("Select an operation",
                options, horizontal=True)
btn = c2.button("Calculate")
if btn:
    if choice == options[0]:
        result = fnum + snum
    elif choice == options[1]:
        result = fnum - snum
    elif choice == options[2]:
        result = fnum * snum
    else:
        result = fnum / snum
    st.success(f'{result:.2f}')
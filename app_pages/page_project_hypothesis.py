import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"1 - We believe that cherry leaves which have powdery mildew have "
        f"clear signs/ marks which will allow Farky & Foods to differentiate "
        f"between healthy and unhealthy cherry trees \n\n "
        f"* How to validate - An average image study can help to investigate it \n"
        f"* Result - Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another.\n\n"
        f"2 - We believe we can predict if a leaf is healthy or not based on images"
        f" of the leaf to a 97% degree of accuracy \n"
        f"* How to validate - Train and valididate a model using Convolutional neural Network (CNN) to achieve "
        f"a model that achieves the required level of accuracy. "
        f"that achieves the required level of accuracy.\n"
        f"* Result - The model achieved an accuracy of 98.22%"
    )
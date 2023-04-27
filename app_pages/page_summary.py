import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal disease that affects many plant species.\n "
        f"* An employee takes a few samples of tree leaves and verifying visually if the "
        f"leaf tree is healthy or has powdery mildew. If there is powdery mildew, the "
        f"employee applies a specific compound to kill the fungus. The time spent applying "
        f"this compound is 1 minute.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset contains +4 thousand images taken from the  "
        f"client's crop fields. The images show healthy cherry leaves and cherry leaves "
        f"that have powdery mildew.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/jamiebradford123/project5/blob/main/README.md.")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The company is concerned about supplying the market with a "
        f"compromised quality product.\n"
        f"* 2 - The company needs a faster more scalable option to check its "
        f"* thousands of trees. A ML system to detect an infected leaf would "
        f"* speed up the process "
        )
    
    st.write(
    f"**Results**\n\n"
    f"* The model can predict if a leaf is healthy to a degree of accuracy of 98%\n"
    f"* Therefore it can be assumed that the ML model can quickly detect"
    f" if the leaf is healthy, providing a scalable option for the business"
    f"and the high accuracy prevents them from supplying the market with"
    f"compromised quality product.\n"
    )

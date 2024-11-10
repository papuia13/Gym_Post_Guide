import streamlit as st
import os

def main():
    st.title("Gym Action Tracker")

    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        st.subheader("Login Section")

        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        if st.button("Login"):
            if username == "admin" and password == "admin":
                st.success("Logged In as {}".format(username))
                # Open pose_detection.py
                script_path = "/t:/MCA/3rd_Sem/ECP/Gym_Action_Tracker/pose_detection.py"
                os.environ["STREAMLIT_RUN_SCRIPT"] = script_path
                st.experimental_rerun()
            else:
                st.warning("Incorrect Username/Password")

    elif choice == "Register":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')
        if st.button("Register"):
            st.success("You have successfully created an account")
            st.info("Go to Login Menu to login")

if __name__ == '__main__':
    main()
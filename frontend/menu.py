import streamlit as st

def main():
    st.title("Gym Action Tracker")

    st.sidebar.header("Navigation")
    if st.sidebar.button("Pose Detection"):
        st.experimental_set_query_params(page="pose_detection")
        st.experimental_rerun()

    if st.sidebar.button("Mass Index Calculator"):
        st.experimental_set_query_params(page="mass_index_calculator")
        st.experimental_rerun()

    if st.sidebar.button("Nutrition Guide"):
        st.experimental_set_query_params(page="nutrition_guide")
        st.experimental_rerun()

    query_params = st.experimental_get_query_params()
    page = query_params.get("page", [None])[0]

    if page == "pose_detection":
        st.write("Navigating to Pose Detection module")
        import pose_detection
        pose_detection.main()

    elif page == "mass_index_calculator":
        import pages.mass_index_calculator as mass_index_calculator
        mass_index_calculator.main()

    elif page == "nutrition_guide":
        st.write("Navigating to Nutrition Guide module")
        import pages.nutrition_guide as nutrition_guide
        nutrition_guide.main()

if __name__ == "__main__":
    main()


import streamlit as st


def predict_result(study_hours):
    """Predict a student's result from daily study hours."""
    if study_hours >= 3:
        return "Pass"
    return "Needs Improvement"


st.set_page_config(
    page_title="Student Result Predictor",
    page_icon="🎓"
)

st.title("Student Result Prediction")
st.write("Enter the number of hours studied per day.")

hours = st.number_input(
    "Study hours per day",
    min_value=0.0,
    max_value=24.0,
    value=3.0,
    step=0.5
)

if st.button("Predict Result"):
    result = predict_result(hours)

    if result == "Pass":
        st.success(f"Predicted result: {result}")
    else:
        st.warning(f"Predicted result: {result}")

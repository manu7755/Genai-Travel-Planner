# manan.py

import streamlit as st
from agent_setup  import agent_executor # ✅ now it will work

st.title("🌍 Manan Travel Planner")

origin = st.text_input("Origin City")
destination = st.text_input("Destination City")
budget = st.text_input("Budget (INR or USD)")
transport = st.selectbox("Preferred Transport", ["Flight", "Train", "Bus", "Car"])

if st.button("Plan My Trip"):
    if not (origin and destination and budget):
        st.error("Please fill all inputs!")
    else:
        query = f"""
        Plan a personalized {transport} trip from {origin} to {destination}
        within a budget of {budget}.
        Include 3 travel options, hotel suggestions, and a 3-day itinerary.
        """
        response = agent_executor.invoke({"input": query})
        st.markdown("### ✅ Your Personalized Plan:")
        st.write(response["output"])

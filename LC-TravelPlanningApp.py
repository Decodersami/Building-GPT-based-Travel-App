#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Jan 25 19:01:20 2024

@author: Samim
"""

import streamlit as st
import langchain

from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.prompts import PromptTemplate

def generate_itinerary(country, number_of_nights, trip_type):
    prompt_template = "Generate a daywise detailed itinerary with specific place names for a {triptype} trip to {country} for {nights} nights. "
    tripprompt = prompt_template.format(triptype = trip_type, country = country, nights=number_of_nights)
    st.text(tripprompt)
    llm = OpenAI(openai_api_key="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", temperature=0.9, max_tokens=3500)
    result = llm(tripprompt)
    
    return result

def main():
  st.title("Travel Planner App(By Samim)")

  country = st.selectbox("Select a Destination:", ["Darjeeling", "Agra", "Jaipur", "Goa", "Kerala Backwaters", "Varanasi", "Rajasthan", "Delhi", "Mumbai", "Kashmir", "Hampi"])
  number_of_nights = st.number_input("Number of nights:", min_value=1, step=1)
  trip_type = st.selectbox("Type of trip:", ["Historical", "Adventure", "Shopping", "Beach", "Trekking"])

  if st.button("Generate Itinerary"):
    itinerary = generate_itinerary(country, number_of_nights, trip_type)
    st.markdown(itinerary)

if __name__ == "__main__":
  main()
  
"""
ChatCSV: A Streamlit application for statistical analysis of CSV data using the ChatOpenAI model.

This module provides a Streamlit user interface where users can upload a CSV file and
ask any statistical question related to the content of the CSV file. It utilizes the
ChatOpenAI model from the langchain library to interpret and answer user questions.

Attributes:
    OPENAI_API_KEY (str): The API key for accessing OpenAI's models.

Functions:
    main(): The primary function that drives the Streamlit application. It configures
            the Streamlit page, accepts CSV file uploads, takes user input for questions,
            and provides the answers using the ChatOpenAI model.

Usage:
    To run this Streamlit application, execute the script. Ensure that you have all the
    required dependencies installed and that you've set your OpenAI API key.

Dependencies:
    os, tempfile, streamlit, langchain

Execution:
    > streamlit run app.py
"""

import os
from tempfile import NamedTemporaryFile

import streamlit as st
from langchain.agents import create_csv_agent
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "" #OPENAI_API_KEY


def main():
    """
    Main function for the Streamlit application.

    Initializes the Streamlit interface for ChatCSV. This function:
    - Configures the Streamlit page with a custom title.
    - Provides an interface for users to upload a CSV file.
    - Accepts user input as a question related to the uploaded CSV.
    - Uses the ChatOpenAI model from the langchain library to process and answer the question.
    - Displays the model's response in the Streamlit interface.

    Uses the temporary file utility to ensure that the uploaded CSV data is accessible
    for the ChatOpenAI model without permanently saving the data on the server.

    The OpenAI model used is "gpt-3.5-turbo-0613" and is set to have a temperature of 0.7

    Note:
        Ensure that the `OPENAI_API_KEY` environment variable is correctly set before running
        the function to allow access to OpenAI's models.

    Returns:
        None. All operations are handled within the function and results are displayed
        in the Streamlit
    """

    st.set_page_config(page_title="ChatCSV")
    st.title("ChatCSV  💬")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    if csv_file:
        with NamedTemporaryFile(mode="w+b", suffix=".csv") as f:
            f.write(csv_file.getvalue())
            f.seek(0)
            user_input = st.text_input(
                "Ask any statistical question related to your CSV"
            )
            csv_agent = create_csv_agent(
                ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo-0613"),
                f.name,
                verbose=True,
                agent_type=AgentType.OPENAI_FUNCTIONS,
            )
            if user_input:
                response = csv_agent.run(user_input)
                with st.chat_message("assistant"):
                    st.write(response)


if __name__ == "__main__":
    main()

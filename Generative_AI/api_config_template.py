"""
API Configuration Template

This file demonstrates how to set up the API key securely for the Generative AI component.

IMPORTANT:
- Do NOT include your real API key in this file.
- Replace "your_api_key_here" with your own key when running locally.
- This file is for demonstration purposes only.
"""

import os

def set_api_key():
    """
    Set your API key here before running the project locally.
    """
    os.environ["GROQ_API_KEY"] = "your_api_key_here"


def get_api_key():
    """
    Retrieve the API key from environment variables.
    """
    return os.environ.get("GROQ_API_KEY")

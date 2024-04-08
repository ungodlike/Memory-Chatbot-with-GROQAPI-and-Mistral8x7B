NOTE : This is a personal mini project

Straightforward chatbot webapplication that has a memory.
Uses GROQ-API and Mistral8x7B (can switch llm).
Memory using ConversationBufferWindowMemory.
Gradio for webapp (use streamlit for better customization)

STEPS TO RUN
0) Make sure you have a groq api key and paste the key in the .env file
1) Create a virtual environment using python -m venv venvname
2) Install requirements using pip install -r requirements.txt
3) Run the app using gradio groqchatbot.py

import gradio as gr
import os
from langchain.chains.conversation.base import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from dotenv import load_dotenv


#loading environment variables from .env file
load_dotenv()

#initialize conversation chain with GROQ lm
groq_api_key = os.environ['GROQ_API_KEY']

def initialize_conversation():
    #initialize conversation memory
    memory = ConversationBufferWindowMemory()
    #initialize GROQchat with apikey, model and other custom settings
    groq_chat = ChatGroq(groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768",
                         temperature=0.2)
    #create and return conversation chain with GROQchat and memory
    return ConversationChain(llm=groq_chat, memory=memory)

#initialize conversation chain
conversation = initialize_conversation()

#handle chatbot responses
def chatbot(user_question):
    #get response from conversation chain based on user question
    response = conversation(user_question)
    #return the response part of the conversation output
    return response['response']

#creating a Gradio interface with chatbot function as the backend (streamlit can be used for more cusotmization)
UI = gr.Interface(fn=chatbot, inputs="textbox", outputs="textbox", title="A ChatBot with memory!", description="Ask a question and get a response. You may ask successive questions")
UI.launch()

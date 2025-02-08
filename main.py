import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)

#Initialize session state for candidate info and conversation history
if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = None
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

st.title("Hiring Assistant Chatbot")


#Candidate Information Form

def candidate_form():
    st.subheader("Candidate Information")

    # Wrap the input fields inside a form
    with st.form("candidate_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        years_experience = st.number_input("Years of Experience", min_value=0, step=1)
        desired_position = st.text_input("Desired Position")
        current_location = st.text_input("Current Location")
        tech_stack = st.text_input("Tech Stack (e.g., Python, NLP, computer vision, etc)")

        # Submit button inside the form
        submitted = st.form_submit_button("Submit Information")

        if submitted:
            if not all([full_name, email, phone, desired_position, current_location, tech_stack]):
                st.error("Please fill in all fields before submitting.")
            else:
                st.session_state.candidate_info = {
                    "full_name": full_name,
                    "email": email,
                    "phone": phone,
                    "years_experience": years_experience,
                    "desired_position": desired_position,
                    "current_location": current_location,
                    "tech_stack": tech_stack
                }
                st.success("Thank you! Your information has been submitted.")
                st.rerun()

# Display the candidate information 
if st.session_state.candidate_info is None:
    candidate_form()
else:
    # Interview Chat Interface
    candidate = st.session_state.candidate_info
    st.subheader(f"Welcome {candidate['full_name']}! Let's start your interview for the position of {candidate['desired_position']}.")

    # Display the conversation history
    for message in st.session_state.conversation_history:
        role = "assistant" if message["role"] == "assistant" else "user"
        with st.chat_message(role):
            st.markdown(message["content"])

    # Input field for candidate messages
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""
    if "user_input_submit" not in st.session_state:
        st.session_state.user_input_submit = False
    
    def generate_reply(user_message):
        # Append the new user message to the conversation history
        st.session_state.conversation_history.append({"role": "user", "content": user_message})
        
        #system prompt for the assistant
        system_prompt = (
            f"You are a hiring assistant chatbot interviewing a candidate for the position of {candidate['desired_position']}.\n"
            f"The candidate has {candidate['years_experience']} years of experience and a tech stack including {candidate['tech_stack']}.\n"
            "Maintain the context of the conversation to handle follow-up questions and ensure a coherent flow. "
            "Ask relevant technical interview questions based on the candidate's tech stack and experience. "
            "If you do not understand a candidate's input or receive unexpected input, provide a meaningful response without deviating from the interview process. "
            "When the candidate indicates that they want to end the interview, conclude gracefully by thanking them and explaining the next steps."
        )
        
        #Prepare the message list with the system prompt and conversation history
        messages = [{"role": "system", "content": system_prompt}] + st.session_state.conversation_history
        
        try:
            # Call the Groq API
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.7,
                max_tokens=200
            )
            bot_reply = response.choices[0].message.content
            # Append the bot's reply to the conversation history
            st.session_state.conversation_history.append({"role": "assistant", "content": bot_reply})
        except Exception as e:
            bot_reply = f"Sorry, I encountered an error: {e}"
            st.session_state.conversation_history.append({"role": "assistant", "content": bot_reply})
        return bot_reply
    def handle_user_input():
        if st.session_state.user_input.strip():
            reply = generate_reply(st.session_state.user_input)
            st.session_state.user_input = ""  # Clear the input field
            st.session_state.user_input_submit = False 

    st.text_input("Your message:", key="user_input", on_change=handle_user_input)

            
    

    # Option to End the Interview

    if st.button("End Interview"):
        st.session_state.conversation_history.append({"role": "user", "content": "I would like to end the interview."})
        conclusion_prompt = (
            "You are a hiring assistant chatbot. Conclude the interview by thanking the candidate, "
            "summarizing the conversation briefly if needed, and explaining the next steps in the process."
        )
        messages = [{"role": "system", "content": conclusion_prompt}] + st.session_state.conversation_history
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.7,
                max_tokens=150
            )
            final_reply = response.choices[0].message.content
            st.session_state.conversation_history.append({"role": "assistant", "content": final_reply})
            st.rerun()
        except Exception as e:
            st.error(f"Error during conclusion: {e}")
            st.rerun()

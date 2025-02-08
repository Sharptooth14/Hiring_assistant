# Hiring Assistant Chatbot

## Project Overview
The Hiring Assistant Chatbot is an AI-driven interview assistant designed to conduct technical interviews based on a candidate's experience and tech stack. Built using **Python, Streamlit, and Groq's LLM (LLaMA-3.3-70b-versatile)**, the chatbot dynamically generates interview questions, maintains context throughout the conversation, analyzes sentiment in candidate responses, and gracefully concludes the interview when requested. It ensures a structured and meaningful interaction, guiding candidates through a comprehensive interview experience.

## Installation Instructions
To set up and run the application locally, follow these steps:

### Prerequisites
- Python 3.8+
- Streamlit
- Groq API Key
- dotenv

### Steps
1. **Clone the Repository:**
   ```sh
   git clone <repository-url>
   cd Hiring-assistant
   ```
2. **Create a Virtual Environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set Up API Key:**
   - Create a `.env` file in the project directory.
   - Add your **Groq API Key**:
     ```sh
     GROQ_API_KEY=your_api_key_here
     ```
5. **Run the Application:**
   ```sh
   streamlit run main.py
   ```
6. **Access the Chatbot:**
   - Open your browser and go to `http://localhost:8501` to interact with the chatbot.

## Usage Guide
1. **Start the Application:** Run the above command and access the UI.
2. **Enter Candidate Information:** Fill in the form with relevant details such as name, email, experience, and tech stack.
3. **Engage in the Interview:** The chatbot will generate questions based on the tech stack provided.
4. **Respond to Questions:** Type answers in the chat input field and continue the conversation.
5. **Sentiment Analysis:** The chatbot will analyze candidate responses and assess sentiment levels.
6. **End the Interview:** Click the "End Interview" button to receive a summary and next steps.

## Technical Details
- **Frameworks & Libraries:**
  - `Streamlit` - UI development
  - `Groq API` - LLM integration (LLaMA-3.3-70b-versatile)
  - `dotenv` - Environment variable management
- **Architectural Decisions:**
  - **Session State Management:** Used to store candidate details and conversation history.
  - **Context Retention:** Ensures a coherent conversation by maintaining history.
  - **Sentiment Analysis:** Uses sentiment analysis to gauge confidence and sentiment in responses.
  - **Error Handling:** Implements robust exception handling for API calls.

## Prompt Design
- **Information Gathering:**
  - System prompt introduces the chatbot as an interviewer and provides context on the candidate’s experience and tech stack.
- **Technical Question Generation:**
  - The chatbot formulates relevant technical questions dynamically.
  - Uses the candidate’s tech stack to drive question complexity.
- **Sentiment Analysis:**
  - Helps evaluate confidence, positivity, and engagement.
- **Error Handling & Flow Control:**
  - If unexpected input is received, the chatbot responds meaningfully without deviating from the interview process.
  - The chatbot gracefully concludes the interview when the candidate requests to exit.

## Challenges & Solutions
### **1. Maintaining Context Throughout the Interview**
   - **Challenge:** Ensuring the chatbot retains previous conversations and asks follow-up questions coherently.
   - **Solution:** Implemented Streamlit's session state to persist conversation history.

### **2. Handling Unexpected Inputs**
   - **Challenge:** Candidates might enter irrelevant responses or unclear answers.
   - **Solution:** Crafted a prompt that instructs the chatbot to provide meaningful responses while staying within the interview scope.

### **3. Error Handling for API Calls**
   - **Challenge:** API failures or missing responses.
   - **Solution:** Wrapped API calls in a `try-except` block to handle failures gracefully and provide a fallback response.

## Future Enhancements
- **Advanced Sentiment Analysis:** Improve sentiment detection with more complex NLP models.
- **Multi-Model Integration:** Combine multiple AI models for better question generation.
- **Admin Dashboard:** Enable recruiters to review chat transcripts and assess candidate performance.

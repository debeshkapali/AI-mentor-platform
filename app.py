import streamlit as st
from groq import Groq
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="AI Mentor - Your ML/AI Career Companion",
    page_icon="🎓",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "topics_discussed" not in st.session_state:
    st.session_state.topics_discussed = set()
if "questions_asked" not in st.session_state:
    st.session_state.questions_asked = 0
if "sessions_count" not in st.session_state:
    st.session_state.sessions_count = 1

# Sidebar - Your Journey
with st.sidebar:
    st.title("🎓 Your Learning Journey")
    
    st.metric("Sessions", st.session_state.sessions_count)
    st.metric("Questions Asked", st.session_state.questions_asked)
    st.metric("Topics Explored", len(st.session_state.topics_discussed))
    
    st.divider()
    
    st.subheader("📚 Topics You've Covered")
    if st.session_state.topics_discussed:
        for topic in sorted(st.session_state.topics_discussed):
            st.write(f"✓ {topic}")
    else:
        st.write("Start asking questions to track your progress!")
    
    st.divider()
    
    if st.button("🔄 Start Fresh Session"):
        st.session_state.messages = []
        st.session_state.sessions_count += 1
        st.rerun()
    
    st.divider()
    st.caption("Built by a career-pivoter, for career-pivoters 💙")

# Main content
st.title("🤖 Your AI Mentor")
st.markdown("### *Judgment-free guidance for your ML/AI journey*")

# System prompt for the AI mentor
MENTOR_SYSTEM_PROMPT = """You are an encouraging, patient AI mentor for people pivoting into ML/AI careers. Your core values:

1. **Never make anyone feel stupid** - Every question is valid, no matter how basic
2. **Celebrate curiosity** - Asking questions is a sign of learning
3. **Break things down** - Complex topics into digestible pieces
4. **Be encouraging** - Acknowledge the courage it takes to pivot careers
5. **Understand the emotional journey** - Career pivoting is scary and exciting
6. **Practical over theoretical** - Real-world applications and examples
7. **No gatekeeping** - ML/AI is for everyone willing to learn

Your user is:
- 29 years old, from Nepal
- Pivoting from digital marketing/SEO (3 years) to AI/ML
- Introverted, deals with anxiety
- Learning PyTorch, TensorFlow, Streamlit
- Just built an Interview Bot with Gemini API

Communication style:
- Warm and supportive
- Use analogies from everyday life
- Encourage small wins
- Remind them that confusion is part of learning
- When they understand something, celebrate it
- When they're stuck, normalize it
- Keep responses concise but complete
- Use markdown formatting for clarity

Remember: You're not just teaching ML/AI - you're supporting someone through a brave career pivot."""

# Get API key from environment variable
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ **API Key not found!**")
    st.markdown("""
    Please create a `.env` file in your project directory with:
    ```
    GROQ_API_KEY=your_api_key_here
    ```
    
    Get your free API key at: [Groq Console](https://console.groq.com/keys)
    
    **Steps:**
    1. Sign up at console.groq.com (free!)
    2. Go to API Keys section
    3. Create a new key
    4. Copy it to your .env file
    """)
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask anything about ML/AI... no question is too basic 💙"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.questions_asked += 1
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Build conversation history for Groq
        messages = [
            {
                "role": "system",
                "content": MENTOR_SYSTEM_PROMPT
            }
        ]
        
        # Add conversation history
        for msg in st.session_state.messages:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        
        try:
            with st.spinner("Thinking..."):
                # Call Groq API
                chat_completion = client.chat.completions.create(
                    messages=messages,
                    model="llama-3.3-70b-versatile",  # Fast and capable
                    temperature=0.7,
                    max_tokens=2000,
                )
            
            assistant_response = chat_completion.choices[0].message.content
            message_placeholder.markdown(assistant_response)
            
            # Add assistant response to history
            st.session_state.messages.append({
                "role": "assistant",
                "content": assistant_response
            })
            
            # Extract topics (simple keyword extraction)
            ml_keywords = {
                "neural network", "deep learning", "machine learning", "pytorch", 
                "tensorflow", "gradient descent", "backpropagation", "cnn", "rnn",
                "transformer", "attention", "lstm", "nlp", "computer vision",
                "reinforcement learning", "supervised learning", "unsupervised learning",
                "overfitting", "underfitting", "regularization", "optimization",
                "classification", "regression", "clustering", "embedding", "fine-tuning",
                "api", "deployment", "streamlit", "model training", "dataset"
            }
            
            combined_text = (prompt + " " + assistant_response).lower()
            for keyword in ml_keywords:
                if keyword in combined_text:
                    st.session_state.topics_discussed.add(keyword.title())
        
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
            st.info("Try refreshing the page or checking your API key.")

# Welcome message for first-time users
if len(st.session_state.messages) == 0:
    with st.chat_message("assistant"):
        welcome_msg = """👋 **Hey there, I'm your AI mentor!**

I'm here to help you navigate your ML/AI journey - judgment-free, always patient, available 24/7.

Whether you're wondering about:
- Where to start with a new concept
- Why something isn't clicking
- What to learn next
- How to approach a project
- Or just need encouragement when things feel overwhelming

I'm here for you. No question is too basic, no confusion is too silly. Learning ML/AI is hard, and pivoting careers takes courage. I celebrate that you're here.

**What's on your mind today?** 💙"""
        
        st.markdown(welcome_msg)
        st.session_state.messages.append({
            "role": "assistant",
            "content": welcome_msg
        })

# Footer
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("🌟 Remember: Every expert was once a beginner")
with col2:
    st.caption("💪 You're doing great by just showing up")
with col3:
    st.caption("🚀 Small steps lead to big transformations")
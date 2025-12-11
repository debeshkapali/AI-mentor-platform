# 🎓 AI Mentor Platform

> *Judgment-free guidance for your ML/AI career journey*

A personal AI mentor built by a career-pivoter, for career-pivoters. Get patient, encouraging support 24/7 as you navigate your transition into Machine Learning and AI.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 🌟 Why This Exists

Career pivoting into ML/AI is **hard**. Finding judgment-free mentorship is even harder. Many "experts" make you feel stupid for asking basic questions. This platform is different.

**Built by someone going through the pivot, for people going through the pivot.**

### Core Principles
- ✨ **Never make anyone feel stupid** - Every question is valid
- 🎯 **Celebrate curiosity** - Asking questions is a sign of learning
- 🧩 **Break things down** - Complex topics into digestible pieces
- 💪 **Understand the emotional journey** - Career pivoting is scary AND exciting
- 🚫 **No gatekeeping** - ML/AI is for everyone willing to learn

---

## ✨ Features

### Current (v1.0 - MVP)
- 🤖 **AI-Powered Mentor** - Patient, encouraging responses using Llama 3.3 (via Groq)
- 💬 **Conversational Interface** - Natural chat experience
- 📊 **Progress Tracking** - Track questions asked, topics covered, and sessions
- 🎯 **Topic Detection** - Automatically identifies ML/AI concepts you're learning
- 🔄 **Session Management** - Start fresh or continue your journey
- 💙 **Encouragement Built-In** - Supportive by design

### Coming Soon
- 💾 Persistent storage (SQLite) - Save progress across sessions
- 📈 Progress visualization - Charts and graphs of your learning journey
- 🗺️ Personalized learning paths - Tailored recommendations
- 🏆 Milestone celebrations - Achievements and badges
- 📚 Resource library - Curated learning materials
- 👥 Community features - Connect with other career-pivoters

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Conda (recommended) or pip

### Installation

1. **Clone the repository**
```bash
git clone git@github.com:debeshkapali/AI-mentor-platform.git
cd AI-mentor-platform
```

2. **Set up your environment**

#### Option A: Using Conda (Recommended)

Create environment from the `environment.yml` file:
```bash
conda env create -f environment.yml
conda activate mentor-env
```

#### Option B: Using pip

Install dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

3. **Set up your API key**

Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free Groq API key at: [console.groq.com](https://console.groq.com/)

4. **Run the application**
```bash
streamlit run mentor_app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 💡 Usage

### Getting Started
1. Launch the app
2. Start asking questions - no question is too basic!
3. Watch your progress grow in the sidebar
4. Learn at your own pace, judgment-free

### Example Questions to Try
- "I'm confused about how neural networks actually learn"
- "Where should I start with deep learning?"
- "What's the difference between supervised and unsupervised learning?"
- "I feel overwhelmed - what should I focus on first?"
- "Can you explain backpropagation like I'm 5?"

---

## 🏗️ Project Structure

```
ai-mentor-platform/
├── mentor_app.py          # Main Streamlit application
├── environment.yml        # Conda environment file
├── requirements.txt       # Pip dependencies
├── .env                   # API keys (not committed to git)
├── .gitignore             # Git ignore file
└── README.md              # This file
```

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Llama 3.3 70B (via Groq API)
- **Language**: Python 3.8+
- **Environment Management**: python-dotenv

### Why These Choices?
- **Streamlit**: Fast prototyping, easy to build with
- **Groq**: Free, fast inference, no regional restrictions
- **Llama 3.3**: Powerful open-source model, great for conversations
- **Simple Stack**: Focus on learning and iteration, not complexity

---

## 🗺️ Roadmap

### Phase 1: Foundation ✅ (Current)
- [x] Basic conversational AI mentor
- [x] Progress tracking
- [x] Topic detection
- [x] Session management

### Phase 2: Persistence (In Progress)
- [ ] SQLite database integration
- [ ] Save conversation history
- [ ] Persistent user profiles
- [ ] Export conversations

### Phase 3: Enhanced Learning
- [ ] Progress visualization with charts
- [ ] Learning path recommendations
- [ ] Milestone achievements
- [ ] Study streak tracking

### Phase 4: Community
- [ ] User authentication
- [ ] Share learning journeys
- [ ] Peer support features
- [ ] Resource sharing

---

## 🤝 Contributing

This project is in active development! Contributions, issues, and feature requests are welcome.

**How to contribute:**
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👤 About the Creator

Built by a career-pivoter from Nepal, transitioning from digital marketing/SEO into ML/AI. This project represents the mentor I wish I had during my journey.

**Current skills:**
- PyTorch, TensorFlow
- Streamlit
- API integrations (Gemini, Groq)

**Previous projects:**
- Interview Practice Bot (Gemini API)

---

## 🙏 Acknowledgments

- The ML/AI community for being welcoming despite the occasional gatekeepers
- Everyone who's ever asked a "basic" question - you're brave
- Groq for their generous free tier
- Anthropic's Claude for helping me build this

---

## 📧 Contact

- GitHub: [@debeshkapali](https://github.com/debeshkapali)
- Project Link: [https://github.com/debeshkapali/AI-mentor-platform](https://github.com/debeshkapali/AI-mentor-platform)

---

<div align="center">

### 💙 Remember: Every expert was once a beginner

**Built with 💙 by a career-pivoter, for career-pivoters**

⭐ Star this repo if it helps you on your journey!

</div>
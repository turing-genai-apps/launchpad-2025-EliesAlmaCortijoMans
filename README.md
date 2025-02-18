# Conversational AI Agent with LangChain

A powerful conversational AI agent built with LangChain, featuring a FastAPI backend and React frontend. This application demonstrates the integration of various tools and capabilities to create an interactive and helpful AI assistant.

## 🌟 Features

- **Interactive Chat Interface**: Clean and responsive React-based chat UI
- **Multiple Tool Integration**: 
  - Current Time Tool
  - Weather Information Tool
  - Programming Jokes Tool
  - Mathematical Calculator Tool
- **Real-time Processing**: Fast response times with async processing
- **Error Handling**: Robust error management and user feedback

## 🛠 Tech Stack

### Backend
- FastAPI
- LangChain
- OpenAI GPT Integration
- Python 3.8+
- uvicorn

### Frontend
- React
- Axios
- CSS3
- Node.js

## 📋 Prerequisites

- Python 3.8 or higher
- Node.js and npm
- OpenAI API key
- Weather API key (optional)

## 🚀 Installation

### Backend Setup

1. Clone the repository
bash
git clone https://github.com/turing-genai-apps/launchpad-2025-EliesAlmaCortijoMans.git
cd launchpad-2025-EliesAlmaCortijoMans

2. Create and activate virtual environment
bash
cd backend
python -m venv venv
---For Windows
.\venv\Scripts\activate
---For Linux/Mac
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Create `.env` file
env
OPENAI_API_KEY=your_openai_api_key_here
WEATHER_API_KEY=your_weather_api_key_here # Optional

### Frontend Setup

1. Navigate to frontend directory
bash
cd frontend

2. Install dependencies
bash
npm install

## 🎮 Running the Application

1. Start the backend server
bash
---From the backend directory
uvicorn app.main:app --reload

2. Start the frontend development server
bash
---From the frontend directory
npm start


3. Access the application at `http://localhost:3000`

## 💡 Usage

The AI agent can help with various tasks:

1. **Time Queries**
   - "What time is it?"
   - "Tell me the current time"

2. **Weather Information**
   - "What's the weather in London?"
   - "Tell me the weather in Tokyo"

3. **Programming Jokes**
   - "Tell me a joke"
   - "Share a programming joke"

4. **Calculations**
   - "Calculate 25 * 4"
   - "What's 150 / 3?"

## 🔧 Project Structure
conversation-agent/
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ ├── App.js
│ │ └── index.js
│ ├── package.json
│ └── public/
└── backend/
├── app/
│ ├── main.py
│ └── agent.py
└── requirements.txt


## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgments

- OpenAI for providing the GPT API
- LangChain for the excellent framework
- FastAPI team for the amazing backend framework
- React team for the frontend framework

## 📫 Contact

Elies Alma Cortijo Mans - [elies.a@turing.com]

Project Link: [https://github.com/turing-genai-apps/launchpad-2025-EliesAlmaCortijoMans](https://github.com/turing-genai-apps/launchpad-2025-EliesAlmaCortijoMans)

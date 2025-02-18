from langchain.agents import AgentExecutor
from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from datetime import datetime
import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()

class ToolFunctions:
    @staticmethod
    def get_current_time() -> str:
        """Get the current date and time."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def get_weather(location: str) -> str:
        """Get weather information for a location."""
        API_KEY = os.getenv("WEATHER_API_KEY")
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                return f"Weather in {location}: {data['weather'][0]['description']}, Temperature: {data['main']['temp']}°C"
            return f"Could not get weather for {location}"
        except Exception as e:
            return f"Error getting weather: {str(e)}"
    
    @staticmethod
    def tell_joke() -> str:
        """Tell a random programming-related joke."""
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the SQL query go to therapy? It had too many relationship issues!",
            "What's a programmer's favorite place? The foo bar!",
            "Why do Python programmers wear glasses? Because they can't C#!",
        ]
        return random.choice(jokes)
    
    @staticmethod
    def calculate_expression(expression: str) -> str:
        """Calculate a mathematical expression."""
        try:
            allowed_chars = set("0123456789+-*/() .")
            if not all(c in allowed_chars for c in expression):
                return "Invalid expression. Only basic math operations allowed."
            return str(eval(expression))
        except Exception as e:
            return f"Error calculating: {str(e)}"

class ConversationAgent:
    def __init__(self):
        # Initialize LangChain's ChatOpenAI with project API key
        self.llm = ChatOpenAI(
            temperature=0.7,
            model="gpt-4o-mini",
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            openai_api_base="https://api.openai.com/v1",  # Default OpenAI API endpoint
        )
        
        # Define tools
        self.tools = [
            Tool(
                name="CurrentTime",
                func=ToolFunctions.get_current_time,
                description="Get the current date and time"
            ),
            Tool(
                name="Weather",
                func=ToolFunctions.get_weather,
                description="Get weather information for a location. Input should be a city name"
            ),
            Tool(
                name="TellJoke",
                func=ToolFunctions.tell_joke,
                description="Tell a random programming-related joke"
            ),
            Tool(
                name="Calculate",
                func=ToolFunctions.calculate_expression,
                description="Calculate a mathematical expression. Example: '2 + 2' or '(3 * 4) / 2'"
            ),
        ]

        # Create prompt template
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful and friendly AI assistant with access to various tools. 
            You can help with calculations, weather information, telling jokes, and more. 
            When someone asks for a joke, use the TellJoke tool.
            When someone asks about time, use the CurrentTime tool.
            When someone asks about weather, use the Weather tool.
            When someone wants to calculate something, use the Calculate tool."""),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])

        # Create the agent
        self.agent = (
            {
                "input": lambda x: x["input"],
                "agent_scratchpad": lambda x: format_to_openai_functions(
                    x["intermediate_steps"]
                ),
            }
            | prompt
            | self.llm
            | OpenAIFunctionsAgentOutputParser()
        )
        
        # Create the agent executor
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True,
            max_iterations=3,
            early_stopping_method="generate"
        )

    def process_message(self, message: str) -> str:
        try:
            response = self.agent_executor.invoke(
                {
                    "input": message,
                }
            )
            return response["output"]
        except Exception as e:
            return f"Error processing message: {str(e)}"
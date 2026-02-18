import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found in environment variables")
    print("Please create a .env file with: GEMINI_API_KEY=your_api_key_here")
    exit(1)

genai.configure(api_key=api_key)

print("=== Gemini Flash 2.0 API Integration ===\n")

model = genai.GenerativeModel("gemini-2.0-flash-exp")

print("Example 1: Simple Question")
response = model.generate_content("What is Python programming language?")
print(f"Response: {response.text}\n")

print("=" * 50)
print("\nExample 2: Code Explanation")
code_prompt = """
Explain this Python code in simple terms:
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""
response = model.generate_content(code_prompt)
print(f"Response: {response.text}\n")

print("=" * 50)
print("\nExample 3: Student Query")
student_query = "What are the key differences between lists and tuples in Python?"
response = model.generate_content(student_query)
print(f"Question: {student_query}")
print(f"Response: {response.text}\n")

print("=" * 50)
print("\nExample 4: Code Generation")
code_request = "Write a Python function to calculate factorial of a number"
response = model.generate_content(code_request)
print(f"Request: {code_request}")
print(f"Response:\n{response.text}\n")

print("=" * 50)
print("\nExample 5: Chat Conversation")

chat = model.start_chat(history=[])

message1 = "Hi! I'm learning Python. Can you help me?"
response1 = chat.send_message(message1)
print(f"Student: {message1}")
print(f"Gemini: {response1.text}\n")

message2 = "What is a decorator in Python?"
response2 = chat.send_message(message2)
print(f"Student: {message2}")
print(f"Gemini: {response2.text}\n")

print("API integration examples completed!")

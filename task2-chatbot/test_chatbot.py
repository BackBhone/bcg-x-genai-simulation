"""Runs a scripted conversation through the chatbot and prints each answer."""

from chatbot import simple_chatbot

test_queries = [
    # The 5 predefined questions
    "What is Apple's total revenue?",
    "How has net income changed over the last year?",
    "What is the profit margin?",
    "How much debt does the company have?",
    "What is the operating cash flow?",
    # Different company and year
    "What is Microsoft's total revenue in 2024?",
    "How has Tesla's net income changed over the last year?",
    # Follow-up questions using conversation state
    "What about Microsoft?",
    "And in 2024?",
    # Edge cases and error handling
    "What is the total revenue?",          # no company named, uses the remembered one
    "How has net income changed in 2023?", # no 2022 data to compare
    "What is Apple's revenue in 2021?",    # year not in the data
    "What is the weather today?",          # not a financial question
]

for query in test_queries:
    print(f"You: {query}")
    print(f"Bot: {simple_chatbot(query)}\n")

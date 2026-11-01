"""
GFC Financial Chatbot (rule-based prototype)
BCG X GenAI Job Simulation, Task 2

Answers a set of predefined financial questions about Microsoft, Tesla and Apple
using data extracted from their 10-K filings (fiscal years 2023 to 2025).
All source figures are in USD millions.
"""

import re
import pandas as pd

# ---------- 1. Load and prepare the data ----------
df = pd.read_csv("financial_data.csv")
df = df.dropna(how="all").dropna(axis=1, how="all")
df["Year"] = df["Year"].astype(int)
df = df.sort_values(["Company", "Year"]).reset_index(drop=True)

COMPANIES = df["Company"].unique().tolist()   # ['Apple', 'Microsoft', 'Tesla']
YEARS = sorted(df["Year"].unique().tolist())  # [2023, 2024, 2025]
LATEST_YEAR = max(YEARS)

# Conversation state: remembers the last company, year and topic the user asked about
state = {"company": None, "year": LATEST_YEAR, "topic": None}

HELP_TEXT = (
    "I can answer these questions for Microsoft, Tesla or Apple (2023 to 2025):\n"
    "  1. What is the total revenue?\n"
    "  2. How has net income changed over the last year?\n"
    "  3. What is the profit margin?\n"
    "  4. How much debt does the company have?\n"
    "  5. What is the operating cash flow?\n"
    "Include a company name and, if you like, a year. Example: 'What is Tesla's total revenue in 2024?'\n"
    "Type 'help' to see this list again or 'exit' to quit."
)


# ---------- 2. Helper functions ----------
def fmt(millions):
    """Turn a figure in USD millions into easy-to-read text, e.g. 416161 -> $416.2 billion."""
    return f"${millions / 1000:,.1f} billion"


def get_row(company, year):
    """Return the data row for one company and year."""
    return df[(df["Company"] == company) & (df["Year"] == year)].iloc[0]


def find_company(query):
    for company in COMPANIES:
        if company.lower() in query:
            return company
    return None


def find_year(query):
    match = re.search(r"\b(20\d{2})\b", query)
    return int(match.group(1)) if match else None


# ---------- 3. Chatbot logic (rule-based if/elif) ----------
def find_topic(query):
    """Match the user's words to one of the predefined questions."""
    if "revenue" in query or "sales" in query:
        return "revenue"
    elif "margin" in query:
        return "margin"
    elif "net income" in query or "profit" in query:
        return "net_income"
    elif "debt" in query or "liabilit" in query:
        return "debt"
    elif "cash" in query:
        return "cash_flow"
    return None


def simple_chatbot(user_query):
    query = user_query.lower().strip()

    if query in ("help", "?", "hi", "hello"):
        return HELP_TEXT

    company = find_company(query)
    year = find_year(query)
    topic = find_topic(query)

    # Nothing recognised at all: explain what the chatbot can do
    if not (company or year or topic):
        return ("Sorry, I can only answer a few predefined financial questions. "
                "Type 'help' to see what I can answer.")

    if year and year not in YEARS:
        return f"Sorry, I only have data for {YEARS[0]} to {YEARS[-1]}."

    # Update conversation state, so follow-ups like "What about Tesla?" work
    if company:
        state["company"] = company
        state["year"] = year or LATEST_YEAR
    elif year:
        state["year"] = year
    if topic:
        state["topic"] = topic

    company, year, topic = state["company"], state["year"], state["topic"]
    if company is None:
        return "Which company do you mean? Please mention Microsoft, Tesla or Apple."
    if topic is None:
        return f"What would you like to know about {company}? Type 'help' to see the questions I can answer."

    row = get_row(company, year)

    # Query 1: total revenue
    if topic == "revenue":
        return f"{company}'s total revenue in {year} was {fmt(row['Total Revenue'])}."

    # Query 2: change in net income over the last year
    elif topic == "net_income":
        if year == YEARS[0]:
            return (f"{company}'s net income in {year} was {fmt(row['Net Income'])}. "
                    f"I don't have {year - 1} data to compare it with.")
        prev = get_row(company, year - 1)
        change = row["Net Income"] - prev["Net Income"]
        pct = change / prev["Net Income"] * 100
        direction = "increased" if change > 0 else "decreased"
        return (f"{company}'s net income {direction} by {fmt(abs(change))} ({pct:+.1f}%) "
                f"from {year - 1} to {year}, reaching {fmt(row['Net Income'])}.")

    # Query 3: profit margin
    elif topic == "margin":
        margin = row["Net Income"] / row["Total Revenue"] * 100
        return (f"{company}'s net profit margin in {year} was {margin:.1f}%. "
                f"That means it kept about {margin:.0f} cents of profit from every dollar of revenue.")

    # Query 4: debt (liabilities compared with assets)
    elif topic == "debt":
        ratio = row["Total Liabilities"] / row["Total Assets"] * 100
        return (f"In {year}, {company} had total liabilities of {fmt(row['Total Liabilities'])} "
                f"against total assets of {fmt(row['Total Assets'])}, a debt ratio of {ratio:.1f}%.")

    # Query 5: operating cash flow
    elif topic == "cash_flow":
        return (f"{company} generated {fmt(row['Operating Cash Flow'])} of cash from operating "
                f"activities in {year}.")


# ---------- 4. Command-line conversation ----------
def run_chat():
    print("GFC Financial Chatbot")
    print(HELP_TEXT)
    while True:
        user_query = input("\nYou: ")
        if user_query.lower().strip() in ("exit", "quit", "bye"):
            print("Bot: Goodbye!")
            break
        print("Bot:", simple_chatbot(user_query))


if __name__ == "__main__":
    run_chat()

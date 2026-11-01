# GFC Financial Chatbot: Rule-Based Prototype

BCG X GenAI Job Simulation, Task 2
Author: Aung Bhone Myat

## Overview
A simple rule-based chatbot that answers predefined financial questions about Microsoft, Tesla and Apple for fiscal years 2023 to 2025. It uses the data extracted from the companies' 10-K filings in Task 1 (`financial_data.csv`, figures in USD millions).

## Files
| File | Purpose |
|---|---|
| `chatbot.py` | The chatbot: data loading, query matching and responses |
| `financial_data.csv` | Financial data from the 10-K filings (Task 1) |
| `test_chatbot.py` | Runs a scripted set of test questions |
| `test_results.txt` | Output of the test script |
| `README.md` | This documentation |

## How to run
```
python chatbot.py         # interactive chat in the command line (type 'exit' to quit)
python test_chatbot.py    # run the scripted tests
```
Requires Python 3 and pandas.

## Predefined queries
1. What is the total revenue?
2. How has net income changed over the last year?
3. What is the profit margin?
4. How much debt does the company have?
5. What is the operating cash flow?

Each query can include a company (Microsoft, Tesla or Apple) and a year (2023 to 2025), for example "What is Tesla's total revenue in 2024?". If no year is given, the latest year (2025) is used.

## How it works
1. **Data loading:** pandas reads the CSV, removes empty rows and columns, and sorts by company and year.
2. **Query matching (rule-based logic):** the chatbot lowercases the input and uses if/elif rules to look for keywords (for example "revenue", "net income", "margin", "debt", "cash"), a company name and a year.
3. **Data retrieval:** the matching row is pulled from the data, and the answer is calculated from the real figures (for example net income change, profit margin and debt ratio), so nothing is hard-coded.
4. **Plain-language answers:** figures are converted from millions into billions (for example $416.2 billion) and explained simply, so users without a finance background can follow them.
5. **Conversation state:** the chatbot remembers the last company, year and topic, so follow-ups like "What about Tesla?" or "And in 2024?" work.
6. **Error handling:** it asks which company the user means when none is given, explains when a year is outside 2023 to 2025 or when there is no earlier year to compare, and points users to 'help' for questions it does not recognise.

## Limitations
- Only understands the 5 predefined question types, matched by keywords rather than real natural language understanding. Unusual wording may not be recognised.
- Covers only 3 companies, 3 years and 5 metrics, from static data that must be updated by hand.
- Answers one company at a time, with no side-by-side comparisons (for example "Which company grew fastest?").
- Gives numbers without wider context, such as one-off tax effects (Apple 2024, Tesla 2023).
- Companies have different fiscal year ends (Microsoft: June, Apple: September, Tesla: December), so the same "year" does not cover exactly the same months.

## Possible improvements
- Use NLP or a large language model to understand questions written in any wording.
- Add comparisons between companies and multi-year trends.
- Connect to SEC EDGAR to update data automatically.
- Build a simple web interface with Flask.

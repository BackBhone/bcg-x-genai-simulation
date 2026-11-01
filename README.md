# BCG X GenAI Job Simulation: Financial Analysis and Chatbot

My work for the BCG X GenAI Job Simulation on Forage (completed November 2026).

**Scenario:** As a junior data scientist in BCG's GenAI Consulting team, I helped build an AI-powered chatbot that gives clients of a financial institution quick insights from company 10-K reports.

## Task 1: Data extraction and analysis
Folder: [`task1-financial-analysis`](task1-financial-analysis)

- Extracted Total Revenue, Net Income, Total Assets, Total Liabilities and Operating Cash Flow for Microsoft, Tesla and Apple (fiscal years 2023 to 2025) from their 10-K filings on SEC EDGAR.
- Cleaned the data and calculated year-over-year growth for every metric in Python with pandas.
- Added financial health ratios (net profit margin, debt ratio, cash flow to net income), a company comparison and charts.
- Wrote findings on each company's performance, including the effect of one-off tax items.

**Key results**
| Company | 2025 revenue | Revenue growth 2025 | 2025 net profit margin |
|---|---|---|---|
| Microsoft | $281.7bn | +14.9% | 36.1% |
| Apple | $416.2bn | +6.4% | 26.9% |
| Tesla | $94.8bn | -2.9% | 4.0% |

## Task 2: Rule-based financial chatbot
Folder: [`task2-chatbot`](task2-chatbot)

- Python chatbot that answers 5 predefined financial questions using the Task 1 data.
- Matches questions with keyword rules, calculates answers live from the data and explains them in plain English.
- Remembers the conversation, so follow-ups like "What about Tesla?" work.
- Handles errors such as a missing company, a year outside the data or an unrelated question.
- Tested with a scripted set of 13 questions (see `test_results.txt`).

## Tools
Python, pandas, Matplotlib, Google Colab, SEC EDGAR

## How to run the chatbot
```
cd task2-chatbot
pip install pandas
python chatbot.py
```
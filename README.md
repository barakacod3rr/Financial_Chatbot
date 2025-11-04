# 💼 AI-Powered Financial Analysis & Chatbot (BCG GenAI Project)

As a **Junior Data Scientist at Boston Consulting Group (BCG)** on the **GenAI Consulting Team**, this project represents an exciting opportunity to blend **finance, data analysis, and generative AI**.  

The goal was to **extract and analyze financial data** from company filings, then **build a prototype AI chatbot** capable of answering key financial queries interactively — showcasing how AI can enhance financial insights for consulting applications.

---

## 📊 Task 1: Financial Data Extraction & Analysis

### 🎯 Objective
Extract and analyze financial data for **Microsoft (MSFT)**, **Tesla (TSLA)**, and **Apple (AAPL)** from their **10-K filings (FY 2022–2024)** to identify trends and prepare data for AI-driven analysis.

### 🧩 Process
- Retrieved key metrics: **Total Revenue**, **Net Income**, **Total Assets**, **Total Liabilities**, and **Operating Cash Flow** from SEC’s [EDGAR database]
- Found the data in section 8 of each report
  
**MICROSOFT**

2023-2024: 

https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/msft-20240630.htm#item_8_financial_statements_and_supplem

2022-2023: 

https://www.sec.gov/Archives/edgar/data/789019/000095017023035122/msft-20230630.htm#item_8_financial_statements_and_supplem


**TESLA**

2023-2024:

https://www.sec.gov/Archives/edgar/data/1318605/000162828025003063/tsla-20241231.htm#ie9fbbc0a99a6483f9fc1594c1ef72807_1148

2022:

https://www.sec.gov/Archives/edgar/data/1318605/000095017023001409/tsla-20221231.htm#financial_statements

**APPLE**

2023-2024:

https://www.sec.gov/Archives/edgar/data/320193/000032019324000123/aapl-20240928.htm#i7bfbfbe54b9647b1b4ba4ff4e0aba09d_169

2022:

https://www.sec.gov/Archives/edgar/data/320193/000032019322000108/aapl-20220924.htm#ief5efb7a728d4285b6b4af1e880101bc_73


- Compiled data into [Excel](financials_2022_2024.xlsx), for use in Python (`pandas`).  
- Calculated **Revenue Growth (%)** and **Net Income Growth (%)** using year-over-year comparisons.  
- Summarized insights on financial performance trends across all three companies.  

### ✅ Outcome
A clean and transformed dataset in the  [jupyter notebook](task1_forage.ipynb) and downloaded the transformed dataframe, [Excel sheet](financialsNew.csv) ready for use in **AI applications** — particularly chatbot training and query responses.

---

## 🤖 Task 2: Financial Chatbot Prototype

### 🎯 Objective
Develop a **Flask-based chatbot** that uses the analyzed data to respond to **predefined financial queries** — a foundational step toward building an AI-powered financial assistant.

### ⚙️ Functionality
- Used the cleaned financial data from **Task 1**, recreated as a new **DataFrame** , [Transformed Dataframe](financialsNew.csv), directly in `app.py` (instead of importing from Excel/CSV) for seamless integration with the chatbot logic.
- Responds to key user queries such as:
  - “What is the total revenue?”
  - “How has net income changed over the last year?”
  - “What is the revenue growth percentage?”
- Uses **lowercased text matching** to ensure flexible queries.  
- Displays a fallback message for non-predefined questions:  
  > “Sorry, I can only provide information on predefined queries.
- Type 'help' and chatbot gives the list of questions you should ask
  
# 3️⃣ Access in your browser
[Financial Chatbot deployed](https://eanns-finance-chatbot.onrender.com/)

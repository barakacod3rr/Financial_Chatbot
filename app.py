from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# -------------------------------
# Financial Data -- Data extracted from task2's datframe in python
# -------------------------------
data = {
    "apple": {
        "2022": {"Total Revenue": 274515, "Net Income": 99803},
        "2023": {"Total Revenue": 365817, "Net Income": 96995},
        "2024": {"Total Revenue": 394328, "Net Income": 93736}
    },
    "microsoft": {
        "2022": {"Total Revenue": 198270, "Net Income": 72738},
        "2023": {"Total Revenue": 211915, "Net Income": 72361},
        "2024": {"Total Revenue": 245122, "Net Income": 88136}
    },
    "tesla": {
        "2022": {"Total Revenue": 81462, "Net Income": 12587},
        "2023": {"Total Revenue": 96773, "Net Income": 14974},
        "2024": {"Total Revenue": 97690, "Net Income": 7153}
    }
}

# -------------------------------
# Simple Chatbot Logic
# -------------------------------
def simple_chatbot(user_query):
    query = user_query.lower().strip()

    # Apple-related questions
    if query == "what is apple's total revenue in 2024?":
        return f"Apple's total revenue in 2024 was ${data['apple']['2024']['Total Revenue']:,} million."
    elif query == "how has apple's net income changed over the last year?":
        diff = data['apple']['2024']['Net Income'] - data['apple']['2023']['Net Income']
        change = (diff / data['apple']['2023']['Net Income']) * 100
        return f"Apple's net income changed by {change:.2f}% from 2023 to 2024."

    # Microsoft-related questions
    elif query == "what is microsoft's total revenue in 2024?":
        return f"Microsoft's total revenue in 2024 was ${data['microsoft']['2024']['Total Revenue']:,} million."
    elif query == "how has microsoft's net income changed over the last year?":
        diff = data['microsoft']['2024']['Net Income'] - data['microsoft']['2023']['Net Income']
        change = (diff / data['microsoft']['2023']['Net Income']) * 100
        return f"Microsoft's net income changed by {change:.2f}% from 2023 to 2024."

    # Tesla-related questions
    elif query == "what is tesla's total revenue in 2024?":
        return f"Tesla's total revenue in 2024 was ${data['tesla']['2024']['Total Revenue']:,} million."
    elif query == "how has tesla's net income changed over the last year?":
        diff = data['tesla']['2024']['Net Income'] - data['tesla']['2023']['Net Income']
        change = (diff / data['tesla']['2023']['Net Income']) * 100
        return f"Tesla's net income changed by {change:.2f}% from 2023 to 2024."

    # Help command
    elif query == "help":
        return (
            "🧾 You can ask me the following questions:\n"
            "• what is apple's total revenue in 2024?\n"
            "• how has apple's net income changed over the last year?\n"
            "• what is microsoft's total revenue in 2024?\n"
            "• how has microsoft's net income changed over the last year?\n"
            "• what is tesla's total revenue in 2024?\n"
            "• how has tesla's net income changed over the last year?\n"
        )

    # Default response
    else:
        return "❌ Sorry, I can only provide information on predefined questions. Type 'help' to see what you can ask."

# -------------------------------
# Flask Routes
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data_in = request.get_json(force=True)
    user_query = data_in.get("query", "")
    response = simple_chatbot(user_query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

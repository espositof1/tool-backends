from flask import Flask, request, jsonify

app = Flask(__name__)

@app.after_request
def apply_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "https://preview--financial-ratio-calculator.lovable.app"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Max-Age"] = "86400"
    return response

@app.route("/api/ratios", methods=["POST"])
def analyze_ratios():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Simple example ratios
        result = {"ratios": {}}
        for year, values in data.items():
            revenue = values.get("revenue", 1)
            cogs = values.get("cogs", 1)
            current_assets = values.get("current_assets", 1)
            current_liabilities = values.get("current_liabilities", 1)
            inventory = values.get("avg_inventory", 1)
            ar = values.get("accounts_receivable", 1)
            credit_sales = values.get("credit_sales", 1)
            debt = values.get("total_debt", 1)
            assets = values.get("total_assets", 1)
            nopat = values.get("nopat", 1)
            capital = values.get("invested_capital", 1)

            result["ratios"][year] = {
                "current_ratio": round(current_assets / current_liabilities, 2),
                "inventory_turnover": round(cogs / inventory, 2),
                "accounts_receivable_days": round((ar / credit_sales) * 365, 1),
                "debt_to_assets": round(debt / assets, 2),
                "roic": round(nopat / capital, 2),
            }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/ratios", methods=["OPTIONS"])
def handle_options():
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

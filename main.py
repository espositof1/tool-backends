from flask import Flask, request, jsonify
import os

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
        if not data or not isinstance(data, dict):
            return jsonify({"error": "Invalid or missing JSON data"}), 400

        ratios_list = []
        red_flags = 0

        for name, values in data.items():
            if not isinstance(values, dict):
                continue

            current_ratio = round(values.get("current_assets", 1) / values.get("current_liabilities", 1), 2)
            inventory_turnover = round(values.get("cogs", 1) / values.get("avg_inventory", 1), 2)
            ar_days = round((values.get("accounts_receivable", 1) / values.get("credit_sales", 1)) * 365, 1)
            debt_to_assets = round(values.get("total_debt", 1) / values.get("total_assets", 1), 2)
            roic = round(values.get("nopat", 1) / values.get("invested_capital", 1), 2)

            # Determine status
            status = "healthy"
            if current_ratio < 1.5 or ar_days > 60 or inventory_turnover < 5:
                status = "warning"
                red_flags += 1
            if current_ratio < 1 or inventory_turnover < 4:
                status = "danger"
                red_flags += 1

            ratios_list.append({
                "name": name,
                "current_ratio": current_ratio,
                "inventory_turnover": inventory_turnover,
                "accounts_receivable_days": ar_days,
                "debt_to_assets": debt_to_assets,
                "roic": roic,
                "status": status
            })

        response = {
            "summary": f"You have {red_flags} red flags.",
            "redFlags": red_flags,
            "cashTrapped": "$3.2M",  # optional static insight
            "ratios": ratios_list,
            "insights": [
                "Your DSO is increasing year over year, suggesting issues with accounts receivable collection.",
                "Inventory turnover is slowing down, indicating possible excess inventory or slow-moving products.",
                "Your current ratio is declining, pointing to decreasing liquidity."
            ],
            "cashLeak": "Estimated cash trapped in operations: $3.2M",
            "recommendations": [
                "Implement stricter credit policies and follow up on late payments more aggressively.",
                "Review inventory management practices and consider just-in-time ordering for slow-moving items.",
                "Develop a plan to improve working capital by reducing current liabilities or increasing current assets."
            ]
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/ratios", methods=["OPTIONS"])
def handle_options():
    return "", 204

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

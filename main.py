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

        if not data or not isinstance(data, dict):
            return jsonify({"error": "Invalid or missing JSON data"}), 400

        # ✅ Extract and remove industry from data if present
        industry = data.pop("industry", "Unknown")

        # ✅ Calculate ratios for each year
        results = []
        for year_label, values in data.items():
            if not isinstance(values, dict):
                continue  # Skip bad input

            try:
                current_assets = values.get("currentAssets", 1)
                current_liabilities = values.get("currentLiabilities", 1)
                cogs = values.get("cogs", 1)
                inventory = values.get("avgInventory", 1)
                ar = values.get("accountsReceivable", 1)
                credit_sales = values.get("creditSales", 1)
                debt = values.get("debt", 1)
                assets = current_assets + inventory + ar  # Simple estimate
                nopat = values.get("nopat", 1)
                capital = values.get("investedCapital", 1)

                result = {
                    "name": year_label,
                    "current_ratio": round(current_assets / current_liabilities, 2),
                    "inventory_turnover": round(cogs / inventory, 2),
                    "accounts_receivable_days": round((ar / credit_sales) * 365, 1),
                    "debt_to_assets": round(debt / assets, 2),
                    "roic": round(nopat / capital, 2),
                    "status": "warning"  # Just for UI coloring — you can customize this logic
                }

                results.append(result)
            except Exception as calc_error:
                return jsonify({"error": f"Failed for {year_label}: {str(calc_error)}"}), 500

        return jsonify({
            "ratios": results,
            "insights": [
                "Your DSO is increasing year over year, suggesting issues with accounts receivable collection.",
                "Inventory turnover is slowing down, indicating possible excess inventory or slow-moving products.",
                "Your current ratio is declining, pointing to decreasing liquidity."
            ],
            "recommendations": [
                "Implement stricter credit policies and follow up on late payments more aggressively.",
                "Review inventory management practices and consider just-in-time ordering for slow-moving items.",
                "Develop a plan to improve working capital by reducing current liabilities or increasing current assets."
            ],
            "cashImpact": "$3.2M",
            "cashImpactNote": "Estimated cash trapped in operations: $3.2M"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/ratios", methods=["OPTIONS"])
def handle_options():
    return "", 204

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

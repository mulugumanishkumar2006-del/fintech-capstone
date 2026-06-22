from flask import Flask, jsonify
import pandas as pd
import os
app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data", "raw", "02_nav_history.csv")

df = pd.read_csv(file_path)

@app.route('/')
def home():
    return jsonify({"message": "Flask API is running"})


@app.route('/top-funds')
def top_funds():
    latest = df.sort_values('date').groupby('amfi_code').tail(1)
    top = latest.sort_values('nav', ascending=False).head(10)

    result = top[['amfi_code', 'nav']].to_dict(orient='records')
    return jsonify(result)


@app.route('/fund/<int:code>')
def fund_details(code):
    fund = df[df['amfi_code'] == code]

    if fund.empty:
        return jsonify({"error": "Invalid AMFI code"}), 404

    return jsonify(fund.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)
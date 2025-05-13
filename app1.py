from flask import Flask, render_template, jsonify, request
import pandas as pd

app = Flask(__name__)

# 載入 Titanic 資料
df = pd.read_csv('titanic.csv', encoding='utf-8-sig')

@app.route('/')
def home():
    return render_template('index23.html')  # 不需要傳 data，DataTables 會 AJAX 打 /api/data

@app.route('/api/data')
def get_data():
    sex = request.args.get('sex', '')
    pclass = request.args.get('pclass', '')
    print(f"🔍 篩選條件: sex={sex}, pclass={pclass}")

    filtered_df = df.copy()

    if sex:
        filtered_df = filtered_df[filtered_df['Sex'].str.lower() == sex.lower()]

    if pclass:
        filtered_df = filtered_df[filtered_df['Pclass'].astype(str) == pclass]

    filtered_df = filtered_df.fillna("")
    return jsonify({'data': filtered_df.to_dict(orient='records')})

if __name__ == '__main__':
    app.run(debug=True)

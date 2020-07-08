from flask import Flask, jsonify
from flask import Flask, render_template, request, jsonify #追加
import random
# 現在時刻取得
from datetime import datetime
# str→dictに変換する関数
import ast

# APIエラー対策
from flask_cors import CORS

# 自作関数のパスを指定するため
import sys
# sys.path.append("../my_mysql/")
# データベース操作の自作関数
import search_man06


app = Flask(__name__)
CORS(app) # <-追加
# 文字化け対策
app.config['JSON_AS_ASCII'] = False

@app.route('/api/youtube', methods=["GET", "POST"])
def api_user_update():
    if request.method == 'POST':
        searches_keyword = request.form['searches_keyword']
        number_of_searches = request.form['number_of_searches']
        region_code = request.form['region_code']

        print('受け取った値：', searches_keyword, number_of_searches, region_code)
    else:
        print('GETメソッドに関してはサポートしていない')

    # print(type(number_of_searches))
    data = search_man06.youtube_api(searches_keyword=searches_keyword, number_of_searches=int(number_of_searches), regionCode=region_code)
    print(data)

    # data = 'aaa'
    # print(data)
    return jsonify(data)



if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 5000)
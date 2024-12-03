from flask import Flask, request, jsonify, render_template
from datetime import datetime
import pexpect
import sys
import sqlite3

app = Flask(__name__)

# データベース名を定義
DATABASE = 'book_data.db'

# データベースの初期化
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                gender TEXT,
                age INTEGER,
                email TEXT,
                phone TEXT,
                paid_plan TEXT,
                login_id TEXT,
                password TEXT,
                created_at TEXT
            )
        ''')
        conn.commit()

# アプリ起動時にデータベースを初期化
init_db()


# //-- 書籍投稿・閲覧サービスのトップページ --//
@app.route('/')
def index():
    return render_template('top_test.html')


# //-- 新規登録 --//
@app.route('/registration')
def registration():
    return render_template('registration_test.html')

@app.route("/registration2",methods=["POST"])
def registration2():     
    # フォームデータを取得
    name = request.form.get('name')
    gender = request.form.get('gender')
    age = request.form.get('age')
    email = request.form.get('male')
    phone = request.form.get('phone')
    paid_plan = request.form.get('paid')
    login_id = request.form.get('id')
    password = request.form.get('password')
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 現在時刻を取得

    # データをデータベースに挿入
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (name, gender, age, email, phone, paid_plan, login_id, password, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, gender, age, email, phone, paid_plan, login_id, password, created_at))
        conn.commit()

    return render_template("msg_test.html", title = "新規登録完了", message = "新規登録が完了しました。")
    
@app.route('/login')
def login():
    return render_template('login_test.html')


# //-- ログイン --//
@app.route('/login2', methods=['POST'])
def login_user():
    login_id = request.form.get('id')
    password = request.form.get('password')

    # データベースからユーザー情報を取得して照合
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE login_id = ? AND password = ?', (login_id, password))
        user = cursor.fetchone()

    if user:
        return render_template("user_test.html", name = user[1])
    else:
        return render_template("msg_test.html", title = "ログイン失敗", message = "ログイン失敗しました。")

# //-- 閲覧 --//
@app.route('/view')
def send():
    return render_template('view_test.html')

@app.route('/view2', methods=['POST'])
def send_transaction():
    data = request.get_json()
    sender = data.get('sender', 'cosmosjapan')
    recipient = data.get('recipient', 'juno1luesv8s490kcmatae2smccnwnscr93yllydkhf')
    amount = data.get('amount')
    passphrase = data.get('passphrase', 'shu270423')

    if not amount:
        return jsonify({"message": "送金額が指定されていません"}), 400

    # JSON形式の execute_command をエスケープして構築
    execute_command = f"'{{\"transfer\":{{\"recipient\":\"{recipient}\", \"amount\":\"{amount}\"}}}}'"

    # junodコマンド全体を構築
    contract_address = "juno17vl5kc3dkyn4yuz4hhvt25hjxpj8q3l2wa7m906nmtkdju9ccu5sq0rp8j"
    command = f"junod tx wasm execute {contract_address} {execute_command} --from {sender} --node https://rpc.testcosmos.directory:443/junotestnet --chain-id uni-6 --gas-prices 0.1ujunox --gas auto --gas-adjustment 1.3 --yes"

   # ギフトに応じたメッセージを選択
    gift_message = {
        100: "いいねしました。",
        1000: "お気に入りにしました。",
        5000: "花束を贈りました。"
    }.get(amount, "送金が成功しました。")

    try:
        # pexpectでコマンドを実行し、標準出力にログを出力
        process = pexpect.spawn(command, encoding='utf-8', timeout=60, logfile=sys.stdout)

        # パスフレーズの入力
        process.expect('Enter keyring passphrase')
        process.sendline(passphrase)

        # コマンド実行後の出力を取得
        process.expect(pexpect.EOF)
        output = process.before
        return jsonify({"message": gift_message, "output": output}), 200

    except pexpect.exceptions.TIMEOUT:
        return jsonify({"message": "エラー: コマンドの実行中にタイムアウトが発生しました"}), 500

    except pexpect.exceptions.ExceptionPexpect as e:
        return jsonify({"message": "送金に失敗しました", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#サーバーを立ち上げるコード
from flask import Flask, request, render_template

app = Flask(__name__)

# プロジェクトのトップ
@app.route('/')
def index():
    return render_template('Home.html')


# 各ゲームに移動
@app.route('/HanoiTower')
def HanoiTower():
    return render_template('HanoiTower.html')

@app.route('/LightsOut')
def LightsOut():
    return render_template('LightsOut.html')

@app.route('/MineSweeper')
def MineSweeper():
    return render_template('MineSweeper.html')

if __name__ == '__main__':
    app.run()
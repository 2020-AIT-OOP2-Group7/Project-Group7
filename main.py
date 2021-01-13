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

@app.route('/MineSweeper_title')
def MineSweeper_title():
    return render_template('MineSweeper_title.html')

@app.route('/MineSweeper_play')
def MineSweeper_play():
    return render_template('MineSweeper_play.html')

@app.route('/MineSweeper_play_normal')
def MineSweeper_play_normal():
    return render_template('MineSweeper_play_normal.html')

@app.route('/MineSweeper_play_hard')
def MineSweeper_play_hard():
    return render_template('MineSweeper_play_hard.html')

if __name__ == '__main__':
    app.run()
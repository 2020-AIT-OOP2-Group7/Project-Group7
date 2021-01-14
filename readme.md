# 役割分担

| 担当 | 名前 |
| --- | ---|
|サーバー | 加藤 |
|マインスイーパー | 福本 |
|ライツアウト | 網野 |
|ハノイの塔 | 亀田 |

# 実行手順
## 1.事前準備
- Flaskを用いてサーバーを立てているため、事前にFlaskのインストールが必要になる。

## 2.サーバー立て
- main.pyを実行し、サーバーを立ち上げる。
- chrome上で（http://127.0.0.1:5000）のリンクへ飛ぶ。

##  3.タイトル画面
- 現在３種類のゲームがある。ボタンをクリックすることで各アプリケーションへ移動することができる。

###  ハノイの塔
    現在制作途中だが、takeを押した柱の一番上の輪を外し、putを押した柱の一番上に外した輪を乗せる。ただし、自分より小さい輪の上には乗せることができない。ゴールの柱に全ての輪を移動させることができるかの手数を競う。輪の数を調整する機能も実装予定。

###  ライツアウト
    ページに移動すると、最初は難易度「EASY」マスの広さは「５x５」で問題が作成される。全てのマス目はクリックするとクリックしたマスと、その上下左右のマス目の色が黒と黄色で反転する。全てのマスの色を黄色にした場合にクリアとなる。難易度調整機能もついており、難易度「EASY」「NORMAL」「HARD」があり、上の難易度にいくほどクリアに必要な最短手数が多くなる。マス目の広さは３x３から１０x１０まで選択できる。難易度と広さを設定したのちにNEXTボタンを押すと設定の変更が適応される。またANSWERボタンを押すことでクリアに必要な最短手数の場所をピンクで示してくれる。この機能は答えと関係のない場所をクリックするとその場所は押すべき場所として認識されない不具合があるのですぐに修正する。

### マインスイーパー
    ページに移動するとまず３つの難易度から選べるページになる。EASYは１０x１０の盤面で地雷が１５個、NORMALは１６x１６の盤面で地雷が４０個、HARDは２０x２０の盤面で地雷が９９個の難易度である。任意のマスをクリックしてそのますに地雷があればゲームオーバー、地雷がなければそのマスを除く周囲８マスの中にいくつ地雷があるかを示す数字が出現して、隣接する地雷のないマスも同時に開かれる。地雷があると思ったマスにはフラグをたてて目印をつける。地雷のあるマスを開くことなく全ての地雷のないマスを開けることができればゲームクリアである。ゲームクリアまでにかかった時間を競う。



#ライブラリを使う宣言
import random
import time

#変数の初期化
a = 0
b = 0
goal = 20

#入力を求める
user = input("")

#競争開始
print("＼スタート！／")
    
#aとb どちらもゴールしていない間続ける
while (a < goal) and (b < goal) :
    print("---")
    a = a + random.randint( 1, 6 )
    b = b + random.randint( 1, 6 )
    print( "a:" + "_🌼"  * a + "___🦋" )
    print( "b:" + "_🍄"  * b + "___🐌" )
    time.sleep(3)
    #from time import sleep
    #sleep(300)

#勝者判定
if a == b:
    winner = "ab" #"🦋同着🐌！"
elif a > b :
    winner = "a"
else :
    winner = "b"

#予想は当たったかどうか
if winner == user:
    print("＼ ゴール！ ／")
    print("**********************************")
    print("************ 大当たり🎯 ************")
    print("**********************************")
else:
    print("＼ ゴール！ ／")
    print("***********************************")
    print("*********** 🪴ざんねん🪴  ***********")
    print("***********************************")

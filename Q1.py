# ユーザーから10回数字を受取り、
#「前回と同じ数を入力した回数」を出力、10回連続したらperfectと返すプログラムを作成せよ。
# 数字をもらって、判定を10回繰り返す。
pre_number = 0
seq_counter = 0
for i in range (10):
    print(f"i={i}")
    # ユーザーから数字をもらう。
    number = int(input("数字を入力してください。："))
    # 初回の挙動
    ## 数字を比較用に確保
    ## 連続回数に1を設定
    if i == 0:
        pre_number = number
        seq_counter = 1
        print("連続なし")
    # 確保した値と入力値が同じか確認
    ## 連続回数をカウント
    ### 10回目ならprefectを出力
    elif i > 0 and pre_number == number:
        seq_counter += 1
        print(f"{seq_counter}回連続")
        if seq_counter == 10:
            print("perfect!!") 
    # 確保した数字が入力値と異なる場合
    ## 連続回数をリセット
    ## 比較用の数字を更新
    elif i > 0 and pre_number != number:
        seq_counter = 1
        pre_number = number
        print("連続なし")
    print(f"seq_counter={seq_counter}")
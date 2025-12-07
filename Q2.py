### 要件 ###
# 入力したn桁の数の中に5があるか調べるプログラムを作成せよ。
###########

# ユーザーから数字を受け取る。
## 表向きは数字の入力を求める
## 裏側はリスト型で受け取る
user_number_list = list(input("数字を入力してください。"))

# 入力された数字に5がないか桁数分繰り返す。
for i in range(len(user_number_list)):
    if int(user_number_list[i]) == 5:
        print("5です！！")
    else:
        print("5じゃないです")

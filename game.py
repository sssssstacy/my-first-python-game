import random

print("🎮 歡迎來到猜數字遊戲！")
print("我已經想好一個 1 到 100 的數字")

answer = random.randint(1, 100)
guess = None

while guess != answer:
    guess = int(input("請輸入你的猜測數字："))

    if guess > answer:
        print("太大了！再試一次")
    elif guess < answer:
        print("太小了！再試一次")
    else:
        print("🎉 恭喜你猜對了！")
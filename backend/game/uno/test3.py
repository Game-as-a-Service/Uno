
from time import sleep
from model.player import Player

# instance 實體 物件 class 類別
p = Player()

# result = p.do_add_plus3(-1, 2) # 跳出
# print(result)

# A(python) >> B(test3.py) >>  efeffwjnowekvnwlbnw >>> C(do_add_plus3)

try:
    result = p.do_add_plus3(-1, 2) # 跳出
    print(result)
except Exception as e:
    print(e) # 補獲 印出錯誤訊息
    # 補救流程

while True:
    print("loop")
    sleep(1)

print("end")
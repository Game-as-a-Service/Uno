
# 資料夾結構

## src [Production Code 程式碼]

* model         >> CA 中的 Entities
* usecase       >> CA 中的 Use cases
* web           >> CA 中的 Adapter/Controllers + Presenters
* repository    >> CA 中的 Adapter/Gateways

## features [BDD 測試資料夾]

* Gherkin
* https://ithelp.ithome.com.tw/articles/10226615
* Behave

## tests [TDD 測試資料夾]

* pytest

# 環境建置

## 安裝 poetry
https://blog.kyomind.tw/python-poetry/

## 啟動 poetry
```shell
# Activate the virtual env.
poetry shell

# Install dependencies into the virtual env.
poetry install

# Run the Python server
./start.sh
```

## 啟動 自建虛擬環境
```shell
python -m venv venv

# mac
source ./venv/bin/active
# windows
.\venv\Scripts\activate.bat 

pip install -r requirement.txt

python app.py
```

網址
```
# 查詢遊戲
http://localhost:5000/game/get_all?game_id=1

# 建立遊戲
http://localhost:5000/game/create_game?game_id=1

# 玩家加入遊戲
http://localhost:5000/game/join_game?game_id=1&player_id=101
http://localhost:5000/game/join_game?game_id=1&player_id=102

# 開始遊戲
http://localhost:5000/game/start_game?game_id=1&player_id=101

# 出牌
http://localhost:5000/game/play_card?game_id=1&player_id=101&index=0

```

## 測試
```shell
# Unit Test 全部檔案
pytest

# Unit Test 單一檔案
pytest -q tests/model/test_game.py 

# Behavior Test 全部檔案
behave

# Behavior Test 單一檔案
behave -i features/game.feature
```




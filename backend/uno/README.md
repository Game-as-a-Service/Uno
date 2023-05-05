
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

## 啟動
```shell
# Activate the virtual env.
poetry shell

# Install dependencies into the virtual env.
poetry install

# Run the Python server
./start.sh
```

## 測試
```shell
# unit test 全部
pytest

# unit test 單一
pytest -q tests/model/test_game.py 


```



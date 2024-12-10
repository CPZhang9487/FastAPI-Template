# FastAPI Template

建立一個簡易的 [FastAPI](https://fastapi.tiangolo.com/) 專案模板以供複製，減少初期的操作配置。

## 專案建置

1. 下載此專案
    ``` bash
    cd /path/to/your/directory
    git clone https://github.com/CPZhang9487/FastAPI-Template.git
    ```
2. 建立 python 虛擬環境
    ``` bash
    python -m venv .venv            # Windows
    python3 -m venv .venv           # Linux
    ```
    - 虛擬環境是為了隔離電腦系統與專案的 python 環境，即可避免依賴庫的版本衝突等問題。
3. 安裝 python 依賴庫
    ``` bash
    # 進入虛擬環境
    .venv\Scripts\activate          # Windows
    source .venv/bin/activate       # Linux

    # 安裝依賴庫
    pip install -r requirements.txt
    ```

## 專案運行

1. 進入虛擬環境
    ``` bash
    .venv\Scripts\activate          # Windows
    source .venv/bin/activate       # Linux
    ```
2. 伺服器運行
    ``` bash
    python app                      # 使用預設 port 80
    ```
    或者自訂參數
    ``` bash
    uvicorn app:app --port 9487
    ```

## 開發日誌

[20241210](dev_notes/20241210.md)

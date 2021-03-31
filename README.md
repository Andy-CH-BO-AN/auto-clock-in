# 說明書
## 步驟一
### 下載python
https://www.python.org/downloads/
### 下載git
https://git-scm.com/downloads
### 下載Chrome
https://www.google.com/intl/zh-TW/chrome/?brand=FKPE&gclid=CjwKCAjw6fCCBhBNEiwAem5SO1H__36dYPSUqPo5RWYWyQe4eM_PMXI1QJGSmtA5y3zBnz3I1vgBLBoCGWwQAvD_BwE&gclsrc=aw.ds
## 步驟二
![img.png](img.png)
### 安裝python
記得勾選Add Python to Path
### 安裝git
### 安裝chrome
## 步驟三
### 開啟命令提示字元(cmd)
### 輸入命令
git clone https://github.com/Andy-CH-BO-AN/auto-clock-in.git
![img_1.png](img_1.png)
## 步驟四
### 進入剛下載的資料夾
### 在資料夾的路徑輸入cmd，按Enter
### 開啟命令提示字元(cmd)
![img_2.png](img_2.png)
### 輸入命令
pip install -r requirements.txt
### 待安裝完畢
## 步驟五
### 進入該資料夾
### 編輯config.json，可以選擇記事本編輯，輸入自己的帳密。
![img_20.png](img_20.png)
![img_21.png](img_21.png)
### 在資料夾的路徑輸入cmd
![img_3.png](img_3.png)
### 輸入測試命令
python main.py 2
### 確認是否有正確執行，成功即可進入下一步驟，失敗可以扣github星星QAQ
## 步驟六
### 更改bat檔
![img_4.png](img_4.png)
### 對clockin.bat點擊右鍵，選擇編輯
![img_5.png](img_5.png)
### 複製專案資料夾路徑
![img_6.png](img_6.png)
### 至cd後面貼上，按ctrl + s(儲存檔案)
### 成功後可以點擊bat檔測試是否可成功打卡
### 對clockout.bat重複做一次步驟六
## 步驟七
### 建立排程
### 按windows鍵
### 在 Windows系統管理工具 中有一個 工作排程器
![img_7.png](img_7.png)
### 點開後在右邊的 動作 有一個建立工作
![img_8.png](img_8.png)
### 輸入名稱
![img_9.png](img_9.png)
### 點擊觸發程序
![img_10.png](img_10.png)
### 點擊新增並且設定上班或下班排程
![img_11.png](img_11.png)
![img_12.png](img_12.png)
### 確定後點擊動作
![img_13.png](img_13.png)
### 點擊新增並且設定動作
![img_14.png](img_14.png)
### 點擊瀏覽，若是設定上班排程選擇clockin.bat
### 下班排程選擇clockout.bat
![img_15.png](img_15.png)
### 選擇確定後再選擇確定
![img_16.png](img_16.png)
### 點擊左上角的工作排程程式庫
![img_17.png](img_17.png)
### 可以看到排程已經設定
![img_18.png](img_18.png)
### 也可以點擊右鍵手動執行
![img_19.png](img_19.png)
### 記得電腦要保持開機
### 請特休的時候調整一下排程，祝龍體安康。

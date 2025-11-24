## ngrok起動

### 目的
ngrokを起動しTunnelURLを生成する。<br>
生成に成功した場合は、home_database(スプレッドシート)に連携およびLINE通知をおこなう。

### 処理概要
* home_databaseのエラー連携フラグ(ngrok_url_access_error_send_flag)が ”FALSE（正常稼働中）” の場合は、処理を中断する。
* ngrok起動結果(TunnelURL、エラーコードなど)は、起動時のログを参照し情報を取得する。
* 生成したTunnelURLは、home_databaseのngrok_url(TunnelURL)およびLINEに連携する。

### タスクスケジューラ
1時間に1度、00分に起動する<br>
※ 必ずngrok停止と同時に使用すること

### 外部連携
[home_database](https://docs.google.com/spreadsheets/d/1ToIMcrIiGCa_lNIbxieLwUWmnyGWFp_fnOpmU8mkOTc/edit?gid=0#gid=0)

#### 概要
5分置きにngrok_url(TunnelURL)の接続確認を行う。

##### エラー連携フラグ(ngrok_url_access_error_send_flag)が「FALSE」 ＆ 接続エラーを検知した場合
エラー連携フラグ(ngrok_url_access_error_send_flag)を ”TRUE” に設定し、LINEにエラー通知を送信

##### エラー連携フラグ(ngrok_url_access_error_send_flag)が「TRUE」 ＆ 接続成功を検知した場合
エラー連携フラグ(ngrok_url_access_error_send_flag)を ”FALSE” に設定し、LINEに接続復旧通知を送信

### 使用するツール・アプリケーション
ngrok.exe

### ライブラリ
``` cmd
pip install gspread
pip install oauth2client
pip install line-bot-sdk
```


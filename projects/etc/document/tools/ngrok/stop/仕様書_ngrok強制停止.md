## ngrok強制停止

### 目的
接続エラーになり、使用不可になったTunnelURLを停止状態にする。

### 処理概要
* home_databaseのエラー連携フラグ(ngrok_url_access_error_send_flag)が ”FALSE（正常稼働中）” の場合は、処理を中断する。
* ngrokを停止状態にする。

### タスクスケジューラ
1時間に1度、58分に起動する<br>
※ 必ずngrok起動と同時に使用すること

### 外部連携
なし

### 使用するツール・アプリケーション
ngrok.exe

### ライブラリ
``` cmd
pip install gspread
pip install oauth2client
```


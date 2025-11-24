@echo off
:: ==============================================
:: Python パッケージ インストールスクリプト
:: ==============================================

:: pip最新化
python -m pip install --upgrade pip

:: ------------------------
:: envファイル読込
:: ------------------------
pip install python-dotenv

:: ------------------------
:: Docker
:: ------------------------
pip install docker

:: ------------------------
:: Google API / スプレッドシート
:: ------------------------
pip install gspread==6.2.1
pip install google-auth==2.41.1
pip install google-auth-oauthlib==1.2.3
pip install cachetools==6.2.2
pip install oauth2client==4.1.3
pip install oauthlib==3.3.1
pip install requests-oauthlib==2.0.0

:: ------------------------
:: 圧縮 / ファイル操作
:: ------------------------
pip install pyminizip==0.2.6
pip install filelock==3.8.0
pip install configparser==7.1.0

:: ------------------------
:: LINE
:: ------------------------
pip install line-bot-sdk==3.21.0

:: ------------------------
:: 仮想環境 / パッケージ管理
:: ------------------------
pip install pipenv==2022.10.12
pip install virtualenv==20.16.5
pip install virtualenv-clone==0.5.7
pip install wheel==0.44.0
pip install setuptools==75.2.0
pip install distlib==0.3.6

echo.
echo ==== インストール完了 ====
pause

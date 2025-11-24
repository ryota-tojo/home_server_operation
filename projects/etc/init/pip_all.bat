@echo off

:: ================================
:: 1. 非同期処理 / HTTP / ネットワーク
:: ================================
pip install aenum==3.1.16
pip install aiohappyeyeballs==2.6.1
pip install aiohttp==3.13.2
pip install aiosignal==1.4.0
pip install async-generator==1.10
pip install async-timeout==5.0.1
pip install frozenlist==1.8.0
pip install h11==0.13.0
pip install httplib2==0.31.0
pip install multidict==6.7.0
pip install yarl==1.22.0
pip install wsproto==1.0.0
pip install idna==3.3
pip install chardet==5.0.0
pip install charset-normalizer==3.1.0
pip install certifi==2021.10.8
pip install requests==2.32.5
pip install urllib3==2.5.0

:: ================================
:: 2. Google API / スプレッドシート
:: ================================
pip install gspread==6.2.1
pip install google-auth==2.41.1
pip install google-auth-oauthlib==1.2.3
pip install cachetools==6.2.2
pip install oauth2client==4.1.3
pip install oauthlib==3.3.1
pip install requests-oauthlib==2.0.0

:: ================================
:: 3. データベース
:: ================================
pip install mysqlclient==2.1.1
pip install psycopg2==2.9.5
pip install SQLAlchemy==2.0.13

:: ================================
:: 4. 暗号化 / セキュリティ
:: ================================
pip install cryptocode==0.1
pip install cryptography==36.0.1
pip install pycryptodomex==3.17
pip install pyOpenSSL==22.0.0
pip install rsa==4.9.1
pip install pyasn1==0.6.1
pip install pyasn1_modules==0.4.2
pip install cffi==1.15.0
pip install pycparser==2.21

:: ================================
:: 5. 画像 / 動画 / PDF
:: ================================
pip install Pillow==9.1.0
pip install pillow-heif==0.12.0
pip install pyheif-iplweb==0.7.1.dev1176
pip install opencv-contrib-python==4.5.5.64
pip install pdf2image==1.16.3
pip install ffmpeg-python==0.2.0

:: ================================
:: 6. OCR
:: ================================
pip install pyocr==0.8.2

:: ================================
:: 7. 自動操作 / GUI / WindowsAPI
:: ================================
pip install pywin32==304
pip install pywin32-ctypes==0.2.0
pip install pyperclip==1.8.2
pip install tkinterdnd2==0.3.0

:: ================================
:: 8. データ処理 / 数値計算
:: ================================
pip install numpy==1.22.2
pip install pandas==1.4.1
pip install python-dateutil==2.8.2
pip install pytz==2021.3
pip install tzdata==2022.2
pip install annotated-types==0.7.0
pip install attrs==21.4.0
pip install typing_extensions==4.15.0
pip install wrapt==2.0.1

:: ================================
:: 9. 圧縮 / ファイル操作
:: ================================
pip install pyminizip==0.2.6
pip install filelock==3.8.0
pip install configparser==7.1.0

:: ================================
:: 10. 端末 / 開発者ユーティリティ
:: ================================
pip install colorama==0.4.5
pip install crayons==0.4.0
pip install tqdm==4.64.0

:: ================================
:: 11. LINE / Slack
:: ================================
pip install line-bot-sdk==3.21.0
pip install slackweb==1.0.5

:: ================================
:: 12. Selenium / ブラウザ自動操作
:: ================================
pip install selenium==4.5.0
pip install webdriver-manager==3.5.3

:: ================================
:: 13. PyInstaller / exe化
:: ================================
pip install pyinstaller==5.5
pip install pyinstaller-hooks-contrib==2022.10
pip install altgraph==0.17.3
pip install pefile==2022.5.30

:: ================================
:: 14. 仮想環境 / パッケージ管理
:: ================================
pip install pip==24.2
pip install pipenv==2022.10.12
pip install virtualenv==20.16.5
pip install virtualenv-clone==0.5.7
pip install wheel==0.44.0
pip install setuptools==75.2.0
pip install distlib==0.3.6

:: ================================
:: 15. 金融 / テクニカル分析
:: ================================
pip install TA-Lib==0.4.24

:: ================================
:: 追加
:: ================================
pip install docker
pip install line-bot-sdk
pip install python-dotenv

echo.
echo ==== インストール完了 ====
pause

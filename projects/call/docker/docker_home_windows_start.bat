:: バッチファイル名（拡張子なし）
set BAT_NAME=%~n0

:: タイムスタンプ生成（YYYYMMDD）
set NOW=%date:~0,4%%date:~5,2%%date:~8,2%

:: プロジェクトルートへcd
call cd.bat

python -m projects.src.tools.docker.home.windows.start.main >> ./projects/call/_log/%BAT_NAME%_%NOW%.log 2>&1
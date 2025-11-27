@echo off
chcp 65001 > nul
title 맨점프 깃허브 원터치 업로드기

echo ==============================================
echo      [ 맨점프 프로젝트 깃허브 업로드 ]
echo ==============================================
echo.
echo 현재 폴더의 모든 변경사항을 감지합니다...
git status -s
echo.
echo ----------------------------------------------
set /p CommitMsg="▶ 작업 내용 요약(커밋 메시지)을 입력하세요: "

:: 메시지가 비어있으면 경고하고 종료
if "%CommitMsg%"=="" goto EmptyError

echo.
echo [1/3] 파일 담는 중 (git add)...
git add .
IF %ERRORLEVEL% NEQ 0 goto ErrorHandler

echo.
echo [2/3] 커밋 기록 중 (git commit)...
git commit -m "%CommitMsg%"
IF %ERRORLEVEL% NEQ 0 goto ErrorHandler

echo.
echo [3/3] 깃허브로 발사! (git push)...
git push origin main
IF %ERRORLEVEL% NEQ 0 goto ErrorHandler

echo.
echo ==============================================
echo        🎉 업로드 성공! 고생하셨습니다. 🎉
echo ==============================================
pause
exit

:EmptyError
echo.
echo [오류] 메시지를 입력하지 않았습니다! 엔터를 누르면 종료합니다.
pause
exit

:ErrorHandler
echo.
echo ==============================================
echo [오류 발생] 위 로그를 확인해주세요. (인터넷 연결 등)
echo ==============================================
pause
exit
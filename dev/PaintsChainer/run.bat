@echo off

REM You maybe need to edit following two line

SET PaintsChainer_PATH=C:\Users\SongJungwoo\Documents\GitHub\co-creation\dev\PaintsChainer
SET Anaconda3_PATH=C:\Users\SongJungwoo\Anaconda3

SET path=%~dp0;%~dp0bin;%path%

call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" amd64

SET LIB=%~dp0lib;%~dp0lib\x64;%LIB%
SET INCLUDE=%~dp0include;%INCLUDE%
SET LIBPATH=%~dp0lib;%~dp0lib\x64;%LIBPATH%

cd /d %PaintsChainer_PATH%

start %Anaconda3_PATH%\Scripts\activate.bat
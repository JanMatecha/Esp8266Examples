rem SET PORT=COM4
FOR /F %%G IN (COM.txt) DO set  PORT=%%G

SET JMENO=filesDownloaded.txt

ampy -p %PORT% ls > %JMENO%

FOR /f "delims=/" %%A IN (%JMENO%) DO (
ampy -p %PORT% get %%A %%A )
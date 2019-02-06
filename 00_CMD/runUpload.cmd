rem SET PORT=COM4
FOR /F %%G IN (COM.txt) DO set  PORT=%%G

SET JMENO=filesUploaded.txt

dir /b *.py > %JMENO%


FOR /f "delims=/" %%A IN (%JMENO%) DO (
ampy -p %PORT% put %%A %%A )
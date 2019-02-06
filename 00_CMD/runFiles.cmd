rem SET PORT=COM4
FOR /F %%G IN (COM.txt) DO set  PORT=%%G

SET JMENO=files.txt

ampy -p %PORT% ls > %JMENO%

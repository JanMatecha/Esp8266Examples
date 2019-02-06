rem SET PORT=COM4
FOR /F %%G IN (COM.txt) DO set  PORT=%%G
putty -serial %PORT% -sercfg 115200,8,n,1,N

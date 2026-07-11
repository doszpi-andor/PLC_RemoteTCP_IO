@ECHO OFF
cd c:\PLC_RemoteTCP_IO
git pull
start c:\PLC_RemoteTCP_IO\.venv\Scripts\pythonw.exe remote_io.py
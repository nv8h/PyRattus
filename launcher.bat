@mkdir .\base\cache
@mkdir .\base\log

@.\base\system\python.exe .\bin\start.py main %*

@rmdir .\base\cache
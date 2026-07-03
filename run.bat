@echo off
REM Change directory to your project folder
cd /d "C:\Users\pooja\PycharmProjects\HybridFramework"
call C:\Users\Pooja\AppData\Local\Programs\Python\Python311\python.exe


REM Run pytest with your options
python -m pytest -s -v -m "sanity" --html=Reports\automation_report.html TestCases\ --browser edge

REM Keep the window open so you can see results/errors
pause



REM pytest -s -v -m "sanity" --html=Reports\automation_report.html TestCases\ --browser edge
REM pytest -s -v -m "regression" --html=Reports\automation_report.html TestCases\ --browser chrome
REM pytest -s -v -m "smoke" --html=Reports\automation_report.html TestCases\ --browser edge
REM pytest -s -v -m "sanity" --html=Reports\automation_report.html TestCases\ --browser chrome



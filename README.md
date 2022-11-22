# doomsday
just a quick python script for practicing doomsday algorithm

how it works:
1. random date is generated in DD/MM/YYYY format and printed
2. user is asked to input day of week (sunday, ..., saturday), capitalization of letters does not matter
3. code checks whether user is correct
4. another date is generated

for compiling into a windows executable use the following method:
1. make sure you have python and pip installed
2. open cmd and run "pip install pyinstaller"
3. navigate to where you saved "doomsday.py"
4. run "pyinstaller --onefile doomsday.py"
5. navigate into /dist/ and look for "doomsday.exe"
6. hf

# InterviewTest

This was completed in Python. You will need Python v3.8.+ or newer to run.

To begin be sure to extract or clone all files into the same folder.

For the first test use test1.py.
- In command line navigate to the folder holding test1.py and input test cases as follows 
- python test1.py FB:12,PLTR:5000 
- python test1.py BABA:1,TSLA:5,WISH:1200

For the second test use test2.py
- In command line navigate to the folder holding test2.py and input test cases as follows 
- python test2.py 7,1,5,3,6,4
- python test2.py 7,6,4,3,1

Custom test cases may also be used. 

for Test 1 there are 5 tickers that can be used such as:
  BABA, PLTR, FB, TSLA, WISH
  These can be found in stocks.json
  
# TROUBLESHOOTING TIPS!

if you encounter the error:
 File "test1.py", line 25
    print(f"Error: Stock with ticker {ticker} was not found")

The solve for this is to use python3 instead of python when executing the command in the CLI 
 
Instead of \
python test1.py FB:12,BABA:5000 \
do \
python3 test1.py FB:12,BABA:5000

This is because I used F-string. python 2 doesnt support that. Using Python3 forces the use of python v3+

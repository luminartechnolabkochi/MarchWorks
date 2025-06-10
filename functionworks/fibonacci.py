"""
READ limit

SET prev=0

set current=1

loop: till i reaches to limit
        CALCULATE next=prev+current
        DISPLAY next        
        SET prev=current
        SET current=next
"""

limit=int(input("enter limit"))

prev=0

current=1

for i in range(1,limit+1):

    next=prev+current

    print(next)

    prev=current

    current=next








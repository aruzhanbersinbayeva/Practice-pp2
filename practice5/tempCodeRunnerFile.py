import re
s=r"ab*"
test=["ab","abb","abbb","a","b","ac","abc"]
for i in test:
    if re.full.match(s,i):
        print(f"'{s}' Matches")
    else:
        print(f"'{s}' Does not match")
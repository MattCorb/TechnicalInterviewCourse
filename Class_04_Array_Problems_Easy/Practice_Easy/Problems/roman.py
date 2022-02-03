def romanToInt(s: str) -> int:
    total = 0
    
    for i in range(0,len(s)):
        hold = len(s)
        if hold >= 2:
            if  s[0] == 'I' and s[1] == 'V':
                    total += 4 
                    s = s[2::]
                    continue   
            elif  s[0] == 'I' and s[1] == 'X':
                    total += 9 
                    s = s[2::]
                    continue
            elif s[0] == 'X' and s[1] == 'L':
                    total += 40
                    s= s[2::]
                    continue
            elif s[0] == 'X' and s[1] == 'C':
                    total += 90
                    s = s[2::]
                    continue
            elif s[0] == 'C' and s[1] == 'D':
                    total += 400
                    s = s[2::]
                    continue
            elif s[0] == 'C' and s[1] == 'M':
                    total += 900
                    s = s[2::]
                    continue
        if s == "":
            break
        if s[0] == 'I':
                    total += 1
                    s = s[1::]
        elif s[0] == 'V':
                    total += 5
                    s = s[1::]
        elif s[0] == 'X':
                    total += 10
                    s = s[1::]
        elif s[0] == 'L':
                    total += 50
                    s = s[1::]
        elif s[0] == 'C':
                    total += 100
                    s = s[1::]
        elif s[0] == 'D':
                    total += 500
                    s = s[1::]
        elif s[0] == 'M':
                    total += 1000
                    s = s[1::]
    return total


print(romanToInt('DCXXI'))


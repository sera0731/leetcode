def repeatedString(s, n):

    if n == 0 or not s :
        return 0

    freq = 0

    for ch in s :
        if ch == 'a' :
            freq += 1
    
    ans = (n//len(s))*freq
    remain = n%len(s)

    for i in range(remain) :
        if s[i] == 'a' :
            ans += 1

    return ans

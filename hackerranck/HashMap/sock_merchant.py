def sockMerchant(n, ar):

    ans = 0
    hm = {}

    for sock in ar :
        hm[sock] = hm.get(sock, 0) + 1

    for i in hm :
        ans += hm[i] // 2

    return ans

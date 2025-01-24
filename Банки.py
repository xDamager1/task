def max_money(banks):
    n = len(banks)
    if n == 0:
        return (0, [])
    if n == 1:
        return (banks[0][1], [(banks[0][0], 1)])

    dp = [0] * n
    dp[0] = banks[0][1]
    dp[1] = max(banks[0][1], banks[1][1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + banks[i][1])

    result_banks = []
    i = n - 1
    while i >= 0:
        if dp[i] == (dp[i - 1] if i > 0 else 0):
            i -= 1
        else:
            result_banks.append(banks[i])
            i -= 2

    result_banks.reverse()
    total_money = dp[n - 1]
    return (total_money, [(name, idx + 1) for idx, (name, _) in enumerate(result_banks)])


num_banks = int(input())
banks = [tuple(input().strip().split() for _ in range(num_banks))]
banks = [(name, int(a)) for name, a in banks[0]]

print(max_money(banks))
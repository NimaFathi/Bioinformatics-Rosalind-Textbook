def dpChange(money, coins):
    ans = []
    for i in range(money + 1):
        ans.append(0)
    for i in range(1, money + 1):
        ans[i] = 2 ** 50
        for j in coins:
            if i >= j:
                if ans[i - j] + 1 < ans[i]:
                    ans[i] = ans[i - j] + 1

    return ans[money]

if __name__ == '__main__':
    money = int(input())
    coins_str = input()
    coins_str = coins_str.split(",")
    coins = [int(i) for i in coins_str]
    print(dpChange(money, coins))
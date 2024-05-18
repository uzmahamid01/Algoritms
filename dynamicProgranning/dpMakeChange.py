def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(change+1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
                
        minCoins[cents] = coinCount
    return minCoins[change]

def main():
    coinValueList = [1, 5, 10, 21, 25]
    change = 63
    minCoins = [0] * (change + 1)
    result = dpMakeChange(coinValueList, change, minCoins)
    print("Minimum number of coins needed to make change for", change, "cents:", result)

if __name__ == "__main__":
    main()
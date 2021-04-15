def merge_tweets(feed, m, tweets, n):
    p1 = m - 1
    p2 = n - 1

    for p in range(n + m - 1, -1, -1):
        if p2 < 0:
            break
        if p1 >= 0 and feed[p1] > tweets[p2]:
            feed[p] = feed[p1]
            p1 -= 1
        else:
            feed[p] = tweets[p2]
            p2 -= 1

# Driver code
feed = [23, 33, 35, 41, 44, 47, 56, 91, 105, 0, 0, 0, 0, 0, 0]
m = 9
tweets = [32, 49, 50, 51, 61, 99]
n = 6
merge_tweets(feed, m, tweets, n)
print(feed)
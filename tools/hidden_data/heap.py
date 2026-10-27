HIDDEN = {
    61: ([
        ("`0 <= len(nums) <= 1000`, and the stream always has at least `k` values when `add` is called",
         "`0 <= len(nums) <= 10^5`, and the stream always has at least `k` values when `add` is called"),
        ("At most `1000` calls to `add`.", "At most `10^5` calls to `add`."),
    ], '''
def generate(rng):
    cases = []
    for k in (3, 1000):
        nums = [rng.randint(-1000, 1000) for _ in range(50000)]
        ops, params = ["KthLargest"], [[k, nums]]
        for _ in range(50000):
            ops.append("add")
            params.append([rng.randint(-1000, 1000)])
        cases.append([ops, params])
    return cases
'''),
    62: ([
        ("`1 <= len(stones) <= 1000`", "`1 <= len(stones) <= 10^5`"),
        ("`1 <= stones[i] <= 1000`", "`1 <= stones[i] <= 10^9`"),
    ], '''
def generate(rng):
    n = 100000
    return [
        [[rng.randint(1, 10**9) for _ in range(n)]],
        [[rng.randint(10**8, 10**9) for _ in range(n)]],
        [[rng.randint(1, 1000) for _ in range(n)]],
        [[1000] * n],
    ]
'''),
    67: ([("At most `10000` calls are made.", "At most `10^5` calls are made.")], '''
def generate(rng):
    ops, params = ["MedianFinder"], [[]]
    for _ in range(50000):
        ops += ["addNum", "findMedian"]
        params += [[rng.randint(-100000, 100000)], []]
    ops.pop()
    params.pop()
    ascending = ["MedianFinder"]
    asc_params = [[]]
    for i in range(49999):
        ascending += ["addNum", "findMedian"]
        asc_params += [[i - 25000], []]
    return [[ops, params], [ascending, asc_params]]
'''),
    66: ([
        ("`0 <= tweetId <= 10^4`, tweet ids are unique", "`0 <= tweetId <= 10^5`, tweet ids are unique"),
        ("At most `10000` calls are made.", "At most `10^5` calls are made."),
    ], '''
def generate(rng):
    def celebrity():
        ops, params = ["Twitter"], [[]]
        for user in range(1, 300):
            ops.append("follow")
            params.append([user, 500])
            for other in rng.sample(range(1, 300), 5):
                if other != user:
                    ops.append("follow")
                    params.append([user, other])
        tweet = 0
        for i in range(42000):
            ops.append("postTweet")
            params.append([500 if i % 21 else rng.randint(1, 299), tweet])
            tweet += 1
        for _ in range(30000):
            ops.append("getNewsFeed")
            params.append([rng.randint(1, 299)])
        return [ops, params]

    def sparse():
        ops, params = ["Twitter", "follow"], [[], [1, 2]]
        tweet = 0
        for _ in range(10):
            ops.append("postTweet")
            params.append([2, tweet])
            tweet += 1
        for _ in range(40000):
            ops.append("postTweet")
            params.append([rng.randint(3, 500), tweet])
            tweet += 1
        for _ in range(20000):
            ops.append("getNewsFeed")
            params.append([1])
        return [ops, params]

    def mixed():
        ops, params = ["Twitter"], [[]]
        tweet = 0
        for _ in range(99999):
            kind = rng.choices(["postTweet", "getNewsFeed", "follow", "unfollow"], [40, 40, 12, 8])[0]
            user = rng.randint(1, 500)
            if kind == "postTweet":
                params.append([user, tweet])
                tweet += 1
            elif kind == "getNewsFeed":
                params.append([user])
            else:
                other = rng.randint(1, 500)
                if other == user:
                    other = user % 500 + 1
                params.append([user, other])
            ops.append(kind)
        return [ops, params]

    return [celebrity(), sparse(), mixed()]
'''),
}

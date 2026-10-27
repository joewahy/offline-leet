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

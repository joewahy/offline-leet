# 66. Design Twitter (Medium)

Design a simplified Twitter. Users post tweets, follow and unfollow each other, and see a news feed.

Implement `Twitter`:

- `Twitter()` creates an empty system.
- `postTweet(userId, tweetId)` makes `userId` post a tweet with the unique id `tweetId`.
- `getNewsFeed(userId)` returns the ids of the 10 most recent tweets in the user's feed, most recent first. The feed contains the user's own tweets and the tweets of everyone they follow.
- `follow(followerId, followeeId)` makes `followerId` start following `followeeId`.
- `unfollow(followerId, followeeId)` makes `followerId` stop following `followeeId`.

## Examples

```
postTweet(1, 5)
getNewsFeed(1)   -> [5]
follow(1, 2)
postTweet(2, 6)
getNewsFeed(1)   -> [6, 5]
unfollow(1, 2)
getNewsFeed(1)   -> [5]
```

## Constraints

- `1 <= userId, followerId, followeeId <= 500`
- `0 <= tweetId <= 10^4`, tweet ids are unique
- `followerId != followeeId`
- At most `10000` calls are made.

## Hints

- Give every tweet an increasing timestamp. For the feed, merge each followed user's latest tweets with a heap.

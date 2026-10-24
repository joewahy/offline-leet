### Approach

Store each user's tweets with a global timestamp, and each user's followees in a set. To build a feed, take the last 10 tweets of the user and each followee, since no older tweet can make the top 10, and pick the 10 newest with `heapq.nlargest`.

`postTweet`, `follow` and `unfollow` are constant time.

### Complexity

- Time: O(1) for post, follow and unfollow. A feed is O(f log 10), about O(f), where `f` is the number of followees.
- Space: O(tweets + follows).

### Watch out

A user's own tweets are included in their feed, so add the user to the set of people before merging.

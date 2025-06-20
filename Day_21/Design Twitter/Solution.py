class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_tweets = defaultdict(list)
        self.user_following = defaultdict(set)
        self.tweet_time = defaultdict(int)  # id => timestamp
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.time += 1
        self.user_tweets[userId].append(tweetId)
        self.tweet_time[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        following = self.user_following[userId]
        users = set(following)
        users.add(userId)  # should see my own tweets too
        tweets = [self.user_tweets[u][::-1][:10] for u in users]  # Get the 10 most recent tweets
        '''
        unconventional way to flatten a list of lists into a single list:
            lists = [[1, 2, 3], [4, 5], [6]]
            flattened = sum(lists, [])
            print(flattened)  # Output: [1, 2, 3, 4, 5, 6]

        or, another way getting flattened tweets:
            flattened_tweets = [tweet for each_user_tweets in tweets for tweet in each_user_tweets]
        '''
        tweets = sum(tweets, [])
        return nlargest(10, tweets, key=lambda tweet: self.tweet_time[tweet])

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        following = self.user_following[followerId]
        if followeeId in following:
            following.remove(followeeId)
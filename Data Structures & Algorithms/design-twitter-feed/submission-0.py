from collections import deque

class Twitter:

    def __init__(self):
        self.dicoTweet = {}
        self.listTweet = deque()
        self.dicoFollow = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.dicoTweet:
            self.dicoTweet[userId].append(tweetId)
        else:
            self.dicoTweet[userId] = [tweetId]
        self.listTweet.appendleft((userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> list[int]:
        listTweet = []
        compte = 10
        pos = 0
        followedUsers = self.dicoFollow.get(userId, set()) | {userId}
        while compte > 0 and pos < len(self.listTweet):
            user, tweet = self.listTweet[pos]
            if user in followedUsers:
                listTweet.append(tweet)
                compte -= 1
            pos += 1
        return listTweet
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.dicoFollow:
            self.dicoFollow[followerId].add(followeeId)
        else:
            self.dicoFollow[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.dicoFollow:
            self.dicoFollow[followerId].discard(followeeId)
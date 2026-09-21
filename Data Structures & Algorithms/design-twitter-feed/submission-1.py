import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time=0

        self.tweets=defaultdict(list)

        self.following=defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        users=self.following[userId] | {userId}
        heap=[]

        for uid in users:
            if self.tweets[uid]:
                idx=len(self.tweets[uid])-1
                timestamp, tweetId=self.tweets[uid][idx]

                heapq.heappush(heap,(-timestamp,tweetId,uid,idx))
        result=[]
        while heap and len(result)<10:
            neg_time,tweetId,uid,idx=heapq.heappop(heap)
            result.append(tweetId)
            idx-=1

            if idx>=0:
                timestamp, tweetId = self.tweets[uid][idx]
                heapq.heappush(heap,(-timestamp,tweetId,uid,idx))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

def __init__(self):
    self.postStack = []
    self.following = {} # follower ID : list/set following
    self.userPosts = {} # user ID : list/set postIDs
    self.postUser = {} # postID : userID

def postTweet(self, userId: int, tweetId: int) -> None:
    self.postStack.append(tweetId)
    if userId not in self.userPosts:
        self.userPosts[userId] = set()
    self.userPosts[userId].add(tweetId)
    self.postUser[tweetId] = userId

def getNewsFeed(self, userId: int) -> List[int]:
    following = set() # a user "privately" follows themselves
    if userId in self.userPosts: 
        following.add(userId)
    if userId in self.following:
        following = following.union(self.following[userId])

    if following: # if the user has posted or if one of their followers has posted
        newsFeed = []
        postIDX = 0
        while postIDX < len(self.postStack) and len(newsFeed) < 10:
            postId = self.postStack[-1 - postIDX]
            if self.postUser[postId] in following:
                newsFeed.append(postId)
            postIDX += 1
        return newsFeed
    return []

def follow(self, followerId: int, followeeId: int) -> None:
    if not followerId in self.following:
        self.following[followerId] = set()
    self.following[followerId].add(followeeId)

def unfollow(self, followerId: int, followeeId: int) -> None:
    if followerId in self.following and followeeId in self.following[followerId]:
        self.following[followerId].remove(followeeId)

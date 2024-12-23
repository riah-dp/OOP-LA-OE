print("Name: Moriah De Pedro")
print("=== OE #3 ===\n")

class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def login(self):
        print(f"Logging in as {self.username}")
    
    def post(self):
        print("Posting a new post")

class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, followers):
        super().__init__(username, password)
        self.followers = followers
    def share_story(self):
        print("Sharing a new story")

class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, tweets):
        super().__init__(username, password)
        self.tweets = tweets
    
    def tweet(self):
        print("Tweeting a new message")
# Create instances
insta = InstagramAccount("insta_user", "password123", 1000)
twitter = TwitterAccount("twitter_user", "password456", 5000)
# Use the methods
insta.login()
insta.post()
insta.share_story()
twitter.login()
twitter.post()
twitter.tweet()
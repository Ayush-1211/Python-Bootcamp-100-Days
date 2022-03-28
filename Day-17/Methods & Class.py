class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("1", "Ayush")
user_2 = User("2", "Anand")

user_1.follow(user_2)

print("User-1 Followers: ", user_1.followers)
print("User-1 Following: ", user_1.following)
print("User-2 Followers: ", user_2.followers)
print("User-2 Following: ", user_2.following)
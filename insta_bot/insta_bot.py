from instabot import Bot

bot = Bot()
bot.login(username="", password="")

######  upload a picture #######
bot.upload_photo("image.jpg", caption="biscuit eating baby")

######  follow someone #######
bot.follow("Enter-user-name-to-follow")

######  send a message #######
users = ["user1", "user2", "user3", "user4.."]
bot.send_message("Hello from Dhaval", users)

######  get follower info #######
my_followers = bot.get_user_followers("dhavalsays")
for follower in my_followers:
    print(follower)

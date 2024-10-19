class Posts:
    def __init__(self, user_message, author):
        self.message = user_message
        self.author = author


    def get_user_post(self):
        print(f"{self.author} has posted {self.message}")
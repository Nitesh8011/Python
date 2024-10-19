from user import User
from posts import Posts

app_user_one = User("Nike","nike@gmail.com","Nike@123","DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("Adidas","adidas@gmail.com","Adi@321","Software Developer")
app_user_two.get_user_info()

app_user_post = Posts("Today is great day","Nike")
app_user_post.get_user_post()
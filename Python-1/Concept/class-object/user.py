class User:
    def __init__(self, user_name, user_email, user_password, user_current_job_title):
        self.name = user_name
        self.email = user_email
        self.password = user_password
        self.current_job = user_current_job_title

    def change_password(self, new_password):
        self.user_password = new_password

    def change_job_title(self, new_job_title):
        self.user_current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} with email {self.email} is currently working as {self.current_job}")
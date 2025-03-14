"""
JAVA: Aidan Wong, Vedant Kothari
SoftDev
K35: Now Again for the First Time
2024-03-12
Time Spent: 2
"""

class User:
    users = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def create_user(cls, username, password):
        new_user = cls(username, password)
        cls.users.append(new_user)
        return new_user

    @classmethod
    def find_user(cls, username):
        for user in cls.users:
            if user.username == username:
                return user
        return None


class Story:
    stories = []

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.contributions = []

    @classmethod
    def create_story(cls, title, content, author):
        new_story = cls(title, content, author)
        cls.stories.append(new_story)
        return new_story

    def add_contribution(self, contribution):
        self.contributions.append(contribution)
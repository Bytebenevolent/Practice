class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email 


class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author


class Forum:
    def __init__(self):
        self.users = []
        self.posts = []
    
    def register(self, username: str, email: str):
        user = User(username, email)
        self.users.append(user)
        return user

    def create_post(self, title: str, content: str, author: User):
        post = Post(title, content, author)
        self.posts.append(post)
        return post

    def search_user_by_username(self, username: str):
        for user in self.users:
            if user.username == username:
                return user
        return "User not found"
    
    def search_user_by_email(self, email: str):
        for user in self.users:
            if user.email == email:
                return user.username, user.email
            else:
                "User not found"

    def search_posts_by_author(self, author: User):
        found_posts = []
        
        for post in self.posts:
            if post.author == author:
                found_posts.append(post)
        return found_posts
        

    def search_post_by_title(self, title: str):
        for post in self.posts:
            if post.title == title:
                return post
        return "Post not found"


# Usage.
forum = Forum()
alex = forum.register('Alex00', 'alex@email.com')
post = forum.create_post('Programming', "Learn Python", alex)

result = forum.search_post_by_title('Programming')
if isinstance(result, Post):
    print(result.title)
else:
    print(result)

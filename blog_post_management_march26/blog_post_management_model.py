class BlogPostException(Exception):
    pass


class PostNotExist(BlogPostException):
    pass


class DuplicatePost(BlogPostException):
    pass


class BlogPost:
    def __init__(self, title, content, author, date):
        self.title = title
        self.content = content
        self.author = author
        self.date = date

    def display(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Posted: ", self.date.strftime("%B %d, %Y %I:%M %p"))
        print("Content: ", self.content)


class Blog:
    def __init__(self, posts):
        self._posts = posts

    # add post, without duplicates
    def add_post(self, post):
        duplicate = self.post_index(post.title)
        if duplicate is None:
            self._posts.append(post)
        else:
            raise DuplicatePost("Post Already Exist")

    # edit post if exist, only title
    def edit_post(self, old_title, new_title):
        index = self.post_index(old_title)
        if index is None:
            raise PostNotExist("No post found on this title")
        else:
            post = self._posts[index]
            post.title = new_title

    # delete post if exist
    def delete_post(self, title):
        index = self.post_index(title)
        if index is None:
            raise PostNotExist("No post found on this title")
        else:
            del self._posts[index]

    # find post return index if exist, else none
    def post_index(self, title):
        index = None
        for i, post in enumerate(self._posts):
            if post.title == title:
                index = i
                break
        return index

    # generative method for posts
    def list_post(self):
        for post in self._posts:
            yield post

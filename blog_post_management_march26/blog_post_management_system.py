from datetime import datetime
from blog_post_management_model import Blog, BlogPost, DuplicatePost, PostNotExist

posts = [
    BlogPost(
        "Python Basics",
        "Python is a high-level, general-purpose, and very popular programming language. Python programming language (latest Python 3) is being used in web development, and Machine Learning applications, along with all cutting-edge technology in Software Industry.",
        "GeeksForGeeks",
        datetime(2024, 3, 24, 10, 30),
    ),
    BlogPost(
        "Python OOPs Concepts",
        "In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms in the programming.",
        "GeeksForGeeks",
        datetime(2024, 3, 25, 10, 30),
    ),
]


def start_blog():
    blog = Blog(posts)
    current_user = input("Enter your name: ")
    while True:
        print("1. View Blogs")
        print("2. Add post")
        print("3. Delete post")
        print("4. Edit post")
        print("5. Quit")
        option = input("Enter an option: ")
        match option:
            case "1":
                print()
                print("Blog List")
                print()
                for post in blog.list_post():
                    post.display()
                    print()

            case "2":
                print()
                print("Add Post")
                title = input("Enter Title: ").strip()
                content = input("Enter Content: ").strip()
                try:
                    blog.add_post(
                        BlogPost(title, content, current_user, datetime.now())
                    )
                    print("Post Added.")
                except DuplicatePost as error:
                    print(error)
                except Exception as error:
                    print(error)
                print()

            case "3":
                print()
                print("Delete Post")
                title = input("Enter Title: ").strip()
                try:
                    blog.delete_post(title)
                    print("Post Deleted.")
                except PostNotExist as error:
                    print(error)
                except Exception as error:
                    print(error)
                print()

            case "4":
                print()
                print("Edit Post")
                old_title = input("Enter old Title: ").strip()
                new_title = input("Enter new Title: ").strip()
                try:
                    blog.edit_post(old_title, new_title)
                    print("Post Edited.")
                except PostNotExist as error:
                    print(error)
                except Exception as error:
                    print(error)
                print()

            case "5":
                break

            case _:
                print("Enter valid option")


start_blog()

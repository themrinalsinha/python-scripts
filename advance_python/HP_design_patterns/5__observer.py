"""
Observer design patterns
"""

class User(object): # observer class
    """
    user class will act role of observer to subject
    """

    def __init__(self, name) -> None:
        self.name = name

    def update(self, article, blog_writer):
        print(f"For {self.name}, new article by {blog_writer.name} is added.")

    def __str__(self) -> str:
        return self.name


class BlogWriter(object):
    """
    BlogWriter class is useful to blog writer to add new articles and manage
    subscribers as well
    """
    def __init__(self, name) -> None:
        self.name          = name
        self.__articles    = [] # Article is the subject
        self.__subscribers = []

    def add_article(self, article):
        """
        add new article and notify subscriber
        """
        self.__articles.append(article)
        self.notify_subscriber(article)

    def get_articles(self):
        """
        get articles written by {self}
        """
        return self.__articles

    def subscribe(self, subscriber):
        """
        Add new subscriber to notify on adding article
        """
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        """
        User can unsubscribe from further notifications
        """
        return self.__subscribers.pop(self.__subscribers.index(subscriber))

    def subscribers(self):
        """
        Get all subscribers
        """
        return self.__subscribers

    def notify_subscriber(self, article):
        """
        Notifying all the subscribers about new addition of an article
        """
        for sub in self.__subscribers:
            sub.update(article, self)

blog_writer = BlogWriter("Mrinal's blog...")
user_1 = User("Mrinal")
user_2 = User("Mayank")
user_3 = User("Lucky")

blog_writer.subscribe(user_1)
blog_writer.subscribe(user_2)
blog_writer.subscribe(user_3)

blog_writer.add_article("My Article - first post")

blog_writer.unsubscribe(user_3)
print(blog_writer.subscribers())

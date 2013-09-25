from mongoengine import *
import datetime

# Define the data-structure
class BlogPost(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    author = StringField(required=True)
    date = DateTimeField(required=True, \
                         default=datetime.datetime.now)
    categories = ListField(StringField(max_length=30))

# Connect to the database
connect('blog_example')

# Save a post
post = BlogPost()
post.title = "Post"
post.content = "I think W, Y, and Z."
post.author = "Daniel Axtens"
post.save()

# Retrieve a post
posts = BlogPost.objects() # everything
posts = BlogPost.objects(author='Daniel Axtens') # only me
post = posts.first()
print('"%s", by "%s": %s' % \
      (post.title, post.author, post.content))

# Update it
post.title = "Freshly Updated Post"
post.save()

# Verify update
print(BlogPost.objects().first().title)

# Clear out the posts
BlogPost.objects().delete()

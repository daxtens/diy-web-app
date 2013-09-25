from mongoengine import *
import datetime

# Define the data-structures
class Comment(EmbeddedDocument):
    author = StringField(required=True,
                         default="Anonymous")
    link = URLField()
    content = StringField(required=True)
    date = DateTimeField(required=True,
                         default=datetime.datetime.now)

class BlogPost(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    author = StringField(required=True)
    date = DateTimeField(required=True, \
                         default=datetime.datetime.now)
    categories = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))


# Connect to the database
connect('blog_example')

# Save a post
post = BlogPost()
post.title = "Post"
post.content = "I think W, Y, and Z."
post.author = "Daniel Axtens"
post.save()

# Add the comments
comment = Comment()
comment.content = "First P0000st!"
post.comments.append(comment)
post.save()

comment = Comment()
comment.author = "Mr. Helpful"
comment.content = "I think you've forgotten X..."
comment.link = "http://helpful.blog.com"
post.comments.append(comment)
post.save()

# Retrieve a post
posts = BlogPost.objects()
post = posts.first()
print('"%s", by "%s": %s' % \
      (post.title, post.author, post.content))
for comment in post.comments:
    if comment.link is not None:
        print('Comment by %s (%s): %s' % \
              (comment.author, comment.link, \
                   comment.content))
    else:
        print('Comment by %s: %s' % \
              (comment.author, comment.content))


# Clear out the posts
BlogPost.objects().delete()

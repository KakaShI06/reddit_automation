import praw
import os
from dotenv import load_dotenv
from controllers.posts import getPost
from constants import POST_FILTER_TYPE, PAGE_NAME, POST_LIMIT
from controllers.voice_over import createVoiceOver, createVoiceOverPost

# Load environment variables from .env file
load_dotenv('.env')

# Access and use the environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
USER_AGENT = os.getenv("USER_AGENT")
CLIENT_ID = os.getenv("CLIENT_ID")

#Initializing reddit instance

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=SECRET_KEY,
    user_agent=USER_AGENT,
)

print('INTIALING REDDIT INSTANCE --->', reddit.read_only)

redditPost = reddit.subreddit(PAGE_NAME)
top_posts = redditPost.top(limit=POST_LIMIT, time_filter=POST_FILTER_TYPE)

posts = getPost(top_posts)

for i, post in enumerate(posts):
    createVoiceOverPost(i, post['title'])

    for comment in post['comments']:
        createVoiceOver(comment['id'], comment['text'], i)






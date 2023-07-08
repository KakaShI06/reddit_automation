import json

def getCommentForPost(comments):
    commentList = []

    for comment in comments:
        if ( len(commentList) > 5 ):
            break

        if ( len(comment.body) < 10 or len(comment.body) > 200 ):
            continue
        
        comment_dic = {
            'id': comment.id,
            'text': comment.body
        }

        print('COMMENT', comment_dic)

        commentList.append(comment_dic)

    return commentList


def getPost(top_posts):
        # Convert individual posts to dictionaries
    post_list = []
    for post in top_posts:
        if post.over_18:
            continue

        post_dict = {
            'title': post.title,
            'score': post.score,
            'url': post.url,
            'id': post.id,
            'comments': getCommentForPost(post.comments)
            # Include other desired fields here
        }
        print('Post Title -> ', post.title)
        post_list.append(post_dict)

    # Convert the list of posts to JSON format
    return post_list
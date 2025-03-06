import praw

def obtener_historias(subreddit, limite=5):
    reddit = praw.Reddit(
        client_id='EAhNUcnGpSMx9U4r_lz8yA',
        client_secret='gHbSkcy4tKIh-UyvCKReThSP2y8SAw',
        user_agent='story_teller'
    )
    
    historias = []
    for post in reddit.subreddit(subreddit).hot(limit=limite):
        if not post.stickied:
            historias.append(post.title + '\n' + post.selftext)
    
    return historias

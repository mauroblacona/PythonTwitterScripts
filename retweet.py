from data import api

tweets=api.GetUserTimeline(screen_name='jjconti')
status_id=tweets[0].id
api.PostRetweet(status_id=status_id, trim_user=False)


#!/usr/bin/python

import csv
from datetime import datetime
import json
import time

import twitter

from data import api


def to_dict(user):
    created_at = datetime.strptime(user.created_at, '%a %b %d %H:%M:%S %z %Y')
    return {
            'screen_name': user.screen_name,
            'name': user.name,
            'created_year': created_at.year,
            'created_month': created_at.month,
            'created_day': created_at.day,
            'statuses_count': user.statuses_count,
            'following': user.following,
            'following_count': user.friends_count,
            'followers_count': user.followers_count,
            'favourites_count': user.favourites_count
    }


def get_followers(account):
    followers = []
    page = api.GetFollowersPaged(screen_name=account, cursor=-1)
    followers.extend(page[2])
    print(len(followers))
    while page[2]:
        try:
            page = api.GetFollowersPaged(screen_name=account, cursor=page[0])
        except twitter.TwitterError:
            time.sleep(180)
            continue
        followers.extend(page[2])
        print(len(followers))
        return followers


def inspect(account):
    print(account)
    followers = get_followers(account)

    followers_dicts = [to_dict(u) for u in followers]
    followers_string = json.dumps(followers_dicts)

    with open('{}.json'.format(account), 'w+') as f:
        f.write(followers_string)

    with open('{}.csv'.format(account), 'w+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=followers_dicts[0].keys())
        writer.writeheader()
        writer.writerows(followers_dicts)


accounts = ['jjconti']
for a in accounts:
    inspect(a)

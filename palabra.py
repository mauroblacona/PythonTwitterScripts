from TwitterSearch import *
from data import api

try:
    tso = TwitterSearchOrder()
    tso.set_keywords(['higuain', 'perro'])
    #tso.set_language('es')
    tso.set_include_entities(False)



    ts = TwitterSearch(
        consumer_key = '4ONmpv3W9PgOxUGMqPccEBU8l',
        consumer_secret = 'chwGJuIdQNGRcVM0rE0hfh5CKJ2RXiCCd3L3akHJ0kBahENl9q',
        access_token = '1006539807122739202-cRX3EIbwOIn0N2MIDdBcaw2oSYa1xu',
        access_token_secret = 'X7mezle2SvBPiaPyI1Y7Qy1bNEF8FftlT2fABno5DwTWk'

    )

    cuenta = 0

    for tweet in ts.search_tweets_iterable(tso):
        usuario = tweet["user"]["screen_name"]
        status_id = tweet["id"]
        if "phyton" in tweet["text"]:
            import ipdb;ipdb.set_trace()
            api.PostUpdate("@{} Vamos Argentina!".format(usuario), in_reply_to_status_id=status_id, auto_populate_reply_metadata=True)
            cuenta += 1
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )


    print(cuenta)
    
            



except TwitterSearchException as e:
    print(e)


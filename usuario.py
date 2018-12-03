from TwitterSearch import *



try:
    tuo = TwitterUserOrder('brunoceratto')



    api = TwitterSearch(
        consumer_key = '4ONmpv3W9PgOxUGMqPccEBU8l',
        consumer_secret = 'chwGJuIdQNGRcVM0rE0hfh5CKJ2RXiCCd3L3akHJ0kBahENl9q',
        access_token = '1006539807122739202-cRX3EIbwOIn0N2MIDdBcaw2oSYa1xu',
        access_token_secret = 'X7mezle2SvBPiaPyI1Y7Qy1bNEF8FftlT2fABno5DwTWk'

    )



    for tweet in api.search_tweets_iterable(tuo):

        #api.PostUpdate('i love python')
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )


except TwitterSearchException as e:
    print(e)


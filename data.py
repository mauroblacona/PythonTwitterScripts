import twitter

consumer_key = "4ONmpv3W9PgOxUGMqPccEBU8l"

consumer_secret = "chwGJuIdQNGRcVM0rE0hfh5CKJ2RXiCCd3L3akHJ0kBahENl9q"

access_key = "1006539807122739202-cRX3EIbwOIn0N2MIDdBcaw2oSYa1xu"

access_secret = "X7mezle2SvBPiaPyI1Y7Qy1bNEF8FftlT2fABno5DwTWk"

api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=    access_key, access_token_secret=access_secret, sleep_on_rate_limit=True)

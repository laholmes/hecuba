from betfair import Betfair

client = Betfair('app_key', 'certs/betfair.pem')
client.login('username', 'password')



# listing tennis markets
from betfair.models import MarketFilter
event_types = client.list_event_types(
    MarketFilter(text_query='tennis')
)
print(len(event_types))                 # 2
print(event_types[0].event_type.name)   # 'Tennis'
tennis_event_type = event_types[0]
markets = client.list_market_catalogue(
    MarketFilter(event_type_ids=[tennis_event_type.event_type.id])
)
markets[0].market_name                  # 'Djokovic Tournament Wins'
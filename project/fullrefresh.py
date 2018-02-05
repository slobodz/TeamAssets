# project/fullrefresh.py

from api.request import token_refresh
from entity.model import product, client_dict, price_client_dict, stock, price, job_log

# get new token here
token = token_refresh()

job_log(token=token)

# run product data
product(token=token, action='delete')
product(token=token, action='put')
product(token=token, action='post')

## run client data
client_dict(token=token, action='delete')
client_dict(token=token, action='put')
client_dict(token=token, action='post')


## run price_client data
price_client_dict(token=token, action='delete')
price_client_dict(token=token, action='put')
price_client_dict(token=token, action='post')


# run stock data
stock(token=token, action='put')
stock(token=token, action='post')

# run price data
price(token=token, action='put')
price(token=token, action='post')


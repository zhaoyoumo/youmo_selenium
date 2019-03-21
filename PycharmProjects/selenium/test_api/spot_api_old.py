
# -*- coding: utf8 -*-

from httpfetcher import HttpFetcher


class SpotAPI(object):
	_site_newdex = 'https://api.newdex.io'
	_site_dadex = 'https://api.test.xjonathan.me/v1'
	_url_ticker = _site_newdex + '/v1/ticker?symbol={}'
	_url_depth = _site_newdex + '/v1/depth?symbol={}'

	def __init__(self, api_key=None, api_seceret_key=None, passphrase=None):
		self.api_key = api_key
		self.api_seceret_key = api_seceret_key
		self.passphrase = passphrase
		self._revoke_order_url = self._site_dadex + '/Order/{}'
		self.take_order_url = self._site_dadex + '/Order'

	def take_order(self, otype, side, marketId, price, size):
		if isinstance(marketId, str):
			if marketId in 'betdicetoken-dice-eos':
				marketId = 1

		headers = {'Content-Type': 'application/json'}
		url = self.take_order_url
		postData = {
			"marketId": marketId,
			"type": otype,
			"side": side,
			"price": price,
			"size": size,
		}
		response = HttpFetcher.GetResponse('post', url, headers, postData)
		if response:
			print ('下{}单成功'.format(side))
			return True

	def revoke_order(self, oid):
		url = self._revoke_order_url.format(oid)
		response = HttpFetcher.GetResponse('delete', url)
		if response:
			print('订单({})删除成功'.format(oid))
			return True

	def get_specific_ticker(self, symbol):
		'get last price about symbol '
		if symbol in 'betdicetoken-dice-eos':
			symbol = 'betdicetoken-dice-eos'

		url = self._url_ticker.format(symbol)
		response = HttpFetcher.GetResponse('get', url)
		response = eval(response.text)

		if response['code'] is 200:
			last_price = float(response['data']['last'])
			return last_price

	def get_depth(self, symbol):
		if symbol in 'betdicetoken-dice-eos':
			symbol = 'betdicetoken-dice-eos'

		url = self._url_depth.format(symbol)
		response = HttpFetcher.GetResponse('get', url)
		response = eval(response.text)

		if response['code'] is 200:
			data = response['data']
			return data


if __name__ == '__main__':
	spot = SpotAPI()
	result = spot.take_order(otype="limit", side='ask', marketId=1, price=4000, size=491.5)
	# result = spot.revoke_order(50)
	# {'marketId': 1, 'type': 'limit', 'side': 'ask', 'price': 0.001575, 'size': 491.5}
	# symbol = 'dice-eos'
	# result = spot.get_specific_ticker(symbol)
	# print(result, type(result))
	# result = spot.get_depth(symbol)
	print(result)

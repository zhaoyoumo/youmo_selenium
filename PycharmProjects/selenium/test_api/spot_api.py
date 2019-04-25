# coding:utf-8

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
		self.token = None

	def get_token(self):
		url = self._site_dadex + '/User/login'
		headers = {'Content-Type': 'application/json'}
		postData = {
			"account": self.api_key,
			"password": self.api_seceret_key,
			"reCAPTCHA": self.passphrase,
		}
		response = HttpFetcher.GetResponse('post', url, headers, postData)
		if response:
			print u'登录成功'
			self.token = response.json().get('token').get('token')
			return self

	def take_order(self, otype, side, marketId, price, size):

		headers = {'Content-Type': 'application/json',
				   'Authorization': 'Bearer {}'.format(self.token)}

		print(headers)
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
			print('下{}单成功'.format(side))
			return response.json()

	def revoke_order(self, oid):
		headers = {'Content-Type': 'application/json',
				   'Authorization': 'Bearer {}'.format(self.token)}

		url = self._revoke_order_url.format(oid)
		print(url)
		response = HttpFetcher.GetResponse('delete', url, headers)
		if response:
			print('订单({})删除成功'.format(oid))
			return response.json()


if __name__ == '__main__':
	api_key = 'zhaoyoumo@outlook.com'
	seceret_key = 'Abcd1234**'
	passphrase = 'string'
	spot_a = SpotAPI('zhaoyoumo@outlook.com', seceret_key, passphrase).get_token()

	api_key = 'wulei_delphy@outlook.com'
	seceret_key = 'Abcd1234**'
	passphrase = 'string'
	spot_b = SpotAPI('wulei_delphy@outlook.com', seceret_key, passphrase).get_token()

	result = spot_a.take_order(otype="limit", side='long', marketId='BTCUSD', price=3000, size=420)
	# result = spot.revoke_order(83)
	# {'marketId': 1, 'type': 'limit', 'side': 'ask', 'price': 0.001575, 'size': 491.5}
	# symbol = 'dice-eos'
	# result = spot.get_specific_ticker(symbol)
	# print(result, type(result))
	# result = spot.get_depth(symbol)
	print(result)

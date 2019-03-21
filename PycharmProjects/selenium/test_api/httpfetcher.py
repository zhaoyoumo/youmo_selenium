import requests
import json

METHOD = dict(
	get='get',
	post='post',
	delete='delete'
)


class HttpFetcher(object):

	@classmethod
	def ret(cls, response):
		if response.status_code is 200:
			return response
		else:
			print('status_code is not 200')

	@classmethod
	def GetResponse(cls, method=None, url=None, headers=None, postData=None):
		'method, url, headers, postData'
		if method == METHOD['get']:
			response = requests.get(url)
			return cls.ret(response)

		if method == METHOD['post']:
			response = requests.post(url, data=json.dumps(postData), headers=headers)
			if response:
				return cls.ret(response)

		if method == METHOD['delete']:
			response = requests.delete(url, headers=headers)
			if response:
				return cls.ret(response)
import requests
from lxml import html

with open('token.nes') as token_file:
	APP_ID = token_file.readline()
WA_URL = 'http://api.wolframalpha.com/v2/query?input={}<{}&appid={}'

def query(num1, num2):
	query_url = WA_URL.format(num1, num2, APP_ID)
	query_result = html.fromstring(requests.get(query_url).content)
	print('- Querying WolframAlpha with request: Is {} less than {}?'.format(num1, num2))

	answer = query_result.xpath('//pod[@id="Result"]/subpod/plaintext/text()')
	return answer[0]=='True'

def sort(numbers):
	print('Unsorted list is: {}\nStarting sort...'.format(numbers))

	i = 1
	swapped = False
	while i < len(numbers):

		j = i
		while j > 0 and query(numbers[j], numbers[j-1]):

			temp = numbers[j-1]
			numbers[j-1] = numbers[j]
			numbers[j] = temp

			j = j - 1
			swapped = True

		if swapped == False:
			i = i + 1
		else:
			swapped = False

	return numbers

list_input = input('Input a comma-separated list of numbers: ')
list = list_input.split(',')
print('Sorted list: {}'.format(sort(list)))
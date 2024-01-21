if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='[*] IP Geolocation Tool')
	parser.add_argument('-u', '--url', help='Locate an IP based on a URL', action='store', default=False, dest='url')
	parser.add_argument('-t', '--target', help='Locate the specified IP', action='store', default=False, dest='ip')
	parser.add_argument('--dat', help='Custom database filepath', action='store', default=False, dest='datfile')
	args = parser.parse_args()



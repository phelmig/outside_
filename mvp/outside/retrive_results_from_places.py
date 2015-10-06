#!/usr/bin/env python
# 24.09.2015 (c) Patrick Helmig
# A small script to trieve all results from a google places search

import urllib2, json, time, codecs

api_key =  'CHANGEME'
base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?key={}&language=de'.format(api_key)
token_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={}&key={}'
query = "&query=Frisuer+in+Frankfurt"



def get_results():
	api_key =  'CHANGEME'
	base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?key={}&language=de'.format(api_key)
	token_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={}&key={}'
	query = "&query=Frisuer+in+Frankfurt"
	"""
	Returns all results for the qurey defined above
	"""
	next_page_token = None
	results = []
	for i in xrange(1000):
		if next_page_token is None:
			req = urllib2.urlopen(base_url + query)
		else:
			time.sleep(2)
			req = urllib2.urlopen(token_url.format(next_page_token,api_key))
		ret = json.loads(req.read())
		results.append(ret.copy())
		if not 'next_page_token' in ret:
			break
		next_page_token = ret['next_page_token']
	return results

def get_details(place_id):
	#"returns phone, website, places_url"
	url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid={}&key={}'.format(place_id,api_key)
	js = json.loads(urllib2.urlopen(url).read())
	if 'result' in js:
		res = js['result']
		return {
		"phone":res.get('international_phone_number'),
		"website":res.get('website'),
		"places_url":res.get('url'),
		}
	else:
		return None



def write_to_csv(results,file_name):
	f = codecs.open(file_name,'w','utf-8')
	f.write(u"Name;Address;Phone;Closed;Lost;Created;Updated;Lng;Lat;PlacesUrl;WWW\n")
	for r in results:
		# json
		for b in r['results']:
			# Name; Address;
			details = get_details(b.get('place_id'))
			f.write(u'{};{};{};{};{};{};{};{};{};{};{}\n'.format(
				b.get('name'),
				b.get('formatted_address'),
				details.get('phone'),
				u'False',
				u'False',
				u'24.09.15 17:21',
				u'24.09.15 17:21',
				b.get('geometry').get('location').get('lng'),
				b.get('geometry').get('location').get('lat'),
				details.get('places_url'),
				details.get('website')

				))


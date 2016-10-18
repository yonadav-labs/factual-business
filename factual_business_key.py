import requests
import csv
# import pdb


# DHUqeEPowyRXhZaPOTAQ8t2RHVHU02kRnplKmjxj
# GniPib2v9mca6jTnsJS4QvQ3Zf2CKHrVM86HCbQ3
KEY = 'DHUqeEPowyRXhZaPOTAQ8t2RHVHU02kRnplKmjxj'

buz_url = 'http://api.v3.factual.com/t/places-us?filters={"category_ids":{"$includes":177}}&q="The UPS store"&limit=20&KEY='+KEY

result_csv_fields = [
    'name',
    'address',
    'city',
    'state',
    'zip',
    'phone',
    'website',
    'yelp_url',
    'facebook_url'
]

result = open('result.csv', 'w')
result_csv = csv.DictWriter(result, fieldnames=result_csv_fields)
result_csv.writeheader()
# pdb.set_trace()

try:
    res = requests.get(url=buz_url).json()
    if res['status'] == 'ok':
        business = []
        for item in res['response']['data']:
            business_ = {}
            business_['name'] = item['name']
            business_['address'] = item['address']
            business_['city'] = item['locality']
            business_['state'] = item['region']
            business_['zip'] = item['postcode']
            business_['phone'] = item['tel']
            business_['website'] = item['website']
            business_['yelp_url'] = ''
            business_['facebook_url'] = ''

            crosswalk_url = 'http://api.v3.factual.com/t/crosswalk-us?filters={"factual_id":"%s"}&KEY=%s' % (item['factual_id'], KEY)
            cres = requests.get(url=crosswalk_url).json()
            if cres['status'] == 'ok':
                for url_item in cres['response']['data']:
                    if url_item['namespace'] in ['facebook', 'yelp'] and 'url' in url_item:
                        business_[url_item['namespace']+'_url'] = url_item['url']
            result_csv.writerow(business_)
        print('\nSuccessfully exported')
except Exception, e:
    print('\nAn Error occured: ')
    print(str(e))

import json
import csv

from factual import Factual

KEY = '9HC9KoACsK3RfA0xOPFnGADfeR6MFGebTXVW9XmR'
KEY = 'DHUqeEPowyRXhZaPOTAQ8t2RHVHU02kRnplKmjxj'
SECRET = 'IMZKglb2pt6THhcN5O7SfzmoMM5YIQvvbYmLLhVV'
SECRET = 'BTPStt2B8jt9l3BfkjgotrQrNAzghUwNgI8oo7Im'

factual = Factual(KEY, SECRET)
places = factual.table('places-us')

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
limit = 50
num_exported = 0

keyword = raw_input("Business Brand: ")

try:
    for i in range(1):
        offset = i * limit  
        data = places.search(keyword).filters({'category_ids':{'$includes':177}}).offset(offset).limit(limit).data()

        if not data:
            break
            
        num_exported += len(data)
        for item in data:
            business_ = {}
            business_['name'] = item.get('name','')
            business_['address'] = item.get('address','')
            business_['city'] = item.get('locality','')
            business_['state'] = item.get('region','')
            business_['zip'] = item.get('postcode','')
            business_['phone'] = item.get('tel','')
            business_['website'] = item.get('website','')
            business_['yelp_url'] = ''
            business_['facebook_url'] = ''

            data = factual.crosswalk().filters({'factual_id':item['factual_id']}).data()
            if data:
                for url_item in data:
                    if url_item['namespace'] in ['facebook', 'yelp'] and 'url' in url_item:
                        business_[url_item['namespace']+'_url'] = url_item['url']
            result_csv.writerow(business_)
        print('\n{} records exported'.format(num_exported))
    print('\nSuccessfully exported')
except Exception, e:
#     # print(e.message['response'])
    # print str(e)
    print "Error: The credential is expired!"
    

## Purpose

Connect to the Global Places API for Factual to retrieve United States location data and possibly website profile date. e.g. (business name, address, city, state, zip, phone, Yelp URL, Facebook URL).  
This is for the business name "The UPS Store".  
You'll need to use your own API key by registering for the free account with Factual.   

## Reference

(http://www.factual.com/products/global)
(http://developer.factual.com/working-with-categories/)
(http://developer.factual.com/places-crosswalk/)
<http://developer.factual.com/api-docs/>
<http://developer.factual.com/data-files/>
<https://www.factual.com/blog/crosswalk-api>

## Sample Request

http://api.v3.factual.com/t/places-us?filters={"category_ids":{"$includes":177}}&KEY=GniPib2v9mca6jTnsJS4QvQ3Zf2CKHrVM86HCbQ3

http://api.v3.factual.com/t/crosswalk-us?filters={%22url%22:%22http://www.yelp.com/biz/the-stand-los-angeles-6%22}&KEY=GniPib2v9mca6jTnsJS4QvQ3Zf2CKHrVM86HCbQ3

http://api.v3.factual.com/t/crosswalk-us?filters={%22factual_id%22:%22114ee5af-a52c-4bcd-9172-b09f16de02fc%22}&KEY=GniPib2v9mca6jTnsJS4QvQ3Zf2CKHrVM86HCbQ3


## To run
	(install requests in advance)
	python factual_business.py

## The result file
	result.csv

You can use your live key in the script.
	Replace it in #6.

Currently it has limit of 50 due to free key.

To get remove the limit, you need to contact to Factual or purchase data file. 

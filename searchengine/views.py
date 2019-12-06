from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from django.http import Http404


from collections import OrderedDict
import json
import urllib.request
import urllib.parse 

# Create your views here.


# def index(request):
	
# 	return render(request, 'index.html')

# def testing(request):
	
# 	url = "http://3.88.165.155:8983/solr/"
# 	core = "Proj4"
# 	url_mid = "/select?q="
# 	url_tail = "&wt=json&indent=true&rows=1000"
	
	
# 	query = request.POST.get('search')
# 	if query is None: query = " "
# 	#query = 'modi in india'
# 	print(query)
	
# 	query = "("+query+")"
	
# 	queryUrl = url+core+url_mid+"text_en%3A"+urllib.parse.quote(query)+"+"+"text_pt%3A"+urllib.parse.quote(query)+"+"+"text_hi%3A"+urllib.parse.quote(query)+url_tail
# 	data = urllib.request.urlopen(queryUrl)
	
# 	data1 = json.load(data)
	
# 	docs = data1['response']['docs']
	
	
# 	print(queryUrl)

	
# 	context = {
# 				'postings': docs, 
# 				'query' : request.POST.get('search'),
				
# 			}
	
# 	return render(request,'search_temp.html', context)
	
# def facetedSearchAPI(request):
	
# 	url = "http://3.88.165.155:8983/solr/"
# 	core = "Proj4"
# 	url_mid = "/select?q="
# 	url_mid_tail = ""
# 	url_final_tail = "&wt=json&indent=true&rows=20"
	
# 	if request.method == "POST":
# 		data = json.loads(request.body)
# 		query = data['query']
# 		country_filter = data['country_filter']
# 		language_filter = data['language_filter']
# 		verified_filter = data['verified_filter']
	
# 	print(query)
# 	queryParsed = urllib.parse.quote(query)
# 	print(queryParsed)
	
# 	if(len(country_filter)>0):
# 		country_filter_url = "&fq=country%3A"
# 		countries = ','.join(country_filter) 
# 		url_mid_tail = url_mid_tail + country_filter_url+countries
	
# 	if(len(language_filter)>0):
# 		language_filter_url = "&fq=lang%3A"
# 		languages = ','.join(language_filter) 
# 		url_mid_tail = url_mid_tail+language_filter_url+languages
	
# 	if(len(verified_filter)>0):
# 		verified_filter_url = "&fq=verified%3A"
# 		verification = ','.join(verified_filter)
# 		url_mid_tail = url_mid_tail+verified_filter_url+verification
	
# 	queryUrl = url+core+url_mid+"text_en%3A"+queryParsed+"+"+"text_pt%3A"+queryParsed+"+"+"text_hi%3A"+queryParsed+url_mid_tail+url_final_tail
# 	data = urllib.request.urlopen(queryUrl)
	
# 	print(queryUrl)
	
# 	docs = json.load(data)['response']['docs']
# 	print(docs[0]['poi_name'])
# 	html = render_to_string('search_res.html', {'postings': docs})
# 	return HttpResponse(html)
	

def index(request):
    return render(request, "main.html")

def search_str(request):
    url = "http://18.223.152.187:8983/solr"
    core = "/Newfinal"
    url_mid = "/select?q="
    url_tail = "&wt=json&indent=true&rows=1000"
	
	
    query = request.POST.get('search')
    if query is None: query = " "
	
    query = "("+query+")"
	
    queryUrl = url+core+url_mid+"text_en%3A"+urllib.parse.quote(query)+"+"+"text_pt%3A"+urllib.parse.quote(query)+"+"+"text_hi%3A"+urllib.parse.quote(query)+url_tail
    data = urllib.request.urlopen(queryUrl)
	
    data1 = json.load(data)
	
    docs = data1['response']['docs']
	
	
    print(queryUrl)

	
    context = {
			    'data': docs, 
			    'query' : request.POST.get('search'),
				
			}
	
    return render(request,'main.html', context)



def facetsearch(request):
    url = "http://18.223.152.187:8983/solr"
    core = "/Newfinal"
    url_mid = "/select?q="
    url_mid_tail = ""
    url_final_tail = "&wt=json&indent=true&rows=20"

    if request.method == "POST":
        #data = request.get_json()
        data = json.loads(request.body)
        print(data)
        query = data['q']
        country_filter = data['cf']
        language_filter = data['lf']
        verified_filter = data['vf']

    print("Reached here 1")
    
    print(query)
    queryParsed = urllib.parse.quote(query)
    print(queryParsed)

    print("Reached here 2")

    if(len(country_filter)>0):
        country_filter_url = "&fq=country%3A"
        countries = ','.join(country_filter)
        url_mid_tail = url_mid_tail + country_filter_url+countries

    if(len(language_filter)>0):
        language_filter_url = "&fq=lang%3A"
        languages = ','.join(language_filter)
        url_mid_tail = url_mid_tail+language_filter_url+languages

    if(len(verified_filter)>0):
        verified_filter_url = "&fq=verified%3A"
        verification = ','.join(verified_filter)
        url_mid_tail = url_mid_tail+verified_filter_url+verification

    print("Reached here 3")

    queryUrl = url+core+url_mid+"text_en%3A"+queryParsed+"+"+"text_pt%3A"+queryParsed+"+"+"text_hi%3A"+queryParsed+url_mid_tail+url_final_tail
    print(queryUrl)
    data = urllib.request.urlopen(queryUrl)

    print(queryUrl)

    print("Reached here 4")

    res_docs = json.load(data)['response']['docs']
   
    print("Reached here 5")
    
    print(res_docs)
    context = {
			    'data': res_docs, 
			    'query' : request.POST.get('search'),
				
			}
    
    return render(request, 'results.html', context)



	

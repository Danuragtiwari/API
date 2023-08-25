

import json
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .forms import CompanySearchForm
from .models import Company

def search_company(request):
    if request.method == 'POST':
        form = CompanySearchForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            
          
            
            # 
            # Working-at-Amazon-EI_IE6036.11,17.htm
            # url = f'https://www.glassdoor.com/Reviews/Working-at-{company_name}-EI_IE6036.11,17.htm'
            
            url = f'https://www.glassdoor.com/Reviews/{company_name}-reviews-SRCH_KE0,12.htm'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            print(soup)

            #
            reviews = soup.find_all('div', class_='review')
            # print(reviews,'REview h ye')
            # for review in reviews:
            #     review_text = review.find('p', class_='review-text').text
            #     rating = float(review.find('span', class_='rating').text)



            
            company = Company.objects.create(
                name=company_name,
                description='Company description from Glassdoor',
                rating=4.5,
            )

     
            company_data = {
                'name': company.name,
                'description': company.description,
                'rating': company.rating,
             
            }
            
            return render(request, 'result.html', {'company_data': json.dumps(company_data)})
    else:
        form = CompanySearchForm()
    
    return render(request, 'search.html', {'form': form})

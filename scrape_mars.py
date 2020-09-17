from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


def scrape():

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    # NASA MARS NEWS
    news_url = ('https://mars.nasa.gov/news/?page=0&per_page=40'
    '&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest')

    browser.visit(news_url)
    time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.body.find_all('div', class_ = "content_title")[1].text.strip()

    news_p = soup.body.find_all('div', class_ = "article_teaser_body")[0].text.strip()
   

# def scrape

    #JPL MARS SPACE IMAGES - FEATURED IMAGE

    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(image_url)
    time.sleep(2)

    my_xpath = '/html/body/div[1]/div/div[3]/section[1]/div/div/article/div[1]/footer/a'

    results = browser.find_by_xpath(my_xpath)
    img = results[0]
    img.click()

    browser.click_link_by_partial_text('more info')

    html1 = browser.html
    soup = BeautifulSoup(html1, 'html.parser')

    feat_img = soup.find_all('figure', class_='lede')
    feat_img_result = feat_img[0].a['href']

    featured_image_url = 'https://www.jpl.nasa.gov' + feat_img_result
    # return

# def scrape
    # MARS FACTS

    facts_url = 'https://space-facts.com/mars/'

    facts_table = pd.read_html(facts_url)

    table_df = facts_table[0]

    mars_table_df = table_df.rename(columns={0: 'Mars: Measurement', 1: 'Measurement: Value'})

    mars_table_df.to_html(classes="table table-striped")

# return


# def scrape 
    # MARS HEMISPHERES

    #Note the inconsistent url
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)

    xpaths = [
            '/html/body/div[1]/div[1]/div[2]/section/div/div[2]/div[1]/div/a', 
            '/html/body/div[1]/div[1]/div[2]/section/div/div[2]/div[2]/div/a', 
            '/html/body/div[1]/div[1]/div[2]/section/div/div[2]/div[3]/div/a', 
            '/html/body/div[1]/div[1]/div[2]/section/div/div[2]/div[4]/div/a'
             ]


    hem_title = []

    hem_url = []

    mars_hem_title_url = []

    for path in xpaths :
        results = browser.find_by_xpath(path)
        img = results[0]
        img.click()
    
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
    
        title = soup.find('h2', class_ = 'title').text
        hem_title.append(title)
        
    
        hem = soup.find('div', class_='downloads')
        hem_result = hem
        img_url = hem_result.find('a')['href']
        hem_url.append(img_url)
       
    
        mars_hem_title_url.append({'title': title, 'img_url': img_url})
 
        browser.visit(hemispheres_url)


  
    browser.quit()
# return


#Store results in dictionary
    notebook_dict = {
                'article_title': news_title, 
                'article_paragraph': news_p,
                'mars_image': featured_image_url,
                'mars_data_table': mars_table_df,
                'hemisphere_image_urls': mars_hem_title_url}

    return notebook_dict
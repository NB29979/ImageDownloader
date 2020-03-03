# coding: UTF-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import feedparser
import re
import json
import sys


def download_images(_site_prop, _url):
    driver.get(_url)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")

    img_tags = soup.find_all('a', {'target':'_blank','href':re.compile(_site_prop['tag_attributes'])})

    for tag in img_tags:
        img_url = tag.attrs['href']
        word_list = tag.attrs['href'].split(_site_prop['split_char'])
        print(word_list[len(word_list) - 1])
        res = requests.get(img_url)
        with open('YOUR_DIR'+word_list[len(word_list) - 1], 'wb') as f:
            f.write(res.content)


if __name__ == "__main__":
   options = Options()
   options.set_headless(True)
   driver = webdriver.Chrome(chrome_options=options)

   with open('site_props.json', 'r') as ref_json:
      json_dict = json.load(ref_json)


   for site_prop in json_dict.values():
      feed_result = feedparser.parse(site_prop['rss'])
      for entry in feed_result.entries:
         if entry.link != site_prop['prev_link']:
            print(entry.title)
            download_images(site_prop, entry.link)
         else:
            break

      if site_prop['prev_link'] != feed_result.entries[0].link:
         site_prop['prev_link'] = feed_result.entries[0].link


   with open('site_props.json', 'w') as target_file:
      json.dump(json_dict,target_file)

   driver.close()
   sys.exit()
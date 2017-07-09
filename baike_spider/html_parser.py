#!/usr/bin/env python
# encoding: utf-8

'''
Created on 2017年7月3日

@author: bulala
'''
import re

from bs4 import BeautifulSoup
import urlparse


class HtmlParser(object):
    
    
    def _get_urls(self, page_url, soup):
        new_urls = set()
        #/view/123.htm
        links = soup.find_all('a', href=re.compile(r'/item/\S*'))
        for link in links :
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
            
        return new_urls
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        
        res_data['url'] = page_url
#         <dd class="lemmaWgt-lemmaTitle-title">
# <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()
        
        summary_none = soup.find('div', class_='lemma-summary')
        if summary_none is not None:
            res_data['summary'] = summary_none.get_text()
        else:
            res_data['summary'] = ''
            
        return res_data
    
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
    




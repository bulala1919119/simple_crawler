#!/usr/bin/env python
# encoding: utf-8

'''
Created on 2017年7月3日

@author: bulala
'''
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        
    
    def collect_data(self, data):
        if data is None:
            return 
        self.datas.append(data)
    
    def output_html(self):
        fout = open('output.html', 'w')
        
        fout.write('<html>')
        fout.write('<head><meta charset="utf-8"></head>')        
        
        fout.write('<body>')
        fout.write('<table>')
        
        for data in self.datas:
            
            fout.write('<tr><td style="width:100px;">%s</td>' % data['url'].encode('utf-8').decode('utf-8'))

            ''' python默认是ascii码 '''
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td></tr>' % data['summary'])
        
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
    
    




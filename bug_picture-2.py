#from scrapy.pipelines.imgs import Imagespipeline

import scrapy
class imgsPileLine(Imagespipeline):
   def get_media_requests(self,item,info):
        yield scrapy.Requests(item['src'])
        def file_path(self,request,response=None,info=None):
         3  imgName = request.url.split('/')[-1]
            return imgName
       def item_completed(self,results,item,info):
            return item
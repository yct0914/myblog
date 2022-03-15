import re
import requests
from rest_framework.response import Response
from rest_framework.request import *
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

def getUrl(text):
    url = re.search(r'href=\"(?P<u>.*?)\"',text).group('u')  
    return url 
class WeiBo(APIView):
    def get(self,request):
        url = 'https://weibo.com/ajax/statuses/hot_band'
        res = requests.get(url)
        newsJson = res.json()['data']['band_list']
        news = []
        i = 0
        for new in newsJson:
            try:
                title = new['note']
                text = new['mblog']['text']
                url = getUrl(text)
                rank = i
                hotNum = new['num']
                obj = {"title":title,'url':url,'rank':rank,'hotNum':hotNum}
                news.append(obj)
                i += 1
            except:
                #如果出错,说明读取到了广告,舍弃
                continue
        return Response(data=news,status=status.HTTP_200_OK)
        


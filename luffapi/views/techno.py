from rest_framework.views import APIView
from rest_framework.response import Response
from luffapi import models
from luffapi.serializers.techno import TechnoSerializer
from rest_framework.viewsets import GenericViewSet,ViewSetMixin
from luffapi.auth.auth import LuffAuth
from rest_framework.parsers import JSONParser,FormParser

class TechnoView(APIView):
    """
     资讯列表
     :param request:
     :param args:
     :param kwargs:
     :return:
     """
    authentication_classes = [LuffAuth, ]
    def get(self,request,*args,**kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            queryset = models.Article.objects.all()
            ser = TechnoSerializer(instance=queryset, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取资讯失败'
        return Response(ret)

class TechnoDetailView(ViewSetMixin,APIView):
    def post(self, request, *args, **kwargs):
        """
        点赞
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pk=kwargs.get('pk')
        ret = {'code': 1000, 'data': None}
        try:
            obj = models.Article.objects.get(id=pk)
            obj.agree_num= obj.agree_num+1
            obj.save(update_fields=['agree_num'])
            # from django.db.models import F, Q
            # obj = models.Article.objects.filter(id=id).update(agree_num=F("agree_num") + 1)
            # print(type(obj))
            ret['data'] = obj.agree_num
        except Exception as e:
            ret['code'] = 1001
            print(2222)
            ret['error'] = '点赞失败'
        print(ret)
        return Response(ret)




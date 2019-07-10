from rest_framework.views import APIView
from rest_framework.response import Response
from luffapi import models
from luffapi.serializers.teacher import TeacherSerializer
from rest_framework.viewsets import GenericViewSet,ViewSetMixin
from rest_framework.parsers import JSONParser,FormParser

class TeacherView(ViewSetMixin,APIView):

    def list(self,request,*args,**kwargs):
        """
        课程列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code':1000,'data':None}
        try:
            queryset = models.Teacher.objects.all()
            ser=TeacherSerializer(instance=queryset,many=True)
            ret['data']=ser.data
        except Exception as e:
            ret['code']=1001
            ret['error']='获取教师失败'
        return Response(ret)


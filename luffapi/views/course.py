from rest_framework.views import APIView
from rest_framework.response import Response
from luffapi import models
from utils.baseutils import BaseUtils
from luffapi.serializers.course import CourseSerializer,CourseDetailSerializer,ChapterSerializer
from rest_framework.viewsets import GenericViewSet,ViewSetMixin
from luffapi.auth.auth import LuffAuth
from rest_framework.parsers import JSONParser,FormParser

class CourseView(ViewSetMixin,APIView):
    parser_classes = [JSONParser, FormParser]
    def list(self,request,*args,**kwargs):
        """
        课程列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret=BaseUtils()
        try:
            queryset=models.Course.objects.all()
            ser=CourseSerializer(instance=queryset,many=True)
            ret.data=ser.data
            ret.code=1000
        except Exception as  e:
            ret.code=1001
            ret.error="获取课程失败"

        return Response(ret.dict)

        # ret = {'code':1000,'data':None}
        # try:
        #     queryset = models.Course.objects.all()
        #     ser=CourseSerializer(instance=queryset,many=True)
        #     ret['data']=ser.data
        # except Exception as e:
        #     ret['code']=1001
        #     ret['error']='获取课程失败'
        # return Response(ret)

    def post(self,request,*args,**kwargs):
        """
        创建课程
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code':1000,'data':None}
        set=CourseSerializer(data=request.data)
        if set.is_valid():
            set.save()
            ret['code'] = 1000
            ret['data'] = '添加成功'
        else:
            ret['code']=1001
            ret['error']=set.errors
        return Response(ret)

    def retrieve(self,request,*args,**kwargs):
        """
        课程详情
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret={'code':1000,'data':None}
        try:
            pk=kwargs.get('pk')
            obj=models.CourseDetail.objects.filter(course_id=pk).first()
            ser=CourseDetailSerializer(instance=obj,many=False)
            ret['data']=ser.data
        except Exception as e:
            ret['code']=1001
            ret['error']='获取课程失败'
        return Response(ret)

    def addchapter(self,request,*args,**kwargs):
        """
        添加章节
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret={'code':1000,'data':None}
        set=ChapterSerializer(data=request.data)
        print(set)
        if set.is_valid():
            set.save()
        else:
            ret['code'] = 1001
            ret['error'] = set.errors
        return Response(ret)



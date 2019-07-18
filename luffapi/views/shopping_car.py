from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet,ViewSetMixin
from rest_framework.response import Response
from django_redis import get_redis_connection
from utils.baseutils import BaseUtils
from luffapi.auth.auth import LuffAuth
from luffapi import models
from utils.exception import PricePolicyInvalid
from django.conf import settings
import json


class ShoppingCarView(APIView):
    authentication_classes = [LuffAuth,]
    conn = get_redis_connection('default')
    def post(self,request,*args,**kwargs):
        """
        将课程添加到购物车
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = BaseUtils()
        try:
            course_id = int(request.data.get('courseid'))
            policy_id = int(request.data.get('policyid'))
            course = models.Course.objects.get(id=course_id)
            price_policy_list = course.price_policy.all()
            price_policy_dict={}
            for item in price_policy_list:
                price_policy_dict[item.id]={
                    'period':item.valid_period,
                    'period_display':item.get_valid_period_display(),
                    'price':item.price,
                }
            if policy_id not in price_policy_dict:
                raise PricePolicyInvalid('价格策略不合法')
            car_key = settings.SHOPPING_CAR_KEY %(request.auth.user_id,course_id)
            car_dict={
                'title':course.name,
                'img':course.course_img,
                'default_policy':policy_id,
                'policy':json.dumps(price_policy_dict)
            }
            self.conn.hmset(car_key,car_dict)
            ret.data='添加成功'
        except Exception as e :
            ret.code=1001
            ret.error='添加失败'
        return Response(ret.dict)

    def delete(self,request,*args,**kwargs):
        """
        删除购物车课程
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret=BaseUtils()
        try:
            course_id_list=request.data.get('courseids')
            key_list=[settings.SHOPPING_CAR_KEY %(request.auth.user_id,course_id) for course_id in course_id_list]
            self.conn.delete(*key_list)
        except Exception as e:
            ret.code=1001
            ret.error='删除失败'
        return Response(ret.dict)

    def patch(self,request,*args,**kwargs):
        ret = BaseUtils()
        try:
            course_id=request.data.get('courseid')
            policy_id=request.data.get('policyid')
            key=settings.SHOPPING_CAR_KEY %(request.auth.user_id,course_id)
            if not self.conn.exists(key):
                ret.code=1001
                ret.error='购物车不存在此课程'
                return Response(ret.dict)
            # policy_dict=json.loads(str(self.conn.hget(key,'policy'),encoding='utf-8'))
            policy_dict=json.loads(self.conn.hget(key,'policy').decode('utf-8'))
            if policy_id not in policy_dict:
                ret.code=1002
                ret.error='价格策略不合法'
            self.conn.hset(key,'default_policy',policy_id)
            ret.data='修改成功'

        except Exception as e:
            ret.code=1004
            ret.error='修改失败'
        return Response(ret.dict)

    def get(self,request,*args,**kwargs):
        """
        展示购物车
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = BaseUtils()
        try:
            key_macth=settings.SHOPPING_CAR_KEY %(request.auth.user_id,"*")
            print(key_macth)
            course_list=[]
            for key in self.conn.scan_iter(key_macth,count=10):
                # print(self.conn.hget(key,'title'))
                info = {
                    'title':self.conn.hget(key,'title').decode('utf-8'),
                    'img':self.conn.hget(key,'img').decode('utf-8'),
                    'policy':json.loads(self.conn.hget(key,'policy').decode('utf-8')),
                    'default_policy':self.conn.hget(key,'default_policy').decode('utf-8')
                }
                print(info)
                course_list.append(info)
            print(course_list)
            ret.data=course_list

        except Exception as e :
            ret.code=1001
            ret.error='获取课程失败'
        return Response(ret.dict)
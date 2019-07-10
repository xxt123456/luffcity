from  luffapi import models
from  rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    course_type=serializers.CharField(source='get_course_type_display')
    level=serializers.CharField(source='get_level_display')
    status=serializers.CharField(source='get_status_display')
    sub_category=serializers.CharField(source='sub_category.name')
    class Meta:
        model = models.Course
        fields = ['id','name','course_img','course_type','sub_category','brief','order','level','pub_date','period','status']
    #
    # def get_sub_category(self,obj):
    #     print(obj)
    #     queryset = obj.sub_category.filter().first()
    #     print(queryset)
    #     return [{'id':row.id,'name':row.name} for row in queryset ]

    def create(self, validated_data):
        course=models.Course.objects.create(name=validated_data['name'],course_type=validated_data['get_course_type_display'],course_img=validated_data['course_img'],sub_category=validated_data['sub_category'],
                                            brief=validated_data['brief'],order=validated_data['order'],level=validated_data['get_level_display'],pub_date=validated_data['pub_date'],
                                            status=validated_data['get_status_display'])
        return course

class CourseDetailSerializer(serializers.ModelSerializer):
    course=serializers.CharField(source='course.name')
    recommend_courses=serializers.SerializerMethodField()
    teachers=serializers.SerializerMethodField()
    course_img=serializers.CharField(source='course.course_img')
    chapter=serializers.SerializerMethodField()

    class Meta:
        model=models.CourseDetail
        fields=['course','course_img','hours','chapter','course_slogan','video_brief_link','why_study','what_to_study_brief','career_improvement','prerequisite','recommend_courses','teachers']


    def get_recommend_courses(self,obj):
        queryset = obj.recommend_courses.all()
        return [{'id':row.id,'name':row.name} for row in queryset ]

    def get_teachers(self,obj):
        queryset=obj.teachers.all()
        return [{'id':row.id,'name':row.name} for row in queryset]

    def get_chapter(self,obj):
        querysey=obj.course.coursechapters.all()
        return [{'chapter':row.chapter,'name':row.name}for row in querysey]

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CourseChapter
        fields="__all__"

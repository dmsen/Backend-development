# Register your models here.
from django.contrib import admin
from django.utils.safestring import mark_safe
from dmseng.settings import MEDIA_URL

from . import models


class ArticleAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('article_title', 'article_information_classification',
                    'publish_date', 'view_times', 'mycol')
    # 可直接点击进入修改页面
    list_display_links = ('article_title',)
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ( 'article_information_classification', )
    # 右侧过滤器
    list_filter = ('is_notice', 'is_case',  'is_recommend')
    search_fields = ('article_title', 'publish_date')
    # inlines
    # 编辑页显示/不显示哪些字段
    # fields = ( 'date_count', 'unique_vistor')
    # exclude = ( 'date_count', 'unique_vistor')
    # 编辑页分块显示
    fieldsets = (
        (None, {
            'fields': ('article_title', 'article_information_classification',
                    'article_cover','article_cover_sm','article_abstract', 'article_content', 'article_tag' ),
        }),
        ('高级设置', {
            'fields': ('is_notice', 'is_case', 'is_recommend', 'is_business_evaluation'),
            'classes': ('wide', 'extrapretty'),
            # 'classes': ('collapse',),
        }),
    )

    # 定义一个list页面的显示名
    def mycol(self, obj):
        return obj.article_title
    mycol.short_description = '新增列'


class ReportAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ['report_title', 'article', 'report_publisher',
                    'report_enable', 'cover_show']
    # 定义一个list页面的显示名
    def cover_show(self, obj):
        return mark_safe("<img src='{media_url}{img_url}' />".format(media_url=MEDIA_URL, img_url=obj.report_cover))
    cover_show.short_description = '封面'

class Message(admin.ModelAdmin):
    list_display = ('username','email','message')
    # 可直接点击进入修改页面
    list_display_links = ('username','email','message')



# vue 霖 项目数据库后台
# 设备
class machinesAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('machineId', 'machineName', 'machTypeId', 'machineDesc' ,'dataOfProdect','office','mwordId')
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ('machineName' ,'dataOfProdect','office')
    # 可直接点击进入修改页面
    list_display_links = ('machineId','machTypeId', 'machineDesc')
    # 右侧过滤器
    list_filter = ('machineId', 'machineName',)
    search_fields = ('machineId', 'machineName',)
    # 编辑页显示/不显示哪些字段
    # fields = ('username', 'sex', 'city', 'english_score')
# 设备类型
class machTypesAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('machTypeId', 'machTypeCode', 'machTypeName', 'machTypeDesc',)
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ('machTypeCode', 'machTypeName', 'machTypeDesc',)
    # 可直接点击进入修改页面
    list_display_links = ('machTypeId',)
    # 右侧过滤器
    list_filter = ('machTypeId', 'machTypeCode', 'machTypeName', 'machTypeDesc',)
    search_fields = ('machTypeId', 'machTypeCode', 'machTypeName', 'machTypeDesc',)
# 用户
class usersAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('id', 'userName', 'password','jurisdiction','status','remarks','roles' )
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ('userName', 'password', 'remarks','roles')
    # 可直接点击进入修改页面
    list_display_links = ('id','jurisdiction','status')
    # 右侧过滤器
    list_filter = ('id', 'userName', 'password','jurisdiction','status','remarks')
    search_fields = ('id', 'userName', 'password','jurisdiction','status','remarks')
# 客户
class customersAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('customerId', 'customerName', 'customerType','customerLevel','sponsor','phone','address','machCount','remark' )
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ('customerName', 'customerType','sponsor','phone','address','machCount','remark')
    # 可直接点击进入修改页面
    list_display_links = ('customerId','customerLevel')
    # 右侧过滤器
    list_filter = ('customerId', 'customerName', 'customerType','customerLevel','sponsor','phone','address','machCount','remark' )
    search_fields = ('customerId', 'customerName', 'customerType','customerLevel','sponsor','phone','address','machCount','remark' )

# 所有监测点
class IOPoints_allAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('IOPId', 'IOPName', )
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ('IOPName', )
    # 可直接点击进入修改页面
    list_display_links = ('IOPId',)
    # 右侧过滤器
    list_filter = ('IOPId', 'IOPName', )
    search_fields = ('IOPId', 'IOPName', )
# 所有网关
class gateways_allAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('gatewayId', 'gatewayName',)
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ('gatewayName',)
    # 可直接点击进入修改页面
    list_display_links = ('gatewayId',)
    # 右侧过滤器
    list_filter = ('gatewayId', 'gatewayName', 'IOPNames', )
    search_fields = ('gatewayId', 'gatewayName', 'IOPNames', )
# 所有机器监测点
class IOPointsAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('IOPointsId', 'machineName','machineGateway','minRange','maxRange','aline','method','physicalName')
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ('minRange','maxRange','aline','method','physicalName')
    # 可直接点击进入修改页面
    list_display_links = ('IOPointsId', 'machineName','machineGateway',)
    # 右侧过滤器
    list_filter = ('IOPointsId', 'machineName', 'machineGateway', 'physicalName')
    search_fields = ('IOPointsId', 'machineName', 'machineGateway', 'physicalName')
# 异常码
class alarmCodesAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('alarmCodeId', 'alarmCodeName','machineName','physicalName','minValue','maxValue','alarmMsg','level','timeLimit')
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ('alarmCodeName','minValue','maxValue','level','timeLimit')
    # 可直接点击进入修改页面
    list_display_links = ('alarmCodeId', 'machineName','physicalName',)
    # 右侧过滤器
    list_filter = ('alarmCodeId', 'machineName', )
    search_fields = ('alarmCodeId', 'machineName')
# 单个异常记录
class  singleAlarmCodesAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('singleAlarmCodeId', 'startTime','duration','singleAlarmCodeStatus',)
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ('startTime','duration','singleAlarmCodeStatus')
    # 可直接点击进入修改页面
    list_display_links = ('singleAlarmCodeId',)
    # 右侧过滤器
    list_filter = ('singleAlarmCodeId', 'startTime','duration' )
    search_fields = ('singleAlarmCodeId', 'startTime','duration')

# 解决方案
class  alarmSolutonsAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('alarmSolutonId', 'alarmSolutonName','alarmSolutonDetail','alarmCodeList',)
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ('alarmSolutonName','alarmSolutonDetail','alarmCodeList')
    # 可直接点击进入修改页面
    list_display_links = ('alarmSolutonId',)
    # 右侧过滤器
    list_filter = ('alarmSolutonId',)
    search_fields = ('alarmSolutonId',)

# 异常处理历史
class  alarmProcessHistoryAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('alarmProcessHistoryId', 'alarmCodeName','alarmSolutonId','callbackMsg','processTime','machineName','alarmCode')
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ('callbackMsg',)
    # 可直接点击进入修改页面
    list_display_links = ('alarmProcessHistoryId', 'alarmCodeName','alarmSolutonId')
    # 右侧过滤器
    list_filter = ('alarmProcessHistoryId', 'alarmCodeName','alarmSolutonId')
    search_fields = ('alarmProcessHistoryId', 'alarmCodeName','alarmSolutonId')
#     霖项目后台
admin.site.register(models.machTypes,machTypesAdmin)
admin.site.register(models.machines,machinesAdmin)
admin.site.register(models.users,usersAdmin)
admin.site.register(models.customers,customersAdmin)
admin.site.register(models.IOPoints_all,IOPoints_allAdmin)
admin.site.register(models.gateways_all,gateways_allAdmin)
admin.site.register(models.IOPoints,IOPointsAdmin)
admin.site.register(models.alarmCodes,alarmCodesAdmin)
admin.site.register(models.singleAlarmCodes,singleAlarmCodesAdmin)
admin.site.register(models.alarmSolutons,alarmSolutonsAdmin)
admin.site.register(models.alarmProcessHistory,alarmProcessHistoryAdmin)
# dmsen项目后台
admin.site.register(models.InformationClassification)
admin.site.register(models.Emailmsg,Message)
admin.site.register(models.Tag)
admin.site.register(models.LinkCategory)
admin.site.register(models.Guid)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Notice)

#hutProject后台
#用户
from apps.app01.hutProject import  hutModel
class hutProjectsUsersAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('id', 'userName', 'password','jurisdiction','status','remarks' )
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ('userName', 'password', 'remarks')
    # 可直接点击进入修改页面
    list_display_links = ('id','jurisdiction','status')
    # 右侧过滤器
    list_filter = ('id', 'userName', 'password','jurisdiction','status','remarks')
    search_fields = ('id', 'userName', 'password','jurisdiction','status','remarks')


class hutNoticeAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('hutNoticeId', 'msg')
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ('msg',)
    # 可直接点击进入修改页面
    list_display_links = ('hutNoticeId',)
    # 右侧过滤器
    list_filter = ('hutNoticeId', 'msg')
    search_fields = ('hutNoticeId', 'msg')


class hutCourseAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('hutCourseId', 'hutCourseName')
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ('hutCourseName',)
    # 可直接点击进入修改页面
    list_display_links = ('hutCourseId',)
    # 右侧过滤器
    list_filter = ('hutCourseId', 'hutCourseName')
    search_fields = ('hutCourseId', 'hutCourseName')

class courseEvaluateAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('courseEvaluateMsg', 'hutCourseId','userid')
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ('courseEvaluateMsg',)
    # 可直接点击进入修改页面
    list_display_links = ('hutCourseId','userid',)
    # 右侧过滤器
    list_filter = ('courseEvaluateMsg', 'userid','hutCourseId')
    search_fields = ('courseEvaluateMsg', 'userid','hutCourseId')

admin.site.register(hutModel.hutNotice,hutNoticeAdmin)
admin.site.register(hutModel.hutProjectsUsers,hutProjectsUsersAdmin)
admin.site.register(hutModel.hutCourse,hutCourseAdmin)
admin.site.register(hutModel.courseEvaluate,courseEvaluateAdmin)
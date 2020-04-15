"""dmseng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from  apps.app01 import views
from  apps.app01.hutProject import hutViews
from django.conf.urls import include
from django.views.static import serve
from dmseng import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index,name='index'),
    url(r'^qishe$', views.yilin,name='yilin'),
    url(r'^xiangce$', views.xiangce,name='xiangce'),
    url(r'^dxiangce$', views.dxiangce,name='dxiangce'),
    # app 轻松订
    url(r'^qsdapp$', views.qsdapp,name='qsdapp'),


    # 配置CKEDITOR 路由
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # 配置图片路径
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    # url(r'^detail/', views.detail),
    url(r'^detail/(?P<pk>\d+)/$', views.detail_test1,name='detail'),
    # 导航
    url(r'^sub_test1/(\d+)/$', views.sub_test1,name='tag'),
    # 搜索功能
    url(r'^search/$',views.search,name='search'),
    # 个人项目首页
    url(r'^projects/$',views.projects_index,name='projects'),
    # 将个人网站include
    url(r'^firstweb/', include('apps.gerenweb.urls', namespace='gerenweb'),),


    # url(r'^websocket/',views.websocket_test),
    # url(r'^echo/',views.echo),
    url(r'^echo/$', views.testWebsocket),
    url(r'^websocket$', views.test_websocket),
    # 霖
    # url(r'^lin$', views.lin, name='lin'),
    url(r'^lin/', include('apps.lin.urls', namespace='linWeb')),
    #  vue项目接口
    url('^beforeLin$', views.before_lin, name='before_lin'),
    # 登陆
    url('^test_login$', views.test_login, name='test_login'),
    # 设备
    url('^machine/machines$', views.test_machine_get, name='test_machine_get'),
    url('^machine/add$', views.test_machine_add, name='test_machine_add'),
    url('^machine/mode$', views.test_machine_mod, name='test_machine_mod'),
    url('^machine/del$', views.test_machine_del, name='test_machine_del'),
    # 设备类型
    url('^machType/machTypes$', views.test_machine_type_get, name='test_machine_type_get'),
    url('^machType/add$', views.test_machine_type_add, name='test_machine_type_add'),
    url('^machType/mode$', views.test_machine_type_mod, name='test_machine_type_mod'),
    url('^machType/del$', views.test_machine_type_del, name='test_machine_type_del'),
    # 用户管理
    url('^user/userInfos$', views.test_user_get, name='test_user_get'),
    url('^user/add$', views.test_user_add, name='test_user_add'),
    url('^user/mode$', views.test_user_mod, name='test_user_mod'),
    url('^user/updata$', views.test_user_updata, name='test_user_updata'),
    url('^user/del$', views.test_user_del, name='test_user_del'),
    url('^user/modeTou$', views.test_userTou_mod, name='test_userTou_mod'),
    # 客户管理
    url('^customer/customers$', views.test_customer_get, name='test_customer_get'),
    url('^customer/add$', views.test_customer_add, name='test_customer_add'),
    url('^customer/mode$', views.test_customer_mod, name='test_customer_mod'),
    url('^customer/del$', views.test_customer_del, name='test_customer_del'),
    # 监测点配置
    url('^gwIop/gateways/notUsed$', views.test_gateways_get, name='test_gateways_get'),
    # 所有机器监测点配置查询
    url('^gwIopMappingConfig/gwIopMappingConfigs$', views.test_machines_IOP_get, name='test_machines_IOP_get'),
    url('^gwIopMappingConfig/add$', views.test_machines_IOP_add, name='test_machines_IOP_add'),
    url('^gwIopMappingConfig/mod$', views.test_machines_IOP_mod, name='test_machines_IOP_mod'),
    url('^gwIopMappingConfig/del$', views.test_machines_IOP_del, name='test_machines_IOP_del'),
    # 根据机器id 查询监测点
    url('^machineIdIOP/get$', views.test_gwIopMappingConfig_get, name='test_gwIopMappingConfig_get'),
    # 监测点组配置查询
    url('^iopGroup/iopGroups$', views.test_iopgs_get, name='test_iopgs_get'),
    # 异常报警
    # 异常码
    url('^alarmCode/alarmCodes$', views.test_alarmCode_get, name='test_alarmCode_get'),
    url('^alarmCode/addCodes$', views.test_alarmCodes_add, name='test_alarmCodes_add'),
    url('^alarmCode/modCodes$', views.test_alarmCodes_mod, name='test_alarmCodes_mod'),
    url('^alarmCode/delCodes$', views.test_alarmCodes_del, name='test_alarmCodes_del'),
    # 解决方案
    url('^solution/get$', views.test_solution_get, name='test_solution_get'),
    url('^solution/add$', views.test_solution_add, name='test_solution_add'),
    url('^solution/mod$', views.test_solution_mod, name='test_solution_mod'),
    url('^solution/del$', views.test_solution_del, name='test_solution_del'),
    # 单个异常记录
    url('^singleAlarmCodes/get$', views.test_singleAlarmCodes_get, name='test_singleAlarmCodes_get'),
    url('^singleAlarmCodes/init$', views.test_singleAlarmCodes_init, name='test_singleAlarmCodes_init'),
    #  故障处理接口
    url('^alarmProcess$', views.test_alarmProcess, name='test_alarmProcess'),
    url('^alarmProcess/history$', views.test_alarmProcess_history, name='test_alarmProcess_history'),
    #  实时预警信息
    url('^alarmInfo/alarmInfoCounts$', views.test_alarmInfoCounts_get, name='test_alarmInfoCounts_get'),
    # 组合异常码
    url('^alarmGroup/alarmGroups$', views.test_alarmCodesGroup_get, name='test_alarmCodesGroup_get'),

    # 历史记录highcharts
    url('^data/historyDatas$', views.test_historyDatas_get, name='test_historyDatas_get'),
    # 历史记录echarts接口1
    url('^data/historyDatasLimitCount$', views.test_historyData_echarts_get, name='test_historyData_echarts_get'),
    # 历史记录echarts接口2
    url('^data/historyDatasLimitCount2$', views.test_historyData_echarts2_get, name='test_historyData_echarts2_get'),
    # 历史记录echarts接口3
    url('^data/historyDatasLimitCount3$', views.test_historyData_echarts3_get, name='test_historyData_echarts3_get'),
    # 数据对比
    url('^data/Contrast$', views.test_contrast_get, name='test_contrast_get'),
    ##################################   hut软件工程【课程评价管理系统】   #############################################
    # 湖工大软件工程系统课程用户管理
    # 登陆
    url('^test_hutLogin$', hutViews.test_login, name='test_hutLogin'),
    url('^hutUser/get$', hutViews.test_user_get, name='test_hutUser_get'),
    url('^hutUser/add$', hutViews.test_user_add, name='test_hutUser_add'),
    # url('^hutUser/mode$', views.test_user_mod, name='test_user_mod'),
    url('^hutUser/updata$', hutViews.test_user_updata, name='test_user_updata'),
    url('^hutUser/del$', hutViews.test_user_del, name='test_hutUser_del'),
    url('^hutUser/modeTou$', hutViews.test_userTou_mod, name='test_userTou_mod'),
    url('^hutUser/notice$', hutViews.test_user_notice, name='test_user_notice'),
    url('^hutUser/getNotice$', hutViews.test_user_getNotice, name='test_user_getNotice'),
    # 湖工大软件工程系统课程课程信息管理
    url('^hutCourse/get$', hutViews.test_course_get, name='test_hutCourse_get'),
    url('^hutCourse/add$', hutViews.test_course_add, name='test_hutCourse_add'),
    url('^hutCourse/mode$', hutViews.test_course_mod, name='test_hutCourse_mod'),
    url('^hutCourse/del$', hutViews.test_course_del, name='test_hutCourse_del'),
    # 课程评价
    url('^hutCourse/evl$', hutViews.test_course_evl, name='test_hutCourse_evl'),
    url('^hutCourse/evlGet$', hutViews.test_course_evlGet, name='test_hutCourse_evlGet'),
    # 地图页面
    url(r'^map/', include('apps.lin.urls', namespace='linWeb')),
]





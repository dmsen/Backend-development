# 用户
import json
from django.http import JsonResponse

import json
import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#  将查询集变成字典形式
def queryset_to_json(queryset):
    obj_arr = []
    for o in queryset:
        obj_arr.append(o.toDict())
    return obj_arr
@csrf_exempt
# 登陆
def test_login(request):
    from .hutModel import hutProjectsUsers
    print("用户登录")

    jsonResponse = json.loads(request.body.decode('utf-8'))
    print (jsonResponse)
    print(request, type(jsonResponse['optionLevel']))
    if(jsonResponse['userName'].strip() =='' or jsonResponse['password'].strip() =='' ):

        return JsonResponse({"result": 2, "msg": '用户名/密码不能为空'})
    else:
        if(jsonResponse['optionLevel'] ==0):
            try:
                # aa = hutProjectsUsers.objects.all().get(userName=jsonResponse['userName']).__dict__[
                #     'password']
                # print(aa)
                if ('lin' == jsonResponse['userName'].strip() and 'lin' == jsonResponse['password'].strip()):
                    return JsonResponse({"result": 0,
                                         "msg": {'id': 1, 'userName': 'lin', 'password': 'lin', 'roles': '最高管理员',
                                                 'jurisdiction': 0, 'status': 1, 'remarks': '最高管理员','userTou':'hutUser/defaultTou.png'}})
                else:
                    return JsonResponse({"result": 3, "msg": '用户名密码错误,请检查登陆方式'})
            except:
                return JsonResponse({"result": 4, "msg": '用户名不存在/密码错误'})
        elif(jsonResponse['optionLevel'] ==1):
            return JsonResponse({"result": 0,
                                 "msg": {'id': 2, 'userName': 'xxx', 'password': 'xxx', 'roles': '访客',
                                         'jurisdiction': 3, 'status': 1, 'remarks': '访客','userTou':'user/defaultTou.png'}})
        elif (jsonResponse['optionLevel'] == 2):
            if(len(hutProjectsUsers.objects.all().filter(userName=jsonResponse['userName'])) == 0):
                return JsonResponse({"result": 5, "msg": '用户不存在'})
            else:

                try:
                    if (jsonResponse['password'] == hutProjectsUsers.objects.all().get(userName=jsonResponse['userName']).__dict__[
                        'password']):
                        userInfo = hutProjectsUsers.objects.all().get(userName=jsonResponse['userName']).__dict__
                        return JsonResponse({"result": 0,
                                             "msg": {
                                                 'id': userInfo['id'],
                                                 'userName':  userInfo['userName'],
                                                 'password':userInfo['password'],
                                                'jurisdiction': userInfo['jurisdiction'],
                                                 'status': userInfo['status'],
                                                 'remarks':userInfo['remarks'],
                                                'userTou':userInfo['userTou']}})
                    else:
                        return JsonResponse({"result": 6, "msg": '用户名密码错误'})
                except:
                    return JsonResponse({"result": 1, "msg": '未知错误'})



            #
            # pastJson = {
            #         "id":1,
            #         "jurisdiction":1,
            #         "password":'',
            #         "remarks":'超级测试员',
            #         "role":'测试员',
            #         "status":0,
            #         "username":"1级管理员"
            #     }
            # return JsonResponse({"result": 0, "msg": pastJson})
    # return HttpResponse(flag)




def test_user_get(request):
    from .hutModel import hutProjectsUsers
    jsonResponse = json.loads(request.body.decode('utf-8'))
    # print("测试用户get——————————————————")
    # print (jsonResponse)
    # pastJson = queryset_to_json(users.objects.all()[:])
    # [jsonResponse["sendPage"]*10-10:jsonResponse["sendPage"]*10]
    if(jsonResponse["sendPage"]):
        pastJson = hutProjectsUsers.objects.all()[jsonResponse["sendPage"]*10-10:jsonResponse["sendPage"]*10]
    else:
        pastJson = hutProjectsUsers.objects.all()[1 * 10 - 10:1 * 10]
    # print (pastJson,type(pastJson))
    lists = []
    for i in range(len(pastJson)):
        lists.append({
            'id': pastJson[i].__dict__['id'],
            'userName': str(pastJson[i].__dict__['userName']),
            'remarks': str(pastJson[i].__dict__['remarks']),
            'level': pastJson[i].__dict__['jurisdiction'],
            "status": pastJson[i].__dict__['status'],
        })
    # print (lists)
    return JsonResponse({"allDateLength": hutProjectsUsers.objects.all().count(), "msg": lists})
    # return JsonResponse({"allDateLength": users.objects.all()[:].count(), "msg": pastJson})
    # return HttpResponse(pastJson)



def test_user_add(request):
    from .hutModel import hutProjectsUsers
    # jsonResponse = json.load(request.body)
    jsonResponse = json.loads(request.body.decode('utf-8'))
    print("增加用户")
    print (jsonResponse,type(jsonResponse))
    dataLists = hutProjectsUsers.objects.all().count()
    try:
        if(dataLists >20):
           return JsonResponse({"result": 0, "msg": "增加失败,用户数目不能超过20人"})
        else:
            hutProjectsUsers.objects.create(**jsonResponse)
    except :
        return JsonResponse({"result": 1, "msg": "增加失败,用户名重复/信息不完整"})
    else:
        return JsonResponse({"result": 0, "msg": "增加成功"})



# 用户个人信息修改
def test_user_updata(request):
    from .hutModel import hutProjectsUsers
    print(request.body.decode('utf-8'))
    print("用户个人信息修改-")
    jsonResponse = json.loads(request.body.decode('utf-8'))
    print (jsonResponse, type(jsonResponse))
    print ("用户个人信息修改-")
    print (jsonResponse['id'],type(jsonResponse['id']))
    try:
        hutProjectsUsers.objects.filter(id=jsonResponse['id']).update(
            userName=jsonResponse['userName'],
            password=jsonResponse['password'],
            remarks=jsonResponse['remarks'],
            status=jsonResponse['status'],
        )
    except:
        return JsonResponse({"result": 1, "msg": "修改失败，用户名重复/信息不完整"})
    else:
        return JsonResponse({"result": 0, "msg": "修改成功"})


def test_userTou_mod(request):
    from .hutModel import hutProjectsUsers,file_delete
    # print(request.FILES)
    # print (request.FILES['croppedImg'])
    # obj = request.FILES.get("croppedImg")
    # print (obj, type(obj), obj.name, obj.chunks())
    # print (obj.file,obj.field_name,obj.name, obj.content_type,
    #               obj.size, obj.charset, obj.content_type_extra)
    userId = int(request.POST.__getitem__('userId'))
    userName = request.POST.__getitem__('userName')
    print("修改用户头像")
    # print (userId,type(userId),userName)
    from django.core.files.base import ContentFile
    # 读取上传的文件中的video项为二进制文件
    file_content = ContentFile(request.FILES['croppedImg'].read())
    # # ImageField的save方法，第一个参数是保存的文件名，第二个参数是ContentFile对象，里面的内容是要上传的图片、视频的二进制内容
    mymodel = hutProjectsUsers.objects.get(id=userId)
    # print(mymodel.userTou == "./hutUser/defaultTou.png")
    if(mymodel.userTou == "./hutUser/defaultTou.png"):
        mymodel.userTou.save(request.FILES['croppedImg'].name + '_' + userName + '.png', file_content)
    else:
        # 删除之前的图片，避免 图片冗杂
        file_delete(hutProjectsUsers, mymodel)
        #再存储头像图片
        mymodel.userTou.save(request.FILES['croppedImg'].name+'_'+userName+'.png', file_content)

    return JsonResponse({"result": 0, "msg": "用户头像修改成功"})


#
def test_user_del(request):
    from .hutModel import hutProjectsUsers
    jsonResponse = json.loads(request.body.decode('utf-8'))
    # print (jsonResponse,type(jsonResponse))
    # print("删除删除））））））））））））））））））））））））））））")
    # print (jsonResponse['id'],jsonResponse['userId'])
    fJurisdiction = hutProjectsUsers.objects.get(id=jsonResponse['id']).__dict__['jurisdiction']
    lJurisdiction = hutProjectsUsers.objects.get(id=jsonResponse['userId']).__dict__['jurisdiction']
    # print(fJurisdiction,lJurisdiction)
    if (jsonResponse['id'] == 1 or jsonResponse['id'] == 2):
        return JsonResponse({"result": 1, "msg": "系统默认用户无法删除"})
    else:
        if (fJurisdiction == lJurisdiction):
            return JsonResponse({"result": 1, "msg": "您们权限相等，无法删除"})
        elif (lJurisdiction > fJurisdiction):
            return JsonResponse({"result": 1 ,"msg": "对方权限比您高，无法删除"})
        else:
            try:
                    hutProjectsUsers.objects.filter(id=jsonResponse['id']).delete()
            except :
                return JsonResponse({"result": 1, "msg": "未知错误"})
            else:
                return JsonResponse({"result": 0, "msg": "删除成功"})



############################################################################################
###课程
import json
from django.http import JsonResponse
def test_course_get(request):
    from .hutModel import hutCourse
    jsonResponse = json.loads(request.body.decode('utf-8'))
    # print(jsonResponse)
    # print("课程")
    if(jsonResponse["sendPage"]):
        pastJson = hutCourse.objects.all()[jsonResponse["sendPage"]*10-10:jsonResponse["sendPage"]*10]
    else:
        pastJson = hutCourse.objects.all()[1 * 10 - 10:1 * 10]
    lists = []
    for i in range(len(pastJson)):
        lists.append({
            'hutCourseId': pastJson[i].__dict__['hutCourseId'],
            'hutCourseName': pastJson[i].__dict__['hutCourseName'],
            "hutCourseDescribe": pastJson[i].__dict__['hutCourseDescribe'],
            'hutCourseTeacher': pastJson[i].__dict__['hutCourseTeacher'],
        })
    # print (lists)
    return JsonResponse({"allDateLength": hutCourse.objects.all().count(), "msg": lists})
    # return JsonResponse({"allDateLength": users.objects.all()[:].count(), "msg": pastJson})
    # return HttpResponse(pastJson)

def test_course_add(request):
    from .hutModel import hutCourse
    jsonResponse = json.loads(request.body.decode('utf-8'))
    print (jsonResponse,type(jsonResponse))
    # dataLists = hutCourse.objects.all().count()
    try:
            hutCourse.objects.create(**jsonResponse)
    except :
        return JsonResponse({"result": 1, "msg": "增加失败,未知问题，请联系管理员解决"})
    else:
        return JsonResponse({"result": 0, "msg": "增加成功"})


def test_course_mod(request):
    from .hutModel import hutCourse
    jsonResponse = json.loads(request.body.decode('utf-8'))
    print("课程修改")
    print (jsonResponse, type(jsonResponse))
    print(jsonResponse['hutCourseId'])
    try:
        hutCourse.objects.filter(hutCourseId=jsonResponse['hutCourseId']).update(
            hutCourseName=jsonResponse['hutCourseName'],
            hutCourseDescribe=jsonResponse['hutCourseDescribe'],
            hutCourseTeacher=jsonResponse['hutCourseTeacher'],
        )
    except:
        return JsonResponse({"result": 1, "msg": "修改失败，课程名重复/信息不完整"})
    else:
        return JsonResponse({"result": 0, "msg": "修改成功"})
#



def test_course_del(request):
    from .hutModel import hutCourse
    from .hutModel import hutProjectsUsers
    jsonResponse = json.loads(request.body.decode('utf-8'))
    # print (jsonResponse,type(jsonResponse))
    print("删除删除））））））））））））））））））））））））））））")
    Jurisdiction = hutProjectsUsers.objects.get(id=jsonResponse['id']).__dict__['jurisdiction']
    if (jsonResponse['hutCourseId'] == 1 or jsonResponse['hutCourseId'] == 2):
        return JsonResponse({"result": 1, "msg": "系统默认信息无法删除"})
    else:
        if (Jurisdiction >= 2):
            return JsonResponse({"result": 1, "msg": "权限不足，无法删除"})
        else:
            try:
                    hutCourse.objects.filter(hutCourseId=jsonResponse['hutCourseId']).delete()
            except :
                return JsonResponse({"result": 1, "msg": "未知错误"})
            else:
                return JsonResponse({"result": 0, "msg": "删除成功"})



# 课程评价
def test_course_evl(request):
    from .hutModel import courseEvaluate,hutCourse,hutProjectsUsers

    jsonResponse = json.loads(request.body.decode('utf-8'))
    print (jsonResponse,type(jsonResponse))
    dataLists = courseEvaluate.objects.all().count()
    courseGet = hutCourse.objects.get(hutCourseId=jsonResponse['hutCourseId'])
    userGet = hutProjectsUsers.objects.get(id=jsonResponse['userid'])
    try:
    # 这里需要单独create
        if(jsonResponse['courseEvaluateMsg'].strip() == ""):
            return JsonResponse({"result": 1, "msg": "评价不能为空"})
        else:
            courseEvaluate.objects.create(userid=userGet,
                            hutCourseId=courseGet,
                            courseEvaluateMsg=jsonResponse['courseEvaluateMsg'],
                            grade=jsonResponse['grade'],
                            courseEvaluateDate=jsonResponse['courseEvaluateDate'],
                            )
    except :
        return JsonResponse({"result": 1, "msg": "评价失败,未知问题，请联系管理员解决"})
    else:
        return JsonResponse({"result": 0, "msg": "评价成功"})


def test_course_evlGet(request):
    from .hutModel import courseEvaluate,hutCourse,hutProjectsUsers
    jsonResponse = json.loads(request.body.decode('utf-8'))
    # print(jsonResponse)
    print("最新课程评价")
    print(jsonResponse)
    if(jsonResponse["sendPage"]):
        pastJson = courseEvaluate.objects.all()[jsonResponse["sendPage"]*10-10:jsonResponse["sendPage"]*10]
    else:
        pastJson = courseEvaluate.objects.all()[1 * 10 - 10:1 * 10]
    lists = []
    # print(pastJson[1].__dict__)
    # print(pastJson[1].__dict__['userid'])
    for i in range(len(pastJson)):
        lists.append({
            'courseEvaluateId': pastJson[i].__dict__['courseEvaluateId'],
            'courseEvaluateMsg': pastJson[i].__dict__['courseEvaluateMsg'],
            "userName": hutProjectsUsers.objects.get(id=pastJson[i].__dict__['userid_id']).userName,
            "courseNmae":hutCourse.objects.get(hutCourseId=pastJson[i].__dict__['hutCourseId_id']).hutCourseName,
            'grade': pastJson[i].__dict__['grade'],
            'courseEvaluateDate': pastJson[i].__dict__['courseEvaluateDate'],
        })
    # print (lists)
    return JsonResponse({"allDateLength": courseEvaluate.objects.all().count(), "msg": lists})





# 用户通知
def test_user_notice(request):
    from .hutModel import hutNotice,hutProjectsUsers

    jsonResponse = json.loads(request.body.decode('utf-8'))
    print("通知")
    print (jsonResponse,type(jsonResponse))
    dataLists = hutNotice.objects.all().count()
    # courseGet = hutProjectsUsers.objects.get(hutCourseId=jsonResponse['hutCourseId'])
    userGet = hutProjectsUsers.objects.get(id=jsonResponse['hutUserId'])
    try:
    # 这里需要单独create
        if(jsonResponse['courseEvaluateMsg'].strip() == ""):
            return JsonResponse({"result": 1, "msg": "评价不能为空"})
        else:
            hutNotice.objects.create(
                            hutNoticeUser=userGet,
                            msg=jsonResponse['courseEvaluateMsg'],
                            byPerson=jsonResponse['userName'],
                            courseEvaluateDate=jsonResponse['courseEvaluateDate'],
                            )
    except :
        return JsonResponse({"result": 1, "msg": "评价失败,未知问题，请联系管理员解决"})
    else:
        return JsonResponse({"result": 0, "msg": "评价成功"})


def queryset_to_json(queryset):
    obj_arr = []
    for o in queryset:
        obj_arr.append(o.toDict())
    return obj_arr

def test_user_getNotice(request):
    from .hutModel import hutNotice,hutProjectsUsers
    jsonResponse = json.loads(request.body.decode('utf-8'))
    # print(jsonResponse)
    pastJson =  queryset_to_json(hutNotice.objects.filter(hutNoticeUser=jsonResponse['userId']))
    pastJsonLength = len(pastJson)
    jsonLists = []
    if(len(pastJson) == 0):
        return JsonResponse({"result": 1, "msg": "为空"})
    else:
        if (jsonResponse["sendPage"]):
            pastJson =  pastJson[jsonResponse["sendPage"]*3-3:jsonResponse["sendPage"]*3]
            for i in range(len(pastJson)):
                jsonLists.append(
                    {"content": pastJson[i]["msg"],
                     "byPerson": pastJson[i]["byPerson"],
                     "time": pastJson[i]["courseEvaluateDate"],
                     }
                )
        else:
            pastJson =  pastJson[0:3]
            for i in range(len(pastJson)):
                jsonLists.append(
                    {"content": pastJson[i]["msg"],
                     "byPerson": pastJson[i]["byPerson"],
                     "time": pastJson[i]["courseEvaluateDate"],
                     }
                )
        return JsonResponse({"result": 0, "msg": jsonLists,"allDateLength": pastJsonLength})













# def test_user_add(request):
#     from .models import users
#     # jsonResponse = json.load(request.body)
#     jsonResponse = json.loads(request.body.decode('utf-8'))
#     print (jsonResponse,type(jsonResponse))
#     dataLists = users.objects.all().count()
#     try:
#         if(dataLists >20):
#            return JsonResponse({"result": 0, "msg": "增加失败,用户数目不能超过20人"})
#         else:
#             users.objects.create(**jsonResponse)
#     except :
#         return JsonResponse({"result": 1, "msg": "增加失败,用户名重复/信息不完整"})
#     else:
#         return JsonResponse({"result": 0, "msg": "增加成功"})
#
# def test_user_mod(request):
#     from .models import users
#     jsonResponse = json.loads(request.body.decode('utf-8'))
#     print (jsonResponse, type(jsonResponse))
#     print (jsonResponse['id'])
#     if(jsonResponse['id'] == 1 or jsonResponse['id'] == 2):
#         return JsonResponse({"result": 1, "msg": "此用户信息不可修改，请修改第二条之后的信息】"})
#     elif(jsonResponse['password'].strip() ==''):
#         return JsonResponse({"result": 1, "msg": "密码不能为空"})
#     else:
#         try:
#             users.objects.filter(id=jsonResponse['id']).update(
#                 userName=jsonResponse['userName'],
#                 jurisdiction=jsonResponse['jurisdiction'],
#                 password=jsonResponse['password'],
#                 remarks=jsonResponse['remarks'],
#                 roles=jsonResponse['roles'],
#                 status=jsonResponse['status']
#             )
#         except:
#             return JsonResponse({"result": 1, "msg": "修改失败，用户名重复/信息不完整"})
#         else:
#             return JsonResponse({"result": 0, "msg": "修改成功"})
#
#
# # 用户部分信息修改
# def test_user_updata(request):
#     from .models import users
#     print(request.body.decode('utf-8'))
#     print("____-")
#     jsonResponse = json.loads(request.body.decode('utf-8'))
#     # print (jsonResponse, type(jsonResponse))
#     print ("____-")
#     print (jsonResponse['id'],type(jsonResponse['id']))
#     if(jsonResponse['id'] == '1' or jsonResponse['id'] == '2'):
#         return JsonResponse({"result": 1, "msg": "此用户信息不可修改，请修改第二条之后的信息"})
#     elif (jsonResponse['password'].strip() == ''):
#         return JsonResponse({"result": 1, "msg": "密码不能为空"})
#     else:
#             try:
#                 users.objects.filter(id=jsonResponse['id']).update(
#                     userName=jsonResponse['userName'],
#                     password=jsonResponse['password'],
#                     remarks=jsonResponse['remarks'],
#                     roles=jsonResponse['roles'],
#                 )
#             except:
#                 return JsonResponse({"result": 1, "msg": "修改失败，用户名重复/信息不完整"})
#             else:
#                 return JsonResponse({"result": 0, "msg": "修改成功"})
#
# def test_userTou_mod(request):
#     from .models import users,file_delete
#     # print(request.FILES)
#     # print (request.FILES['croppedImg'])
#     obj = request.FILES.get("croppedImg")
#     print (obj, type(obj), obj.name, obj.chunks())
#     print (obj.file,obj.field_name,obj.name, obj.content_type,
#                   obj.size, obj.charset, obj.content_type_extra)
#     userId = int(request.POST.__getitem__('userId'))
#     userName = request.POST.__getitem__('userName')
#     print (userId,type(userId),userName)
#     from django.core.files.base import ContentFile
#     # 读取上传的文件中的video项为二进制文件
#     file_content = ContentFile(request.FILES['croppedImg'].read())
#     # # ImageField的save方法，第一个参数是保存的文件名，第二个参数是ContentFile对象，里面的内容是要上传的图片、视频的二进制内容
#     if(userId == 1 or userId == 2):
#         return  JsonResponse({"result": 1, "msg": "此用户信息不可更改,请更改自己的用户信息"})
#     else:
#         mymodel = users.objects.get(id=userId)
#         # 删除之前的图片，避免 图片冗杂
#         file_delete(users, mymodel)
#         mymodel.userTou.save(request.FILES['croppedImg'].name+'_'+userName+'.png', file_content)
#         return JsonResponse({"result": 0, "msg": "用户头像修改成功"})
#



# 课程信息
# def test_machine_type_get(request):
#     from .models import machTypes
#     jsonResponse = json.loads(request.body.decode('utf-8'))
#     # print (jsonResponse["sendPage"])
#     try:
#         pastJson = queryset_to_json(machTypes.objects.all()[jsonResponse["sendPage"] * 10 - 10:jsonResponse["sendPage"] * 10])
#     except:
#         #  获得全部数据 便于下拉选择
#         pastJson = queryset_to_json(machTypes.objects.all()[:])
#     return JsonResponse({"allDateLength": machTypes.objects.all()[:].count(), "msg": pastJson})
#
# def test_machine_type_add(request):
#     from .models import machTypes
#     # jsonResponse = json.load(request.body)
#     jsonResponse = json.loads(request.body.decode('utf-8'))
#     print (jsonResponse,type(jsonResponse))
#     print (jsonResponse['machTypeName'])
#     dataLists = machTypes.objects.all().count()
#     try:
#         if(dataLists >20):
#            return JsonResponse({"result": 0, "msg": "增加失败，上限为20个"})
#         else:
#             machTypes.objects.create(**jsonResponse)
#     except :
#         return JsonResponse({"result": 1, "msg": "增加失败,设备类型名重复/信息不完整"})
#     else:
#      return JsonResponse({"result": 0, "msg": "增加成功"})
#
# def test_machine_type_mod(request):
#     from .models import machTypes
#     jsonResponse = json.loads(request.body.decode('utf-8'))
#     # print (jsonResponse, type(jsonResponse))
#     # print (jsonResponse['machTypeId'])
#     try:
#         machTypes.objects.filter(machTypeId=jsonResponse['machTypeId']).update(
#             machTypeName=jsonResponse['machTypeName'],
#             machTypeDesc=jsonResponse['machTypeDesc'])
#     except:
#         return JsonResponse({"result": 1, "msg": "修改失败，设备类型名重复/信息不完整"})
#     else:
#         return JsonResponse({"result": 0, "msg": "修改成功"})
#
# def test_machine_type_del(request):
#     from .models import machTypes
#     jsonResponse = json.loads(request.body.decode('utf-8'))
#     # print (jsonResponse,type(jsonResponse))
#     # print (jsonResponse['machTypeId'])
#     dataLists = machTypes.objects.all().count()
#     try:
#         if (dataLists <= 2):
#             return JsonResponse({"result": 1, "msg": "删除失败,数据至少要存在2条"})
#         else:
#             machTypes.objects.filter(machTypeId=jsonResponse['machTypeId']).delete()
#     except :
#         return JsonResponse({"result":1, "msg": "删除失败"})
#     else:
#      return JsonResponse({"result": 0, "msg": "删除成功"})


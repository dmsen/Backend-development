
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from dmseng.settings import MEDIA_ROOT, THUMB_SIZE
import os
from libs.images import make_thumb

from django.db.models.fields.files import ImageFieldFile
# Create your models here.

class Tag(models.Model):
    """标签"""
    tag_name_en = models.CharField(max_length=128, verbose_name="标签en")
    tag_name_cn = models.CharField(max_length=128, verbose_name="标签cn")

    def __str__(self):
        return self.tag_name_cn

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class LinkCategory(models.Model):
    """链接分类"""
    link_category_name_en = models.CharField(max_length=128, verbose_name="链接分类en")
    link_category_name_cn = models.CharField(max_length=128, verbose_name="链接分类cn")

    def __str__(self):
        return self.link_category_name_cn

    class Meta:
        verbose_name = "链接分类"
        verbose_name_plural = verbose_name


class InformationClassification(models.Model):
    """项目分类"""
    info_name_en = models.CharField(max_length=128, verbose_name="项目分类en")
    info_name_cn = models.CharField(max_length=128, verbose_name="项目分类cn")

    def __str__(self):
        return self.info_name_cn

    class Meta:
        verbose_name = "项目分类"
        verbose_name_plural = verbose_name

class Article(models.Model):
    """文章信息"""
    article_title = models.CharField(max_length=128, verbose_name='文章标题')
    article_cover = models.ImageField(upload_to='./article/%Y/%m%d/', verbose_name='文章封面',default='./article/defaultpic.jpg')
    article_cover_sm = models.ImageField(upload_to='./article/%Y/%m%d/', verbose_name='缩略图',default='./article/defaultpic_sm.jpg')

    article_information_classification = models.ForeignKey(InformationClassification, verbose_name="项目分类")
    article_tag = models.ManyToManyField(Tag, verbose_name="标签", related_name='article_set') # related_name : modelname_set
    article_abstract = models.CharField(max_length=128,blank=True,null=True, verbose_name='文章摘要')
    # 文章详情用富文本
    article_content =RichTextUploadingField(verbose_name="文章详情")
    publish_date = models.DateTimeField(auto_now_add=True,verbose_name='更新时间')
    view_times = models.IntegerField(default=0, verbose_name="浏览次数")
    is_notice = models.BooleanField(default=False, verbose_name="开启公告", help_text="如果为True, 在首页公告显示")
    is_case = models.BooleanField(default=False, verbose_name="经典案例")
    is_business_evaluation = models.BooleanField(default=False, verbose_name="阿里商评")
    is_recommend = models.BooleanField(default=False, verbose_name="小研推荐")

    def increase_views(self):
        self.view_times += 1
        self.save(update_fields=['view_times'])
    def __str__(self):
        return self.article_title

    def save(self, *args, **kwargs):
        # 将上传的图片先保存
        super().save()
        base, ext = os.path.splitext(self.article_cover.name)
        # 从头像中生成缩略图
        thumb_pixbuf = make_thumb(os.path.join(MEDIA_ROOT, self.article_cover.name), size=THUMB_SIZE)
        # 缩略图的保存文件全路径
        thumb_path = os.path.join(MEDIA_ROOT, base + f'.{THUMB_SIZE}x{THUMB_SIZE}' + ext)
        # 缩略图相对路径
        relate_thumb_path = os.path.join('/'.join(self.article_cover.name.split('/')[:-1]), os.path.basename(thumb_path))
        relate_thumb_path = base + f'.{THUMB_SIZE}x{THUMB_SIZE}' + ext
        # 保存缩略图
        thumb_pixbuf.save(thumb_path)
        # 保存字段值
        self.article_cover_sm = ImageFieldFile(self, self.article_cover_sm, relate_thumb_path)
        super().save() # 再保存一下，包括缩略图等

    class Meta:
        verbose_name = "项目表"
        verbose_name_plural = verbose_name
        ordering = ["-publish_date"]


class Guid(models.Model):
    """导航信息"""
    guid_name = models.CharField(max_length=128, verbose_name="导航名")
    tag = models.ForeignKey(Tag, verbose_name="相关tag")
    guid_enable = models.BooleanField(default=True, verbose_name="是否启用")

    class Meta:
        verbose_name = "导航信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.guid_name


class Emailmsg(models.Model):
    username = models.CharField(max_length=128, verbose_name="用户名")
    email = models.EmailField(max_length=26,verbose_name='邮箱')
    message = models.TextField(max_length=200,verbose_name='信息')
    class Meta:
        verbose_name = "简历邮箱信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username


class  Notice(models.Model):
    title = models.CharField(verbose_name='标题',max_length=30)
    abstract = models.CharField(verbose_name='摘要',max_length=30)
    article_content = RichTextUploadingField(verbose_name="文章详情")
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name ="公告"
        verbose_name_plural = verbose_name






# vue 霖 数据库
 # 删除之前的图片，避免 图片冗杂 需要导入的东西
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
# 用户
class users(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='用户id')
    userName = models.CharField(max_length=10, verbose_name='用户名',unique=True)
    password = models.CharField(max_length=30, verbose_name='密码')
    userTou = models.ImageField(upload_to='./user/%Y/%m%d/', verbose_name='用户头像',
                                      default='./user/defaultTou.png')
    USER_CHOICE = (
        (0, 0),
        (1, 1),
        (2,2),
        (3,3)
    )
    USER_STATUS = (
        (0, 0),
        (1, 1),
    )
    roles = models.CharField(max_length=10, verbose_name='职位',default="搬砖工")
    jurisdiction = models.IntegerField(choices=USER_CHOICE, verbose_name='权限等级',default=1)
    status = models.IntegerField(choices=USER_STATUS, verbose_name='用户状态',default=1)
    remarks = models.CharField(max_length=10, verbose_name='remarks')
    # def __str__(self):
    #     return self.userName
    def toDict(self):
        return dict([(attr, getattr(self, attr)) for attr in
                     [f.name for f in self._meta.fields]])  # type(self._meta.fields).__name__
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        db_table = '用户'
        ordering = ['id']

# 删除之前的图片，避免 图片冗杂
@receiver(pre_delete, sender=users)
# sender = 你要修改图片字段所在的类
def file_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    # print('进入文件删除方法，删的是',instance.alter_file)
    instance.userTou.delete(False)

# 客户
class customers(models.Model):
    customerId= models.AutoField(primary_key=True,verbose_name = '顾客id')
    customerName= models.CharField(max_length=10,verbose_name = '顾客名',unique=True)
    customerType= models.CharField(max_length = 30,verbose_name = '顾客类型')
    CHOICE = (
        (1, 1),
        (1, 0),
    )
    customerLevel= models.IntegerField(choices=CHOICE,verbose_name = '顾客等级')
    sponsor= models.CharField(max_length = 6,verbose_name = '赞助商')
    phone= models.CharField(max_length=11,verbose_name = '联系电话')
    address= models.CharField(max_length = 10,verbose_name = '地址')
    machCount= models.IntegerField(verbose_name = '机器数目')
    remark= models.CharField(max_length=10,verbose_name = 'remark')
    def __str__(self):
        return self.customerName
    def toDict(self):
        return dict([(attr, getattr(self, attr)) for attr in
                     [f.name for f in self._meta.fields]])  # type(self._meta.fields).__name__
    class Meta:
        verbose_name = "客户"
        verbose_name_plural = verbose_name
        db_table = '客户'
        ordering = ['customerId']


# 机器类型
class machTypes(models.Model):
    machTypeId = models.AutoField(primary_key=True, verbose_name='机器类型id')
    machTypeCode = models.CharField(max_length=10, verbose_name='机器类型编号', default="defaultTypeCode")
    machTypeName = models.CharField(max_length=10, verbose_name='机器类型名称',unique=True)
    machTypeDesc = models.CharField(max_length=30, verbose_name='机器类型描述')

    def __str__(self):
        return self.machTypeCode

    def toDict(self):
        return dict([(attr, getattr(self, attr)) for attr in
                     [f.name for f in self._meta.fields]])  # type(self._meta.fields).__name__

    class Meta:
        verbose_name = "机器类型"
        verbose_name_plural = verbose_name
        db_table = '机器类型'
        ordering = ['machTypeId']
# 设备
class machines(models.Model):
    import django.utils.timezone as timezone
    # AutoField :自增型字段（值自增）----int
    machineId= models.AutoField(primary_key=True,verbose_name = '机器id') #合法
    # CharField 文本型字段---》varchar
    # 必填项：max_length:最大字符长度（max_length将在数据库层和Django表单验证中起作用）
    machineName= models.CharField(max_length=10,verbose_name = '机器名称',unique=True)
    # IntegerField()：整型字段
    # machTypeId= models.IntegerField(max_length=10,verbose_name = '机器类型id')
    machTypeId = models.ForeignKey(machTypes, verbose_name='机器类型id',related_name='machine_machTypeId')
    # machTypeId = models.OneToOneField(machTypes, verbose_name='机器类型id')
    machineDesc = models.TextField(max_length = 30,verbose_name = '机器描述')
    # DateField :日期型字段
    # DateTimeField： 日期时间型字段
    #二个属性
    #auto_now_add: insert 的时候会更新这个字段
    # auto_now:insert/update 的时候会更新这个值
    dataOfProdect= models.DateTimeField(default = timezone.now,verbose_name = '生产日期')
    office = models.CharField(max_length = 10,verbose_name = '办事处')
    mwordId = models.IntegerField(verbose_name = 'mworkid',default=1)
    customerName = models.ForeignKey(customers, verbose_name='客户',related_name='customers_customerName')
    # def __str__(self):
    #     return self.machineName

    def toDict(self):
        return dict([(attr, getattr(self, attr)) for attr in
                     [f.name for f in self._meta.fields]])  # type(self._meta.fields).__name__
    class Meta:
        verbose_name = "机器/设备"
        verbose_name_plural = verbose_name
        db_table = '设备'
        ordering = ['machineId']



# 所有监测点
class IOPoints_all(models.Model):
    IOPId = models.AutoField(primary_key=True, verbose_name='监测点')
    IOPName= models.CharField(max_length = 30,verbose_name = '监测点名',unique = True)

    def __str__(self):
        return self.IOPName
    class Meta:
        verbose_name = "所有监测点"
        verbose_name_plural = verbose_name
        db_table = '所有监测点'
        ordering = ['IOPId']
# 所有网关
class  gateways_all(models.Model):
    gatewayId = models.AutoField(primary_key=True, verbose_name='网关Id')
    gatewayName= models.CharField(max_length = 30,verbose_name = '网关名',unique = True)
    IOPNames = models.ManyToManyField(IOPoints_all,verbose_name = '监测点名',related_name='iopname')
    def __str__(self):
        return self.gatewayName

    def toDict(self):
        return dict([(attr, getattr(self, attr)) for attr in
                     [f.name for f in self._meta.fields]])  # type(self._meta.fields).__name__
    class Meta:
        verbose_name = "所有网关"
        verbose_name_plural = verbose_name
        db_table = '所有网关'
        ordering = ['gatewayId']
# 机器监测点
class IOPoints(models.Model):
    IOPointsId= models.AutoField(primary_key=True,verbose_name = '机器监测点id')
    physicalName = models.CharField(max_length = 16,verbose_name = '机器监测点物理名称',unique = True)
    machineName = models.ForeignKey(machines,verbose_name = '机器名')
    machineGateway = models.ForeignKey(gateways_all,verbose_name = '网关')
    minRange = models.IntegerField(verbose_name = '最小量程',null = True,blank = True,default = 0)
    maxRange = models.IntegerField(verbose_name='最大量程', null=False, blank=False)
    aline = models.IntegerField(verbose_name='校准值', null=True,blank = True)
    method = models.IntegerField(verbose_name='计算方式', null=True,blank = True,default = 1)
    def toDict(self):
        return dict([(attr, getattr(self, attr)) for attr in
                     [f.name for f in self._meta.fields]])  # type(self._meta.fields).__name__
    def __str__(self):
        return self.physicalName
    class Meta:
        verbose_name = "所有机器监测点"
        verbose_name_plural = verbose_name
        db_table = '所有机器监测点'
        ordering = ['IOPointsId']

# 异常码
class alarmCodes(models.Model):
    alarmCodeId= models.CharField(max_length = 16,primary_key=True,verbose_name = '异常码id',unique = True)
    alarmCodeName = models.CharField(max_length = 16,verbose_name = '异常码名字')
    machineName = models.ForeignKey(machines,verbose_name = '机器名')
    physicalName = models.ForeignKey(IOPoints, verbose_name='监控点物理量')
    minValue = models.IntegerField(verbose_name = '最小值',null = False,blank = False,default = 0)
    maxValue = models.IntegerField(verbose_name='最大值', null=False, blank=False)
    alarmMsg = models.CharField(max_length = 36,verbose_name='异常信息', null=True,blank = True)
    level = models.IntegerField(verbose_name='异常级别', null=True,blank = True,default = 1)
    timeLimit = models.IntegerField(verbose_name='异常时延', null=True, blank=True, default=10)
    # def __str__(self):
    #     return self.alarmCodeName
    def toDict(self):
        return dict([(attr, getattr(self, attr)) for attr in
                     [f.name for f in self._meta.fields]])  # type(self._meta.fields).__name__
    class Meta:
        verbose_name = "异常码"
        verbose_name_plural = verbose_name
        db_table = '异常码'
        ordering = ['alarmCodeId']

#  单个异常记录
class singleAlarmCodes(models.Model):
    import django.utils.timezone as timezone
    singleAlarmCodeId= models.AutoField(primary_key=True,verbose_name = '单个异常记录id')
    machineName = models.ForeignKey(machines,verbose_name = '机器名')
    alarmCodeName = models.ForeignKey(alarmCodes, verbose_name='异常码名字')
    startTime= models.DateTimeField(default = timezone.now,verbose_name = '开始时间')
    duration = models.IntegerField(verbose_name='持续时间', null=True, blank=True, default=10)
    singleAlarmCodeStatus = models.IntegerField(verbose_name='异常记录状态', default=0)
    def toDict(self):
        return dict([(attr, getattr(self, attr)) for attr in
                     [f.name for f in self._meta.fields]])  # type(self._meta.fields).__name__
    class Meta:
        verbose_name = "单个异常记录"
        verbose_name_plural = verbose_name
        db_table = '单个异常记录'
        ordering = ['singleAlarmCodeId']

#  解决方案
class alarmSolutons(models.Model):
    alarmSolutonId= models.AutoField(primary_key=True,verbose_name = '解决方案id')
    alarmSolutonName = models.CharField(max_length = 32,verbose_name = '解决方案名称',unique=True)
    alarmSolutonDetail = models.CharField(max_length = 32, verbose_name='解决方案描述')
    alarmCodeList= models.TextField(verbose_name = '适用与异常码/组合码')
    def toDict(self):
        return dict([(attr, getattr(self, attr)) for attr in
                     [f.name for f in self._meta.fields]])  # type(self._meta.fields).__name__
    class Meta:
        verbose_name = "解决方案"
        verbose_name_plural = verbose_name
        db_table = '解决方案'
        ordering = ['alarmSolutonId']

#  异常处理历史
class alarmProcessHistory(models.Model):
    alarmProcessHistoryId= models.AutoField(primary_key=True,verbose_name = '异常处理历史id')
    alarmCode = models.CharField(max_length=16, verbose_name='异常码编号', null=True, blank=True)
    alarmCodeName = models.CharField(max_length = 16,verbose_name = '异常码名称',null=True,blank=True)
    alarmSolutonId = models.CharField(max_length=32, verbose_name='解决方案编号', null=True, blank=True)
    # alarmSolutonName = models.CharField(max_length = 32, verbose_name='解决方案名称',null=True,blank=True)
    callbackMsg= models.TextField(verbose_name = '反馈信息',null=True,blank=True)
    processTime = models.DateTimeField(auto_now_add = True, verbose_name='处理时间')
    machineName = models.CharField(max_length = 16, verbose_name='机器名称',null=True,blank=True)
    def toDict(self):
        return dict([(attr, getattr(self, attr)) for attr in
                     [f.name for f in self._meta.fields]])  # type(self._meta.fields).__name__
    class Meta:
        verbose_name = "异常处理历史"
        verbose_name_plural = verbose_name
        db_table = '异常处理历史'
        ordering = ['alarmProcessHistoryId']


# # 网关
# class dataCongfigs(models.Model):
#     configId= models.AutoField(primary_key=True,verbose_na
#       e = '网关id')·
# ield(max_length = 30,verbose_name = '网关')
#     ioc= models.CharField(max_length = 30,verbose_name = 'ioc')
#     physicalName= models.CharField(max_length = 30,verbose_name = '物理名称')
#     minLC= models.IntegerField(max_length=10,verbose_name = '最小量程')
#     maxLC= models.IntegerField(max_length=10,verbose_name = '最大量程')
#     aline= models.IntegerField(max_length=10,verbose_name = '校准值')
#     method= models.IntegerField(max_length=10,verbose_name = '计算方法')
#     token = models.CharField(max_length = 10,verbose_name = 'token')






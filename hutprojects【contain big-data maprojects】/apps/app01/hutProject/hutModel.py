from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver



class hutProjectsUsers(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='用户id')
    userName = models.CharField(max_length=10, verbose_name='用户名',unique=True)
    password = models.CharField(max_length=30, verbose_name='密码')
    userTou = models.ImageField(upload_to='./hutUser/%Y/%m%d/', verbose_name='用户头像',
                                      default='./hutUser/defaultTou.png')
    USER_CHOICE = (
        (0, 0),
        (1, 1),
        (2,2),
        (3, 3),
    )
    USER_STATUS = (
        (0, 0),
        (1, 1),
    )
    jurisdiction = models.IntegerField(choices=USER_CHOICE, verbose_name='权限等级',default=1)
    status = models.IntegerField(choices=USER_STATUS, verbose_name='用户状态',default=1)
    remarks = models.CharField(max_length=10, verbose_name='remarks')
    # hutNotice = models.ForeignKey(hutNotice ,verbose_name='通知',related_name='hutNotice',null = True,blank = True)
    # def __str__(self):
    #     return self.userName
    def toDict(self):
        return dict([(attr, getattr(self, attr)) for attr in
                     [f.name for f in self._meta.fields]])  # type(self._meta.fields).__name__
    class Meta:
        verbose_name = "湖工大软件工程系统用户"
        verbose_name_plural = verbose_name
        db_table = '湖工大软件工程系统用户'
        ordering = ['id']
# 删除之前的图片，避免 图片冗杂
@receiver(pre_delete, sender=hutProjectsUsers)
# sender = 你要修改图片字段所在的类
def file_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    # print('进入文件删除方法，删的是',instance.alter_file)
    instance.userTou.delete(False)


class hutNotice(models.Model):
    """通知"""
    import django.utils.timezone as timezone
    hutNoticeId = models.AutoField(primary_key=True, verbose_name='通知id')
    msg  = models.TextField(max_length=200,verbose_name='通知内容')
    CHOICE = (
        (0, 0),
        (1, 1),
    )
    status =  models.IntegerField(choices=CHOICE,verbose_name = '通知状态',default=0)
    courseEvaluateDate = models.DateTimeField(default=timezone.now, verbose_name='通知时间')
    byPerson = models.CharField(verbose_name='发布通知者',default="lin",max_length=10)
    hutNoticeUser = models.ForeignKey(hutProjectsUsers, verbose_name='通知人' )
    class Meta:
        verbose_name = "湖工大软件工程系统通知"
        verbose_name_plural = verbose_name
        db_table = '湖工大软件工程系统通知'
    def toDict(self):
        return dict([(attr, getattr(self, attr)) for attr in
                     [f.name for f in self._meta.fields]])

class hutCourse(models.Model):
    """课程信息"""
    hutCourseId = models.AutoField(primary_key=True, verbose_name='课程id')
    hutCourseName =  models.CharField(max_length=16, verbose_name="课程名")
    hutCourseDescribe = models.CharField(max_length=16, verbose_name="课程描述")
    hutCourseTeacher = models.CharField(max_length=16, verbose_name="任课老师")
    class Meta:
        verbose_name = "湖工大软件工程系统课程信息"
        verbose_name_plural = verbose_name
        db_table = '湖工大软件工程系统课程信息'





class courseEvaluate(models.Model):
    """课程评价"""
    import django.utils.timezone as timezone
    courseEvaluateId = models.AutoField(primary_key=True, verbose_name='课程评价id')
    courseEvaluateMsg = models.TextField(max_length=200,verbose_name="课程评价" ,null = True,blank = False)
    hutCourseId = models.ForeignKey(hutCourse, verbose_name="课程id", related_name='hutCourseId_courseId')
    userid = models.ForeignKey(hutProjectsUsers, verbose_name='用户id', related_name='hutProjectsUsersId')
    grade = models.FloatField(verbose_name="评分", default=5 )
    courseEvaluateDate = models.DateTimeField(default = timezone.now,verbose_name = '评价时间')
    class Meta:
        verbose_name = "湖工大软件工程系统课程评价"
        verbose_name_plural = verbose_name
        db_table = '湖工大软件工程系统课程评价'
        ordering = ('-courseEvaluateDate',)
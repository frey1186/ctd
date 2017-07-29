from django.db import models
from django.contrib.auth.models import User as DjangoUser
# Create your models here.


class Process(models.Model):
    check_date = models.DateField('检查日期', auto_now=True)
    process_name = models.CharField('项目名称', max_length=128, )
    zb_file = models.FileField('招标文件', upload_to='uploads')
    tb_file_in = models.FileField('投标文件', upload_to='uploads')
    lowmistake_check = models.BooleanField('低级错误检查', default=True)
    filestyle_check = models.BooleanField('文件格式检查', default=True)
    wrongword_check = models.BooleanField('错别字检查', default=True)
    tbprice_check = models.BooleanField('投标价格检查', default=True)
    tb_file_out = models.FilePathField('投标文件下载', blank=True, null=True)
    check_result = models.TextField('检查结果', blank=True, null=True)

    def __str__(self):
        return '<%s-%s>' % (self.check_date, self.process_name)



class UserProfile(models.Model):
    '''
    用户表
    '''
    user = models.OneToOneField(DjangoUser)
    name = models.CharField(u'姓名', max_length=16, )
    role = models.CharField(u'角色', max_length=16,
                            blank=True, null=True)
    memo = models.CharField(u'说明', max_length=255,
                            blank=True, null=True)

    def __str__(self):
        # return  the username of the User
        return '%s(%s)' % (self.user.username, self.name)


class TechContent(models.Model):
    '''
    技术方案目录标题表
    '''
    name = models.CharField(u'标题名', max_length=16)
    level = models.IntegerField(u'标题级别')
    memo = models.TextField(u'备注')
    uptitle = models.ForeignKey('self', verbose_name=u'上级标题', null=True)
    user = models.ForeignKey(UserProfile, verbose_name=u'属主',)

    def __str__(self):
        return self.name


class PartTemplate(models.Model):
    '''
    分块内容模版
    如：技术培训部分，现场培训部分，原厂培训部分
    '''
    name = models.CharField(u'模版名称', max_length=16)
    content = models.ForeignKey( TechContent, verbose_name=u'对应目录',)
    tempfile = models.FileField(u'模版文件', upload_to='uploads/temp')
    memo = models.TextField(u'备注')
    change_time = models.DateTimeField(u'模版修改时间', auto_now=True)
    user = models.ForeignKey(UserProfile, verbose_name=u'属主', )

    def __str__(self):
        return '<%s-%s>' % (self.change_time, self.name)


class TechTemplate(models.Model):
    '''
    技术方案模版表
    '''
    name = models.CharField(u'模版名称', max_length=16)
    tech_content = models.ManyToManyField(TechContent, verbose_name=u'目录')
    memo = models.TextField(u'备注')
    change_time = models.DateTimeField(u'模版修改时间', auto_now=True)
    user = models.ForeignKey(UserProfile, verbose_name=u'属主', )

    def __str__(self):
        return self.name

class SubmitFile(models.Model):
    '''
    提交表
    '''
    project_name = models.CharField(u'项目名称', max_length=32)
    profile = models.FileField(u'配置文件', upload_to='uploads/profile')
    tech_template = models.ForeignKey(TechTemplate, verbose_name=u'技术方案模版',)
    submit_time = models.DateTimeField(u'提交时间', auto_now=True)
    download_file = models.FilePathField(u'文件下载')
    user = models.ForeignKey(UserProfile, verbose_name=u'属主', )

    def __str__(self):
        return '<%s-%s>' % (self.submit_time, self.project_name)



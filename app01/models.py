from django.db import models

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

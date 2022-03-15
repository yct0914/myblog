from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField('用户名', max_length=20)
    password = models.CharField('密码', max_length=50)
    nickname = models.CharField('昵称', max_length=50)
    email = models.EmailField('邮箱')
    create_date = models.DateTimeField('创建时间',auto_now_add=True)
    update_date = models.DateTimeField('更新时间', auto_now=True)
    def __str__(self) -> str:
        return self.username
    class Meta:
        db_table = 'User'
        managed = True
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        
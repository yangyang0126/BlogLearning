from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
import markdown
from django.utils.html import strip_tags
from mdeditor.fields import MDTextField

# 制作日历
import calendar


# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Category(models.Model):
    
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
@python_2_unicode_compatible
class Post(models.Model):  

    # 文章标题
    title = models.CharField(max_length=70)

    # 文章正文，我们使用了 TextField
    body = MDTextField()

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    
    # 获取具体年份、月份、日期，用于首页显示
    def get_year(self):
        return self.created_time.year

    def get_month(self):
        month = self.created_time.month    
        return calendar.month_abbr[month]
        
    def get_day(self):
        return self.created_time.day     
    
    
        
    # 文章摘要
    # excerpt = models.CharField(max_length=200, blank=True)
    excerpt = MDTextField()
    
    # 文章首图
    firstimage = models.CharField(max_length=200, blank=True)

    # 这是分类与标签
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章浏览量
    views = models.PositiveIntegerField(default=0)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    
    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # 指定文章排序方式
    # -代表逆序排列
    class Meta:
        ordering = ['-created_time']
    
    # 自动保存文章摘要     
    def save(self, *args, **kwargs):    
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)


    

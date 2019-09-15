# -*- coding: utf-8 -*-
"""
设置模板标签
"""
from django import template
from ..models import Post, Category, Tag
from django.db.models.aggregates import Count
import os

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    """获取最新的5篇文章"""
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    """归档"""
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    # 记得在顶部引入 count 函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    # 记得在顶部引入 Tag model
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    
@register.simple_tag
def get_foodpicture_1():
  
    abspath = os.getcwd()
    filePath = abspath + "\\blog\\static\\images_food\\1\\"
    title = []
    path = []
    for EveryPath in os.listdir(filePath):
        title.append(EveryPath[:-4])
        path.append("static\\images_food\\1\\"+EveryPath)
    return zip(title,path)
    
@register.simple_tag
def get_foodpicture_2():
  
    abspath = os.getcwd()
    filePath = abspath + "\\blog\\static\\images_food\\2\\"
    title = []
    path = []
    for EveryPath in os.listdir(filePath):
        title.append(EveryPath[:-4])
        path.append("static\\images_food\\2\\"+EveryPath)
    return zip(title,path)
    
    
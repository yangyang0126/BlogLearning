# -*- coding: utf-8 -*-
"""
设置模板标签
"""
from django import template
from ..models import Post, Category

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
    """分类"""
    return Category.objects.all()
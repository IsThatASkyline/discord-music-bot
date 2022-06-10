from django import template
from django.db.models import *
from tasks.models import Category
from tasks.forms import CreateCategoryForm
from django.shortcuts import render, redirect

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('tasks/list_categories.html', takes_context=True )
def show_categories(context):
    request = context['request']
    form = CreateCategoryForm
    user_id = request.user.id
    categories = Category.objects.annotate(cnt=Count('tasks', filter=Q(tasks__user_id__exact=user_id)))

    return {"categories": categories, "form": form}



# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: urls.py
# author: ScCcWe
# time: 2020/8/20 23:04

from django.conf.urls import url, include
from .views import add_book, show_books

urlpatterns = [
    url('add_book', add_book),
    url('show_book', show_books),
]

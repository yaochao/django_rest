#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/4/6

from hello_rest.models import Book
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Book(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        return instance


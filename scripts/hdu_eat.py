#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""今天吃什么"""
import random
c = {'第一餐厅':['麻辣香锅','牛肉面','水饺','麻辣烫'],'第二餐厅':['石锅拌饭','铁板饭','黄焖鸡','煲仔饭'],'第三餐厅':['烤肉饭','砂锅','炒饭'],'第五餐厅':['烧腊','肠粉','煎饼果子'],'美食城':['烤鱼','烤串','螺蛳粉']}
x = {'弗雷德广场':['外婆家','新白鹿','一点点','古茗'],'宝龙广场':['太二酸菜鱼','西贝','喜茶','奈雪'],'高沙商业街':['烤鱼烧烤','小龙虾','串串香','火锅'],'金沙印象城':['哥老官','绿茶','弄堂里','喜姐炸串']}
def r():
    return f"【食堂】{random.choice(list(c.keys()))} -> {random.choice(random.choice(list(c.values())))}\n【下沙】{random.choice(list(x.keys()))} -> {random.choice(random.choice(list(x.values())))}"
print(r())

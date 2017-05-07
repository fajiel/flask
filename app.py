#!/usr/bin/python
# coding=utf-8

import re
import time
import random
from flask import Flask, render_template, jsonify, request, redirect, url_for
from datas import get_data


app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def hello_world():
    """
    折线图/柱状图页面
    """
    return render_template('index.html')


@app.route('/contrast')
def contrast():
    """
    三家数据折线图/柱状图页面
    """
    # 计算数据

    return render_template('contrast.html')

@app.route('/worldcloud')
def worldcloud():
    """
    词云图页面
    """
    datas = get_data("worldcloud")
    data_list = []
    for i in range(len(datas[0])):
        data_list.append({"name": datas[0][i], "value": datas[1][i]})
    print data_list
    # 计算数据
    name_list = [item['name'].encode('utf-8') for item in data_list]
    return render_template('woldcloud.html', data_list=data_list, name_list=name_list)


@app.route('/get_item', methods=["POST"])
def get_item():
    """
    弹幕数据发送
    img: 'static/heisenberg.png' //图片
    info: '弹幕文字信息' //文字
    font-size: 23 // 字体大小
    href: 'http://www.yaseng.org' //链接
    close: true //显示关闭按钮
    speed: 8 //延迟,单位秒,默认8
    bottom: 70 //距离底部高度,单位px,默认随机
    color: '#fff' //颜色,默认白色
    old_ie_color: '#000000' //ie低版兼容色,不能与网页背景相同,默认黑色
    """
    item_list = []
    # 生成随机颜色
    color = '1234567890abcdef'
    choice = random.choice
    for i in range(10):
        item_i = {
            'img': '../static/img/' + random.choice(['JD.ico', 'tmall.ico', 'weibo.ico']),
            'info': random.choice([u"正向内容", u"负向内容"]),
            'size': 15,
            'href': '/',
            'close': False,
            'speed': random.randint(12, 20),
            'bottom': random.randint(100, 400),
            'old_ie_color': '#000000',
        }
        info_color = {u"正向内容": '#FF0000', u"负向内容": '#00688B'}
        item_i['color'] =info_color[item_i['info']]
        item_list.append(item_i)

    if request.method == "POST":
        return jsonify(data=item_list)


@app.route('/realtime')
def real_time():
    """
    弹幕页面
    """
    return render_template('realtime.html')


@app.route('/get_date', methods=["POST"])
def overview_app():
    """
    折线图数据发送
    """
    if request.method == "POST":
        return jsonify(data=[[320, 332, 301, 334, 390, 330, 320], [120, 132, 101, 134, 90, 230, 210]])


@app.route('/get_contrast', methods=["POST"])
def contrast_data():
    """
    三个品牌折线图数据发送
    """
    if request.method == "POST":
        data = get_data("contrast_data")
        # 保留三位小数
        data_t = [[round(i, 3) for i in i_list] for i_list in data]
        return jsonify(data=data_t)


@app.route('/worldcloud_data/<date>')
def worldcloud_data(date):
    """
    词语图数据源展示页面
    """
    # return render_template('index.html')
    worldcloud_date = 234
    return render_template('show_data.html', date=date, list=worldcloud_date)


@app.route('/source_data/<date>')
def source_data(date):
    """
    数据折线图数据源展示页面
    """
    # return render_template('index.html')
    date_list = [230, 234]
    return render_template('show_data.html', date=date, list=date_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
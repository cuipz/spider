# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ViewItem(scrapy.Item):
    #city:
    city_id = scrapy.Field()#ok
    city_name = scrapy.Field()#ok
    city_state = scrapy.Field()#ok
    city_view_number = scrapy.Field()#ok
    city_comment_number = scrapy.Field()
    city_href = scrapy.Field()#ok
    #view:
    view_id = scrapy.Field()#ok
    view_name = scrapy.Field()#ok
    view_ename = scrapy.Field()#ok
    view_type = scrapy.Field()#ok
    view_isHot = scrapy.Field()
    view_city_l = scrapy.Field()#ok
    view_view_l = scrapy.Field()
    view_comment_number = scrapy.Field()#ok
    view_score = scrapy.Field()#ok
    view_addr = scrapy.Field()#ok
    view_photo_number = scrapy.Field()#ok
    view_jianjie = scrapy.Field()#ok
    view_isWeb = scrapy.Field()#ok
    view_phone = scrapy.Field()#ok
    view_isEmail = scrapy.Field()#ok
    view_href = scrapy.Field()#ok
    #comment
    com_id = scrapy.Field()#ok
    com_view = scrapy.Field()#ok
    com_date_p = scrapy.Field()#ok
    com_date = scrapy.Field()#ok
    com_user_id = scrapy.Field()#ok
    com_score = scrapy.Field()#ok
    com_g = scrapy.Field()#ok
    com_number = scrapy.Field()
    com_title = scrapy.Field()#ok
    com_detail = scrapy.Field()#ok
    com_isCopy = scrapy.Field()
    com_copy_detail = scrapy.Field()
    #comment user
    user_id = scrapy.Field()#ok
    user_name = scrapy.Field()#ok
    user_g = scrapy.Field()#ok
    user_join_time = scrapy.Field()#ok
    user_isVip = scrapy.Field()
    user_from_city = scrapy.Field()#ok
    user_comment_tui_number = scrapy.Field()
    user_comment_share = scrapy.Field()#ok
    user_city_number = scrapy.Field()
    user_photo_number = scrapy.Field()#ok
    #h_around
    h_id = scrapy.Field()#ok
    h_name = scrapy.Field()#ok
    h_dis = scrapy.Field()#ok
    h_view = scrapy.Field()#ok
    #res_around
    res_id = scrapy.Field()#ok
    res_name = scrapy.Field()#ok
    res_dis = scrapy.Field()#ok
    res_view = scrapy.Field()#ok
    #view_around
    v_id = scrapy.Field()#ok
    v_name = scrapy.Field()#ok
    v_dis = scrapy.Field()#ok
    v_view = scrapy.Field()#ok
    
    sign = scrapy.Field()

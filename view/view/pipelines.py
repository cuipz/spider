# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ViewPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(host='localhost',user='root',password='212316',db='spider',port=3306)
        self.cursor = self.connect.cursor()
    
    def process_item(self, item, spider):
        '''
        print(item['city_name'])
        if item['city_name'] != None:
            sql_city = 'INSERT INTO city(city_name,city_state,city_view_number) VALUE (%s,%s,%s)'
            data_city = [item['city_name'],item['city_state'],item['city_view_number']]
            try:
                self.cursor.execute(sql_city,(data_city))
                self.connect.commit()
            except Exception as e:
                print('err:' + e)
                self.connect.rollback()
        '''
        print(item['view_name'] + "view")
        if item['view_name'] != None:
            sql_view = 'INSERT INTO view(view_name,view_ename,view_type,view_city_l,view_comment_number,view_score,view_addr,view_photo_number,view_jianjie,view_isWeb,view_phone,view_isEmail) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            data_view = [item['view_name'],item['view_ename'],item['view_type'],item['view_city_l'],item['view_comment_number'],item['view_score'],item['view_addr'],item['view_photo_number'],item['view_jianjie'],item['view_isWeb'],item['view_phone'],item['view_isEmail']]
            try:
                self.cursor.execute(sql_view,(data_view))
                self.connect.commit()
                print("ok")
            except Exception as e:
                print('err:' + e)
                self.connect.rollback()
        
        print(item['com_view'] + "comment")
        if item['com_view'] != None:
            sql_comment = 'INSERT INTO comment(com_view,com_date_p,com_date,com_user_id,com_score,com_title,com_detail,com_g) VALUE (%s,%s,%s,%s,%s,%s,%s,%s)'
            data_comment = [item['com_view'],item['com_date_p'],item['com_date'],item['com_user_id'],item['com_score'],item['com_title'],item['com_detail'],item['com_g']]
            try:
                self.cursor.execute(sql_comment,(data_comment))
                self.connect.commit()
                print("ok")
            except Exception as e:
                print('err:' + e)
                self.connect.rollback()
        
        print(item['user_name'])
        if item['user_name'] != None:
            sql_user = 'INSERT INTO comment_user(user_name,user_g,user_join_time,user_from_city,user_comment_tui_number,user_comment_share,user_photo_number) VALUE (%s,%s,%s,%s,%s,%s,%s)'
            data_user = [item['user_name'],item['user_g'],item['user_join_time'],item['user_from_city'],item['user_comment_tui_number'],item['user_comment_share'],item['user_photo_number']]
            try:
                self.cursor.execute(sql_user,(data_user))
                self.connect.commit()
                print("ok")
            except Exception as e:
                print('err:' + e)
                self.connect.rollback()
            
        print(item['h_name'])
        if item['h_name'] != None:
            sql_around_h = 'INSERT INTO hotel_around(h_name,h_dis,h_view) VALUE (%s,%s,%s)'
            data_around_h = [item['h_name'],item['h_dis'],item['h_view']]
            try:
                self.cursor.execute(sql_around_h,(data_around_h))
                self.connect.commit()
                print("ok")
            except Exception as e:
                print('err:' + e)
                self.connect.rollback()
            
        print(item['res_name'])
        if item['res_name'] != None:
            sql_around_res = 'INSERT INTO res_around(res_name,res_dis,res_view) VALUE (%s,%s,%s)'
            data_around_res = [item['res_name'],item['res_dis'],item['res_view']]
            try:
                self.cursor.execute(sql_around_res,(data_around_res))
                self.connect.commit()
                print("ok")
            except Exception as e:
                print('err:' + e)
                self.connect.rollback()
            
        print(item['v_name'])
        if item['v_name'] != None:
            sql_around_view = 'INSERT INTO view_around(v_name,v_dis,v_view) VALUE (%s,%s,%s)'
            data_around_view = [item['v_name'],item['v_dis'],item['v_view']]
            try:
                self.cursor.execute(sql_around_view,(data_around_view))
                self.connect.commit()
                print("ok")
            except Exception as e:
                print('err:' + e)
                self.connect.rollback()
        
        return item
        
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()

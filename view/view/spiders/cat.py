# -*- coding: utf-8 -*-
import scrapy
import time
from view.items import ViewItem

class CatSpider(scrapy.Spider):
    name = 'cat'
    allowed_domains = ['tripadvisor.cn']
    start_urls = ['https://www.tripadvisor.cn/Attractions-g294211-Activities-oa20-China.html']
    
    def __init__(self):
        self.item = ViewItem()
        self.item['city_href'] = None
        self.item['city_name'] = None
        self.item['city_state'] = None
        self.item['view_name'] = None
        self.item['view_href'] = None
        self.item['view_ename'] = None
        self.item['view_type'] = None
        self.item['view_city_l'] = None
        self.item['city_view_number'] = None
        self.item['view_comment_number'] = None
        self.item['view_score'] = None
        self.item['view_addr'] = None
        self.item['view_photo_number'] = None
        self.item['view_jianjie'] = None
        self.item['view_isWeb'] = None
        self.item['view_phone'] = None
        self.item['view_isEmail'] = None
        self.item['com_view'] = None
        self.item['com_date_p'] = None
        self.item['com_date'] = None
        self.item['com_user_id'] = None
        self.item['com_score'] = 0
        self.item['com_g'] = None
        self.item['com_title'] = None
        self.item['com_detail'] = None
        self.item['h_name'] = None
        self.item['h_dis'] = None
        self.item['res_name'] = None
        self.item['res_dis'] = None
        self.item['v_name'] = None
        self.item['v_dis'] = None
        self.item['user_name'] = None
        self.item['user_g'] = None
        self.item['user_join_time'] = None
        self.item['user_from_city'] = None
        self.item['user_comment_tui_number'] = None
        self.item['user_comment_share'] = None
        self.item['user_photo_number'] = None
        self.city_view_number = 0
    
    def parse(self, response):
        views = response.xpath('//ul[@class="geoList"]/li')
        for view in views:
            item = self.item
            item['city_href'] = view.xpath('a/@href').extract_first()
            if item['city_href'] != None:
                yield scrapy.Request("https://www.tripadvisor.cn" + item['city_href'], meta={'item': item}, callback=self.parse_city_view)
            else:
                print("city_error")
            
        
        next_link = response.xpath('//a[@class="guiArw sprite-pageNext  pid0"]/@href').extract_first()
        yield scrapy.Request("https://www.tripadvisor.cn" + next_link, callback=self.parse)
        
    
    def parse_city_view(self, response):
        item = response.meta['item']
        item['city_name'] = response.xpath('//*[@id="taplc_trip_planner_breadcrumbs_0"]/ul/li[4]/a/span/text()').extract_first()
        item['city_state'] = response.xpath('//*[@id="taplc_trip_planner_breadcrumbs_0"]/ul/li[3]/a/span/text()').extract_first()
        
        city_views = response.xpath('//div[@class="attraction_element"]')
        for city_view in city_views:
            self.city_view_number += 1
            item['view_href'] = city_view.xpath('.//div[@class="listing_title "]/a/@href').extract_first()
            if item['view_href'] != None:
                yield scrapy.Request("https://www.tripadvisor.cn" + item['view_href'], meta={'item': item}, callback=self.parse_city_view_d)
            else:
                print("view_error")
            
        
        next_link = response.xpath('//div[@class="unified pagination "]/a[@class="nav next rndBtn ui_button primary taLnk"]/@href').extract_first()
        if next_link != None:
            yield scrapy.Request("https://www.tripadvisor.cn" + next_link, meta={'item': item}, callback=self.parse_city_view)
        else:
            item['city_view_number'] = str(self.city_view_number)
            self.city_view_number = 0
            #yield item
        
    
    def parse_city_view_d(self, response):
        item = response.meta['item']
        #view
        item['view_ename'] = response.xpath('//h1[@id="HEADING"]/div/text()').extract_first()
        item['view_type'] = response.xpath('//*[@id="taplc_resp_attraction_header_ar_responsive_0"]/div/div[1]/div/span/div/a/text()').extract_first()
        item['view_city_l'] = response.xpath('//*[@id="taplc_resp_attraction_header_ar_responsive_0"]/div/div[1]/div/div[2]/div/span/b/span/text()').extract_first()
        item['view_comment_number'] = response.xpath('//*[@id="taplc_location_detail_reviews_card_0"]/div[2]/a[2]/text()').extract_first()[:-3]
        item['view_score'] = response.xpath('//*[@id="taplc_location_detail_reviews_card_0"]/div[2]/span/text()').extract_first()
        item['view_addr'] = response.xpath('//*[@id="taplc_resp_attraction_header_ar_responsive_0"]/div/div[2]/div/div[1]/div/div/span[2]/text()').extract_first() + response.xpath('//*[@id="taplc_resp_attraction_header_ar_responsive_0"]/div/div[2]/div/div[1]/div/div/span[2]/span[1]/text()').extract_first() + response.xpath('//*[@id="taplc_resp_attraction_header_ar_responsive_0"]/div/div[2]/div/div[1]/div/div/span[2]/span[2]/text()').extract_first()
        item['view_photo_number'] = response.xpath('//*[@id="taplc_resp_photo_mosaic_ar_responsive_0"]/div/div[4]/div[2]/div[2]/span/span[2]/text()').extract_first()[7:-2]
        item['view_jianjie'] = response.xpath('//*[@id="component_6"]/div/div[2]/span[1]/text()').extract_first()
        view_name = response.xpath('//*[@id="HEADING"]/text()').extract_first()
        item['view_name'] = view_name
        view_isWeb = response.xpath('//*[@id="taplc_location_detail_contact_card_ar_responsive_0"]/div[3]/div[2]/div[1]/div/span[2]/text()').extract_first()
        if view_isWeb != None:
            item['view_isWeb'] = "有"
        else:
            item['view_isWeb'] = "无"
        
        item['view_phone'] = response.xpath('//*[@id="taplc_location_detail_contact_card_ar_responsive_0"]/div[3]/div[2]/div[2]/div/text()').extract_first()
        view_isEmail = response.xpath('//*[@id="taplc_location_detail_contact_card_ar_responsive_0"]/div[3]/div[2]/div[4]/div/span[2]/text()').extract_first()
        if view_isEmail != None:
            item['view_isEmail'] = "有"
        else:
            item['view_isEmail'] = "无"
        
        yield item
        
        print("------------------------------------------")
        #comment
        view_comments = response.xpath('//div[@class="review-container"]')
        for view_comment in view_comments:
            item['com_view'] = view_name
            item['com_date_p'] = view_comment.xpath('.//div[@class="prw_rup prw_reviews_stay_date_hsx"]/text()').extract_first()
            item['com_date'] = view_comment.xpath('.//span[@class="ratingDate"]/@title').extract_first()
            item['com_user_id'] = view_comment.xpath('.//div[@class="info_text"]/div[1]/text()').extract_first()
            item['com_score'] = str(int(view_comment.xpath('.//div[@class="reviewSelector"]/div/div[2]/span[1]/@class').extract_first()[-2:])/10)
            item['com_g'] = view_comment.xpath('.//span[@class="helpful_text"]/span[2]/text()').extract_first()
            item['com_title'] = view_comment.xpath('.//span[@class="noQuotes"]/text()').extract_first()
            item['com_detail'] = view_comment.xpath('.//div[@class="prw_rup prw_reviews_text_summary_hsx"]/div/p/text()').extract_first()
            yield item
            if item['com_user_id'] != None:
                yield scrapy.Request("https://www.tripadvisor.cn/members/" + item['com_user_id'], meta={'item': item}, callback=self.parse_user)
            else:
                print("user_error")
        
        #h_around
        h_arounds = response.xpath('//div[@id="taplc_resp_hr_nearby_ar_responsive_0"]/div[1]/div[@class="grids is-shown-at-tablet"]/div[1]/div/div[@class="prw_rup prw_common_btf_nearby_poi_entry ui_column is-6 poiTile"]')
        for h_around in h_arounds:
            item['h_name'] = h_around.xpath('.//div[@class="poiName"]/text()').extract_first()
            item['h_dis'] = h_around.xpath('.//div[@class="distance"]/text()').extract_first()
            item['h_view'] = view_name
            yield item
            
        #res_around
        res_arounds = response.xpath('//div[@id="taplc_resp_hr_nearby_ar_responsive_0"]/div[1]/div[@class="grids is-shown-at-tablet"]/div[2]/div/div[@class="prw_rup prw_common_btf_nearby_poi_entry ui_column is-6 poiTile"]')
        for res_around in res_arounds:
            item['res_name'] = res_around.xpath('.//div[@class="poiName"]/text()').extract_first()
            item['res_dis'] = res_around.xpath('.//div[@class="distance"]/text()').extract_first()
            item['res_view'] = view_name
            yield item
            
        #view_around
        view_arounds = response.xpath('//div[@id="taplc_resp_hr_nearby_ar_responsive_0"]/div[1]/div[@class="grids is-shown-at-tablet"]/div[3]/div/div[@class="prw_rup prw_common_btf_nearby_poi_entry ui_column is-6 poiTile"]')
        for view_around in view_arounds:
            item['v_name'] = view_around.xpath('.//div[@class="poiName"]/text()').extract_first()
            item['v_dis'] = view_around.xpath('.//div[@class="distance"]/text()').extract_first()
            item['v_view'] = view_name
            yield item
        
    
    def parse_user(self, response):
        item = response.meta['item']
        #user
        item['user_name'] = response.xpath('//*[@id="MODULES_MEMBER_CENTER"]/div[1]/div[1]/div[1]/div/div/span/text()').extract_first()
        item['user_g'] = response.xpath('//*[@id="MODULES_MEMBER_CENTER"]/div[2]/div[2]/div[2]/div/span/text()').extract_first()
        item['user_join_time'] = response.xpath('//*[@id="MODULES_MEMBER_CENTER"]/div[1]/div[1]/div[2]/div[1]/p/text()').extract_first()
        item['user_from_city'] = response.xpath('//*[@id="MODULES_MEMBER_CENTER"]/div[1]/div[1]/div[2]/div[2]/p/text()').extract_first()
        item['user_comment_tui_number'] = response.xpath('//*[@id="MODULES_MEMBER_CENTER"]/div[1]/div[2]/div/ul/li[4]/a/text()').extract_first()
        item['user_comment_share'] = response.xpath('//*[@id="MODULES_MEMBER_CENTER"]/div[1]/div[2]/div/ul/li[1]/a/text()').extract_first()
        item['user_photo_number'] = response.xpath('//*[@id="MODULES_MEMBER_CENTER"]/div[1]/div[2]/div/ul/li[2]/a/text()').extract_first()
        yield item
    

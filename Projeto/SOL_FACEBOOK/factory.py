#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SOL_FACEBOOK import user
from SOL_FACEBOOK import cover_photo
from SOL_FACEBOOK import education
from SOL_FACEBOOK import experience
from SOL_FACEBOOK import page
from SOL_FACEBOOK import video
from SOL_FACEBOOK import post

class Factory:
    """
    Essa classe será responsável por criar objetos a partir de dicionários
    """

    @staticmethod
    def user(dictionary: dict) -> user.User:
        a_user = user.User()
        if ("id") in dictionary:
            a_user.id = dictionary["id"]
        if ("about") in dictionary:
            a_user.about = dictionary["about"]
        if ("bio") in dictionary:
            a_user.bio = dictionary["bio"]
        if ("birthday") in dictionary:
            a_user.birthday = dictionary["birthday"]
        if ("cover") in dictionary:
            a_user.cover = Factory.cover_photo(dictionary=dictionary["cover"])
        if ("education") in dictionary:
            for i in dictionary["education"]:
                a_user.education.append(Factory.education(dictionary=i))
        if ("email") in dictionary:
            a_user.email = dictionary["email"]
        if ("favorite_athletes") in dictionary:
            for i in dictionary["favorite_athletes"]:
                a_user.favorite_athletes.append(Factory.experience(dictionary=i))
        if ("favorite_teams") in dictionary:
            for i in dictionary["favorite_teams"]:
                a_user.favorite_teams.append(Factory.experience(dictionary=i))
        if ("first_name") in dictionary:
            a_user.first_name = dictionary["first_name"]
        if ("gender") in dictionary:
            a_user.gender = dictionary["gender"]
        if ("hometown") in dictionary:
            a_user.hometown = Factory.page(dictionary=dictionary["hometown"])
        if ("inspirational_people") in dictionary:
            for i in dictionary["inspirational_people"]:
                a_user.inspirational_people.append(Factory.experience(dictionary=i))
        if ("interested_in") in dictionary:
            a_user.interested_in = dictionary["interested_in"]
        if ("languages") in dictionary:
            for i in dictionary["languages"]:
                a_user.languages.append(Factory.experience(dictionary=i))
        if ("last_name") in dictionary:
            a_user.last_name = dictionary["last_name"]
        if ("locale") in dictionary:
            a_user.locale = dictionary["locale"]
        if ("location") in dictionary:
            a_user.location = Factory.page(dictionary=dictionary["location"])
        if ("meeting_for") in dictionary:
            a_user.meeting_for = dictionary["meeting_for"]
        if ("middle_name") in dictionary:
            a_user.middle_name = dictionary["middle_name"]
        if ("name") in dictionary:
            a_user.name = dictionary["name"]
        if ("name_format") in dictionary:
            a_user.name_format = dictionary["name_format"]
        if ("political") in dictionary:
            a_user.political = dictionary["political"]
        if ("quotes") in dictionary:
            a_user.quotes = dictionary["quotes"]
        if ("relationship_status") in dictionary:
            a_user.relationship_status = dictionary["relationship_status"]
        if ("religion") in dictionary:
            a_user.religion = dictionary["religion"]
        if ("significant_other") in dictionary:
            a_user.significant_other = Factory.user(dictionary=dictionary["significant_other"])
        if ("sports") in dictionary:
            for i in dictionary["sports"]:
                a_user.sports.append(Factory.experience(dictionary=i))
        if ("timezone") in dictionary:
            a_user.timezone = dictionary["timezone"]
        if ("video_upload_limits") in dictionary:
            a_user.video_upload_limits = dictionary["video_upload_limits"]
        if ("viewer_can_send_gift") in dictionary:
            a_user.viewer_can_send_gift = dictionary["viewer_can_send_gift"]
        if ("website") in dictionary:
            a_user.website = dictionary["website"]
        if ("relationship") in dictionary:
            a_user.relationship = dictionary["relationship"]
        if ("work") in dictionary:
            for i in dictionary["work"]:
                a_user.work.append(Factory.experience(dictionary=i))
        return a_user

    @staticmethod
    def cover_photo(dictionary: dict) -> cover_photo.Cover_Photo:
        a_cover_photo = cover_photo.Cover_Photo
        if ("id" in dictionary):
            a_cover_photo.id = dictionary["id"]
        if ("cover_id" in dictionary):
            a_cover_photo.cover_id = dictionary["cover_id"]
        if ("offset_x" in dictionary):
            a_cover_photo.offset_x = dictionary["offset_x"]
        if ("offset_y" in dictionary):
            a_cover_photo.offset_y = dictionary["offset_y"]
        if ("source" in dictionary):
            a_cover_photo.source = dictionary["source"]
        return a_cover_photo

    @staticmethod
    def education(dictionary: dict) -> education.Eduction:
        a_education = education.Eduction()
        if ("id" in dictionary):
            a_education.id = dictionary["id"]
        if ("classes" in dictionary):
            for experience in dictionary["classes"]:
                a_education.classes.append(Factory.experience(dictionary=dictionary["classes"]))
        if ("concentration" in dictionary):
            for page in dictionary["concentration"]:
                a_education.concentration.append(Factory.page(dictionary=dictionary["concentration"]))
        if ("degree" in dictionary):
            a_education.degree = Factory.page(dictionary=dictionary["degree"])
        if ("school" in dictionary):
            a_education.school = Factory.page(dictionary=dictionary["school"])
        if ("type" in dictionary):
            a_education.type = dictionary["type"]
        if ("with" in dictionary):
            for user in dictionary["with"]:
                a_education.with_.append(Factory.user(dictionary=dictionary["with"]))
        if ("year" in dictionary):
            a_education.year = Factory.page(dictionary=dictionary["year"])
        return a_education

    @staticmethod
    def experience(dictionary: dict) -> experience.Experience:
        a_experience = experience.Experience
        if ("id" in dictionary):
            a_experience.id = dictionary["id"]
        if ("description" in dictionary):
            a_experience.description = dictionary["description"]
        if ("from" in dictionary):
            a_experience.from_ = Factory.user(dictionary=dictionary["from"])
        if ("name" in dictionary):
            a_experience.name = dictionary["name"]
        if ("with" in dictionary):
            for user in dictionary["with"]:
                a_experience.with_.append(Factory.user(dictionary=dictionary["with"]))
        return a_experience

    @staticmethod
    def page(dictionary: dict) -> page.Page:
        a_page = page.Page
        if ("id" in dictionary):
            a_page.id = dictionary["id"]
        if ("about" in dictionary):
            a_page.about = dictionary["about"]
        if ("access_token" in dictionary):
            a_page.token = dictionary["access_token"]
        if ("best_page" in dictionary):
            a_page.best_page = Factory.page(dictionary=dictionary["best_page"])
        if ("category" in dictionary):
            a_page.category = dictionary["category"]
        if ("category_list" in dictionary):
            a_page.category_list = dictionary["category_list"]
        if ("contact_address" in dictionary):
            a_page.contact_address = dictionary["contact_address"]
        if ("country_page_likes" in dictionary):
            a_page.country_page_likes = dictionary["country_page_likes"]
        if ("cover" in dictionary):
            a_page.cover = Factory.cover_photo(dictionary=dictionary["cover"])
        if ("current_location" in dictionary):
            a_page.current_location = dictionary["current_location"]
        if ("description" in dictionary):
            a_page.description = dictionary["description"]
        if ("emails" in dictionary):
            a_page.emails = dictionary["emails"]
        if ("fan_count" in dictionary):
            a_page.likes = dictionary["fan_count"]
        if ("features" in dictionary):
            a_page.features = dictionary["features"]
        if ("featured_video" in dictionary):
            a_page.featured_video = Factory.video(dictionary=dictionary["featured_video"])
        if ("general_info" in dictionary):
            a_page.general_info = dictionary["general_info"]
        if ("is_permanently_closed" in dictionary):
            a_page.is_permanently_closed = dictionary["is_permanently_closed"]
        if ("is_published" in dictionary):
            a_page.is_published = dictionary["is_published"]
        if ("is_unclaimed" in dictionary):
            a_page.is_unclaimed = dictionary["is_unclaimed"]
        if ("is_verified" in dictionary):
            a_page.is_verified = dictionary["is_verified"]
        if ("leadgen_tos_accepted" in dictionary):
            a_page.leadgen_tos_accepted = dictionary["leadgen_tos_accepted"]
        if ("link" in dictionary):
            a_page.link = dictionary["link"]
        if ("location" in dictionary):
            a_page.location = dictionary["location"]
        if ("name" in dictionary):
            a_page.name = dictionary["name"]
        if ("new_like_count" in dictionary):
            a_page.new_like_count = dictionary["new_like_count"]
        if ("parent_page" in dictionary):
            a_page.parent_page = Factory.page(dictionary=dictionary["parent_page"])
        if ("phone" in dictionary):
            a_page.phone = dictionary["phone"]
        if ("single_line_address" in dictionary):
            a_page.single_line_address = dictionary["single_line_address"]
        if ("store_number" in dictionary):
            a_page.store_number = dictionary["store_number"]
        if ("username" in dictionary):
            a_page.username = dictionary["username"]
        if ("website" in dictionary):
            a_page.website = dictionary["website"]
        return a_page

    @staticmethod
    def video(dictionary: dict) -> video.Video:
        a_video = video.Video
        if ("id" in dictionary):
            a_video.id = dictionary["id"]
        if ("created_time" in dictionary):
            a_video.created_time = dictionary["created_time"]
        if ("description" in dictionary):
            a_video.description = dictionary["description"]
        if ("embed_html" in dictionary):
            a_video.embed_html = dictionary["embed_html"]
        if ("format" in dictionary):
            a_video.format = dictionary["format"]
        if ("from" in dictionary):
            a_video.from_ = dictionary["from"]
        if ("icon" in dictionary):
            a_video.icon = dictionary["icon"]
        if ("length" in dictionary):
            a_video.length = dictionary["length"]
        if ("permalink_url" in dictionary):
            a_video.permalink_url = dictionary["permalink_url"]
        if ("picture" in dictionary):
            a_video.picture = dictionary["picture"]
        if ("place" in dictionary):
            a_video.place = dictionary["place"]
        if ("privacy" in dictionary):
            a_video.privacy = dictionary["privacy"]
        if ("source" in dictionary):
            a_video.source = dictionary["source"]
        if ("status" in dictionary):
            a_video.status = dictionary["status"]
        if ("updated_time" in dictionary):
            a_video.updated_time = dictionary["updated_time"]
        return a_video

    @staticmethod
    def feed_targeting(dictionary: dict) -> post.Feed_targeting:
        a_feed = post.Feed_targeting()
        if "age_max" in dictionary:
            a_feed.age_max = dictionary["age_max"]
        if "age_min" in dictionary:
            a_feed.age_min = dictionary["age_min"]
        if "genders" in dictionary:
            a_feed.genders = dictionary["genders"]
        if "geo_locations" in dictionary:
            a_feed.geo_locations = dictionary["geo_locations"]
        if "locales" in dictionary:
            a_feed.locales = dictionary["locales"]
        if "education_statuses" in dictionary:
            a_feed.education_statuses = dictionary["education_statuses"]
        if "fan_of" in dictionary:
            a_feed.fan_of = dictionary["fan_of"]
        if "relationship_statuses" in dictionary:
            a_feed.relationship_statuses = dictionary["relationship_statuses"]
        return a_feed

    @staticmethod
    def post(dictionary: dict) -> post.Post:
        a_post=post.Post()
        if ("id" in dictionary):
            a_post.id = dictionary["id"]
        if ("admin_creator" in dictionary):
            for i in dictionary["admin_creator"]:
                a_post.admin_creator.append(i)
        if ("caption" in dictionary):
            a_post.caption = dictionary["caption"]
        if ("created_time" in dictionary):
            a_post.created_time = dictionary["created_time"]
        if ("description" in dictionary):
            a_post.description = dictionary["description"]
        if ("feed_targeting" in dictionary):
            a_post.feed_targeting = Factory.feed_Targeting(dictionary=dictionary["feed_targeting"])
        if ("from" in dictionary):
            a_post.from_ = Factory.user(dictionary=dictionary["from"])
        if ("icon" in dictionary):
            a_post.icon = dictionary["icon"]
        if ("is_hidden" in dictionary):
            a_post.is_hidden = dictionary["is_hidden"]
        if ("is_published" in dictionary):
            a_post.is_published = dictionary["is_published"]
        if ("link" in dictionary):
            a_post.link = dictionary["link"]
        if ("message" in dictionary):
            a_post.message = dictionary["message"]
        if ("message_tags" in dictionary):
            a_post.message_tags = dictionary["message_tags"]
        if ("name" in dictionary):
            a_post.name = dictionary["name"]
        if ("object_id" in dictionary):
            a_post.object_id = dictionary["object_id"]
        if ("parent_id" in dictionary):
            a_post.parent_id = dictionary["parent_id"]
        if ("picture" in dictionary):
            a_post.picture = dictionary["picture"]
        if ("place" in dictionary):
            a_post.place = dictionary["place"]
        if ("privacy" in dictionary):
            a_post.privacy = dictionary["privacy"]
        if ("properties" in dictionary):
            for i in dictionary["properties"]:
                a_post.properties.append(i)
        if ("shares" in dictionary):
            a_post.shares = dictionary["shares"]
        if ("source" in dictionary):
            a_post.source = dictionary["source"]
        if ("status_type" in dictionary):
            a_post.status_type = dictionary["status_type"]
        if ("story" in dictionary):
            a_post.story = dictionary["story"]
        if ("story_tags" in dictionary):
            a_post.story_tags = dictionary["story_tags"]
        if ("targeting" in dictionary):
            a_post.targeting = dictionary["targeting"]
        if ("to" in dictionary):
            for i in dictionary["to"]:
                a_post.to.append(Factory.user(dictionary=i))
        if ("type" in dictionary):
            a_post.type = dictionary["type"]
        if ("updated_time" in dictionary):
            a_post.updated_time = dictionary["updated_time"]
        if ("with_tags" in dictionary):
            a_post.with_tags = dictionary["with_tags"]
        if a_post.type == "video":
            a_post.video=video.Video()
            a_post.video.id=a_post.object_id
            a_post.video.source=a_post.source
        if a_post.type == "photo":
            a_post.image=a_post.source
        return a_post

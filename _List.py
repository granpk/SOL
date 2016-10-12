__author__ = 'Joao'
import _Actions
import lib.tweepy as tweepy
import _Access
import _Tweet
class List:
     def __init__(self, dictionary=dict()):
         self.subscriber_count=""
         self.user=""
         self.mode=""
         self._api=""
         self.name=""
         self.id_str=""
         self.member_count=""
         self.full_name=""
         self.id=""
         self.slug=""
         self.uri=""
         self.description=""
         self.created_at=""
         self.following=""
         if ("subscriber_count" in dictionary):
             self.subscriber_count=dictionary["subscriber_count"]
         if ("user" in dictionary):
             self.user=dictionary["user"]
         if ("mode" in dictionary):
             self.mode=dictionary["mode"]
         if ("_api" in dictionary):
             self._api=dictionary["_api"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("id_str" in dictionary):
             self.id_str=dictionary["id_str"]
         if ("member_count" in dictionary):
             self.member_count=dictionary["member_count"]
         if ("full_name" in dictionary):
             self.full_name=dictionary["full_name"]
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("slug" in dictionary):
             self.slug=dictionary["slug"]
         if ("uri" in dictionary):
             self.uri=dictionary["uri"]
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("created_at" in dictionary):
             self.created_at=dictionary["created_at"]
         if ("following" in dictionary):
             self.following=dictionary["following"]

     def getTweets(self,max_id=None, count=None, include_rts=None,Access : _Access.WeakAccess = None):
         return _Actions.Actions.getTweetsFromList(owner_screen_name=self.user,slug=self.slug,max_id=max_id,count=count,include_rts=include_rts,Access=Access)

     def postRemoveMember(self,member_id=None, member_screen_name=None,Access : _Access.WeakAccess = None):
        return _Actions.Actions(screen_name=member_screen_name, user_id=member_id, owner_screen_name=self.user,owner_id=None, slug=self.slug, list_id=None)



     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "LIST: "+str(dic)
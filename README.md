#Einsteinish (http://einsteinish.com)
----

We are developing knowledge library for learning Qunatum Universe. The best resources to learn something on the web are scattered and we may waste lot of time. We aim to elinimate this by recommending the best resources.

##Version 1 features

+ Users can share any link of interesting blog post or video in the Resource Section.
+ Resources are divided in topics.
+ Users can share snippets(a shorte blog post) on their wall to share their views and experiences in learning.
+ Users can save interesting resources to their profile for later use.
+ Topic follow button allow users to follow topics to get interesting news, new resources.
+ Explore section lets view the ongoing activity of the site at a glance.

##Later features

+ Moderators and more active users will be able to edit wiki like content in the topics and resources.
+ Tracks will be introduced to give users ability to create content for the their audiences and distribute them.
+ Users can follow other interesting users.


##Tools/Apps Used

+ [Django 1.6.11](https://www.djangoproject.com/)
+ [Twitter Bootstrap](http://getbootstrap.com/)
+ [django-registration](https://django-registration.readthedocs.org/en/latest/)
+ [django-guardian](https://github.com/lukaszb/django-guardian)
+ [django-braces](https://github.com/brack3t/django-braces/)
+ [django-ratings](https://github.com/dcramer/django-ratings/)
+ MySQL (sqlite3 for dev)
+ [django-haystack](http://haystacksearch.org/)
+ [elasticsearch](http://elasticsearch.org/)

*For full requirements, see requirment.txt*


##Install

+ See INSTALL.md for full installation instructions.
+ http://www.einsteinish.com


## Contact

+ [mail us](mailto:contact.einsteinish@gmail.com).

## LICENSE

This project is licensed under [MIT License](http://mit-license.org). See LICENSE.txt

## Note

+ djangoratings-vote : ip-address width = 64. Otherwise, we get the following error: Data truncated for column 'ip_address' at row 1
+ discus comment tool requires registration. 
+ Upgraded to Django 1.8.7 on Jan. 2, 2015 (2 fixes - 1. Import user after loading app, 2. NoReverseMatch for admin delete)

# Einsteinish (http://einsteinish.com)

We are developing knowledge library for learning Qunatum Universe. The best resources to learn something on the web are scattered and we may waste lot of time. We aim to elinimate this by recommending the best resources.

---

![alt text](https://github.com/Einsteinish/Einstein/blob/master/static/img/Blackhole.jpg)

---

## Features

### Current Features

+ Users can share any link of interesting blog post or video in the Resource Section.
+ Resources are divided in topics.
+ Users can share snippets(a shorte blog post) on their wall to share their views and experiences in learning.
+ Users can save interesting resources to their profile for later use.
+ Topic follow button allow users to follow topics to get interesting news, new resources.
+ Explore section lets view the ongoing activity of the site at a glance.

### Planned Features

+ Moderators and more active users will be able to edit wiki like content in the topics and resources.
+ Tracks will be introduced to give users ability to create content for the their audiences and distribute them.
+ Users can follow other interesting users.

---

## Tools/Apps Used

+ [Django 1.8.7](https://www.djangoproject.com/)
+ [Twitter Bootstrap](http://getbootstrap.com/)
+ [django-registration](https://django-registration.readthedocs.org/en/latest/)
+ [django-guardian](https://github.com/lukaszb/django-guardian)
+ [django-braces](https://github.com/brack3t/django-braces/)
+ [django-ratings](https://github.com/dcramer/django-ratings/)
+ MySQL (sqlite3 for dev)
+ [django-haystack](http://haystacksearch.org/)
+ [elasticsearch](http://elasticsearch.org/) : sudo systemctl start elasticsearch (run), sudo systemctl enable elasticsearch (booting time autorun)

*For full requirements, see requirment.txt*

---

## Install

+ See INSTALL.md for full installation instructions.
+ http://www.einsteinish.com

## Contact

+ [mail us](mailto:contact.einsteinish@gmail.com).

## LICENSE

This project is licensed under [MIT License](http://mit-license.org). See LICENSE.txt

---

## Note

+ **Error Handling:** Ensure `ip-address width = 64` to avoid data truncation errors.
+ **Comments:** Disqus comment tool requires registration.
+ **Updates:** 
  + Upgraded to Django 1.8.7 on Jan. 2, 2016 with critical fixes.
  + Introduced thumbnail and video fields to Resources.
  + Switched `upload_to` folder paths to enhance media management.
  + Enabled markdown support for text fields.
+ **Tutorials:** 
  + [Errors and Fixes for einsteinish.com](http://www.bogotobogo.com/python/Django/Python-Django-1.8-collection-of-errors-and-fixes.php)
  + [Using Elasticsearch with einsteinish.com](http://www.bogotobogo.com/python/Django/Python-Django-Haystack-Elasticsearch.php)

## To Do

+ Remote Thumbnail column

# SpiderToBlogKaifulee
Use scrapy to crawl the articals from Kaifulee's Sina blog


## debug note
the parse function in Spider must return item, without which couldn't write file through pipelines
must save the settings.py after updated it. Feed up with pipelines not be loaded
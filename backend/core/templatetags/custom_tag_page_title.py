from django import template
from django.urls import resolve
from django.urls.exceptions import Resolver404
from loguru import logger


register = template.Library()

def get_page_title(url):
    page_title='Dashboard'
    try:
        myfunc, myargs, mykwargs = resolve(url)
        if myfunc:
            page_title=myfunc.__name__.title()
            if "_" in page_title:
                page_title = page_title.replace('_',' ')
            if "Index" in page_title:
                page_title='Dashboard'
            logger.debug("Page Title:> {} ",page_title,feature="f-strings")
    except Resolver404:
        logger.debug("something went wrong",feature="f-strings")
        pass

    return page_title


register.filter('get_page_title', get_page_title)


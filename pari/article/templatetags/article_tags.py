from mezzanine import template

register = template.Library()


@register.inclusion_tag("article/includes/capsule_video.html")
def capsule_video_for(article, width, height):
    return { 'article': article,
             'width': width,
             'height': height,
           }

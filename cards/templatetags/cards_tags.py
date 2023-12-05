from django import template

from cards.models import Card

register = template.Library()

@register.filter
def filter_by_box(cards, box_label):
    return cards.filter(box=box_label)

@register.inclusion_tag("cards/box_links.html")
def boxes_as_links():
    boxes = []
    BOX_CATEGORIES = ['Easy', 'Medium', 'Hard']

    for box_category in BOX_CATEGORIES:
        card_count = Card.objects.filter(box=box_category).count()
        boxes.append({
            "name": box_category,
            "card_count": card_count,
        })

    return {"boxes": boxes}

# def topics_as_links():
#     boxes = []
#     for box_num in BOXES:
#         card_count = Card.objects.filter(box=box_num).count()
#         boxes.append({
#             "number": box_num,
#             "card_count": card_count,
#         })

#     return {"boxes": boxes}
from django import template

from ..models import GroupMember, Group

register = template.Library()


@register.simple_tag()
def get_user_groups(user):
    return GroupMember.objects.filter(
                user=user)

@register.simple_tag
def get_other_groups():
    return Group.objects.all()
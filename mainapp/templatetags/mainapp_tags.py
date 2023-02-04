from django import template

from messageapp.models import Chat

register = template.Library()


@register.simple_tag
def get_unread_messages(user):
    return Chat.objects.unreaded(user=user).filter(members__in=[user.id]).count()


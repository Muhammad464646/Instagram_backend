from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Notification
from posts.models import Like, Post,Comment
from social.models import Follow
@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        liker = instance.user
        if post.user != liker:
            Notification.objects.create(
                user=post.user,           
                from_user=liker,          
                type='like',               
                post=post
            )   
    


@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        commenter = instance.user
        if post.user != commenter:
            Notification.objects.create(
                user=post.user,
                from_user=commenter,
                type='comment',
                post=post
            )


@receiver(post_save, sender=Follow)
def create_follow_notification(sender, instance, created, **kwargs):
    if created:
        user = instance.follower
        from_user = instance.following
        Notification.objects.create(
            user=from_user,
            from_user=user,
            type='follow'
        )
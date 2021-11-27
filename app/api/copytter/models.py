import random
import string
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def randomname(n):
    randlst = [
        random.choice(
            string.ascii_letters +
            string.digits) for i in range(n)]
    return ''.join(randlst)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Profile(models.Model):
    STATUS_OFFICAL = "official"
    STATUS_PUBLIC = "public"
    STATUS_CLOSE = "close"
    STATUS_BOT = "machine"
    STATUS_BLOCK = "block"

    ACCOUNTS_STATUS = {
        (STATUS_OFFICAL, '公式'),
        (STATUS_PUBLIC, '一般'),
        (STATUS_CLOSE, '非公開'),
        (STATUS_BOT, 'BOT'),
        (STATUS_BLOCK, '凍結')
    }

    profile_user_id = models.CharField(
        default=randomname(10), max_length=32, unique=True)

    status = models.CharField(
        max_length=10,
        choices=ACCOUNTS_STATUS,
        default=STATUS_PUBLIC)

    age = models.IntegerField(default=0, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    follow_count = models.IntegerField(default=0)
    follower_count = models.IntegerField(default=0)
    gender = models.CharField(max_length=20, blank=True)
    icon_pass = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    profile_first_registed = models.BooleanField(default=False)
    profile_message = models.TextField(max_length=300, blank=True)
    sensitive_entry = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)

    def __repr__(self):
        return "{}".format(self.user.username)

    __str__ = __repr__


class Follow(models.Model):
    follow_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follow_user')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')


class Entry(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_CLOSE = "close"
    STATUS_BOT = "machine"

    STATUS_SET = (
        (STATUS_DRAFT, "下書き"),
        (STATUS_PUBLIC, "公開中"),
        (STATUS_CLOSE, '非公開'),
        (STATUS_BOT, 'BOT')
    )
    status = models.CharField(
        choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)

    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    media_close = models.BooleanField(default=False)
    relation_cont = models.IntegerField(default=0)
    relation_id = models.CharField(max_length=8, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "{}: {}".format(self.author, self.id)

    __str__ = __repr__


class Media(models.Model):
    media_type = models.CharField(max_length=8)
    media_url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

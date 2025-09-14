from django.db.models.signals import post_save
from django.dispatch import receiver

from Profile.models import Profile
from django.contrib.auth.models import User

@receiver(post_save,sender=User)
def create_user_profile_signal(sender, instance, created, **kwargs) :
    if created :
        profile = Profile.objects.create(user=instance)
        profile.save()
        print("Profile Created")

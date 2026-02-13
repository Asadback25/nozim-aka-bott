from django.db import models
import uuid

from django.contrib.auth.models import User


class BotUsers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name




class RegisterTravel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='travels')
    from_city = models.CharField(max_length=255)
    to_city = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    leader_person = models.CharField(max_length=255)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.from_city


class TravelParticipants(models.Model):
    travel = models.ForeignKey(RegisterTravel, on_delete=models.CASCADE,related_name='participants')
    user_id = models.IntegerField()
    registered_date = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    has_passport = models.BooleanField(default=True)
    passport_image = models.ImageField(upload_to='passport_images/',null=True,blank=True)
    phone_number = models.CharField(max_length=255)


    def __str__(self):
        return self.first_name
from django.db import models
from django.db.models.signals import pre_save
import string
import random
from covid_crm.utlis import slugify_slug



class User_custom(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    mobile = models.IntegerField(max_length=10)
    email = models.EmailField()
    oxygen = models.BooleanField(default=None)
    food = models.BooleanField(default=None)
    free_service= models.BooleanField()

    def __str__(self):
        return f'{self.first_name}{self.id}'


class Hospital(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length = 500)
    contact_no = models.CharField(max_length= 10, null=True, blank=True)
    icu_beds_availablity = models.IntegerField()
    slug = models.SlugField(unique = True,blank=True, null=True)
    free= models.BooleanField(default=False)


    def __str__(self):
        return f'{self.name}'


# Method to check uniquness of slug:
def Unique_slug_generator(sender, instance, *args, **kwargs):
    if sender is Hospital:
        qs = Hospital.objects.filter(name=instance.name)
    if sender is Tiffin_service_provider:
        qs = Tiffin_service_provider.objects.filter(name=instance.name)
    if  qs.exists() and not instance.slug :
        instance.slug = slugify_slug(instance.name)+str((''.join(random.choice(string.ascii_letters) for i in range(4))))
    else :
        if not instance.slug:
            print('entered in else loop')
            instance.slug=slugify_slug(instance.name)
        else:
            pass
 
pre_save.connect(Unique_slug_generator, sender = Hospital)


class Tiffin_service_provider(models.Model):
    choices_place = (('Vadodara', 'Vadodara'),
                     ('Surat','Surat'),
                      ('Ahemdabad','Ahemdabad'),
                     ('Bharuch','Bharuch'),

                     ('Rajkot','Rajkot'),
                     ('Anand','Anand'))
    
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=500,choices=choices_place, default=None)
    tiffin_image = models.ImageField(upload_to='tf_image',default= 'static/images/cov_bg.png')
    phone = models.CharField(max_length=10)
    timing = models.DateTimeField()
    food_available = models.CharField(max_length=2000, null=True, blank=True)
    covid_food = models.BooleanField(default=False)
    free= models.BooleanField(default=False)
    slug = models.SlugField(unique = True,blank=True, null=True)

    def __str__(self):
        return self.name

pre_save.connect(Unique_slug_generator, sender = Tiffin_service_provider)

    


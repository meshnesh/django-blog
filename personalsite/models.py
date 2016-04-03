from __future__ import unicode_literals

from django.conf import settings

from django.db import models
from django.db.models.signals import pre_save

from django.core.urlresolvers import reverse

from django.utils import timezone
from django.utils.text import slugify

from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

# Create your models here.

class ImageManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(ImageManager, self).filter(draft=False).filter(publish__lte=timezone.now())

def upload_location(instance, filename):
	return "%s%s"%(instance.id, filename)

class Image(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	image = models.ImageField(
		upload_to = upload_location, 
		storage = gd_storage,
		null=True, 
		blank=True,
		width_field="width_field",
		height_field="height_field")
	height_field = models.IntegerField(default=300)
	width_field = models.IntegerField(default=300)
	content = models.TextField()
	site_url = models.URLField(default= "")
	
	updated = models.DateTimeField(auto_now=False,auto_now_add=True)
	timestamp = models.DateTimeField(auto_now=True,auto_now_add=False)

	objects = ImageManager()

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("personalsite:home", kwargs={"slug": self.slug})

	class Meta:
		ordering = ["-timestamp", "-updated"]

def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Image.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s%s"%(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_image_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_image_receiver, sender=Image)
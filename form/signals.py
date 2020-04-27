from .models import ImageForm
from django.db.models.signals import post_save,pre_save
import os
from webapp.settings import PROCESSING_FILES,BASE_DIR


base_dir =BASE_DIR


def get_processing(sender,instance,created,**kwargs):
	print(instance.name,instance.image.url)
	global path_of_uploaded_img
	path_of_uploaded_img  = instance.image.url

	
post_save.connect(get_processing,sender=ImageForm)

def returnPath():
	return path_of_uploaded_img,(base_dir+path_of_uploaded_img)

if __name__=='__main__':
	path = os.path.join(base_dir,'instance.image.url')
	print(path)
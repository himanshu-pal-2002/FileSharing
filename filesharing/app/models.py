from django.db import models
import uuid
from uuid import uuid4
import os

# Create Models for Folder: 
class Folder(models.Model):

    uid = models.UUIDField( primary_key = True, editable = False, default = uuid.uuid4)
    created_at = models.DateField(auto_now=True)

# Generate random folder for saving files:
def get_upload_path(instance, filename):
    return os.path.join(str(instance.folder.uid) , filename)


# For saving the files:
class Files(models.Model):

    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path)
    created_at = models.DateField(auto_now=True)



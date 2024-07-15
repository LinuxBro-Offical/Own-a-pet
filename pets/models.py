from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    vaccination_status = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    images = models.ManyToManyField('Image', blank=True)
    videos = models.ManyToManyField('Video', blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='pet_images')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image of {self.pet.name}"


class Video(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='pet_videos')
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return f"Video of {self.pet.name}"

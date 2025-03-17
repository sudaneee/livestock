from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='slider_images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(upload_to='service_icons/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    stats = models.JSONField()  # e.g., {"livestock_vaccinated": 69000, "farmers_trained": 150000}

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    date = models.DateField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def comment_count(self):
        return self.comments.count()

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)  # Commenter's name
    email = models.EmailField()  # Commenter's email
    text = models.TextField()  # Comment text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f'Comment by {self.name} on {self.news.title}'

class Team(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team_images/', blank=True, null=True)
    social_links = models.JSONField()  # e.g., {"facebook": "url", "twitter": "url"}

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    quote = models.TextField()
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    image = models.ImageField(upload_to='testimonial_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='partner_logos/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Picture(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pitures/', blank=True, null=True)

    def __str__(self):
        return self.title



class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='events/', blank=True, null=True)

    def __str__(self):
        return self.title

class Paragraph(models.Model):
    title = models.CharField(max_length=255)
    content= models.TextField() 

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=255)
    video_id = models.CharField(max_length=20, unique=True)
    thumbnail_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_video_url(self):
        return f"https://www.youtube.com/watch?v={self.video_id}"

    def get_thumbnail_url(self):
        return f"https://img.youtube.com/vi/{self.video_id}/hqdefault.jpg"


class Agency(models.Model):
    name = models.CharField(max_length=255)
    content= models.TextField() 
    image = models.ImageField(upload_to='agencies/', blank=True, null=True)

    def __str__(self):
        return self.name 


class Gallery(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)  # Optional title for the image
    image = models.ImageField(upload_to='gallery_images/')  # Image file
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.title if self.title else f"Gallery Image {self.id}"






class Media(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('video', 'Video'),
        ('audio', 'Audio'),
    ]

    title = models.CharField(max_length=200)  # Title of the media
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)  # Video or Audio
    youtube_link = models.URLField(blank=True, null=True)  # YouTube video link (optional)
    audio_file = models.FileField(upload_to='audio_jingles/', blank=True, null=True)  # Audio file (optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.title

    def clean(self):
        # Ensure either YouTube link or audio file is provided, but not both
        if self.media_type == 'video' and not self.youtube_link:
            raise ValidationError("YouTube link is required for video media.")
        if self.media_type == 'audio' and not self.audio_file:
            raise ValidationError("Audio file is required for audio media.")
        if self.youtube_link and self.audio_file:
            raise ValidationError("Cannot provide both YouTube link and audio file.")
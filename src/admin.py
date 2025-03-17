from django.contrib import admin
from .models import Slider, Service, About, Media, Gallery, Project, Agency, Video, News, Team, Testimonial, Partner, Picture, Event, Paragraph

# Register your models here.

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'link')
    search_fields = ('title', 'description')
    list_filter = ('title',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon', 'link')
    search_fields = ('title', 'description')
    list_filter = ('title',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')
    list_filter = ('title',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'link')
    search_fields = ('title', 'description')
    list_filter = ('title',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'date', 'link')
    search_fields = ('title', 'description')
    list_filter = ('date', 'title')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'image')
    search_fields = ('name', 'role')
    list_filter = ('role',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('quote', 'name', 'role', 'image')
    search_fields = ('name', 'role')
    list_filter = ('role',)

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'link')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Paragraph)
class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_id')
    search_fields = ('title', 'video_id')
    list_filter = ('title',)

@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')
    search_fields = ('name', 'content')
    list_filter = ('name',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'created_at')
    list_filter = ('media_type',)
    search_fields = ('title',)
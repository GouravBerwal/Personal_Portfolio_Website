from django.contrib import admin
from .models import Profile, Skill, Project, Experience, ContactMessage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'title')
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'title', 'sub_title', 'email', 'phone')
        }),
        ('Biography', {
            'fields': ('bio_1', 'bio_2', 'bio_3', 'bio_4', 'bio_5', 'about_quote')
        }),
        ('Links', {
            'fields': ('resume_link', 'nav_resume_link', 'github_url', 'linkedin_url', 'leetcode_url', 'instagram_url')
        }),
        ('Assets & Images', {
            'fields': ('hero_avatar', 'about_photo', 'hero_bg', 'contact_bg')
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'icon_image', 'order')
    list_editable = ('order', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'github_url', 'order')
    list_editable = ('order', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'tech_stack', 'bullet_1')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'date_range', 'is_right', 'order')
    list_editable = ('order', 'is_right')
    search_fields = ('role', 'company')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'phone', 'message', 'created_at')

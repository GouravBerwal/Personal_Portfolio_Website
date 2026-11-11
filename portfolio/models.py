from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, default="Gourav Berwal")
    title = models.CharField(
        max_length=200,
        default="Undergraduate Student @ CSE Dept., CGC University Mohali"
    )
    sub_title = models.CharField(
        max_length=255,
        default="CGC University Mohali — Computer Science & Engineering"
    )
    bio_1 = models.TextField(
        default="I'm a Computer Science and Engineering student at CGC University, Mohali, with a strong interest in software development, data analytics, and building technology that solves real-world problems."
    )
    bio_2 = models.TextField(
        default="I enjoy understanding how things work, exploring data, writing code, and transforming complex problems into simple, practical solutions. My approach combines analytical thinking with a passion for continuous learning and building."
    )
    bio_3 = models.TextField(
        default="My technical interests include Python, SQL, Data Analytics, Data Visualization, and Backend Development. I enjoy working with data, identifying meaningful patterns, developing applications, and creating solutions that are both useful and scalable."
    )
    bio_4 = models.TextField(
        default="Currently, I'm gaining professional experience as a Python Developer Intern at AlphaWizz, where I'm strengthening my development skills and learning how software is designed and built in a professional environment."
    )
    bio_5 = models.TextField(
        default="Beyond technology, I believe in curiosity, consistency, and lifelong learning. I enjoy reading novels, listening to music, and exploring new ideas that challenge the way I think."
    )
    about_quote = models.TextField(
        default="I don't just want to write code. I want to build things that make a difference."
    )
    email = models.EmailField(default="gouravberwal003@gmail.com")
    phone = models.CharField(max_length=30, default="+91 9516637166")
    resume_link = models.CharField(
        max_length=255,
        default="/resume/",
        help_text="Path or URL to resume PDF"
    )
    nav_resume_link = models.CharField(
        max_length=255,
        default="/resume/",
        help_text="Path or URL to resume PDF in navbar"
    )
    hero_avatar = models.CharField(max_length=255, default="images/Gourav.jpg")
    about_photo = models.CharField(max_length=255, default="images/Gaurav.jpg")
    hero_bg = models.CharField(max_length=255, default="images/CGC.jpg")
    contact_bg = models.CharField(max_length=255, default="images/World Map.jpg")
    instagram_url = models.URLField(default="https://www.instagram.com/_gouravgurjar__")
    linkedin_url = models.URLField(default="https://www.linkedin.com/in/gouravberwal/")
    github_url = models.URLField(default="https://github.com/GouravBerwal")
    leetcode_url = models.URLField(default="https://leetcode.com/", blank=True)

    class Meta:
        verbose_name = "Profile Information"
        verbose_name_plural = "Profile Information"

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('languages', 'Languages & Frameworks'),
        ('data_bi', 'Data Analysis & BI'),
        ('db', 'Databases'),
        ('tools', 'Tools & Cloud'),
        ('web', 'Web Technologies'),
    ]

    name = models.CharField(max_length=100)
    icon_image = models.CharField(
        max_length=255,
        help_text="Path under static/, e.g., images/Python.png"
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='languages',
        blank=True
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('filter-se', 'Software Engineering'),
        ('filter-ml', 'Machine Learning / AI'),
        ('filter-da', 'Data Analytics'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='filter-se'
    )
    tech_stack = models.CharField(max_length=255)
    bullet_1 = models.TextField(help_text="Primary feature/summary point")
    bullet_2 = models.TextField(blank=True, help_text="Architecture/Logic point")
    bullet_3 = models.TextField(blank=True, help_text="Impact/Optimization point")
    image = models.CharField(
        max_length=255,
        help_text="Path under static/, e.g., images/Amazon.png"
    )
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    doc_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title

    def get_points(self):
        pts = [self.bullet_1]
        if self.bullet_2:
            pts.append(self.bullet_2)
        if self.bullet_3:
            pts.append(self.bullet_3)
        return pts


class Experience(models.Model):
    role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    company_url = models.URLField(blank=True)
    date_range = models.CharField(max_length=100)
    logo = models.CharField(
        max_length=255,
        help_text="Path under static/, e.g., images/acmegrade_logo.png"
    )
    points = models.TextField(
        help_text="Enter each bullet point on a separate line"
    )
    is_right = models.BooleanField(
        default=False,
        help_text="Check to align this card on the right side of the timeline"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.role} - {self.company}"

    def get_points_list(self):
        return [p.strip() for p in self.points.strip().split('\n') if p.strip()]


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} ({self.email}) at {self.created_at.strftime('%Y-%m-%d %H:%M')}"

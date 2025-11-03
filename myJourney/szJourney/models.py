from django.db import models

# --- For index.html ---

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    level = models.CharField(max_length=50)  # e.g. Beginner, Intermediate, Advanced

    def __str__(self):
        return self.name


class Challenge(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    how_overcome = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    institution = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    year_completed = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"


# --- For aboutMe.html ---

class Hobby(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='hobbies/', blank=True, null=True)  # optional

    def __str__(self):
        return self.name

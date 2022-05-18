from django import models
from django.contrib.auth.models import User


# class Profile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	bio = models.CharField(default='Hello, tweeper', max_length=100)
# 	image = models.ImageField(default='default.png')


#     def __str__(self):
# 		return f'Profile{self.user.username}'



# class Post(models.Model):
# 	timestamp = models.DateTimeField(default=timezone.now)
# 	content = models.TextField()
# 	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    # class Meta:
    #     ordering = ['-timestamp']

    # def __str__(self):
	# 	return self.content
        
        

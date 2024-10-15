# from django.db import models
#
#
# class User(models.Model):
#
#     nickname = models.CharField(
#         max_length=100,
#         unique=True,  # TODO: потом сделай уникальность регистронезависимым
#     )
#
#     profile_image = models.ImageField(upload_to='/avatars/')
#     password = models.TextField()
#     followers = models.ManyToManyField(to='User')
#
#
# class Publication(models.Model):
#     image = models.ImageField(upload_to='/publication_images/')
#     description = models.TextField(null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')
#     likes = models.ManyToManyField(User, related_name='likes', unique=True)
#
#
# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
#     text = models.TextField()
#
#
# # class Follower(models.Model):
# #     follower_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followeds')
# #     followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

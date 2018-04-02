from basic.models import *

User.objects.all().delete()
AdvancedUser.objects.all().delete()
Post.objects.all().delete()
PostContent.objects.all().delete()
SystemMesg.objects.all().delete()
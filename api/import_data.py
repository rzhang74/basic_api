from test_api import *
from basic.models import *

test_register('user1', 'qb', 'user', '1', 'user1@gmail.com')
test_register('user2', 'qb', 'user', '2', 'user2@gmail.com')
test_register('user3', 'qb', 'user', '3', 'user3@gmail.com')
test_register('user4', 'qb', 'user', '4', 'user4@gmail.com')

user1 = User.objects.get(username = 'user1')
user2 = User.objects.get(username = 'user2')
user3 = User.objects.get(username = 'user3')
user4 = User.objects.get(username = 'user4')

post1 = Post(title='Post1')
post2 = Post(title='Post2')
post3 = Post(title='Post3')

post1.save()
post2.save()
post3.save()

postContent1 = PostContent(pid=post1, uid=user1, content="I am user 1 in post 1")
postContent2 = PostContent(pid=post1, uid=user2, content="I am user 2 in post 1")
postContent3 = PostContent(pid=post1, uid=user3, content="I am user 3 in post 1")
postContent4 = PostContent(pid=post2, uid=user2, content="I am user 2 in post 2")
postContent5 = PostContent(pid=post2, uid=user3, content="I am user 3 in post 2")

postContent1.save()
postContent2.save()
postContent3.save()
postContent4.save()
postContent5.save()

mesg1 = SystemMesg(content="hello user1", uid=user1)
mesg2 = SystemMesg(content="hello again user1", uid=user1)
mesg3 = SystemMesg(content="hello user2", uid=user2)
mesg4 = SystemMesg(content="hello user3", uid=user3)

mesg1.save()
mesg2.save()
mesg3.save()
mesg4.save()
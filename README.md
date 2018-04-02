# basic_api

This small project is created by python3 with django2. Before running code, make sure you have mysql installed, a database named Forum already created, and password set empty. Or you can change it in setting.py.

I made a file called import_data.py for importing some test data. To delete them, there is a file called delete_data.py.

I made a file called test_api.py for testing register, login, and logout. Change the base 'http://localhost:8000/' if necessary. Uncommented all the @permission_classes((IsAuthenticated,)) so that you could fully test these three functionality. I commented them for better testing of the get requests.

The following get requests are:

get_posts: simply go to base + get_posts for testing

get_post_by_title: go to base + get_post_by_title + ?title=param for testing

get_user_by_username: go to base + get_user_by_username + ?username=param for testing (default user are user1, user2, user3, and user4)

get_system_mesg_by_username: go to base + get_system_mesg_by_username + ?username=param for testing
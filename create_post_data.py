import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prepair.settings')
django.setup()

from faker import Faker

from communication.models import Post, Comment
from accounts.models import Member
from airports.models import Airport


def populate_posts_comment():

    all_airports = Airport.objects.all()

    member_ids = Member.objects.exclude(user__username='bfolks2').values_list('id', flat=True)
    member_length = len(member_ids)

    body_fake = Faker()
    word_list = ['airport', 'runway', 'frequency', 'landing', 'takeoff', 'weather', 'taxiway', 'tower', 'clearance',
                 'arrival', 'departure', 'turbulence', 'winds', 'obstacle', 'services', 'approach', 'the', 'this',
                 'on', 'from', 'light', 'heavy']

    for airport in all_airports:
        posts = Post.objects.filter(airport=airport)
        if not posts.exists():
            rand = random.randint(0, member_length - 1)
            member_id = member_ids[rand]
            data = {
                'member': Member.objects.get(id=member_id),
                'airport': airport,
                'body': body_fake.sentence(nb_words=15, ext_word_list=word_list)
            }
            Post.objects.create(**data)

    all_posts = Post.objects.all()
    for post in all_posts:
        comments = Comment.objects.filter(post=post)
        if not comments.exists():
            coinflip = random.randint(1, 2)
            # Only create Comments for half of posts that do not already have a comment
            if coinflip == 1:
                rand = random.randint(0, member_length - 1)
                member_id = member_ids[rand]
                data = {
                    'member': Member.objects.get(id=member_id),
                    'post': post,
                    'body': body_fake.sentence(nb_words=12, ext_word_list=word_list)
                }
                Comment.objects.create(**data)


def edit_posts_comments():
    all_posts = Post.objects.all()
    all_comments = Comment.objects.all()

    body_fake = Faker()
    word_list = ['airport', 'runway', 'frequency', 'landing', 'takeoff', 'weather', 'taxiway', 'tower', 'clearance',
                 'arrival', 'departure', 'turbulence', 'winds', 'obstacle', 'services', 'approach', 'the', 'this',
                 'on', 'from', 'light', 'heavy']

    for post in all_posts:
        coinflip = random.randint(1, 2)
        if coinflip == 1:
            post.body = body_fake.sentence(nb_words=15, ext_word_list=word_list)
            post.save()

    for comment in all_comments:
        coinflip = random.randint(1, 2)
        if coinflip == 1:
            comment.body = body_fake.sentence(nb_words=12, ext_word_list=word_list)
            comment.save()


if __name__ == '__main__':
    print('Populating Post DB')
    # populate_posts_comment()
    # edit_posts_comments()
    print('Finished')

from instapy import InstaPy
from instapy import smart_run
import config

session = InstaPy(username = config.USERNAME, password = config.PASSWORD, headless_browser = False)
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)

with smart_run(session):
    session.set_relationship_bounds(enabled = True,
                                    delimit_by_numbers=True,
                                    max_followers=500,
                                    min_followers=30,
                                    min_following=50
                                    )
    session.set_do_follow(True, percentage=100)
    session.set_dont_like(["nsfw"])

    session.like_by_tags(["space", "exploration"], amount = 3, media='Photo')

    session.set_smart_hashtags(['space', 'exploration'], limit=3, sort='top', log_tags=True)
    session.like_by_tags(amount=10, use_smart_hashtags=True)
    session.set_do_comment(True, percentage=50)
    session.set_comments(['Space is hard and fun!', 'We should venture out into the outer space!'])

session.end()
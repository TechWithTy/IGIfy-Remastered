import unittest

from utilities.targets import build_targets_from_hashtags


class DummyUser:
    def __init__(self, pk, username):
        self.pk = pk
        self.username = username


class DummyMedia:
    def __init__(self, pk, user):
        self.pk = pk
        self.id = pk
        self.user = user


class DummyClient:
    def __init__(self, user_id=None):
        self.user_id = user_id
        # maps tag -> list of medias for 'top' and 'recent'
        self._top = {}
        self._recent = {}
        self._likers = {}

    # Private API preferred
    def hashtag_medias_top(self, tag, amount=20):
        return list(self._top.get(tag, []))[:amount]

    def hashtag_medias_recent(self, tag, amount=20):
        return list(self._recent.get(tag, []))[:amount]

    # Public fallbacks (not used here but need to exist)
    def hashtag_medias_top_gql(self, tag, amount=20):
        return []

    def hashtag_medias_recent_gql(self, tag, amount=20):
        return []

    def media_info(self, mpk):
        # Return a minimal object with .user where possible; here medias already have user
        for medias in list(self._top.values()) + list(self._recent.values()):
            for m in medias:
                if m.pk == mpk:
                    return m
        return DummyMedia(mpk, None)

    def media_likers(self, mpk):
        return list(self._likers.get(mpk, []))


class TestBuildTargets(unittest.TestCase):
    def test_basic_authors_only(self):
        cl = DummyClient()
        # Hashtag with space should sanitize to variants
        tag = "real estate"
        author1 = DummyUser(1, "author_one")
        author2 = DummyUser(2, "author_two")
        m1 = DummyMedia(101, author1)
        m2 = DummyMedia(102, author2)
        cl._top["realestate"] = [m1]
        cl._top["real_estate"] = [m2]

        mapping = build_targets_from_hashtags(
            cl=cl,
            hashtags=[tag],
            media_source='top',
            media_count=10,
            max_users=10,
            exclude_self=True,
            include_likers=False,
            verbose=True,
        )
        self.assertEqual(mapping.get("author_one"), "1")
        self.assertEqual(mapping.get("author_two"), "2")

    def test_include_likers_and_cap(self):
        cl = DummyClient()
        author = DummyUser(3, "author")
        m = DummyMedia(201, author)
        cl._top["hashtag"] = [m]
        # Likers
        cl._likers[201] = [DummyUser(11, "u11"), DummyUser(12, "u12"), DummyUser(13, "u13")]

        mapping = build_targets_from_hashtags(
            cl=cl,
            hashtags=["hashtag"],
            media_source='top',
            media_count=5,
            max_users=3,  # cap at 3
            exclude_self=True,
            include_likers=True,
            verbose=False,
        )
        # Expect exactly 3 entries due to cap
        self.assertEqual(len(mapping), 3)

    def test_fallback_to_recent(self):
        cl = DummyClient()
        # top empty, recent has media
        author = DummyUser(21, "auth21")
        cl._recent["homes"] = [DummyMedia(301, author)]

        mapping = build_targets_from_hashtags(
            cl=cl,
            hashtags=["homes"],
            media_source='top',  # will fallback to recent
            media_count=5,
            max_users=10,
            exclude_self=True,
            include_likers=False,
            verbose=True,
        )
        self.assertIn("auth21", mapping)

    def test_exclude_self(self):
        cl = DummyClient(user_id=99)
        # Author is self, should be excluded
        self_user = DummyUser(99, "me")
        other = DummyUser(100, "other")
        cl._top["tag"] = [DummyMedia(401, self_user), DummyMedia(402, other)]

        mapping = build_targets_from_hashtags(
            cl=cl,
            hashtags=["tag"],
            media_source='top',
            media_count=10,
            max_users=10,
            exclude_self=True,
            include_likers=False,
        )
        self.assertNotIn("me", mapping)
        self.assertIn("other", mapping)


if __name__ == '__main__':
    unittest.main()


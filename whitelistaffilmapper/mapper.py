from django.conf import settings
from django.contrib.auth.models import Group


class WhitelistAffilGroupMapper(object):
    """
    makes sure that the user is in a Group for every wind affil,
    autovivifying Groups if necessary.

    In contrast to the djangowind default, this only
    bothers with affils in a whitelist.

    This is useful for, eg, internal apps where
    course affils don't matter and would only clutter the system.
    In that case, we can whitelist just 'tlcxml' or similar
    important unix group affils.
    """

    def map(self, user, affils):
        whitelist = []
        if hasattr(settings, 'AFFILS_WHITELIST'):
            whitelist = settings.AFFILS_WHITELIST
        for affil in affils:
            if affil not in whitelist:
                continue
            try:
                group = Group.objects.get(name=affil)
            except Group.DoesNotExist:
                group = Group(name=affil)
                group.save()
            user.groups.add(group)
        user.save()

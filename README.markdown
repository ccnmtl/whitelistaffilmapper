makes sure that the user is in a Group for every wind affil,
autovivifying Groups if necessary.

In contrast to the djangowind default, this only
bothers with affils in a whitelist.

This is useful for, eg, internal apps where
course affils don't matter and would only clutter the system.
In that case, we can whitelist just 'tlcxml' or similar
important unix group affils.


in your `settings_shared.py` you normally would have something like:

    WIND_AFFIL_HANDLERS = ['djangowind.auth.AffilGroupMapper',
                           'djangowind.auth.StaffMapper',
                           'djangowind.auth.SuperuserMapper']

To use this, just change it to:

    WIND_AFFIL_HANDLERS = ['whitelistaffilmapper.WhitelistAffilGroupMapper',
                           'djangowind.auth.StaffMapper',
                           'djangowind.auth.SuperuserMapper']
    AFFIL_WHITELIST = ['tlcxml.cunix.local:columbia.edu', ]


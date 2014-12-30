from __future__ import unicode_literals
# -*- coding: utf-8 -*-
# This file is in the public domain

# this is the only django import permitted in settings files
from django.core.exceptions import ImproperlyConfigured

def getcreds(fname="db.host", project=None, credsroot='~/creds', credsdir=None):
    """Return a list of userid and password and perhaps other arbitrary
    data on subsequent lines. You just have to know what you are 
    retrieving.
    """
    import os
    if credsdir is None:
        if project is None:
            raise ImproperlyConfigured('Missing setting: "project"')
        credsdir = os.path.join(credsroot, project)
    creds = []
    fname = os.path.join(credsdir, fname)
    with open(fname, 'r') as f:
        for line in f:
            creds.append(line.strip())
    if not creds:
        raise ImproperlyConfigured('Missing setting: %s' % fname)
    return creds


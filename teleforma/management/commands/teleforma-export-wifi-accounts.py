from optparse import make_option
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from telemeta.models import *
from telemeta.util.unaccent import unaccent
from teleforma.exam.models import *
import logging
import codecs


class Command(BaseCommand):
    help = "Export all WiFi accounts"
    args = 'path'

    def handle(self, *args, **options):
        path = args[0]
        f = open(path, 'w')

        for user in User.objects.all():
            profile = Profile.objects.filter(user=user)
            if profile:
            	p = profile[0]
                f.write(p.wifi_login + ',' + p.wifi_pass + '\n')

        f.close()

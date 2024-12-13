from django.contrib import admin

from htmlwebsite.models import Contact

from htmlwebsite.models import poll
from htmlwebsite.models import vote
from htmlwebsite.models import Election
from htmlwebsite.models import Candidate



# Register your models here.
admin.site.register(Contact)
admin.site.register(poll)
admin.site.register(vote)
admin.site.register(Election)
admin.site.register(Candidate)


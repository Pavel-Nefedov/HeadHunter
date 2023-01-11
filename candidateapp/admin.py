from django.contrib import admin

from candidateapp.models import (AdvancedTraining, Candidate, ContactInfo,
                                 Education, PositionAndSelery, Resume,
                                 WorkExperience)

admin.site.register(Candidate)
admin.site.register(Resume)

admin.site.register(ContactInfo)
admin.site.register(PositionAndSelery)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(AdvancedTraining)

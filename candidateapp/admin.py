from django.contrib import admin

from candidateapp.models import Candidate, Resume, ContactInfo, PositionAndSelery, WorkExperience, \
    Education, AdvancedTraining

admin.site.register(Candidate)
admin.site.register(Resume)

admin.site.register(ContactInfo)
admin.site.register(PositionAndSelery)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(AdvancedTraining)


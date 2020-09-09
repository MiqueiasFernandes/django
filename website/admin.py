from django.contrib import admin

from website.models import *

# Register your models here.

admin.site.register(UniprotKb)
admin.site.register(Gene)
admin.site.register(GeneOntology)
admin.site.register(PDB)
admin.site.register(Pfam)
admin.site.register(Taxonomy)

from django.contrib import admin
from .models import Proposal


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('client', 'value', 'approved', 'analyzed')
    readonly_fields = ('approved', 'analyzed')


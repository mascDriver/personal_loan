from django.contrib import admin
from .models import Proposal, Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('customer', 'value', 'approved', 'analyzed')
    readonly_fields = ('approved', 'analyzed')

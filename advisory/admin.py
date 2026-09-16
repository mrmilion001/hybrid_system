from django.contrib import admin
from .models import PolicyClause, Rule

@admin.register(PolicyClause)
class PolicyClauseAdmin(admin.ModelAdmin):
    list_display = ('clause_id', 'domain', 'topic', 'title', 'clause_type', 'active')
    list_filter = ('domain', 'clause_type', 'active')
    search_fields = ('clause_id', 'title', 'provision', 'keywords')
    list_editable = ('active',)
    ordering = ('clause_id',)

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ('rule_id', 'domain', 'name', 'stop_processing', 'requires_human_review', 'active')
    list_filter = ('domain', 'stop_processing', 'requires_human_review', 'active')
    search_fields = ('rule_id', 'name', 'description')
    list_editable = ('active',)
    ordering = ('rule_id',)
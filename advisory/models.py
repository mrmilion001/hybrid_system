from django.db import models

# Create your models here.
from django.db import models


class PolicyClause(models.Model):
    clause_id = models.CharField(max_length=30, unique=True)
    domain = models.CharField(max_length=50)
    topic = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    provision = models.TextField()
    source_title = models.CharField(max_length=255)
    source_reference = models.CharField(max_length=100, blank=True)
    source_url = models.URLField(blank=True)
    keywords = models.JSONField(default=list, blank=True)
    clause_type = models.CharField(
        max_length=30,
        choices=[
            ("deterministic", "Deterministic"),
            ("explanatory", "Explanatory"),
            ("procedural", "Procedural"),
        ],
    )
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.clause_id


class Rule(models.Model):
    rule_id = models.CharField(max_length=30, unique=True)
    domain = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    conditions = models.JSONField(default=dict)
    actions = models.JSONField(default=dict)
    clause_ids = models.JSONField(default=list, blank=True)
    stop_processing = models.BooleanField(default=False)
    requires_human_review = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rule_id
from django.db import models

#model for service request
class ServiceRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )
    REQUEST_TYPES = (
        ('Gas Leak', 'Gas Leak'),
        ('Meter Installation', 'Meter Installation'),
        ('Maintenance', 'Maintenance'),
        ('Gas Refill','Gas Refill')
    )

    request_type = models.CharField(max_length=100, choices=REQUEST_TYPES)
    details = models.TextField(null=True,blank=True)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_resolved = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.request_type} - {self.status}"

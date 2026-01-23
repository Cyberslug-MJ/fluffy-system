from django.db import models

class Sermon(models.Model):
    title = models.CharField(max_length=200)
    tags = models.CharField(max_length=2,choices=(
        ('AS','Academic Seminar'),
        ('FS','Fresher\'s Orientation'),
        ('RT','Relationship Talk'),
        ('FL','Financial Literacy'),
        ('CS','Communion Service'),
        ('OT','Other'),
    ))
    scripture_references = models.TextField()
    body = models.TextField()
    preacher = models.ForeignKey('Preacher',on_delete=models.CASCADE)
    date_preached = models.DateField()
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.title + '  - ' + self.tags


class Preacher(models.Model):
    full_name = models.CharField(max_length=150)
    bio = models.TextField()
    preacher_contact = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class VisitUsInfo(models.Model):
    full_name = models.CharField(max_length=150)
    notes = models.TextField(blank=True,null=True)  # Optional field for additional notes.
    contact_number = models.CharField(max_length=15)
    status = models.CharField(max_length=2,choices=(
        ('NW','NEW'),
        ('VS','VISITED'),
        ('CD','CONFIRMED'),
        ('CT','CONTACTED'),
        ('DN','DID NOT SHOW'),
        ('FP','FOLLOWED UP')
    ))
    intent_type = models.CharField(max_length=2,choices=(
        ('VS','VISIT'),
        ('JN','JOIN'),
        ('IN','INFO'),
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    timeframe = models.CharField(max_length=2,choices=(
        ('CS','COMING SERVICE'),
        ('TW','WITHIN THE NEXT 2 WEEKS'),
        ('NS','NOT SURE'),
        ('IN','JUST INFO'),
    ))

    def __str__(self):
        return self.full_name + ' ' + f'visitor-{self.pk}'


class VisitationAudit(models.Model):
    visit_us_info = models.ForeignKey(VisitUsInfo, on_delete=models.CASCADE, related_name='audits')
    previous_status = models.CharField(max_length=2,choices=(
        ('NW','NEW'),
        ('VS','VISITED'),
        ('CD','CONFIRMED'),
        ('CT','CONTACTED'),
        ('DN','DID NOT SHOW'),
        ('FP','FOLLOWED UP')
    ))
    new_status = models.CharField(max_length=2,choices=(
        ('NW','NEW'),
        ('VS','VISITED'),
        ('CD','CONFIRMED'),
        ('CT','CONTACTED'),
        ('DN','DID NOT SHOW'),
        ('FP','FOLLOWED UP')
    ))
    changed_at = models.DateTimeField(auto_now_add=True)
    # changed_by = models.CharField(max_length=100)  # Could be a username or identifier of the staff member.

    def __str__(self):
        return self.visit_us_info.full_name + ' ' + self.new_status


class Staff(models.Model):
    full_name = models.CharField(max_length=150)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name + ' ' + self.title
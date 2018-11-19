from django.db import models
from django.contrib.auth.models import User



class Communication(models.Model):
    uuid = models.UUIDField(unique=True, primary_key=True)
    TYPE_LIST = (
        (1, 'Meeting'),
        (2, 'Phone'),
        (3, 'Email'),
    )
    subject = models.CharField(max_length=50)
    notes = models.TextField()
    kind = models.PositiveSmallIntegerField(choices=TYPE_LIST)
    date = models.DateField()
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'communications'

    def __unicode__(self):
        return u"%s" % self.subject

    def get_absolute_url(self):
        return reverse('comm_detail', [self.uuid,])

    def get_update_url(self):
        return reverse('comm_update', [self.uuid,])

    def get_delete_url(self):
        return reverse('comm_delete', [self.uuid,])

    def exists(self):
        try:
            Communication.objects.get(uuid=self.uuid)
            return True
        except(self.DoesNotExist):
            return False

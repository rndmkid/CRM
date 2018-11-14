from django.db import models
from django.urls import reverse
import uuid


class Contact(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    account = models.ForeignKey('accounts.Account',
                                on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'contacts'

    @property
    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def __unicode__(self):
        return u'%s' % self.full_name

    def get_absolute_url(self):
        return reverse('contact_detail', args=[self.uuid])

    def get_update_url(self):
        return reverse('contact_update', args=[self.uuid])

    def get_delete_url(self):
        return reverse('contact_delete', args=[self.uuid])

    def exists_in_db(self):
        try:
            Contact.objects.get(uuid=self.uuid)
            return True
        except(self.DoesNotExist):
            return False

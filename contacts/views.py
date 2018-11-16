from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseForbidden
from uuid import UUID
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.http import Http404
from django.views.generic.edit import DeleteView


from .models import Contact
from .forms import ContactForm
from accounts.models import Account



@login_required()
def contact_detail(request, uuid):

    contact = Contact.objects.get(uuid=uuid)

    return render(request, 
                'contact_detail.html', 
                {'contact': contact}
    )

@login_required()
def contact_cru(request, uuid=None, account=None):

    if not request.POST and not uuid:
        contact = Contact()
    else:
        try:
            contact = Contact.objects.get(uuid=uuid)
        except:
            contact = None
    
    if request.POST:
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            # make sure the user owns the account
            account = form.cleaned_data['account']
            if account.owner != request.user:
                return HttpResponseForbidden()
            # save the data
            form.save()
            # return the user to the account detail view
            reverse_url = reverse(
                'account_detail',
                args=(account.uuid,)
            )
            return HttpResponseRedirect(reverse_url)
        else:
            # if the form isn't valid, still fetch the account so it can be passed to the template
            account = form.cleaned_data['account']
    else:
        form = ContactForm(instance=contact)
        account = Account.objects.get(uuid=request.session['account'])

    variables = {
        'form': form,
        'contact': contact,
        'account': account
    }

    if request.is_ajax():
        template = 'contact_item_form.html'
    else:
        template = 'contact_cru.html'

    return render(request, template, variables)

class ContactMixin(object):
    model = Contact

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Contact'})
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactMixin, self).dispatch(*args, **kwargs)

class ContactDelete(ContactMixin, DeleteView):
    template_name = 'object_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super(ContactDelete, self).get_object()
        if not obj.account.owner == self.request.user:
            raise Http404
        account = Account.objects.get(uuid=obj.account.uuid)
        self.account = account
        return obj

    def get_success_url(self):
        return reverse(
            'account_detail',
            args=(self.account.uuid,)
        )

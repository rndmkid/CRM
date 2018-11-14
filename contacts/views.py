from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseForbidden
from uuid import UUID
from django.core.exceptions import ObjectDoesNotExist

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

    if uuid:
        try:
            contact = Contact.objects.get(uuid=uuid)
            if contact.account.owner != request.user:
                return HttpResponseForbidden()
        except ObjectDoesNotExist:
            pass
    else:
        contact = Contact()

    if request.POST:
        form = ContactForm(request.POST,)
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

    # this is used to fetch the account if it exists as a URL parameter
    if request.GET:
        account = Account.objects.get(
            uuid=request.GET.get('account', ''))

    variables = {
        'form': form,
        'contact': contact,
        'account': account
    }

    template = 'contact_cru.html'

    return render(request, template, variables)

##@login_required()
##def contact_cru(request):
##
##    if request.POST:
##        form = ContactForm(request.POST)
##        if form.is_valid():
##            # make sure the user owns the account
####            account = form.cleaned_data['account']
####            if account.owner != request.user:
####                return HttpResponseForbidden()
##            # save the data
##            contact = form.save(commit=False)
##            contact.owner_id = request.user.id
##            account = Account.objects.get(
##                uuid=request.session['account'])
##            contact.account = account
##            contact.save()
##            # return the user to the account detail view
##            reverse_url = reverse(
##                'account_detail',
##                args=(account.uuid,)
##            )
##            return HttpResponseRedirect(reverse_url)
##    else:
##        form = ContactForm()
##
##    variables = {
##        'form': form,
##    }
##
##    template = 'contact_cru.html'
##
##    return render(request, template, variables)

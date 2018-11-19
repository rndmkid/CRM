from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse

from .models import Communication
from accounts.models import Account

@login_required()
def comm_detail(request, uuid):

    comm = Communication.objects.get(uuid=uuid)
    if comm.owner != request.user:
            return HttpResponseForbidden()

    return render(request, 'comm_detail.html', {'comm':comm})

@login_required()
def comm_cru(request, uuid=None, account=None):

    if not request.POST and not uuid:
        comm = Communication()
    else:
        try:
            comm = Communication.objects.get(uuid=uuid)
        except:
            comm = None

    if request.POST:
        form = CommunicationForm(request.POST, instance=comm)
        if form.is_valid():
            # make sure the user owns the account
            account = form.cleaned_data['account']
            if account.owner != request.user:
                return HttpResponseForbidden()
            # save the data
            form.save()
            # return the user to the account detail view
            reverse_url = reverse('account_detail', args=(account.uuid,))
            return HttpResponseRedirect(reverse_url)
        else:
            # if the form isn't valid, still fetch the account so it can be passed to the template
            account = form.cleaned_data['account']
    else:
        form = CommunicationForm(instance=comm)
        account = Account.objects.get(uuid=request.session['account'])
        
    variables = {
        'form': form,
        'comm':comm,
        'account': account
    }

    template = 'communications/comm_cru.html'

    return render(request, template, variables)

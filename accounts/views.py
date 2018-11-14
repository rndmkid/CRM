from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Account
from subscribers.models import Subscriber

from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.http import HttpResponseRedirect 

from .forms import AccountForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from contacts.models import Contact
from json import JSONEncoder

class AccountList(ListView):
    model = Account
    paginate_by = 12
    template_name = 'account_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        try:
            a = self.request.GET.get('account',)
        except KeyError:
            a = None
        if a:
            account_list = Account.objects.filter(
                name__icontains=a,
                owner=self.request.user
            )
        else:
            account_list = Account.objects.filter(owner=self.request.user)
        return account_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AccountList, self).dispatch(*args, **kwargs)

@login_required()
def account_detail(request, uuid):

    account = Account.objects.get(uuid=uuid)
    if account.owner != request.user:
        return HttpResponseForbidden()

    contacts = Contact.objects.filter(account=account)
    
    variables = {
	    'account': account,
            'contacts': contacts,
    }

    
    request.session['account'] = account.uuid.hex
    
    return render(request, 'account_detail.html', variables)

@login_required()
def account_cru(request, uuid=None):

    if uuid:
        account = get_object_or_404(Account, uuid=uuid)
        if account.owner != request.user:
            return HttpResponseForbidden()
    else:
        account = Account(owner=request.user)

    if request.POST:
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            redirect_url = reverse(
                'account_detail',
                args=(account.uuid,)
            )
            return HttpResponseRedirect(redirect_url)
    else:
        form = AccountForm(instance=account)

    variables = {
        'form': form,
        'account':account
    }

    if request.is_ajax():
        template = 'account_item_form.html'
    else:
        template = 'account_cru.html'

    return render(request, template, variables)

@login_required()
def account_create(request):

    if request.POST:
        form = AccountForm(request.POST)
        
        account = form.save(commit=False)
        account.owner_id = request.user.id
        account.save()
        redirect_url = reverse(
            'account_detail',
            args=(account.uuid,)
        )
        return HttpResponseRedirect(redirect_url)
    else:
##        sub = Subscriber.objects.get(username=request.user.username)
##        account = Account()
##        account.user_id = request.user.id
        form = AccountForm()

    variables = {
        'form': form,
    }

    template = 'account_cru.html'

    return render(request, template, variables)

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate

from django.http import HttpResponseRedirect

from prepair.utils import get_redirect_link
from prepair.views import PrepairViewSet
from .models import Member
from .serializers import MemberSerializer, UserSerializer
from .forms import CreateMemberForm


def register_member(request):

    if request.method == 'POST':
        member_form = CreateMemberForm(data=request.POST)
        if member_form.is_valid():
            # Requires additional custom validation because this Form will likely not map to the User directly
            # once it is fully implemented
            username = member_form.data.get('username')
            password1 = member_form.data.get('password1')
            password2 = member_form.data.get('password2')

            if not password1 == password2:
                data = {'errors': ['Passwords do not match'], 'member_form': member_form}
                return render(request, 'accounts/register.html', data)

            # Create User model
            new_user = User.objects.create(username=username)
            new_user.set_password(password1)
            new_user.save()

            # Create Member model, link to Django User
            new_member = Member.objects.create(user=new_user)
            new_member.save()

            data = {'registered': True}
            return render(request, 'accounts/register.html', data)

        else:
            data = {'errors': member_form.errors, 'member_form': member_form}
            return render(request, 'accounts/register.html', data)

    member_form = CreateMemberForm
    return render(request, 'accounts/register.html', {'member_form': member_form})


def login_view(request):

    redirect_to = get_redirect_link(request)

    if request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        db_user_query = User.objects.filter(username=username)
        if db_user_query.exists() and not db_user_query.first().is_active:
            return render(request, 'accounts/login.html', {'username': username, 'inactive': True, 'next': redirect_to})

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(redirect_to)
        else:
            return render(request, 'accounts/login.html', {'invalid': True, 'next': redirect_to})
    else:
        data = {'next': redirect_to}
        return render(request, 'accounts/login.html', data)


def logout_view(request):
    redirect_to = get_redirect_link(request)

    logout(request)
    return HttpResponseRedirect(redirect_to)


class MemberViewSet(PrepairViewSet):
    """
    DRF Viewset for Member objects
    """

    prepair_model_class = Member
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    filter_fields = ('pk', 'user', 'home_airport')
    iexact_filter_fields = tuple()


class UserViewSet(PrepairViewSet):
    """
    DRF Viewset for Member objects
    """

    prepair_model_class = User
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_fields = ('pk', 'username')
    iexact_filter_fields = tuple()

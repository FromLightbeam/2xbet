from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

import re
import acaunt.forms as forms
import acaunt.user_db_conect as user_db_conect
import log_conector
import acaunt.log_money as log_money

def signup(request):
    if request.method == 'GET':
        if('user_id' in request.session):
            response = HttpResponseRedirect('/accaunt/user/')
            return response
        form = forms.RegistrationForm
        return render(request, 'acaunt/signup.html',{'form': form,} )
    if request.method =='POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = user_db_conect.registration(form.cleaned_data['username'],
                                                form.cleaned_data['name_1'],
                                                form.cleaned_data['name_2'],
                                                form.cleaned_data['password'],
                                                form.cleaned_data['password_confirmation'])
            print(user)
            if not user:
                form = forms.RegistrationForm
                return render(request, 'acaunt/signup.html',{'form': form,} )
            log_conector.add_log(user['id'], 'sign up')
            response = HttpResponseRedirect('/')
            return response
        form = forms.RegistrationForm
        return render(request, 'acaunt/signup.html',{'form': form,} )

def login(request):
    if request.method == 'GET':
        if('user_id' in request.session):
            response = HttpResponseRedirect('/accaunt/user/')
            return response
        form = forms.LoginForm
        return render(request, 'acaunt/login.html',{'form': form,} )
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = user_db_conect.authenticate(form.cleaned_data['username'],
                                                form.cleaned_data['password'])
            if not user:
                return render(request, 'acaunt/login.html', {'form': form})
            log_conector.add_log(user['id'], 'log in')
            response = HttpResponseRedirect('/accaunt/user/')
            #response = HttpResponse("okey")
            request.session.set_expiry(None)
            request.session['user_id'] = user['id']
            return response
        return render(request, 'acaunt/login.html', {'form': form})


def logout(request):
    response = HttpResponseRedirect('/accaunt/login/')
    try:
        user_id = request.session['user_id']
        user = user_db_conect.get_user_by_id(user_id)
        del request.session['user_id']
        log_conector.add_log(user['id'], 'log out')
    except KeyError:
        pass
    return response


def user_page(request):
    if('user_id' in request.session):
        user_id = request.session['user_id']
        user = user_db_conect.get_user_by_id(user_id)
        bets = user_db_conect.get_users_bet(user_id)
        q = True
        return render(request, 'acaunt/user_page.html', {'user': user, 'q': q, 'bets': bets, })
    else:
        q = False
        return render(request, 'acaunt/user_page.html',{'q': q,} )
    #if username:
        #user = user_db_conect.get_user(username)
        #return render(request, 'acaunt/user_page.html', {'user': user, })


def addmoney(request):
    if('user_id' in request.session):
        user_id = request.session['user_id']
        if request.method == 'POST':
            money = request.POST['name']
            money1 = int(money)
            if re.findall(r'[a-zA-Z]+', money):
                return HttpResponse('')
            money = user_db_conect.add_money(user_id, int(money))
            data = {
                'money': money
            }
            log_money.add_log(user_id, 'add', money1)
            return JsonResponse(data)
    else:
        data = {
         'error': 'yser das not exist'
        }
        return JsonResponse(data)

def withdrawmoney(request):
    if('user_id' in request.session):
        user_id = request.session['user_id']
        if request.method == 'POST':
            money = request.POST['name']
            money1 = int(money)
            if re.findall(r'[a-zA-Z]+', money):
                return HttpResponse('')
            money = user_db_conect.withdraw_money(user_id, int(money))
            if money == False:
                data = {'error': 'excess cash limit' }
            else:
                log_money.add_log(user_id, 'withdraw', money1)
                data = {'money': money }
            return JsonResponse(data)
    else:
        data = {
         'error': 'user das not exist'
        }
        return JsonResponse(data)


def user_logs_mon(request):
    if('user_id' in request.session):
        user_id = request.session['user_id']
        user = user_db_conect.get_user_by_id(user_id)
        q = True
        logs = user_db_conect.get_logs_money(user_id)
        bets = user_db_conect.get_users_bet(user_id)
        ans = []
        for i in logs:
            a = []
            for ii in i:
                a.append(ii)
            ans.append(a)
        for i in ans:
            for j in bets:
                if i[3] == j[0]:
                    i.append(j[13])
                    i.append(j[14])


        return render(request, 'acaunt/logsmoney.html', {'user': user, 'q': q, 'logs': ans, })
    else:
        q = False
        return render(request, 'acaunt/user_page.html',{'q': q,} )

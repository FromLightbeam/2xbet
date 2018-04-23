from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

import acaunt.forms as forms
import acaunt.user_db_conect as user_db_conect
import acaunt.log_money as log_money
import log_conector
import admin_ac.admin_conector as admin_conector
import admin_ac.forms as admin_forms



def login(request):
    if request.method == 'GET':
        if 'admin_user_id' in request.session:
            return HttpResponseRedirect('/admin/user/')
        form = forms.LoginForm
        return render(request, 'admin_ac/login.html', {'form': form ,})
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = user_db_conect.authenticate(form.cleaned_data['username'],
                                               form.cleaned_data['password'])

            print(user)
            if not user:
                return  HttpResponseRedirect('/admin/')
            elif admin_conector.is_admin(user):

                print("\n\nadmin\n\n")

                log_conector.add_log(user['id'], 'log in')
                response = HttpResponseRedirect('/admin/user/')
                request.session.set_expiry(None)
                request.session['admin_user_id'] = user['id']
                return response
        response = HttpResponseRedirect('/admin/')
        return response


def logout(request):
    response = HttpResponseRedirect('/admin/')
    try:
        user_id = request.session['admin_user_id']
        user = user_db_conect.get_user_by_id(user_id)
        del request.session['admin_user_id']
        log_conector.add_log(user['id'], 'log out')
    except KeyError:
        pass
    return response



def page(request):
    if 'admin_user_id' in request.session:
        admin_id = request.session['admin_user_id']
        admin = user_db_conect.get_user_by_id(admin_id)
        list_user = admin_conector.get_all_users()
        return render(request, 'admin_ac/page.html', {'admin': admin, 'list_user': list_user, })
    else:
        return HttpResponseRedirect('/admin/')

def club(request):
    if 'admin_user_id' in request.session:
        admin_id = request.session['admin_user_id']
        admin = user_db_conect.get_user_by_id(admin_id)
        clubs = admin_conector.get_all_club()
        return render(request, 'admin_ac/page_club.html', {'admin': admin, 'clubs': clubs, })
    else:
        return HttpResponseRedirect('/admin/')

def match(request):
    if 'admin_user_id' in request.session:
        admin_id = request.session['admin_user_id']
        admin = user_db_conect.get_user_by_id(admin_id)
        matchs = admin_conector.get_all_match()
        return render(request, 'admin_ac/page_match.html', {'admin': admin, 'matchs': matchs, })
    else:
        return HttpResponseRedirect('/admin/')


def logs(request):
    if 'admin_user_id' in request.session:
        admin_id = request.session['admin_user_id']
        admin = user_db_conect.get_user_by_id(admin_id)
        logs = admin_conector.get_all_logs()
        return render(request, 'admin_ac/page_logs.html', {'admin': admin, 'logs': logs, })
    else:
        return HttpResponseRedirect('/admin/')

def user_spec(request, id=1):
    if 'admin_user_id' in request.session:
        admin_id = request.session['admin_user_id']
        admin = user_db_conect.get_user_by_id(admin_id)
        user = user_db_conect.get_user_by_id(int(id))
        return render(request, 'admin_ac/user_spec.html', {'admin': admin, 'user': user, })

def del_user(request, id=None):
    if 'admin_user_id' in request.session:
        admin_id = request.session['admin_user_id']
        user_db_conect.del_user_by_id(int(id))
        response = HttpResponseRedirect('/admin/')
        return response

def locks_user(request, id):
    if 'admin_user_id' in request.session:
        admin_id = request.session['admin_user_id']
        user_db_conect.locks_user_by_id(int(id))
        response = HttpResponseRedirect('/admin/')
        return response

def unlocks_user(request, id):
    if 'admin_user_id' in request.session:
        admin_id = request.session['admin_user_id']
        user_db_conect.unlocks_user_by_id(int(id))
        response = HttpResponseRedirect('/admin/')
        return response

def create_club(request):
    if 'admin_user_id' in request.session:
        admin_id = request.session['admin_user_id']
        if request.method == 'POST':
            name = request.POST['name']
            if name == ' ' or name == '':
                return HttpResponse('')
            else:
                admin_conector.create_club(name)
                return HttpResponse('')


def del_club(request, id=None):
    if 'admin_user_id' in request.session:
        admin_id = request.session['admin_user_id']
        admin_conector.del_club(int(id))
        return HttpResponseRedirect('/admin/club/')


def match_create(request):
    if 'admin_user_id' in request.session:
        if request.method == 'GET':
            form  = admin_forms.MatchCreate
            return render(request, 'admin_ac/match_create.html', {'form': form, })
        if request.method == 'POST':
            form = admin_forms.MatchCreate(request.POST)
            if form.is_valid():
                if form.cleaned_data['club_1'] != form.cleaned_data['club_2']:
                    admin_conector.match_create(form.cleaned_data['club_1'],
                                                form.cleaned_data['club_2'],
                                                form.cleaned_data['date'],
                                                form.cleaned_data['coefficient'] )
            return HttpResponseRedirect('/admin/match/')

def bet_test(id_match, id_win, cofficient):
    bet_match = admin_conector.get_bet_mtach_by_id_match(id_match, id_win)
    admin_conector.add_wingame(id_win)
    if id_win != False:
        for item in bet_match:
            bet = admin_conector.get_bet_by_id_btm(item[0])
            money = bet[1]*cofficient
            user_db_conect.add_money(bet[3], money)
            log_money.add_log_bet(bet[3], 'win', money, bet[0])

def match_spec(request, id=None):
    if 'admin_user_id' in request.session:
        if request.method == 'GET':
            match = admin_conector.get_match_by_id(int(id))
            form = admin_forms.MatchEdit()
            form.fields['coefficient'].initial = match[6]
            form.fields['date'].initial = match[3]
            form.fields['club_1'].initial = match[1]
            form.fields['club_2'].initial = match[2]
            if match[4] != None and match[5] != None:
                form.fields['gool_club_1'].initial = match[4]
                form.fields['gool_club_2'].initial = match[5]
            return render(request, 'admin_ac/match_spec.html', {'form': form, 'match': match, })
        if request.method == 'POST':
            form = admin_forms.MatchEdit(request.POST)
            if form.is_valid():
                match = admin_conector.get_match_by_id(int(id))
                if form.cleaned_data['gool_club_1'] != None and form.cleaned_data['gool_club_2'] != None:
                    if match[7] == False:
                        test = True
                        if form.cleaned_data['gool_club_1']  < form.cleaned_data['gool_club_2']:
                            bet_test(match[0], match[2], match[6])
                            admin_conector.add_game(form.cleaned_data['club_1'])
                            admin_conector.add_game(form.cleaned_data['club_2'])
                        elif  form.cleaned_data['gool_club_1']  > form.cleaned_data['gool_club_2']:
                            bet_test(match[0], match[1], match[6])
                            admin_conector.add_game(form.cleaned_data['club_1'])
                            admin_conector.add_game(form.cleaned_data['club_2'])
                        else:
                            bet_test(match[0], False, match[6])
                            admin_conector.add_game(form.cleaned_data['club_1'])
                            admin_conector.add_game(form.cleaned_data['club_2'])
                    else:
                        test = True
                else:
                    test = False
                admin_conector.update_match(id,
                                            form.cleaned_data['club_1'],
                                            form.cleaned_data['club_2'],
                                            form.cleaned_data['date'],
                                            form.cleaned_data['coefficient'],
                                            form.cleaned_data['gool_club_1'],
                                            form.cleaned_data['gool_club_2'],
                                            test)
                return HttpResponseRedirect('/admin/match/')


def match_del(request, id=None):
    if 'admin_user_id' in request.session:
        admin_conector.match_del(int(id))
        return HttpResponseRedirect('/admin/match/')


def bets(request):
    if 'admin_user_id' in request.session:
        admin_id = request.session['admin_user_id']
        admin = user_db_conect.get_user_by_id(admin_id)
        if request.method == 'GET':
            form = admin_forms.SearchForm()
            bets = admin_conector.get_all_bets()
            return render(request, 'admin_ac/bets.html', {'admin': admin, 'form': form, 'bets': bets, })
        else:
            if request.method == 'POST':
                form = admin_forms.SearchForm(request.POST)
                if form.is_valid():
                    bets = admin_conector.get_all_bets(form.cleaned_data['date'],
                                                        form.cleaned_data['date_max'],
                                                        form.cleaned_data['money_min'],
                                                        form.cleaned_data['money_max'])
                return render(request, 'admin_ac/bets.html', {'admin': admin, 'form': form, 'bets': bets, })

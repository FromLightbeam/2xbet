from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

import acaunt.user_db_conect as us
import admin_ac.admin_conector as admin_conector
import lab.rate_connector as rate_connector
import acaunt.user_db_conect as udbc
import acaunt.log_money as lg
import lab.forms as forms

def index(request):
    matches  = admin_conector.get_all_match()
    if('user_id' in request.session):
        user_id = request.session['user_id']
        user = us.get_user_by_id(user_id)
        return render(request, 'index.html', {'user': user, 'q': True, 'matches': matches})
    else:
        return render(request, 'index.html', {'q': False,'matches': matches})

def rate(request ,id_match):
    if ('user_id' in request.session):
        match  = rate_connector.get_match_by_id_rate(id_match)
        user = us.get_user_by_id(request.session['user_id'])

        form = forms.BetForm(id_match)

        q = True
        return render(request, 'lab/rate.html', { 'user': user, 'q': q, 'match': match, 'form': form })
    else:
        q = False
        return render(request, 'lab/rate.html', {'q': q, })

def bet_put(request, id_match):
    if ('user_id' in request.session):
        user_id = request.session['user_id']
        if request.method == 'POST':
            bet_money = request.POST['money']    
            event_id = request.POST['event']
            money = udbc.withdraw_money(user_id, int(bet_money))
            if money != False:
                id_bet = rate_connector.bet_put(user_id, event_id, bet_money)
                lg.add_log_bet(user_id, 'bet', int(money), id_bet)
                return HttpResponseRedirect('/')
            else:
                HttpResponseRedirect('/rate/{0}/'.format(id1))
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/accaunt/login/')

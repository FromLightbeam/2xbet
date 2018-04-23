from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

import acaunt.user_db_conect as us
import admin_ac.admin_conector as admin_conector
import lab.rate_connector as rate_connector
import acaunt.user_db_conect as udbc
import acaunt.log_money as lg
import lab.forms as forms

def index(request):
    mch  = admin_conector.get_all_match()
    if('user_id' in request.session):
        user_id = request.session['user_id']
        user = us.get_user_by_id(user_id)
        q = True
        return render(request, 'index.html', {'user': user, 'q': q, 'match': mch})
    else:
        q = False
        return render(request, 'index.html', {'q': q,'match': mch})

def rate(request ,id1):
    if ('user_id' in request.session):
        mch  = rate_connector.get_match_by_id_rate(id1)
        user_id = request.session['user_id']
        user = us.get_user_by_id(user_id)
        chois = ((mch[0][5],mch[0][1]), (mch[0][6],mch[0][2]))
        form = forms.BetMake({'choise': chois, })
        q = True
        return render(request, 'lab/rate.html', {'user': user, 'q': q, 'match': mch, 'form': form, })
    else:
        q = False
        return render(request, 'lab/rate.html', {'q': q, })

def bet_put(request, id1=None):
    if ('user_id' in request.session):
        user_id = request.session['user_id']
        if request.method == 'POST':
            num = request.POST['num']
            club = request.POST['club']
            money = udbc.withdraw_money(user_id, int(num))
            if money != False:
                id_bet = rate_connector.bet_put(user_id, id1, int(club), int(num))
                lg.add_log_bet(user_id, 'bet', int(num), id_bet)
                return HttpResponseRedirect('/')
            else:
                HttpResponseRedirect('/rate/{0}/'.format(id1))
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/accaunt/login/')

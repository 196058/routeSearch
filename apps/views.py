from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth import logout
from django.template.context_processors import request
from django.views.generic import ListView, DetailView

from .form import UserAddForm, LoginForm, MecaAddForm, PaddyAddForm
from .models import User, Mecainfo, Paddy


def index(request):
    # ゲストログインでの利用後に新規登録せずindexに遷移した場合にsession削除
    # if (request.session.get('paddy_info') is not None) and (request.session.get('meca_info') is not None):
    #     del request.session['paddy_info']
    #     del request.session['meca_info']
    return render(request, 'index.html')


# 新規登録
def shinki_add(request):
    # formを使わないため処理なし
    return render(request, 'Shinki_Function/shinki_add.html')


def shinki_add_confirm(request):
    if request.method == 'POST':
        input_id = request.POST.get('id')
        print("[shinki_add_confirm]入力ID: ", input_id)
        user_info = UserAddForm(request.POST)
        try:
            check = User.objects.get(id=input_id)
            if check is not None:
                return HttpResponse('入力されたユーザIDはすでに登録されています。<br>ユーザIDを変えてください。')
        except User.DoesNotExist:
            if user_info.is_valid():
                context = {
                    'user_info': user_info
                }
                return render(request, 'Shinki_Function/shinki_add_confrim.html', context)
            else:
                return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')


def shinki_add_comp(request):
    if request.method == 'POST':
        # ゲストログインでの利用後に新規登録した際の田んぼ情報、機械情報をDBに登録するプログラム
        # if (request.session.get('paddy_info') is not None) and (request.session.get('meca_info') is not None):
        #     id = request.POST.get('id')
        #     # paddy_info情報の登録（Guest）
        #     paddy_info = PaddyAddForm(request.session.get('paddy_info'))
        #     paddy_info.id = id
        #     if paddy_info.is_valid():
        #         paddy_info.save()
        #         del request.session['paddy_info']
        #     # field_info情報の登録（Guest）
        #     field_info = FieldAddForm(request.session.get('field_info'))
        #     field_info.id = id
        #     if field_info.is_valid():
        #         field_info.save()
        #         del request.session['field_info']
        #     # meca_infoの登録（Guest）
        #     meca_info = MecaAddForm(request.session.get('meca_info'))
        #     meca_info.id = id
        #     if meca_info.is_valid():
        #         meca_info.save()
        #         del request.session['meca_info']

        user_info = UserAddForm(request.POST)
        if user_info.is_valid():
            user_info.save()
            # context = {
            #     'form': user_info
            # }
            return render(request, 'Shinki_Function/shinki_add_comp.html')
        else:
            return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')


# ログイン
def login(request):
    login_form = LoginForm()
    context = {
        'form': login_form
    }
    return render(request, 'Login_Function/login.html', context)


def member_login(request):
    user_info = request.session.get('user_info')
    print(user_info)
    try:
        if request.method == 'POST':
            user_id = request.POST.get('id')
            user = User.objects.get(id=user_id)
            if user.pass_word == request.POST['pass_word']:
                context = {
                    'id': user.id,
                    'user_name': user.user_name,
                    'pass_word': user.pass_word,
                    'mail': user.mail,
                }
                request.session['user_info'] = context
                return render(request, 'Login_Function/home.html')
            else:
                return HttpResponse('NoMatch')
        # homeへ戻るボタン
        elif user_info != 'None':
            return render(request, 'Login_Function/home.html')

        else:
            return HttpResponse('間違ったメソッドを使用しています。')
    except User.DoesNotExist:
        return HttpResponse('NotFound')


def member_logout(request):
    del request.session['user_info']
    logout(request)
    return render(request, 'index.html')


# def doorway_choice(request):
#     return render(request, 'Login_Function/doorway_choice.html')


# def route_info(request):
#     return render(request, 'Login_Function/route_info.html')


def route_search(request):
    # if request.method == 'POST':
    #     if request.POST['meca'] != None:
    #         meca_name = request.POST['meca']
    #
    #     else:
    #         meca_info = MecaAddForm(request.POST)
    #         if meca_info.is_valid():
    #             meca_info.save()
    #             context = {
    #                 'form': meca_info
    #             }
    #             return render(request, 'Login_Function/kikai_add_comp.html', context)
    #         else:
    #             return HttpResponse('フォームの入力に誤りがあります')
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Login_Function/route_search.html')


def tanbo_master(request):
    user_info = request.session.get('user_info')
    # paddyテーブルをユーザIDで検索しname順に整列
    paddy = Paddy.objects.filter(id=user_info['id']).order_by('name')
    context = {
        'paddy': paddy
    }
    return render(request, 'Login_Function/tanbo_master.html', context)


def tanbo_info(request):
    # # 登録した田んぼを一覧表示する処理
    # user_info = request.session.get('user_info')
    # paddy_info = Paddy.objects.filter(id=user_info['id']).order_by('name')
    # context = {
    #     'paddy': paddy_info
    # }
    # return render(request, 'Login_Function/tanbo_info.html', context)
    return render(request, 'Login_Function/tanbo_info.html')


def tanbo_add(request):
    # formを使わないため処理なし
    return render(request, 'Login_Function/tanbo_add.html')


def tanbo_add_confirm(request):
    if request.method == 'POST':
        paddy = PaddyAddForm(request.POST)
        if paddy.is_valid():
            context = {
                'paddy': paddy
            }
            return render(request, 'Login_Function/tanbo_add_confirm.html', context)
        else:
            return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')


def tanbo_add_comp(request):
    if request.method == 'POST':
        paddy = PaddyAddForm(request.POST)
        if paddy.is_valid():
            paddy.save()
            context = {
                'form': paddy
            }
            return render(request, 'Login_Function/tanbo_add_comp.html', context)
        else:
            return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')


def tanbo_del_confirm(request):
    # if request.method == 'POST':
    #     paddy_id = request.POST.get('paddy_id')
    #     paddy_info = Paddy.objects.get(paddy_id=paddy_id)
    #     context = {
    #         'meca_info': paddy_info
    #     }
    #     return render(request, 'Login_Function/tanbo_del_confirm.html', context)
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Login_Function/tanbo_del_confirm.html')


def tanbo_del_comp(request):
    # if request.method == 'POST':
    #     user_info = request.session.get('user_info')
    #     user_id = user_info['id']
    #     paddy_name = request.POST.get('paddy_name')
    #     print(user_info['id'], request.POST.get('name'))
    #     record = Paddy.objects.get(id=user_id, name=paddy_name)
    #     print('record', record)
    #     record.delete()
    #     return render(request, 'Login_Function/tanbo_del_comp.html')
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Login_Function/tanbo_del_comp.html')


def tanbo_edit(request):
    # if request.method == 'POST':
    #     paddy_id = request.POST.get('paddy_id')
    #     # meca_info = MecaAddForm(request.POST)
    #     paddy_info = Paddy.objects.get(paddy_id=paddy_id)
    #     print("[tanbo_edit]paddy_info:", paddy_info)
    #     context = {
    #         'meca_info': paddy_info
    #     }
    #     request.session['paddy_name'] = paddy_info.name
    #     return render(request, 'Login_Function/tanbo_edit.html', context)
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Login_Function/tanbo_edit.html')


def tanbo_edit_confirm(request):
    # if request.method == 'POST':
    #     paddy_info = PaddyAddForm(request.POST)
    #     user_info = request.session.get('user_info')
    #     user_id = user_info['id']
    #     paddy_name = request.POST.get('name')
    #     if paddy_name != request.session.get('paddy_name'):
    #         try:
    #             check = Paddy.objects.get(id=user_id, name=paddy_name)
    #             if check is not None:
    #                 return HttpResponse('入力された田んぼ名はすでに登録されています。<br>田んぼ名を変えてください。')
    #         except Paddy.DoesNotExist:
    #             pass
    #
    #     if paddy_info.is_valid():
    #         context = {
    #             'paddy_info': paddy_info,
    #             'id': user_id,
    #         }
    #         return render(request, 'Login_Function/tanbo_edit_confirm.html', context)
    #     else:
    #         return HttpResponse('フォームの入力に誤りがあります')
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Login_Function/tanbo_edit_confirm.html')


def tanbo_edit_comp(request):
    # if request.method == 'POST':
    #     user_info = request.session.get('user_info')
    #     user_id = user_info['id']
    #     paddy_name = request.session.get('paddy_name')
    #     paddy_info = Paddy.objects.get(id=user_id, name=paddy_name)
    #     paddy_form = PaddyAddForm(request.POST, instance=paddy_info)
    #     if paddy_form.is_valid():
    #         paddy_form.save()
    #         return render(request, 'Login_Function/tanbo_edit_comp.html')
    # #
    # else:
    #     return HttpResponse('フォームの入力に誤りがあります')
    return render(request, 'Login_Function/tanbo_edit_comp.html')


def kikai_master(request):
    user_info = request.session.get('user_info')
    meca_info = Mecainfo.objects.filter(id=user_info['id']).order_by('name')
    context = {
        'meca_info': meca_info
    }
    return render(request, 'Login_Function/kikai_master.html', context)


def kikai_info(request):
    # 田んぼ情報の取得
    # if request.method == 'POST':
    #     if request.POST['paddy'] != None:
    #         paddy_na
    #     paddy_info = PaddyAddForm(request.POST)
    # 機械一覧処理
    user_info = request.session.get('user_info')
    meca_info = Mecainfo.objects.filter(id=user_info['id']).order_by('name')
    context = {
        'meca_info': meca_info
    }
    return render(request, 'Login_Function/kikai_info.html', context)
    # return render(request, 'Login_Function/kikai_info.html')


def kikai_add(request):
    # 確認画面から内容修正した場合に入力値を取得する為のPOST
    # if request.method == 'POST':
    #     meca_info = MecaAddForm(request.POST)
    #     if meca_info.is_valid():
    #         context = {
    #             'form': meca_info
    #         }
    #         return render(request, 'Login_Function/kikai_add.html', context)
    #     else:
    #         return HttpResponse('フォームの入力に誤りがあります')
    # else:
    user_info = request.session.get('user_info')
    user_id = {
        'id': user_info['id'],
    }
    meca_info = MecaAddForm(user_id)
    meca_info.id = user_info['id']
    print("[kikai_add]meca_info_id: ", meca_info.id)
    context = {
        'form': meca_info,
    }
    return render(request, 'Login_Function/kikai_add.html', context)


def kikai_add_confirm(request):
    if request.method == 'POST':
        user_info = request.session.get('user_info')
        user_id = user_info['id']
        meca_name = request.POST.get('name')
        print('[kikai_add_confirm]', meca_name)
        # print("[kikai_add_confirm]id: ", request.POST.get('id'))
        meca_info = MecaAddForm(request.POST)
        print("add_conf", meca_info)
        try:
            check = Mecainfo.objects.get(id=user_id, name=meca_name)
            if check is not None:
                return HttpResponse('入力された機械名はすでに登録されています。<br>機械名を変えてください。')
        except Mecainfo.DoesNotExist:
            if meca_info.is_valid():
                context = {
                    'meca_info': meca_info
                }
                return render(request, 'Login_Function/kikai_add_confirm.html', context)
            else:
                return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')


def kikai_add_comp(request):
    if request.method == 'POST':
        meca_info = MecaAddForm(request.POST)
        if meca_info.is_valid():
            meca_info.save()
            context = {
                'form': meca_info
            }
            return render(request, 'Login_Function/kikai_add_comp.html', context)
        else:
            return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')


def kikai_del_confirm(request):
    if request.method == 'POST':
        meca_id = request.POST.get('meca_id')
        # meca_info = MecaAddForm(request.POST)
        meca_info = Mecainfo.objects.get(meca_id=meca_id)
        # print("[kikai_edit]maca_id:", meca_info.meca_id)
        context = {
            'meca_info': meca_info
        }
        return render(request, 'Login_Function/kikai_del_confirm.html', context)
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Login_Function/kikai_del_confirm.html')


def kikai_del_comp(request):
    if request.method == 'POST':
        user_info = request.session.get('user_info')
        user_id = user_info['id']
        meca_name = request.POST.get('name')
        print(user_info['id'], request.POST.get('name'))
        # meca_info = MecaAddForm(request.POST)
        record = Mecainfo.objects.get(id=user_id, name=meca_name)
        print('record', record)
        record.delete()
        return render(request, 'Login_Function/kikai_del_comp.html')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Login_Function/kikai_del_comp.html')


# 正
def kikai_edit(request):
    if request.method == 'POST':
        meca_id = request.POST.get('meca_id')
        # meca_info = MecaAddForm(request.POST)
        meca_info = Mecainfo.objects.get(meca_id=meca_id)
        print("[kikai_edit]maca_id:", meca_info)
        context = {
            'meca_info': meca_info
        }
        # 変更前の機械名をsessionで保持
        request.session['meca_name'] = meca_info.name
        return render(request, 'Login_Function/kikai_edit.html', context)
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')


# 仮
# def kikai_edit(request, meca_id):
#     print("[kikai_edit]meca_id:", meca_id)
#     # if request.method == 'POST':
#     meca_info = get_object_or_404(Mecainfo, pk=meca_id)
#     meca_form = MecaAddForm(instance=meca_info)
#     print("[kikai_edit]meca_info:", meca_info.meca_id)
#     print("[kikai_edit]meca_info_id:", meca_info.id)
#     form = MecaAddForm()
#     context = {
#         'meca_info': meca_info,
#         'meca_form': meca_form,
#         'form': form,
#     }
#     request.session['meca_name'] = meca_info.name
#     return render(request, 'Login_Function/kikai_edit.html', context)
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')


def kikai_edit_confirm(request):
    if request.method == 'POST':
        meca_info = MecaAddForm(request.POST)
        user_info = request.session.get('user_info')
        user_id = user_info['id']
        meca_name = request.POST.get('name')
        # 機械名の変更があった場合DB内の機械名と比較
        if meca_name != request.session.get('meca_name'):
            try:
                check = Mecainfo.objects.get(id=user_id, name=meca_name)
                if check is not None:
                    return HttpResponse('入力された機械名はすでに登録されています。<br>機械名を変えてください。')
            except Mecainfo.DoesNotExist:
                pass

        if meca_info.is_valid():
            context = {
                'meca_info': meca_info,
                'id': user_id,
            }
            return render(request, 'Login_Function/kikai_edit_confirm.html', context)
        else:
            return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')


# def kikai_edit_comp(request):
#     if request.method == 'POST':
#         meca_id = request.POST['meca_id']
#         print("[kikai_edit_comp]meca_id: ", meca_id)
#         # データ取得
#         meca_info = get_object_or_404(Mecainfo, pk=meca_id)
#         print("[kikai_edit_comp]meca_info: ", meca_info)
#         meca_form = MecaAddForm(request.POST, instance=meca_info)
#         print("[kikai_edit_comp]meca_form: ", meca_form)
#         if meca_form.is_valid():
#             meca_form.save()
#             return render(request, 'Login_Function/kikai_edit_comp.html')
#         else:
#             return HttpResponse('フォームの入力に誤りがあります')
#     else:
#         return HttpResponse('フォームの送信に使用しているメソッドが違います')


def kikai_edit_comp(request):
    if request.method == 'POST':
        user_info = request.session.get('user_info')
        user_id = user_info['id']
        # 変更前の機械名を取得
        meca_name = request.session.get('meca_name')
        # ユーザIDと変更前の機械名で対象レコード取得
        meca_info = Mecainfo.objects.get(id=user_id, name=meca_name)
        meca_form = MecaAddForm(request.POST, instance=meca_info)
        print('[kikai_edit_comp]meca_form', meca_form['id'], meca_form['full_length'])
        if meca_form.is_valid():
            print(meca_form)
            meca_form.save()
            # 変更前機械名のsession削除
            del request.session['meca_name']
            return render(request, 'Login_Function/kikai_edit_comp.html')
    else:
        return HttpResponse('フォームの入力に誤りがあります')


# ゲスト
def Guest_route_search(request):
    # 田んぼsessionと機械情報を取得
    # paddy_info = request.session.get('paddy_info')
    # if request.method == 'POST':
    #     meca_info = MecaAddForm(request.POST)
    #     request.session['meca_info'] = meca_info
    #
    #
    #
    #
    # ルート検索プログラム
    return render(request, 'Guest_Function/route_search.html')


def Guest_tanbo_info(request):
    # マップ表示プログラム
    return render(request, 'Guest_Function/tanbo_info.html')


def Guest_kikai_info(request):
    # tanbo_info.htmlから田んぼ情報を取得
    # 田んぼ情報をsessionに保持
    return render(request, 'Guest_Function/kikai_info.html')


# def solicit_create_account(request):
#     return render(request, 'Guest_Function/solicit_create_account.html')


def proposal(request):
    return render(request, 'Guest_Function/proposal.html')


# 管理者
def admin_login(request):
    login_form = LoginForm()
    context = {
        'form': login_form
    }
    return render(request, 'Kanrisya_Function/login.html', context)
    # return render(request, 'Kanrisya_Function/login.html')


def admin_home(request):
    admin_info = request.session.get('admin_info')
    print(admin_info)
    try:
        if request.method == 'POST':
            admin_id = request.POST.get('id')
            admin = User.objects.get(id=admin_id)
            if admin.pass_word == request.POST['pass_word']:
                context = {
                    'id': admin.id,
                    'user_name': admin.user_name,
                    'pass_word': admin.pass_word,
                    'mail': admin.mail,
                }
                request.session['admin_info'] = context
                return render(request, 'Kanrisya_Function/home.html', context)
            else:
                return HttpResponse('NoMatch')
        # homeへ戻るボタン
        elif admin_info != 'None':
            return render(request, 'Kanrisya_Function/home.html')

        else:
            return HttpResponse('間違ったメソッドを使用しています。')
    except User.DoesNotExist:
        return HttpResponse('NotFound')
    # return render(request, 'Kanrisya_Function/home.html')


def admin_logout(request):
    del request.session['user_info']
    logout(request)
    return render(request, 'Kanrisya_Function/login.html')


def admin_master(request):
    # 管理者テーブル未作成↓
    # admin_info = User.objects.all()
    # context = {
    #     'admin_info': admin_info
    # }
    # return render(request, 'Kanrisya_Function/admin_master.html', context)
    return render(request, 'Kanrisya_Function/admin_master.html')


def admin_search(request):
    name_key = request.POST.get('name_key')
    print(name_key)
    user_info = User.objects.filter(user_name__icontains=name_key)
    print('user_info', user_info)
    context = {
        'user_info': user_info
    }
    return render(request, 'Kanrisya_Function/admin_master.html', context)
    # return render(request, 'Kanrisya_Function/users_master.html')


def admin_list(request):
    user_info = User.objects.all()
    print('user_info', user_info)
    context = {
        'user_info': user_info
    }
    return render(request, 'Kanrisya_Function/admin_master.html', context)


def admin_add(request):
    return render(request, 'Kanrisya_Function/admin_add.html')


def admin_add_confirm(request):
    # if request.method == 'POST':
    #     input_id = request.POST.get('id')
    #     print("[admin_add_confirm]入力ID: ", input_id)
    #     admin_info = UserAddForm(request.POST)
    #     try:
    #         check = User.objects.get(id=input_id)
    #         if check is not None:
    #             return HttpResponse('入力されたユーザIDはすでに登録されています。<br>ユーザIDを変えてください。')
    #     except User.DoesNotExist:
    #         if admin_info.is_valid():
    #             context = {
    #                 'admin_info': admin_info
    #             }
    #             return render(request, 'Kanrisya_Function/admin_add_confirm.html', context)
    #         else:
    #             return HttpResponse('フォームの入力に誤りがあります')
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Kanrisya_Function/admin_add_confirm.html')


def admin_add_comp(request):
    # if request.method == 'POST':
    #     admin_info = UserAddForm(request.POST)
    #     if admin_info.is_valid():
    #         admin_info.save()
    #         context = {
    #             'form': admin_info
    #         }
    #         return render(request, 'Kanrisya_Function/admin_add_comp.html', context)
    #     else:
    #         return HttpResponse('フォームの入力に誤りがあります')
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Kanrisya_Function/admin_add_comp.html')


def admin_del_confirm(request):
    # if request.method == 'POST':
    #     admin_id = request.POST.get('admin_id')
    #     admin_info = User.objects.get(id=admin_id)
    #     context = {
    #         'admin_info': admin_info
    #     }
    #     return render(request, 'Kanrisya_Function/admin_del_confirm.html', context)
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Kanrisya_Function/admin_del_confirm.html')


def admin_del_comp(request):
    # if request.method == 'POST':
    #     admin_id = request.POST.get('admin_id')
    #     admin_record = User.objects.get(id=admin_id)
    #     print('[admin_del_comp]admin_record', admin_record)
    #     admin_record.delete()
    #     return render(request, 'Kanrisya_Function/admin_del_comp.html')
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Kanrisya_Function/admin_del_comp.html')


def admin_edit(request):
    # if request.method == 'POST':
    #     admin_id = request.POST.get('id')
    #     admin_info = User.objects.get(id=admin_id)
    #     print("[admin_edit]admin_info:", admin_info)
    #     context = {
    #         'admin_info': admin_info
    #     }
    #     request.session['admin_id'] = admin_info.id
    #     return render(request, 'Kanrisya_Function/admin_edit.html', context)
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Kanrisya_Function/admin_edit.html')


def admin_edit_confirm(request):
    # if request.method == 'POST':
    #     admin_info = UserAddForm(request.POST)
    #     admin_id = request.POST.get('id')
    #     if admin_id != request.session.get('admin_id'):
    #         try:
    #             check = User.objects.get(id=admin_id)
    #             if check is not None:
    #                 return HttpResponse('入力されたIDはすでに登録されています。<br>IDを変えてください。')
    #         except User.DoesNotExist:
    #             pass
    #
    #     if admin_info.is_valid():
    #         context = {
    #             'admin_info': admin_info,
    #             'id': admin_id,
    #         }
    #         return render(request, 'Kanrisya_Function/admin_edit_confirm.html', context)
    #     else:
    #         return HttpResponse('フォームの入力に誤りがあります')
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Kanrisya_Function/admin_edit_confirm.html')


def admin_edit_comp(request):
    # if request.method == 'POST':
    #     admin_id = request.session.get('admin_id')
    #     admin_info = User.objects.get(id=admin_id)
    #     admin_form = UserAddForm(request.POST, instance=admin_info)
    #     print('[admin_edit_comp]admin_form', admin_form['id'], admin_form['name'])
    #     if admin_form.is_valid():
    #         print(admin_form)
    #         admin_form.save()
    #         # admin_idのsession削除
    #         del request.session['admin_id']
    #         return render(request, 'Kanrisya_Function/admin_edit_comp.html')
    # else:
    #     return HttpResponse('フォームの入力に誤りがあります')
    return render(request, 'Kanrisya_Function/admin_edit_comp.html')


def users_master(request):
    user_info = User.objects.all()
    print('user_info', user_info)
    context = {
        'user_info': user_info
    }
    return render(request, 'Kanrisya_Function/users_master.html', context)
    # return render(request, 'Kanrisya_Function/users_master.html')


def users_search(request):
    name_key = request.POST.get('name_key')
    print(name_key)
    user_info = User.objects.filter(user_name__icontains=name_key)
    print('user_info', user_info)
    context = {
        'user_info': user_info
    }
    return render(request, 'Kanrisya_Function/users_master.html', context)
    # return render(request, 'Kanrisya_Function/users_master.html')


def users_list(request):
    user_info = User.objects.all()
    print('user_info', user_info)
    context = {
        'user_info': user_info
    }
    return render(request, 'Kanrisya_Function/users_master.html', context)


def users_add(request):
    return render(request, 'Kanrisya_Function/users_add.html')


def users_add_confirm(request):
    if request.method == 'POST':
        input_id = request.POST.get('id')
        print("[users_add_confirm]入力ID: ", input_id)
        user_info = UserAddForm(request.POST)
        try:
            check = User.objects.get(id=input_id)
            if check is not None:
                return HttpResponse('入力されたユーザIDはすでに登録されています。<br>ユーザIDを変えてください。')
        except User.DoesNotExist:
            if user_info.is_valid():
                context = {
                    'user_info': user_info
                }
                return render(request, 'Kanrisya_Function/users_add_confirm.html', context)
            else:
                return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/users_add_confirm.html')


def users_add_comp(request):
    if request.method == 'POST':
        user_info = UserAddForm(request.POST)
        if user_info.is_valid():
            user_info.save()
            context = {
                'form': user_info
            }
            return render(request, 'Kanrisya_Function/users_add_comp.html', context)
        else:
            return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/users_add_comp.html')


def users_del_confirm(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        user_info = User.objects.get(id=user_id)
        context = {
            'user_info': user_info
        }
        return render(request, 'Kanrisya_Function/users_del_confirm.html', context)
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/users_del_confirm.html')


def users_del_comp(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        user_record = User.objects.get(id=user_id)
        print('[users_del_comp]user_record', user_record)
        user_record.delete()
        return render(request, 'Kanrisya_Function/users_del_comp.html')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/users_del_comp.html')


def users_edit(request):
    # if request.method == 'POST':
    #     user_id = request.POST.get('id')
    #     user_info = User.objects.get(id=user_id)
    #     print("[users_edit]user_info:", user_info)
    #     context = {
    #         'user_info': user_info
    #     }
    #     request.session['user_id'] = user_info.id
    #     return render(request, 'Kanrisya_Function/users_edit.html', context)
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Kanrisya_Function/users_edit.html')


def users_edit_confirm(request):
    # if request.method == 'POST':
    #     user_info = UserAddForm(request.POST)
    #     user_id = request.POST.get('id')
    #     if user_id != request.session.get('user_id'):
    #         try:
    #             check = User.objects.get(id=user_id)
    #             if check is not None:
    #                 return HttpResponse('入力されたユーザIDはすでに登録されています。<br>ユーザIDを変えてください。')
    #         except User.DoesNotExist:
    #             pass
    #
    #     if user_info.is_valid():
    #         context = {
    #             'user_info': user_info,
    #             'id': user_id,
    #         }
    #         return render(request, 'Kanrisya_Function/users_edit_confirm.html', context)
    #     else:
    #         return HttpResponse('フォームの入力に誤りがあります')
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Kanrisya_Function/users_edit_confirm.html')


def users_edit_comp(request):
    # if request.method == 'POST':
    #     user_id = request.session.get('user_id')
    #     user_info = User.objects.get(id=user_id)
    #     user_form = UserAddForm(request.POST, instance=user_info)
    #     print('[users_edit_comp]user_form', user_form['id'], user_form['name'])
    #     if user_form.is_valid():
    #         print(user_form)
    #         user_form.save()
    #         del request.session['user_id']
    #         return render(request, 'Kanrisya_Function/users_edit_comp.html')
    # else:
    #     return HttpResponse('フォームの入力に誤りがあります')
    return render(request, 'Kanrisya_Function/users_edit_comp.html')


# 問い合わせ
def inquiry_master(request):
    # if request.method == 'POST':
    #     inquiry_info = User.objects.all()
    #     context = {
    #         'inquiry_info': inquiry_info
    #     }
    #   return render(request, 'Kanrisya_Function/inquiry_master.html', context)
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Kanrisya_Function/inquiry_master.html')


def inquiry_search(request):
    # if request.method == 'POST':
    #     inquiry_key = request.POST.get('inquiry_key')
    #     inquiry_info = User.objects.filter(title__iexact=inquiry_key)
    #     context = {
    #         'inquiry_info': inquiry_info
    #     }
    #     return render(request, 'Kanrisya_Function/inquiry_master.html', context)
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Kanrisya_Function/inquiry_master.html')


def inquiry_add(request):
    return render(request, 'Kanrisya_Function/inquiry_add.html')


def inquiry_add_confirm(request):
    return render(request, 'Kanrisya_Function/inquiry_add_confirm.html')


def inquiry_add_comp(request):
    return render(request, 'Kanrisya_Function/inquiry_add_comp.html')


def inquiry_del_confirm(request):
    return render(request, 'Kanrisya_Function/inquiry_del_confirm.html')


def inquiry_del_comp(request):
    return render(request, 'Kanrisya_Function/inquiry_del_comp.html')


def inquiry_edit(request):
    return render(request, 'Kanrisya_Function/inquiry_edit.html')


def inquiry_edit_confirm(request):
    return render(request, 'Kanrisya_Function/inquiry_edit_confirm.html')


def inquiry_edit_comp(request):
    return render(request, 'Kanrisya_Function/inquiry_edit_comp.html')


# エラー
def login_notexit_error(request):
    return render(request, 'error/login_notexit_error.html')


def login_wrong_error(request):
    return render(request, 'error/login_wrong_error.html')


def map_error(request):
    return render(request, 'error/map_error.html')


def register_error(request):
    return render(request, 'error/register_error.html')

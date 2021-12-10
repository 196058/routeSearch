from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth import logout
from django.template.context_processors import request
from django.views.generic import ListView, DetailView

from .form import UserAddForm, LoginForm, MecaAddForm, PaddyAddForm
from .models import User, Mecainfo, Paddy


def index(request):
    return render(request, 'index.html')


# 新規
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
        user_info = UserAddForm(request.POST)
        if user_info.is_valid():
            user_info.save()
            context = {
                'form': user_info
            }
            return render(request, 'Shinki_Function/shinki_add_comp.html', context)
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
    return render(request, 'Login_Function/route_search.html')


def tanbo_master(request):
    user_info = request.session.get('user_info')
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
    # # 新しく田んぼを登録する処理
    #
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
    return render(request, 'Login_Function/tanbo_edit.html')


def tanbo_edit_confirm(request):
    return render(request, 'Login_Function/tanbo_edit_confirm.html')


def tanbo_edit_comp(request):
    return render(request, 'Login_Function/tanbo_edit_comp.html')


def kikai_master(request):
    user_info = request.session.get('user_info')
    meca_info = Mecainfo.objects.filter(id=user_info['id']).order_by('name')
    context = {
        'meca_info': meca_info
    }
    return render(request, 'Login_Function/kikai_master.html', context)


def kikai_info(request):
    # 機械一覧処理
    user_info = request.session.get('user_info')
    meca_info = Mecainfo.objects.filter(id=user_info['id']).order_by('name')
    context = {
        'meca_info': meca_info
    }
    # 機械登録処理
    return render(request, 'Login_Function/kikai_info.html')


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
# def kikai_edit(request):
# if request.method == 'POST':
#     meca_id = request.POST.get('meca_id')
#     # meca_info = MecaAddForm(request.POST)
#     meca_info = Mecainfo.objects.get(meca_id=meca_id)
#     print("[kikai_edit]maca_id:", meca_info)
#     context = {
#         'meca_info': meca_info
#     }
#     return render(request, 'Login_Function/kikai_edit.html', context)
# else:
#     return HttpResponse('フォームの送信に使用しているメソッドが違います')


# 仮
def kikai_edit(request, meca_id):
    print("[kikai_edit]meca_id:", meca_id)
    # if request.method == 'POST':
    meca_info = get_object_or_404(Mecainfo, pk=meca_id)
    meca_form = MecaAddForm(instance=meca_info)
    print("[kikai_edit]meca_info:", meca_info.meca_id)
    print("[kikai_edit]meca_info_id:", meca_info.id)
    context = {
        'meca_info': meca_info,
        'meca_form': meca_form,
    }
    request.session['meca_name'] = meca_info.name
    return render(request, 'Login_Function/kikai_edit.html', context)
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')


def kikai_edit_confirm(request):
    if request.method == 'POST':
        meca_info = MecaAddForm(request.POST)
        user_info = request.session.get('user_info')
        user_id = user_info['id']
        if meca_info.is_valid():
            meca_name = request.POST.get('name')
            print('[kikai_edit_confirm]', meca_name)
            print("[kikai_edit_confirm]meca_info:", meca_name)
        # print("[kikai_edit_confirm]mecaid: ", meca_info.meca_id)
        try:
            check = Mecainfo.objects.get(id=user_id, name=meca_name)
            if check is not None:
                return HttpResponse('入力された機械名はすでに登録されています。<br>機械名を変えてください。')
        except Mecainfo.DoesNotExist:
            if meca_info.is_valid():
                context = {
                    'meca_info': meca_info,
                    'user_id': user_id,
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
    # print("[kikai_edit_comp]meca_id:", meca_id)
    if request.method == 'POST':
        # meca_info = MecaAddForm(request.POST)
        user_info = request.session.get('user_info')
        user_id = user_info['id']
        meca_name = request.session.get('meca_name')
        meca_info = Mecainfo.objects.get(id=user_id, name=meca_name)
        # print("[kikai_edit_comp]meca_id:", meca_info.meca_id)
        # id = meca_info.id
        # meca_name = meca_info.name
        # meca_info = get_object_or_404(Mecainfo, id=id, name=meca_name)
        meca_form = MecaAddForm(request.POST, instance=meca_info)
        print(type(meca_form['id']))
        # meca_form['id'] = user_id
        print('[kikai_edit_comp]meca_form', meca_form['id'], meca_form['full_length'])
        if meca_form.is_valid():
            meca_form.save()
            return render(request, 'Login_Function/kikai_edit_comp.html')
    else:
        return HttpResponse('フォームの入力に誤りがあります')

    #     meca_id = request.POST['meca_id']
    #     print("[kikai_edit_comp]meca_id: ", meca_id)
    #     # データ取得
    #
    #     print("[kikai_edit_comp]meca_info: ", meca_info)
    #
    #     print("[kikai_edit_comp]meca_form: ", meca_form)
    #
    #
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')


# ゲスト
def Guest_route_search(request):
    return render(request, 'Guest_Function/route_search.html')


def Guest_tanbo_info(request):
    return render(request, 'Guest_Function/tanbo_info.html')


def Guest_kikai_info(request):
    return render(request, 'Guest_Function/kikai_info.html')


# def solicit_create_account(request):
#     return render(request, 'Guest_Function/solicit_create_account.html')


def proposal(request):
    return render(request, 'Guest_Function/proposal.html')


# 管理者
def admin_login(request):
    # login_form = LoginForm()
    # context = {
    #     'form': login_form
    # }
    # return render(request, 'Kanrisya_Function/login.html', context)
    return render(request, 'Kanrisya_Function/login.html')


def admin_home(request):
    # admin_info = request.session.get('admin_info')
    # print(admin_info)
    # try:
    #     if request.method == 'POST':
    #         admin_id = request.POST.get('id')
    #         admin = User.objects.get(id=admin_id)
    #         if admin.pass_word == request.POST['pass_word']:
    #             context = {
    #                 'id': admin.id,
    #                 'user_name': admin.user_name,
    #                 'pass_word': admin.pass_word,
    #                 'mail': admin.mail,
    #             }
    #             request.session['admin_info'] = context
    #             return render(request, 'Kanrisya_Function/home., context)
    #         else:
    #             return HttpResponse('NoMatch')
    #     # homeへ戻るボタン
    #     elif admin_info != 'None':
    #         return render(request, 'Kanrisya_Function/home.html')
    #
    #     else:
    #         return HttpResponse('間違ったメソッドを使用しています。')
    # except User.DoesNotExist:
    #     return HttpResponse('NotFound')
    return render(request, 'Kanrisya_Function/home.html')


def admin_master(request):
    # 管理者rollを指定する（未設定）↓
    # admin_info = User.objects.filter(roll='')
    # context = {
    #     'admin_info': admin_info
    # }
    # return render(request, 'Kanrisya_Function/admin_master.html', context)
    return render(request, 'Kanrisya_Function/admin_master.html')


def admin_add(request):
    # admin_info = UserAddForm
    # context = {
    #     'form': admin_info
    # }
    # return render(request, 'Kanrisya_Function/admin_add.html', context)
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
    return render(request, 'Kanrisya_Function/admin_edit.html')


def admin_edit_confirm(request):
    return render(request, 'Kanrisya_Function/admin_edit_confirm.html')


def admin_edit_comp(request):
    return render(request, 'Kanrisya_Function/admin_edit_comp.html')


def users_master(request):
    # 利用者rollを指定する（未設定）↓
    # user_info = User.objects.filter(roll='')
    # context = {
    #     'user_info': user_info
    # }
    # return render(request, 'Kanrisya_Function/users_master.html', context)
    return render(request, 'Kanrisya_Function/users_master.html')


def users_add(request):
    # user_info = UserAddForm
    # context = {
    #     'form': user_info
    # }
    # return render(request, 'Kanrisya_Function/users_add.html', context)
    return render(request, 'Kanrisya_Function/users_add.html')


def users_add_confirm(request):
    # if request.method == 'POST':
    #     input_id = request.POST.get('id')
    #     print("[shinki_add_confirm]入力ID: ", input_id)
    #     user_info = UserAddForm(request.POST)
    #     try:
    #         check = User.objects.get(id=input_id)
    #         if check is not None:
    #             return HttpResponse('入力されたユーザIDはすでに登録されています。<br>ユーザIDを変えてください。')
    #     except User.DoesNotExist:
    #         if user_info.is_valid():
    #             context = {
    #                 'user_info': user_info
    #             }
    #             return render(request, 'Kanrisya_Function/users_add_confirm.html', context)
    #         else:
    #             return HttpResponse('フォームの入力に誤りがあります')
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Kanrisya_Function/users_add_confirm.html')


def users_add_comp(request):
    # if request.method == 'POST':
    #     user_info = UserAddForm(request.POST)
    #     if user_info.is_valid():
    #         user_info.save()
    #         context = {
    #             'form': user_info
    #         }
    #         return render(request, 'Kanrisya_Function/users_add_comp.html', context)
    #     else:
    #         return HttpResponse('フォームの入力に誤りがあります')
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Kanrisya_Function/users_add_comp.html')


def users_del_confirm(request):
    # if request.method == 'POST':
    #     user_id = request.POST.get('user_id')
    #     user_info = User.objects.get(id=user_id)
    #     context = {
    #         'user_info': user_info
    #     }
    #     return render(request, 'Kanrisya_Function/users_del_confirm.html', context)
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Kanrisya_Function/users_del_confirm.html')


def users_del_comp(request):
    # if request.method == 'POST':
    #     user_id = request.POST.get('user_id')
    #     user_record = User.objects.get(id=user_id)
    #     print('[users_del_comp]user_record', user_record)
    #     user_record.delete()
    #     return render(request, 'Kanrisya_Function/users_del_comp.html')
    # else:
    #     return HttpResponse('フォームの送信に使用しているメソッドが違います')
    return render(request, 'Kanrisya_Function/users_del_comp.html')


def users_edit(request):
    return render(request, 'Kanrisya_Function/users_edit.html')


def users_edit_confirm(request):
    return render(request, 'Kanrisya_Function/users_edit_confirm.html')


def users_edit_comp(request):
    return render(request, 'Kanrisya_Function/users_edit_comp.html')


# 問い合わせ
def inquiry_master(request):
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

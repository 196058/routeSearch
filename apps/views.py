from django.shortcuts import render, HttpResponse
from django.contrib.auth import logout
from django.template.context_processors import request

from .form import UserAddForm, LoginForm, MecaAddForm, PaddyAddForm, AdminLoginForm, AdminAddForm, InquiryAddForm
from .models import User, Mecainfo, Paddy, Admin, Inquiry


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
        input_name = request.POST.get('user_name')
        user_info = UserAddForm(request.POST)

        try:
            check = User.objects.get(user_name=input_name)
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
            user_name = request.POST.get('user_name')
            user = User.objects.get(user_name=user_name)
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
                return render(request, 'error/login_wrong_error.html')
                # return HttpResponse('NoMatch')
        # homeへ戻るボタン
        elif user_info != 'None':
            return render(request, 'Login_Function/home.html')

        else:
            return HttpResponse('間違ったメソッドを使用しています。')
    except User.DoesNotExist:
        return render(request, 'error/login_notexit_error.html')
        # return HttpResponse('NotFound')


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
        user_info = request.session.get('user_info')
        user_id = user_info['id']
        paddy_name = request.POST.get('name')
        paddy_info = PaddyAddForm(request.POST)
        # DBのpaddy_nameの重複チェック
        try:
            check = Mecainfo.objects.get(id=user_id, name=paddy_name)
            if check is not None:
                return HttpResponse('入力された田んぼ名はすでに登録されています。<br>田んぼ名を変えてください。')
        except Paddy.DoesNotExist:
            if paddy_info.is_valid():
                context = {
                    'paddy_info': paddy_info,
                    'id': user_id,
                }
                return render(request, 'Login_Function/kikai_add_confirm.html', context)
            else:
                return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')


def tanbo_add_comp(request):
    if request.method == 'POST':
        paddy = PaddyAddForm(request.POST)
        if paddy.is_valid():
            paddy.save()
            return render(request, 'Login_Function/tanbo_add_comp.html')
        else:
            return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')


def tanbo_del_confirm(request):
    # if request.method == 'POST':
    #     paddy_id = request.POST.get('paddy_id')
    #     paddy_info = Paddy.objects.get(paddy_id=paddy_id)
    #     context = {
    #         'paddy_info': paddy_info
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
    # # コード：田んぼの変更範囲次第でFieldの処理も追加する
    # if request.method == 'POST':
    #     paddy_id = request.POST.get('paddy_id')
    #     paddy_info = Paddy.objects.get(paddy_id=paddy_id)
    #     print("[tanbo_edit]paddy_info:", paddy_info)
    #     context = {
    #         'paddy_info': paddy_info
    #     }
    #     # tanbo_edit_confirmでpaddy_nameの重複チェックに使用
    #     request.session['paddy_name'] = paddy_info.name
    #     # tanbo_edit_compで変更するデータを特定するために使用
    #     request.session['paddy_id'] = paddy_id
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
    #     # 田んぼ名の変更があった場合paddy_nameの重複チェック
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
    #     paddy_id = request.session.get('paddy_id')
    #     paddy_info = Paddy.objects.get(paddy_id=paddy_id)
    #     paddy_form = PaddyAddForm(request.POST, instance=paddy_info)
    #     if paddy_form.is_valid():
    #         paddy_form.save()
    #         # 変更のために使用したsessionを削除
    #         del request.session['paddy_name']
    #         del request.session['paddy_id']
    #         return render(request, 'Login_Function/tanbo_edit_comp.html')
    # else:
    #     return HttpResponse('フォームの入力に誤りがあります')
    return render(request, 'Login_Function/tanbo_edit_comp.html')


def kikai_master(request):
    user_info = request.session.get('user_info')
    # DB内をuser_idで検索し、機械名順に整列
    meca_info = Mecainfo.objects.filter(id=user_info['id']).order_by('name')
    context = {
        'meca_info': meca_info
    }
    return render(request, 'Login_Function/kikai_master.html', context)


def kikai_info(request):
    # 田んぼ情報の取得
    if request.method == 'POST':
        # if request.POST['paddy'] != None:
        #     paddy_number = request.POST['paddy']
        #     paddy_info = Paddy.objects.filter(id=paddy_number)
        #     request.session['paddy_info'] = paddy_info
        paddy_info = PaddyAddForm(request.POST)
    # 機械一覧処理
    user_info = request.session.get('user_info')
    meca_info = Mecainfo.objects.filter(id=user_info['id']).order_by('name')
    context = {
        'meca_info': meca_info
    }
    return render(request, 'Login_Function/kikai_info.html', context)
    # return render(request, 'Login_Function/kikai_info.html')


def kikai_add(request):
    # formを使わないため処理なし
    return render(request, 'Login_Function/kikai_add.html')


def kikai_add_confirm(request):
    if request.method == 'POST':
        user_info = request.session.get('user_info')
        user_id = user_info['id']
        meca_name = request.POST.get('name')
        meca_info = MecaAddForm(request.POST)
        # DBのmeca_nameの重複チェック
        try:
            check = Mecainfo.objects.get(id=user_id, name=meca_name)
            if check is not None:
                return HttpResponse('入力された機械名はすでに登録されています。<br>機械名を変えてください。')
        except Mecainfo.DoesNotExist:
            if meca_info.is_valid():
                context = {
                    'meca_info': meca_info,
                    'id': user_id,
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
        meca_info = Mecainfo.objects.get(meca_id=meca_id)
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
        record = Mecainfo.objects.get(id=user_id, name=meca_name)
        record.delete()
        return render(request, 'Login_Function/kikai_del_comp.html')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Login_Function/kikai_del_comp.html')


def kikai_edit(request):
    if request.method == 'POST':
        meca_id = request.POST.get('meca_id')
        meca_info = Mecainfo.objects.get(meca_id=meca_id)
        context = {
            'meca_info': meca_info
        }
        # kikai_edit_confirmでmeca_nameの重複チェックに使用
        request.session['meca_name'] = meca_info.name
        # kikai_edit_compで変更するデータを特定するために使用
        request.session['meca_id'] = meca_id
        return render(request, 'Login_Function/kikai_edit.html', context)
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')


def kikai_edit_confirm(request):
    if request.method == 'POST':
        meca_info = MecaAddForm(request.POST)
        user_info = request.session.get('user_info')
        user_id = user_info['id']
        meca_name = request.POST.get('name')
        # 機械名の変更があった場合meca_nameの重複チェック
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


def kikai_edit_comp(request):
    if request.method == 'POST':
        meca_id = request.session.get('meca_id')
        meca_info = Mecainfo.objects.get(meca_id=meca_id)
        # DBにあるmeca_infoをrequest.POSTに変更
        meca_form = MecaAddForm(request.POST, instance=meca_info)
        if meca_form.is_valid():
            meca_form.save()
            # 変更のために使用したsession削除
            del request.session['meca_name']
            del request.session['meca_id']
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
    # 処理なし
    return render(request, 'Guest_Function/proposal.html')


# 管理者
def admin_login(request):
    login_form = AdminLoginForm()
    context = {
        'form': login_form
    }
    return render(request, 'Kanrisya_Function/login.html', context)
    # return render(request, 'Kanrisya_Function/login.html')


def admin_home(request):
    admin_info = request.session.get('admin_info')
    try:
        if request.method == 'POST':
            admin_name = request.POST.get('user_name')
            admin = Admin.objects.get(user_name=admin_name)
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
    except Admin.DoesNotExist:
        return HttpResponse('NotFound')
    # return render(request, 'Kanrisya_Function/home.html')


def admin_logout(request):
    del request.session['admin_info']
    logout(request)
    return render(request, 'Kanrisya_Function/login.html')


def admin_master(request):
    admin_info = Admin.objects.all()
    context = {
        'admin_info': admin_info
    }
    return render(request, 'Kanrisya_Function/admin_master.html', context)
    # return render(request, 'Kanrisya_Function/admin_master.html')


def admin_search(request):
    name_key = request.POST.get('name_key')
    # DBのuser_nameとkeyの部分一致で名前検索
    admin_info = Admin.objects.filter(user_name__icontains=name_key)
    context = {
        'admin_info': admin_info
    }
    return render(request, 'Kanrisya_Function/admin_master.html', context)
    # return render(request, 'Kanrisya_Function/users_master.html')


def admin_add(request):
    return render(request, 'Kanrisya_Function/admin_add.html')


def admin_add_confirm(request):
    if request.method == 'POST':
        input_user_name = request.POST.get('user_name')
        admin_info = AdminAddForm(request.POST)
        try:
            check = Admin.objects.get(user_name=input_user_name)
            if check is not None:
                return HttpResponse('入力されたユーザ名はすでに登録されています。<br>ユーザ名を変えてください。')
        except Admin.DoesNotExist:
            if admin_info.is_valid():
                context = {
                    'admin_info': admin_info
                }
                return render(request, 'Kanrisya_Function/admin_add_confirm.html', context)
            else:
                return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/admin_add_confirm.html')


def admin_add_comp(request):
    if request.method == 'POST':
        admin_info = AdminAddForm(request.POST)
        if admin_info.is_valid():
            admin_info.save()
            context = {
                'form': admin_info
            }
            return render(request, 'Kanrisya_Function/admin_add_comp.html', context)
        else:
            return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/admin_add_comp.html')


def admin_del_confirm(request):
    if request.method == 'POST':
        admin_id = request.POST.get('id')
        admin_info = Admin.objects.get(id=admin_id)
        context = {
            'admin_info': admin_info
        }
        return render(request, 'Kanrisya_Function/admin_del_confirm.html', context)
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/admin_del_confirm.html')


def admin_del_comp(request):
    if request.method == 'POST':
        admin_id = request.POST.get('id')
        admin_record = Admin.objects.get(id=admin_id)
        admin_record.delete()
        return render(request, 'Kanrisya_Function/admin_del_comp.html')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/admin_del_comp.html')


def admin_edit(request):
    if request.method == 'POST':
        admin_id = request.POST.get('id')
        admin_info = Admin.objects.get(id=admin_id)
        print("[admin_edit]admin_info:", admin_info.id)
        context = {
            'admin_info': admin_info,
        }
        # admin_edit_confirmでuser_nameの重複チェックの際に使用
        request.session['admin_name'] = admin_info.user_name
        # admin_edit_compで変更するデータを特定するために使用
        request.session['admin_id'] = admin_info.id
        return render(request, 'Kanrisya_Function/admin_edit.html', context)
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/admin_edit.html')


def admin_edit_confirm(request):
    if request.method == 'POST':
        admin_info = AdminAddForm(request.POST)
        admin_name = request.POST.get('user_name')
        # ユーザ名の変更があった場合user_nameの重複チェック
        if admin_name != request.session.get('admin_name'):
            try:
                check = Admin.objects.get(user_name=admin_name)
                if check is not None:
                    return HttpResponse('入力されたIDはすでに登録されています。<br>IDを変えてください。')
            except Admin.DoesNotExist:
                pass
        if admin_info.is_valid():
            context = {
                'admin_info': admin_info,
            }
            return render(request, 'Kanrisya_Function/admin_edit_confirm.html', context)
        else:
            return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/admin_edit_confirm.html')


def admin_edit_comp(request):
    if request.method == 'POST':
        admin_id = request.session.get('admin_id')
        admin_info = Admin.objects.get(id=admin_id)
        # DBにあるadmin_infoをrequest.POSTの内容に変更
        admin_form = AdminAddForm(request.POST, instance=admin_info)
        if admin_form.is_valid():
            admin_form.save()
            # 変更のために使用したsession削除
            del request.session['admin_id']
            del request.session['admin_name']
            return render(request, 'Kanrisya_Function/admin_edit_comp.html')
    else:
        return HttpResponse('フォームの入力に誤りがあります')
    # return render(request, 'Kanrisya_Function/admin_edit_comp.html')


def users_master(request):
    user_info = User.objects.all()
    context = {
        'user_info': user_info
    }
    return render(request, 'Kanrisya_Function/users_master.html', context)
    # return render(request, 'Kanrisya_Function/users_master.html')


def users_search(request):
    name_key = request.POST.get('name_key')
    # DBのuser_nameとkeyの部分一致で名前検索
    user_info = User.objects.filter(user_name__icontains=name_key)
    context = {
        'user_info': user_info
    }
    return render(request, 'Kanrisya_Function/users_master.html', context)
    # return render(request, 'Kanrisya_Function/users_master.html')


def users_add(request):
    return render(request, 'Kanrisya_Function/users_add.html')


def users_add_confirm(request):
    if request.method == 'POST':
        input_name = request.POST.get('user_name')
        user_info = UserAddForm(request.POST)
        # ユーザ名の重複チェック
        try:
            check = User.objects.get(user_name=input_name)
            if check is not None:
                return HttpResponse('入力されたユーザ名はすでに登録されています。<br>ユーザ名を変えてください。')
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
        user_record.delete()
        return render(request, 'Kanrisya_Function/users_del_comp.html')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/users_del_comp.html')


def users_edit(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        user_info = User.objects.get(id=user_id)
        context = {
            'id': user_id,
            'user_info': user_info
        }
        # user_edit_compでDBから変更するデータを検索するために使用
        request.session['user_id'] = user_info.id
        # user_edit_compで変更するデータを特定するために使用
        request.session['user_name'] = user_info.user_name
        return render(request, 'Kanrisya_Function/users_edit.html', context)
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/users_edit.html')


def users_edit_confirm(request):
    if request.method == 'POST':
        user_info = UserAddForm(request.POST)
        user_name = request.POST.get('user_name')
        # ユーザ名の変更があった場合のuser_nameの重複チェック
        if user_name != request.session.get('user_name'):
            try:
                check = User.objects.get(user_name=user_name)
                if check is not None:
                    return HttpResponse('入力されたユーザ名はすでに登録されています。<br>ユーザ名を変えてください。')
            except User.DoesNotExist:
                pass
        if user_info.is_valid():
            context = {
                'user_info': user_info,
            }
            return render(request, 'Kanrisya_Function/users_edit_confirm.html', context)
        else:
            return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/users_edit_confirm.html')


def users_edit_comp(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user_info = User.objects.get(id=user_id)
        # 現在DBにあるデータ(user_info)をrequest.POSTの内容に変更
        user_form = UserAddForm(request.POST, instance=user_info)
        if user_form.is_valid():
            user_form.save()
            # 変更のために使用したsessionの削除
            del request.session['user_id']
            del request.session['user_name']
            return render(request, 'Kanrisya_Function/users_edit_comp.html')
    else:
        return HttpResponse('フォームの入力に誤りがあります')
    # return render(request, 'Kanrisya_Function/users_edit_comp.html')


# 問い合わせ
def inquiry_master(request):
    inquiry_info = Inquiry.objects.all()
    context = {
        'inquiry_info': inquiry_info
    }
    return render(request, 'Kanrisya_Function/inquiry_master.html', context)
    # return render(request, 'Kanrisya_Function/inquiry_master.html')


def inquiry_search(request):
    if request.method == 'POST':
        title_key = request.POST.get('title_key')
        # DBのtitleとkeyの部分一致での検索
        inquiry_info = Inquiry.objects.filter(title__iexact=title_key)
        context = {
            'inquiry_info': inquiry_info
        }
        return render(request, 'Kanrisya_Function/inquiry_master.html', context)
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/inquiry_master.html')


def inquiry_add(request):
    return render(request, 'Kanrisya_Function/inquiry_add.html')


def inquiry_add_confirm(request):
    if request.method == 'POST':
        inquiry_info = InquiryAddForm(request.POST)
        if inquiry_info.is_valid():
            context = {
                'inquiry_info': inquiry_info
            }
            return render(request, 'Kanrisya_Function/inquiry_add_confirm.html', context)
        else:
            return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/inquiry_add_confirm.html')


def inquiry_add_comp(request):
    if request.method == 'POST':
        inquiry_info = InquiryAddForm(request.POST)
        if inquiry_info.is_valid():
            inquiry_info.save()
            return render(request, 'Kanrisya_Function/inquiry_add_comp.html')
        else:
            return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/inquiry_add_comp.html')


def inquiry_del_confirm(request):
    if request.method == 'POST':
        inquiry_no = request.POST.get('inquiry_no')
        inquiry_info = Inquiry.objects.get(inquiry_no=inquiry_no)
        context = {
            'inquiry_info': inquiry_info
        }
        return render(request, 'Kanrisya_Function/inquiry_del_confirm.html', context)
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/inquiry_del_confirm.html')


def inquiry_del_comp(request):
    if request.method == 'POST':
        inquiry_no = request.POST.get('inquiry_no')
        inquiry_record = Inquiry.objects.get(inquiry_no=inquiry_no)
        inquiry_record.delete()
        return render(request, 'Kanrisya_Function/inquiry_del_comp.html')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/inquiry_del_comp.html')


def inquiry_edit(request):
    if request.method == 'POST':
        inquiry_no = request.POST.get('inquiry_no')
        inquiry_info = Inquiry.objects.get(inquiry_no=inquiry_no)
        context = {
            # 'inquiry_no': inquiry_no,
            'inquiry_info': inquiry_info
        }
        request.session['inquiry_no'] = inquiry_info.inquiry_no
        return render(request, 'Kanrisya_Function/inquiry_edit.html', context)
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/inquiry_edit.html')


def inquiry_edit_confirm(request):
    if request.method == 'POST':
        inquiry_info = InquiryAddForm(request.POST)
        if inquiry_info.is_valid():
            context = {
                'inquiry_info': inquiry_info,
            }
            return render(request, 'Kanrisya_Function/inquiry_edit_confirm.html', context)
        else:
            return HttpResponse('フォームの入力に誤りがあります')
    else:
        return HttpResponse('フォームの送信に使用しているメソッドが違います')
    # return render(request, 'Kanrisya_Function/inquiry_edit_confirm.html')


def inquiry_edit_comp(request):
    if request.method == 'POST':
        inquiry_no = request.session.get('inquiry_no')
        inquiry_info = Inquiry.objects.get(inquiry_no=inquiry_no)
        # DBにあるinquiry_infoをrequest.POSTの内容に変更
        inquiry_form = InquiryAddForm(request.POST, instance=inquiry_info)
        if inquiry_form.is_valid():
            inquiry_form.save()
            # 変更の為に使用したsessionを削除
            del request.session['inquiry_no']
            return render(request, 'Kanrisya_Function/inquiry_edit_comp.html')
    else:
        return HttpResponse('フォームの入力に誤りがあります')
    return render(request, 'Kanrisya_Function/inquiry_edit_comp.html')


# エラー
def login_notexit_error(request):
    # 処理なし
    return render(request, 'error/login_notexit_error.html')


def login_wrong_error(request):
    # 処理なし
    return render(request, 'error/login_wrong_error.html')


def map_error(request):
    # 処理なし
    return render(request, 'error/map_error.html')


def register_error(request):
    # 処理なし
    return render(request, 'error/register_error.html')

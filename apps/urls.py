from django.urls import path
from . import views
urlpatterns = [
    # テストJSON表示用パス
    path('route/', views.route, name='route'),
    path('map/', views.map, name='map'),
    path('position/', views.position, name='position'),

    path('', views.index, name='index'),

    # 新規
    path('sign_up/add/', views.shinki_add, name='shinki_add'),
    path('sign_up/add_confirm/', views.shinki_add_confirm, name='shinki_add_confirm'),
    path('sign_up/add_comp/', views.shinki_add_comp, name='shinki_add_comp'),

    # ログイン
    path('login/', views.login, name='login'),
    path('member/member_login/', views.member_login, name='member_login'),
    path('menber/menber_logout/', views.member_logout, name='member_logout'),
    # path('member/doorway_choice/', views.doorway_choice, name='doorway_choice'),
    # path('member/route_info/', views.route_info, name='route_info'),
    path('member/route_search/', views.route_search, name='route_search'),
    path('member/tanbo_master/', views.tanbo_master, name='tanbo_master'),
    path('member/tanbo_info/', views.tanbo_info, name='tanbo_info'),
    path('member/tanbo_add/', views.tanbo_add, name='tanbo_add'),
    path('member/tanbo_add_confirm/', views.tanbo_add_confirm, name='tanbo_add_confirm'),
    path('member/tanbo_add_comp/', views.tanbo_add_comp, name='tanbo_add_comp'),
    path('member/tanbo_del_confirm/', views.tanbo_del_confirm, name='tanbo_del_confirm'),
    path('member/tanbo_del_comp/', views.tanbo_del_comp, name='tanbo_del_comp'),
    path('member/tanbo_edit/', views.tanbo_edit, name='tanbo_edit'),
    path('member/tanbo_edit_confirm/', views.tanbo_edit_confirm, name='tanbo_edit_confirm'),
    path('member/tanbo_edit_comp/', views.tanbo_edit_comp, name='tanbo_edit_comp'),
    path('member/kikai_master/', views.kikai_master, name='kikai_master'),
    path('member/kikai_info/', views.kikai_info, name='kikai_info'),
    path('member/kikai_add/', views.kikai_add, name='kikai_add'),
    path('member/kikai_add_confirm/', views.kikai_add_confirm, name='kikai_add_confirm'),
    path('member/kikai_add_comp/', views.kikai_add_comp, name='kikai_add_comp'),
    path('member/kikai_del_confirm/', views.kikai_del_confirm, name='kikai_del_confirm'),
    path('member/kikai_del_comp/', views.kikai_del_comp, name='kikai_del_comp'),
    path('member/kikai_edit/', views.kikai_edit, name='kikai_edit'),
    path('member/kikai_edit_confirm/', views.kikai_edit_confirm, name='kikai_edit_confirm'),
    path('member/kikai_edit_comp/', views.kikai_edit_comp, name='kikai_edit_comp'),

    # ゲスト
    path('gest/route_search/', views.guest_route_search, name='Guest_route_search'),
    path('gest/tanbo_info/', views.guest_tanbo_info, name='Guest_tanbo_info'),
    path('gest/kikai_info/', views.guest_kikai_info, name='Guest_kikai_info'),
    # path('gest/solicit_create_account', views.solicit_create_account, name='soliit_create_account'),
    path('gest/proposal', views.proposal, name='proposal'),

    # 管理者admin
    path('admin/admin_login/', views.admin_login, name='admin_login'),
    path('admin/admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin/admin_home/', views.admin_home, name='admin_home'),
    path('admin/admin_master/', views.admin_master, name='admin_master'),
    path('admin/admin_search/', views.admin_search, name='admin_search'),
    path('admin/admin_add/', views.admin_add, name='admin_add'),
    path('admin/admin_add_confirm/', views.admin_add_confirm, name='admin_add_confirm'),
    path('admin/admin_add_comp/', views.admin_add_comp, name='admin_add_comp'),
    path('admin/admin_del_confirm/', views.admin_del_confirm, name='admin_del_confirm'),
    path('admin/admin_del_comp/', views.admin_del_comp, name='admin_del_comp'),
    path('admin/admin_edit/', views.admin_edit, name='admin_edit'),
    path('admin/admin_edit_confirm/', views.admin_edit_confirm, name='admin_edit_confirm'),
    path('admin/admin_edit_comp/', views.admin_edit_comp, name='admin_edit_comp'),

    path('admin/users_master/', views.users_master, name='users_master'),
    path('admin/users_search/', views.users_search, name='users_search'),
    path('admin/users_add/', views.users_add, name='users_add'),
    path('admin/users_add_confirm/', views.users_add_confirm, name='users_add_confirm'),
    path('admin/users_add_comp/', views.users_add_comp, name='users_add_comp'),
    path('admin/users_del_confirm/', views.users_del_confirm, name='users_del_confirm'),
    path('admin/users_del_comp/', views.users_del_comp, name='users_del_comp'),
    path('admin/users_edit/', views.users_edit, name='users_edit'),
    path('admin/users_edit_confirm/', views.users_edit_confirm, name='users_edit_confirm'),
    path('admin/users_edit_comp/', views.users_edit_comp, name='users_edit_comp'),

    path('admin/inquiry_master/', views.inquiry_master, name='inquiry_master'),
    path('admin/inquiry_search/', views.inquiry_search, name='inquiry_search'),
    path('admin/inquiry_add/', views.inquiry_add, name='inquiry_add'),
    path('admin/inquiry_add_confirm/', views.inquiry_add_confirm, name='inquiry_add_confirm'),
    path('admin/inquiry_add_comp/', views.inquiry_add_comp, name='inquiry_add_comp'),
    path('admin/inquiry_del_confirm/', views.inquiry_del_confirm, name='inquiry_del_confirm'),
    path('admin/inquiry_del_comp/', views.inquiry_del_comp, name='inquiry_del_comp'),
    path('admin/inquiry_edit/', views.inquiry_edit, name='inquiry_edit'),
    path('admin/inquiry_edit_confirm/', views.inquiry_edit_confirm, name='inquiry_edit_confirm'),
    path('admin/inquiry_edit_comp/', views.inquiry_edit_comp, name='inquiry_edit_comp'),

    # エラー
    path('error/login_notexit_error/', views.login_notexit_error, name='login_notexit_error'),
    path('error/login_wrong_error/', views.login_wrong_error, name='login_wrong_error'),
    path('error/map_error/', views.map_error, name='map_error'),
    path('error/register_error/', views.register_error, name='register_error'),
]

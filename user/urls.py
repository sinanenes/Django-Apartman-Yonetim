from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),
    path('addcontent/', views.addcontent, name='addcontent'),
    path('contents/', views.contents, name='contents'),
    path('contentedit/<int:id>', views.contentedit, name='contentedit'),
    path('contentdelete/<int:id>', views.contentdelete, name='contentdelete'),
    path('contentaddimage/<int:id>', views.contentaddimage, name='contentaddimage'),
    path('demands/', views.demands, name='demands'),
    path('adddemand/', views.adddemand, name='adddemand'),
    path('demandedit/<int:id>', views.demandedit, name='demandedit'),
    path('demanddelete/<int:id>', views.demanddelete, name='demanddelete'),
    path('payments/', views.payments, name='payments'),
    path('addpayment/', views.addpayment, name='addpayment'),
    path('paymentedit/<int:id>', views.paymentedit, name='paymentedit'),
    path('paymentdelete/<int:id>', views.paymentdelete, name='paymentdelete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('expenses/',views.Expense_List, name='Expense-List' ),
]
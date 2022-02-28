from django.urls import path
from .views import home, final, createform, Questions, index, after, q


urlpatterns = [
    # path('/home/togo', togo, name='togo'),
    # path('', home, name='home1'),
    path('/<po>', final, name="final"),
    path('', createform, name="index"),
    path('Question/<prod_id>', Questions, name="Question"),
    path('submit/afterward/', after, name='After'),
    path('submit/<myid>', index, name='Home'),
    path('create_form/', q.as_view(template_name='Creators/Creator_form.html'), name='list')
]

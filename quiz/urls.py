from django.urls import path
from .views import Quiz, RandomQuestionTopic, StartQuiz

app_name='quiz'

urlpatterns = [
     path('', Quiz.as_view(), name='quiz'),
    #path('q/', Question.as_view(), name='question'),
    #path('a/', Answer.as_view(), name='answer'),
    path('r/<str:topic>/', RandomQuestionTopic.as_view(), name='RandomQuestionTopic'),
    path('single/<str:title>/', StartQuiz.as_view(), name='quiz'),
]
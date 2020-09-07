from django.shortcuts import render
from django.views.generic import View
from utils.word_counter import *


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'writing_assistant.html', context={})

    def post(self, request, *args, **kwargs):
        essay = request.POST.get('essay')

        formatted_essay = str_formatter(essay)
        formatted_essay = empty_remover(formatted_essay)
        splited_list = ten_column_spliter(formatted_essay)

        words_count = len(formatted_essay)
        word_list = splited_list
        print(word_list)
        return render(request,
                      'writing_assistant.html',
                      context={'words_count': words_count, 'word_list': word_list})

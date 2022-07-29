from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from time import gmtime

# Create your views here.

''' 
    Return and render all polls list. 
                                        '''


@login_required(login_url='login_page')
def polls_list(request):
    context = {}
    user = request.user
    polls = Poll.objects.all().exclude(author=user).filter(is_active=True)
    context['polls'] = polls
    return render(request, 'polls/polls_list.html', context)


''' 
    Return and render poll details. 
                                        '''


@login_required(login_url='login_page')
def poll_details(request, pk):
    context = {}
    requested_poll = get_object_or_404(Poll, pk=pk)
    poll_options = PollOption.objects.all().filter(poll=requested_poll)
    context['is_active'] = requested_poll.is_active
    user = request.user
    if requested_poll.author == user:
        context['role'] = 'author'
    else:
        context['role'] = 'guest'

    context['is_voted'] = 'false'
    for option in poll_options:
        if Vote.objects.all().filter(user=user, poll_option=option):
            context['is_voted'] = True

    context['requested_poll'] = requested_poll
    context['poll_options'] = poll_options

    if request.method == 'POST' and context['role'] == 'guest':
        poll_option_id = request.POST['option']
        vote(request, poll_option_id)
        return render(request, 'polls/vote_success.html', context)
    elif request.method == 'POST' and context['role'] == 'author':
        action_text = request.POST['is_active']
        if action_text == 'Close Poll':
            requested_poll.is_active = False
            requested_poll.save()
            context['is_active'] = False
        else:
            requested_poll.is_active = True
            requested_poll.save()
            context['is_active'] = True

    return render(request, 'polls/poll_details.html', context)


@login_required(login_url='login_page')
def poll_create(request):
    context = {}
    if request.method == 'POST':
        author = request.user
        title = request.POST['title']
        is_active = True
        # date_start = request.POST['date_start']
        # date_end = request.POST['date_end']
        # poll = Poll(author=author, title=title, date_start=date_start, date_end=date_end)
        poll = Poll(author=author, title=title, is_active=True)
        poll.save()

        index = 1
        while request.POST.get(f'option_{index}', False):
            option = request.POST[f'option_{index}']
            option_obj = PollOption(poll=poll, option=option)
            option_obj.save()
            index += 1
        return redirect('polls_list')

    return render(request, 'polls/poll_edit.html', context)


@login_required(login_url='login_page')
def poll_delete(request, pk):
    # poll_to_delete = get_object_or_404(Poll, pk=pk)
    Poll.objects.get(pk).delete()
    return redirect('polls_list')


@login_required(login_url='login_page')
def polls_user(request):
    context = {}
    polls = Poll.objects.all().filter(author=request.user)
    context['polls'] = polls
    return render(request, 'polls/polls_list.html', context)


def vote(request, poll_option_id):
    context = {}
    voter = request.user
    voted_poll_option = get_object_or_404(PollOption, pk=poll_option_id)
    vote_obj = Vote(user=voter, poll_option=voted_poll_option)
    vote_obj.save()
    # if vote_obj is not None:
    #     return render


@login_required(login_url='login_page')
def results(request):
    context = {}
    closed_polls = Poll.objects.all().filter(is_active=False)
    context['results'] = True
    context['polls'] = closed_polls
    return render(request, 'polls/polls_list.html', context)


@login_required(login_url='login_page')
def result_details(request, pk):
    context = {}
    option_votes_dict = {}
    poll = get_object_or_404(Poll, pk=pk)
    poll_options = PollOption.objects.all().filter(poll=poll)
    for option in poll_options:
        option_votes_dict[option.option] = Vote.objects.all().filter(poll_option=option).count()
        # print(option_votes_dict)
        # for key, value in option_votes_dict:
        #     print(f'{key} -> {value}')

    context['option_votes_dict'] = sorted(option_votes_dict.items())
    context['poll_title'] = poll.title
    return render(request, 'polls/result_details.html', context)


'''     ToDo 
-Tests
-if voted Check (Done +-)
-success page after vote (Done +-)
-styles
-blockchain
-poll_editing?
-poll closing opening (Done +-)
-open polls (Done)
-closed polls (Done)

-unability to vote on closed polls (Done)
-poll_list only active polls (Done)
-results of closed polls in poll details (Done)
'''

''' 

created by

'''

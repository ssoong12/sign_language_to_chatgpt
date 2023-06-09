from django.shortcuts import render
from .models import TeamMember

# Create your views here.


def team_intro(request):
    team_members = [
        {'photo_filename': '1', 'name': '손경현', 'email': '30team01@aivle.com'},
        {'photo_filename': '2', 'name': '강준형', 'email': '30team02@aivle.com'},
        {'photo_filename': '3', 'name': '김주영', 'email': '30team03@aivle.com'},
        {'photo_filename': '4', 'name': '김효진', 'email': '30team04@aivle.com'},
        {'photo_filename': '5', 'name': '이승현', 'email': '30team05@aivle.com'},
        {'photo_filename': '6', 'name': '박서진', 'email': '30team06@aivle.com'},
        {'photo_filename': '7', 'name': '박예온', 'email': '30team07@aivle.com'},
        
    ]
    return render(request, 'team/result.html', {'team_members': team_members})

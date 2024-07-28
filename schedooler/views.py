from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from schedooler.models import Schedool, Routine


# Create your views here.
@api_view(['POST'])
def registry_schedool(request):
    # 일정 등록
    try:
        schedool = Schedool.objects.create(datetime=request.data['datetime'], title=request.data['title'],
                                         content=request.data['content'])
        # routine rule 이 있을 경우 Routine 등록
        if 'routine_rule' in request.data:
            print(request.data)
            Routine.objects.create(schedool=schedool, routine_rule=request.data['routine_rule'],
                                   start_time=request.data['start_time'], end_time=request.data['end_time'])
    except ValidationError:
        return Response({'message': '등록에 실패했습니다.'}, status=400)

    return Response({'message': '등록에 성공했습니다.'})

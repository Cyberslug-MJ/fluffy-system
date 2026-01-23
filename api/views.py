from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import SermonListSerializer,SermonDetailSerializer, VisitUsInfoSerializer,ReachUsSerializer,PreacherSerializer
from . models import Sermon, Staff, Preacher
from .pagination import paginate_my_way
from .filters import SermonFilter
from django.shortcuts import get_object_or_404



@api_view(['GET'])
def home(request):
    recent = Sermon.objects.all().order_by('-id')[:5]
    # get the last 5 sermons.

    if request.method == 'GET':
        serializer = SermonListSerializer(recent,many=True)
        return Response({'sermons':serializer.data},status=status.HTTP_200_OK)
    

@api_view(['GET'])  # List all sermons - POST via adminPanel only.
def sermon_list(request):
    if request.method == 'GET':
        filterset = SermonFilter(request.GET,queryset=Sermon.objects.all())
        if not filterset.is_valid():
            return Response({'error':'filter parameters invalid'},status=status.HTTP_400_BAD_REQUEST)
        
        sermons = filterset.qs
        return paginate_my_way(sermons,request,SermonListSerializer)
    

@api_view(['GET'])
def sermon_detail(request,pk):
    sermon = get_object_or_404(Sermon,pk=pk)
    if request.method == 'GET':
        serializer = SermonDetailSerializer(sermon)
        return Response({'sermon':serializer.data},status=status.HTTP_200_OK)
    

@api_view(['POST'])
def visit_us(request):
    if request.method == 'POST':
        serializer = VisitUsInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Submitted!'},status=status.HTTP_201_CREATED)
        
        else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET'])
def reach_us(request):
    instances = Staff.objects.all()
    serializer = ReachUsSerializer(instances,many=True)
    return Response({'data':serializer.data},status=status.HTTP_200_OK)


@api_view(['GET'])
def preacher_bio(request,pk):
    preacher = get_object_or_404(Preacher,pk=pk)

    if request.method == 'GET':
        serializer = PreacherSerializer(preacher)
        return Response({'preacher':serializer.data},status=status.HTTP_200_OK)
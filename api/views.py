# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AudioBlock
from .serializers import *
from datetime import timedelta
from django.utils import timezone

class AudioBlockListAPIView(APIView):
    def get(self, request, format=None):
        try:
            audio_blocks = AudioBlock.objects.all()
            serializer = AudioBlockSerializer(audio_blocks, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AudioBlockCreateAPIView(APIView):
    def post(self, request, format=None):
        try:
            serializer = AudioBlockSerializer(data=request.data)
            if serializer.is_valid():
                audio_block = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AudioBlockRetrieveAPIView(APIView):
    def get(self, request, pk, format=None):
        try:
            audio_block = AudioBlock.objects.get(pk=pk)
            serializer = AudioBlockSerializer(audio_block)
            return Response(serializer.data)
        except AudioBlock.DoesNotExist:
            return Response({'error': 'AudioBlock not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AudioBlockUpdateAPIView(APIView):
    def put(self, request, pk, format=None):
        try:
            audio_block = AudioBlock.objects.get(pk=pk)
            serializer = AudioBlockSerializer(audio_block, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AudioBlock.DoesNotExist:
            return Response({'error': 'AudioBlock not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AudioBlockDeleteAPIView(APIView):
    def delete(self, request, pk, format=None):
        try:
            audio_block = AudioBlock.objects.get(pk=pk)
            audio_block.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AudioBlock.DoesNotExist:
            return Response({'error': 'AudioBlock not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AudioFragmentAPIView(APIView):
    def get(self, request):
        start_time = request.GET.get('start_time')
        end_time = request.GET.get('end_time')

        # Convert start_time and end_time to timedelta objects
        start_time = timedelta(seconds=int(start_time))
        end_time = timedelta(seconds=int(end_time))

        audio_fragments = AudioBlock.objects.filter(
            duration_start_time__isnull=False,
            duration_end_time__isnull=False,
            duration_start_time__lte=start_time,
            duration_end_time__gte=end_time
        )
        serializer = AudioFragmentSerializer(audio_fragments, many=True)
        return Response(serializer.data)



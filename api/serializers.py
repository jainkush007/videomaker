from rest_framework import serializers
from .models import AudioBlock


class AudioBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBlock
        fields = '__all__'


class AudioFragmentSerializer(serializers.ModelSerializer):
    volume = serializers.SerializerMethodField()

    class Meta:
        model = AudioBlock
        fields = '__all__'

    def get_volume(self, obj):
        if obj.type == 'video_music':
            return obj.high_volume
        else:
            return obj.low_volume
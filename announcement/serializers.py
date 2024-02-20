from announcement.models import Announcement
from rest_framework import serializers

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
        depth = 1
        

class CreateAnnouncementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        fields = '__all__'


    def save(self):
        data = self._validated_data
        # add Announcement
        announcement = self.Meta.model(**data)
        announcement.save()

        return AnnouncementSerializer(announcement).data


class UpdateAnnouncementSerializer(serializers.ModelSerializer):
    header = serializers.CharField(required=False)
    announced_datetime = serializers.DateTimeField(required=False)
    description = serializers.CharField(required=False)
    
    class Meta:
        model = Announcement
        fields = '__all__'


class DeleteAnnouncementSerializer(serializers.ModelSerializer):
    pks = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(
            queryset=Announcement.objects.all()
        ), required=True
    )

    class Meta:
        model = Announcement
        fields = ['pks']

    def save(self):
        for model in self._validated_data['pks']:
            model.delete()
        return True
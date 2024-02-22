from notification.models import Notification
from authentication.models import User
from rest_framework import serializers


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        depth = 1
        

class CreateNotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = '__all__'


    def save(self):
        data = self._validated_data
        # add Notification
        notification = self.Meta.model(**data)
        notification.save()

        return NotificationSerializer(notification).data


class UpdateNotificationSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False)
    receiver = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False)
    message = serializers.CharField(required=False)
    create_date = serializers.DateTimeField(required=False)
    is_read = serializers.BooleanField(required=False)

    class Meta:
        model = Notification
        fields = '__all__'


class DeleteNotificationSerializer(serializers.ModelSerializer):
    pks = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(
            queryset=Notification.objects.all()
        ), required=True
    )

    class Meta:
        model = Notification
        fields = ['pks']

    def save(self):
        for model in self._validated_data['pks']:
            model.delete()
        return True
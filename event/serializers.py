from event.models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        depth = 1
        

class CreateEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


    def save(self):
        data = self._validated_data
        # add Event
        event = self.Meta.model(**data)
        event.save()

        return EventSerializer(event).data


class UpdateEventSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    location_name = serializers.CharField(required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
    start_time = serializers.TimeField(required=False)
    end_time = serializers.TimeField(required=False)
    description = serializers.CharField(required=False)
    
    class Meta:
        model = Event
        fields = '__all__'


class DeleteEventSerializer(serializers.ModelSerializer):
    pks = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(
            queryset=Event.objects.all()
        ), required=True
    )

    class Meta:
        model = Event
        fields = ['pks']

    def save(self):
        for model in self._validated_data['pks']:
            model.delete()
        return True
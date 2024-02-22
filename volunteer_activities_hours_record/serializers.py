from volunteer_activities_hours_record.models import VolunteerActivitiesHoursRecord
from authentication.models import User
from rest_framework import serializers


class VolunteerActivitiesHoursRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerActivitiesHoursRecord
        fields = '__all__'
        depth = 1
        

class CreateVolunteerActivitiesHoursRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = VolunteerActivitiesHoursRecord
        fields = '__all__'


    def save(self):
        data = self._validated_data
        # add VolunteerActivitiesHoursRecord
        vah_record = self.Meta.model(**data)
        vah_record.save()

        return VolunteerActivitiesHoursRecordSerializer(vah_record).data


class UpdateVolunteerActivitiesHoursRecordSerializer(serializers.ModelSerializer):
    borrower = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False)
    name = serializers.CharField(required=False)
    category = serializers.CharField(required=False)
    hours = serializers.IntegerField(required=False)
    location_name = serializers.CharField(required=False)
    academic_year = serializers.CharField(required=False)
    create_date = serializers.DateTimeField(required=False)
    verification = serializers.FileField(required=False)
    status = serializers.CharField(required=False)

    class Meta:
        model = VolunteerActivitiesHoursRecord
        fields = '__all__'


class DeleteVolunteerActivitiesHoursRecordSerializer(serializers.ModelSerializer):
    pks = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(
            queryset=VolunteerActivitiesHoursRecord.objects.all()
        ), required=True
    )

    class Meta:
        model = VolunteerActivitiesHoursRecord
        fields = ['pks']

    def save(self):
        for model in self._validated_data['pks']:
            model.delete()
        return True
from authentication.models import User, Education
from django.db.models import Q
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 3
    

class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def save(self):
        data = self._validated_data
        # add User
        user = self.Meta.model(**data)
        user.set_password(user.password)
        user.save()

        return UserSerializer(user).data

  
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
        depth = 2
        

class CreateEducationSerializer(serializers.ModelSerializer):
    default_error_messages = {
        'student_id_number_already_exists': (
            'This Student ID Number already exists.'
        )
    }

    class Meta:
        model = Education
        fields = '__all__'

    def validate(self, attrs):
        if Education.objects.filter(
                student_id_number=attrs.get('student_id_number')).exists():
            raise serializers.ValidationError({
                'student_id_number': self.error_messages['student_id_number_already_exists'],
            })

        return attrs

    def save(self):
        data = self._validated_data
        # add Education
        education = self.Meta.model(**data)
        education.save()

        return EducationSerializer(education).data


class UpdateEducationSerializer(serializers.ModelSerializer):
    student_id_number = serializers.CharField(required=False)
    faculty = serializers.CharField(required=False)
    department = serializers.CharField(required=False)
    education_level = serializers.CharField(required=False)
    status = serializers.CharField(required=False)
    
    default_error_messages = {
        'student_id_number_already_exists': (
            'This Student ID Number already exists.'
        )
    }

    class Meta:
        model = Education
        fields = '__all__'

    def validate(self, attrs):
        if Education.objects.filter(
                ~Q(id=self.instance.id), student_id_number=attrs.get('student_id_number')).exists():
            raise serializers.ValidationError({
                'student_id_number': self.error_messages['student_id_number_already_exists'],
            })

        return attrs


class DeleteEducationSerializer(serializers.ModelSerializer):
    pks = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(
            queryset=Education.objects.all()
        ), required=True
    )

    class Meta:
        model = Education
        fields = ['pks']

    def save(self):
        for model in self._validated_data['pks']:
            model.delete()
        return True
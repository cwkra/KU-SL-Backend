from student_loan_request_record.models import StudentLoanRequestRecord
from authentication.serializers import (
    UserSerializer, 
    EducationSerializer,
)
from authentication.models import User
from rest_framework import serializers


class StudentLoanRequestRecordSerializer(serializers.ModelSerializer):
    borrower = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all())
    borrower_name = serializers.CharField(required=False)
    class Meta:
        model = StudentLoanRequestRecord
        fields = '__all__'
        depth = 3
        

class CreateStudentLoanRequestRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLoanRequestRecord
        fields = '__all__'


    def save(self):
        data = self._validated_data
        # add StudentLoanRequestRecord
        request_record = self.Meta.model(**data)
        request_record.save()

        return StudentLoanRequestRecordSerializer(request_record).data


class UpdateStudentLoanRequestRecordSerializer(serializers.ModelSerializer):
    borrower = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False)
    borrower_name = serializers.CharField(required=False)
    academic_year = serializers.CharField(required=False)
    semester = serializers.CharField(required=False)
    tuition_fees = serializers.DecimalField(max_digits=8, decimal_places=2, required=False, default=0)
    create_date = serializers.DateTimeField(required=False)
    status = serializers.CharField(required=False)

    class Meta:
        model = StudentLoanRequestRecord
        fields = '__all__'


class DeleteStudentLoanRequestRecordSerializer(serializers.ModelSerializer):
    pks = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(
            queryset=StudentLoanRequestRecord.objects.all()
        ), required=True
    )

    class Meta:
        model = StudentLoanRequestRecord
        fields = ['pks']

    def save(self):
        for model in self._validated_data['pks']:
            model.delete()
        return True
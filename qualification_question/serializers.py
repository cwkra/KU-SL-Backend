from qualification_question.models import QualificationQuestion
from rest_framework import serializers


class QualificationQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationQuestion
        fields = '__all__'
        depth = 1
        

class CreateQualificationQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = QualificationQuestion
        fields = '__all__'


    def save(self):
        data = self._validated_data
        # add QualificationQuestion
        qualification_question = self.Meta.model(**data)
        qualification_question.save()

        return QualificationQuestionSerializer(qualification_question).data


class UpdateQualificationQuestionSerializer(serializers.ModelSerializer):
    question = serializers.CharField(required=False)
    choice = serializers.JSONField(required=False)
    question_type = serializers.CharField(required=False)
    
    class Meta:
        model = QualificationQuestion
        fields = '__all__'


class DeleteQualificationQuestionSerializer(serializers.ModelSerializer):
    pks = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(
            queryset=QualificationQuestion.objects.all()
        ), required=True
    )

    class Meta:
        model = QualificationQuestion
        fields = ['pks']

    def save(self):
        for model in self._validated_data['pks']:
            model.delete()
        return True
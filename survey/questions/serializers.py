from .models import Questions
from rest_framework import serializers

from answers.serializers import AnswersSerializer




class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'

class QuestionsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    answers =  AnswersSerializer(many=True)

    def validate(self, data):
        super().validate(data)
        # type = text
        # vì ở dưới code mình dùng answers liên tục nên get 1 lần rồi dùng chứ không gọi hàm get liên tục
        answers = data.get('answers')
        type_questions = data.get('type_questions')
        if type_questions == 'text':
            if len(answers) != 0:
                raise serializers.ValidationError({'answers': ["No answer in question that is text"]})
        else: # type != text
            # check len = 0, vì là câu hỏi lựa chọn thì chắc chắn phải có danh sách đáp án, không thể rỗng 
            # như câu hỏi dạng text
            if len(answers) == 0:
                raise serializers.ValidationError({'answers': ["Answers must not be null"]})
            # dưới đây là trường hợp có answer
            num_right_answers = sum(1 for answer in answers if answer.get('isRight') == True)
            if type_questions == 'yes/no':
                # nếu là câu hỏi lựa chọn 1 đáp án (đúng, sai) thì trong danh sách answer phải có 1 đáp án đúng
                if num_right_answers != 1:
                    raise sercializers.ValidationError({'answers': ["Need only one right answer."]})
            else: # trường hợp này type là section/multiselection, không có đáp án đúng
                if num_right_answers != 0:
                    raise serializers.ValidationError({'answers': ["No need any right answer."]})
        # validate xong, return data
        # các usecase validate:
        # - type là text => không có answer
        # - type không phải text => phải có ít nhất 1 answer
        #   + type là yes/no => có duy nhất 1 đáp án đúng
        #   + type là selection, multiselection => không có đáp án đúng
        return data

    class Meta:
        model = Questions
        fields = ['id','title', 'type_questions', 'isRequired', 'answers']

        

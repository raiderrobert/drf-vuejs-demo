from rest_framework.response import Response

from .models import Question, Choice
from rest_framework import viewsets, status
from .serializers import QuestionSerializer, ChoiceSerializer, ChoiceIDSerializer
from rest_framework.decorators import detail_route


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed, edited, or voted on.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @detail_route(methods=['post'], serializer_class=ChoiceIDSerializer)
    def vote(self, request, pk=None):
        """
        API endpoint to vote on an choice
        """

        serializer = ChoiceIDSerializer(data=request.data)
        if serializer.is_valid():
            choice = Choice.objects.select_related('question').get(id=serializer.initial_data['id'])
            if choice.question.pk == int(pk):
                choice.votes = choice.votes + 1
                choice.save()

            return Response({'id': choice.id, 'votes': choice.votes}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows choices to be viewed or edited.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

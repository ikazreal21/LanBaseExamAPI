from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import generics, parsers
import pandas as pd
from tablib import Dataset

from .serializers import *
from .models import *

class UploadViewSet(generics.GenericAPIView):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("Working")

    parser_classes = [parsers.MultiPartParser]
    
    def post(self, request, *args, **kwargs):
        file = request.FILES['file_uploaded']
        df = pd.read_excel(file)
        
        """Rename the headeers in the excel file
           to match Django models fields"""
        
        rename_columns = {
                        "Subject" : "subject", 
                        "Questions": "question", 
                        "A": "mc1",
                        "B": "mc2", 
                        "C": "mc3",
                        "D": "mc4", 
                        "E": "mc5",
                        "Correct": "correct"
                        }
        
        df.rename(columns = rename_columns, inplace=True)
        
        #Call the Student Resource Model and make its instance
        questions_resource = QuestionsResources()
        
        # Load the pandas dataframe into a tablib dataset
        dataset = Dataset().load(df)
        
        # Call the import_data hook and pass the tablib dataset
        result = questions_resource.import_data(dataset,\
             dry_run=True, raise_errors = True)

        if not result.has_errors():
            result = questions_resource.import_data(dataset, dry_run=False)
            return Response({"status": "Questions Data Imported Successfully"})

        return Response({"status": "Not Imported Question Data"})
    
class QuestionList(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = ExamQuestionSerializer

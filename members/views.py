

# Create your views here.
from .serializer import Jay
import pandas as pd
import pickle
from transformers import pipeline
from rest_framework import status
from .models import Nari
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView
from .models import Nari
from .serializer import Jay
from rest_framework.request import Request
from .models import Banner
from .serializer import Ba
from .serializer import *
from rest_framework.generics import RetrieveAPIView
from .models import Create
from rest_framework.response import Response
import requests
from googletrans import Translator
from gtts import gTTS
from django.http import FileResponse
from rest_framework.views import APIView
from io import BytesIO
class Li(ListAPIView):
    queryset = Nari.objects.all() 
    serializer_class = Jay 
class Va(CreateAPIView):
    queryset=Nari.objects.all()
    serializer_class=Jay
class Ma(RetrieveAPIView):
        queryset=Nari.objects.all()
        serializer_class=Jay
class De(DestroyAPIView):
    queryset=Nari.objects.all()
    serializer_class=Jay
class Ban(ListAPIView):
     queryset=Banner.objects.all()
     serializer_class=Ba
class Cr(ListAPIView):
     queryset=Create.objects.all()
     serializer_class=Cre
class Ct(ListAPIView):
     queryset=Circle.objects.all()
     serializer_class=Cir
class P111(ListAPIView):
     queryset=P1.objects.all()
     serializer_class=P11
class P222(ListAPIView):
     queryset=P2.objects.all()
     serializer_class=P22
class Addd(ListAPIView):
     queryset=Add.objects.all()
     serializer_class=add1
class Discount12(ListAPIView):
     queryset=Discount.objects.all()
     serializer_class=Discount1
class Mobile12(ListAPIView):
     queryset=Mobile.objects.all()
     serializer_class=Mobile1

class Mobile13(RetrieveAPIView):
     queryset=Mobile.objects.all()
     serializer_class=Mobile1
class Cart1(CreateAPIView):
     queryset=Cart
     serializer_class=Cart12
class product123(ListAPIView):
     queryset=product3.objects.all()
     serializer_class=product31
class P451(CreateAPIView):
     queryset=P1.objects.all()
     serializer_class=P11
class Mobile135(CreateAPIView):
     queryset=Mobile.objects.all()
     serializer_class=Mobile1


generator = pipeline("text-generation", model="gpt2-medium")
def generate_text(prompt):
    # Generate text with tighter controls
    generated_text = generator(prompt, 
                               max_length=50,  # Limit the length to 50 tokens
                               num_return_sequences=1, 
                               temperature=0.7,  # Balance randomness vs. coherence
                               no_repeat_ngram_size=2)  # Prevent repeated n-grams
    return generated_text[0]['generated_text']



# Serializer for the input prompt
class PromptSerializer(serializers.Serializer):
    prompt = serializers.CharField()

# CreateAPIView to handle POST requests and generate text
class HuggingFaceListView(CreateAPIView):
    serializer_class = PromptSerializer

    def create(self, request, *args, **kwargs):
        # Validate incoming data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract prompt from validated data
        prompt = serializer.validated_data['prompt']

        # Generate text using the pipeline
        generated_text = generate_text(prompt)

        
        return Response({"generated_text": generated_text}, status=status.HTTP_201_CREATED)
class Pp(APIView):
     
     def post(self,request):
          name=request.data.get('name')
          l1=request.data.get('l1')
          l2=request.data.get('l2')
          t=Translator()
          ll=t.translate(name,src=l1,dest=l2)
          cc=ll.text
          print(cc)
          lba=gTTS(cc)
          
          
          mp3_fp = BytesIO()
          lba.write_to_fp(mp3_fp)
          mp3_fp.seek(0)
          


          return FileResponse(mp3_fp, as_attachment=True, filename="translation.mp3", content_type='audio/mpeg')
class Ha(APIView):
     def post(self,request):
          name=request.data.get("name")
          l1=request.data.get("l1")
          l2=request.data.get("l2")
          t=Translator()
          s1=t.translate(name,src=l1,dest=l2)
          cc=s1.text
          print(cc)
          return Response({"generated":cc})
class Sk(APIView):
     #"Age","Gender","Academic_Level","Avg_Daily_Usage_Hours","Most_Used_Platform","Sleep_Hours_Per_Night","Conflicts_Over_Social_Media"
     def post(self,request):
          l1=request.data.get('l1')#age
          l2=request.data.get('l2')#"Academic_Level"
          l3=request.data.get('l3')#"Avg_Daily_Usage_Hours"
          l4=request.data.get('l4')
          l5=request.data.get('l5')
          l6=request.data.get('l6')
          l7=request.data.get('l7')
          
          file_path = r'C:\Users\ADMIN\Desktop\backend\app\media\files\addiction.pkl'
          agb=pickle.load(open(file_path,"rb"))
          bb=agb.predict([[l1,l2,l3,l4,l5,l6,l7]])
          if bb==0:
             c="not-addicted"
          elif bb==1:
              c="addicted"
          return Response({"response":c})
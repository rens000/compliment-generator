from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import google.generativeai as genai

GENAI_API_KEY = settings.GEMINI_API_KEY

genai.configure(api_key=GENAI_API_KEY)

class ComplimentView(APIView):
    def get(self, request):
        person = request.GET.get('person')
        
        extra_info = self.get_extra_info(person)
        
        prompt = f"Generate a short, 1 sentence compliment for {person}. Here are some details about them: {extra_info}. Take just one of the points at random and say something kind (and perhaps a bit funny)."

        try:
            model = genai.GenerativeModel("gemini-1.5-pro-latest")
            response = model.generate_content(prompt)
            
            compliment = response.text.strip()
            
            data = {"compliment": compliment}
            return Response(data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def get_extra_info(self, person):
        if person == "mom":
            return "community organizer, founded local pflag chapter, brightens up any room, somehow always happy, goes out of her way to spend time with family driving hours, offers consistent support and will always listen on the phone, always growing as a human - went to family therapy, lover of nature (hiking, backpacking, canoing), at peace with the world, amazing gift giver, always down for an adventure, incredible patience and understanding (teaches me how to be more understanding of others), deep empathy"
        if person == "dad":
            return "a good listener, calm and collected, true to himself, consistent, kind, gentle, and loyal, good at golf and raquetball, always came to all my soccer games in high school, sort of okay at worldle, makes sort of funny dad jokes, lover of whoppers"
        if person == "davis":
            return "my younger sibling, inquisitive, painfully smart, autistic, queer just like me! (maybe even more), has amazing style, gave me a bunch of their old clothes for xmas in a trash bag, traveled accross vietnam together, steady and loving to their partner kae, cares about what counts, sent me poutine once, one of my closest friends, always willing to give advice, patient with my endless yapping and rants"
        if person == "kai":
            return "my younger brother, funny, wise beyond his years, straight yet somehow still one of my best friends, amazing tennis player top in school, joined swim for the first time his senior year, the beautiful one according to mimi, puts time into his family despite being the youngest, unnecessarily modest"



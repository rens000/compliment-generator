from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import google.generativeai as genai
import random

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
        details = {
            "mom": [
                "community organizer, founded local pflag chapter (although she no longer is president), works on abortion access",
                "brightens up any room, somehow always happy",
                "amazing gift giver",
                "always down for an adventure, hiking, biking last summer, kayaking at the late, backpacking when i was young",
                "deep empathy, shows me how to empathize with others",
                "believes in my language (french and spanish) skills even when i do not",
                "very nice curly hair",
                "taught me to value beauty in people and the world"
            ],
            "dad": [
                "a good listener, calm and collected",
                "true to himself, consistent, kind, gentle, and loyal",
                "makes sort of funny dad jokes",
                "lover of whoppers",
                "occassionally alright at worldle",
                "always went to my soccer games in high school",
                "strong in fighting his RA",
                "always takes good care of the cats",
            ],
            "davis": [
                "my younger sibling, inquisitive, painfully smart",
                "gave me a bunch of their old clothes for xmas in a trash bag",
                "sent me poutine once",
                "one of my closest friends",
                "always willing to give advice and yap on the phone",
                "good consistent to their partner kae",
                "has a silly laugh",
                "took a train journey from chicago to san fran with me"
            ],
            "kai": [
                "funny, wise beyond his years",
                "amazing tennis player top in school",
                "puts time into his family despite being the youngest",
                "unnecessarily modest",
                "joined swim his last year in highschool",
                "will go on many future bike rides with me!",
                "swims laps at the pool with me sometimes",
                "politically informed, lover of hasanabi"
            ],
        }

        random_num = random.randint(0, 7)
        return details.get(person)[random_num]



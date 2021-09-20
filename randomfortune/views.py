from django.shortcuts import render
import random
# Create your views here.
def fortune(request):
  fortune=random.choice(fortuneList)
  context={'fortune':fortune}
  return render(request,"randomfortune/fortune.html", context)

fortuneList=[
  "You are the Best Data Sciencist",
  'Code More and More',
  "Analyse, Think and Act",
  'Never settle for Less',
  'Be your Best Version',
  'Code Everyday'
]
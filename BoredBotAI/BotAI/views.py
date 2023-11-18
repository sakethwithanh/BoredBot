from django.shortcuts import render
import requests

def bored_api(request):
    # Bored API endpoint
    api_url = "https://www.boredapi.com/api/activity"

    # Make a GET request to the Bored API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        activity_data = response.json()

        # Pass the activity data to the template
        return render(request, 'activity.html', {'activity': activity_data})
    else:
        # Handle errors, for example, show a default activity
        return render(request, 'activity.html', {'activity': {'activity': 'Default Activity'}})



# Create your views here.

def landPage(request):
    return  render(request, 'land.html')
def homePage(request):
    return render(request,'home.html')
 
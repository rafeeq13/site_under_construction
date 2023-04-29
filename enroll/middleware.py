from django.shortcuts import render
class MyMidddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=render(request,'enroll/site.html')
        return response
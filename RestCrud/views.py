from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from urllib import request


class StudentData(APIView):

    #Create
    def post(self,request):
        serializer = StudentDetails(data=request.data)


        if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)

        return Response(serializer.errors, status=400)

    #     new_data=Student(name=request.data["name"],
    #                      age=request.data["age"],
    #                      mark=request.data["mark"],
    #                      course=request.data["course"],
    #                      email=request.data["email"],
    #                      mobile=request.data["mobile"],
    #                      )
    #     new_data.save()

    #     return Response("Student Added Successfully")

    
    
    #Read
    def get(self,request):
        data=Student.objects.all()
        student_data=[]
        for i in data:
            student_data.append({
                "id":i.id,
                "name":i.name,
                "course":i.course,
                "age":i.age,
                "mark":i.mark,
                "email":i.email,
                "mobile":i.mobile,

            })
        return Response(student_data)
    
     #Readbyid

    def get(self,request,pro_id):
        data=Student.objects.get(id=pro_id)
        # student_data=[]
        # for i in data:
        student_data={

            "id":data.id,
            "name":data.name,
            "course":data.course,
            "age":data.age,
            "mark":data.mark,
            "email":data.email,
            "mobile":data.mobile,

            }
        return Response(student_data)
    
    # #update
    def put(self,request,pro_id):
        data=Student.objects.filter(id=pro_id)
        data.update(name=request.data["name"],
                    age=request.data["age"],
                    mark=request.data["mark"],
                    course=request.data["course"],
                    email=request.data["email"],
                    mobile=request.data["mobile"],)
        return Response("Updated put Successfully")
    
    
    def patch(self,request,pro_id):
        data=Student.objects.filter(id=pro_id)
        data.update(name=request.data["name"],
                    age=request.data["age"],
                    mark=request.data["mark"],
                    course=request.data["course"],
                    email=request.data["email"],
                    mobile=request.data["mobile"])
        return Response("Updated patch Successfully")



    #Delete
    def delete(self, request, pro_id):
        data = Student.objects.get(id=pro_id)
        data.delete()
        return Response("Deleted Successfully")


    


    




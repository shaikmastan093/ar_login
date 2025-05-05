from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import LoginData
from .serializers import LoginDataSerializer
from rest_framework import status

# CREATE NEW LOGIN ENTRY
@api_view(['POST'])
def login_create_view(request):
    if request.method == 'POST':
        mobile_number = request.data.get('mobile_number')

        existing_entry = LoginData.objects.filter(mobile_number=mobile_number).first()
        if existing_entry:
            return Response({"message": "Data already Exist"}, status=status.HTTP_201_CREATED)

       
        # if LoginData.objects.filter(mobile_number=mobile_number).exists():
        #     return Response(
        #         {"error": "Mobile number already exists. Please use a different number."},
        #         status=status.HTTP_400_BAD_REQUEST
        #     )

        serializer = LoginDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data Saved Successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# LIST ALL LOGIN ENTRYS
@api_view(['GET'])
def login_list_view(request):
    if request.method == 'GET':
        login_entries = LoginData.objects.all()
        serializer = LoginDataSerializer(login_entries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# GET SPECIFIC LOGIN ENTRY
@api_view(['GET'])
def login_detail_view(request, pk):
    try:
        login_entry = LoginData.objects.get(pk=pk)
    except LoginData.DoesNotExist:
        return Response({"error": "Entry not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoginDataSerializer(login_entry)
        return Response(serializer.data, status=status.HTTP_200_OK)

# UPDATE SPECIFIC LOGIN ENTRY
@api_view(['PUT'])
def login_update_view(request, pk):
    try:
        login_entry = LoginData.objects.get(pk=pk)
    except LoginData.DoesNotExist:
        return Response({"error": "Entry not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = LoginDataSerializer(login_entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data Updated Successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE LOGIN ENTRY
@api_view(['DELETE'])
def login_delete_view(request, pk):
    try:
        login_entry = LoginData.objects.get(pk=pk)
    except LoginData.DoesNotExist:
        return Response({"error": "Entry not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        login_entry.delete()
        return Response({"message": "Data Deleted Successfully!"}, status=status.HTTP_204_NO_CONTENT)

from gettext import install
from logging import raiseExceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import  Material
from .serializers import MaterialSerializer, MaterialSerializerRead
from rest_framework import serializers, status

@api_view(['GET', ])
def ApiOverview(request):
    api_urls = {
        'All Materials': '/materials',
        'Search by Material Type': '/materials?material_type=material_type',
        'Add': '/material/create',
        'Update': '/material/update/pk',
        'Delete': '/material/delete/pk'
    }
  
    return Response(api_urls)

@api_view(['POST', ])
def add_material(request):
    material = MaterialSerializer(data=request.data)

    if Material.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    
    material.is_valid(raise_exception=True)
    material.save()
    return Response(material.data)

@api_view(['GET', ])
def view_materials(request):

    if request.query_params:
        materials = Material.objects.filter(**request.query_params.dict())
    else:
        materials = Material.objects.all()

    if materials:
        materials_serialized = MaterialSerializerRead(materials, many=True)
        return Response(materials_serialized.data)
    else:
        return Response(data={})

@api_view(['PUT', 'POST'])
def update_material(request, pk):
    material = Material.objects.get(pk=pk)
    material_serialized = MaterialSerializer(instance=material, data=request.data)

    material_serialized.is_valid(raise_exception=True)
    material_serialized.save()
    return Response(material_serialized.data)


@api_view(['DELETE', ])
def delete_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    material.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
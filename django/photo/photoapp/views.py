from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Photo
from .forms import PhotoForm
# api
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import PhotoSerializer

# Create your views here.
def home(request):
    # HttpResponse("텍스트") : 텍스트 형태로 응답
    # HttpResponse(template.render()) : 데이터 + html 페이지 형태로 응답
    # => render() : 주 응답 방식
    # return HttpResponse("Hello Photo")

    # 테이블에 있는 내용 담아서 전송 => 조회한 결과를 photo_list.html 문서와 같이 보냄 
    # select * from photo == photos = Photo.objects.all()

    photos = Photo.objects.all()

    return render(request, "photo_list.html", {"photos":photos})

def post(request):
    # get(페이지 보여주기) / post(사용자 입력값 가져오기)
    # 일반 방식
    # if request.method == "POST":
    #     title = request.POST["title"] # ['name'] : html 파일 내에 name과 동일
    #     auther = request.POST["auther"]
    #     image = request.POST["image"]
    #     description = request.POST["description"]
    #     price = request.POST["price"]

    #     # 테이블 등록
    #     # insert into 테이블명 values(입력값) => SQL 구문

    #     # Photo 객체 생성 / save() == insert
    #     photo = Photo(title = title, auther = auther, image = image, description = description, price = price)
    #     photo.save()
    #     # 등록 완료 후 리스트로 이동
    #     return redirect("/photo/")
    # return render(request, "photo_post.html")

    # form 사용 방식
    # get(비어있는 form) / post(내용이 들어있는 form)
    if request.method == "POST":
        form =PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save()
            return redirect("home")
    else:
        form = PhotoForm()
    return render(request, "photo_post.html", {"form":form})


def detail(request, pk):
    # pk에 해당하는 이미지 정보를 찾아서 같이 보내주기
    # select * from photo where id=pk;

    # get_object_or_404(Photo, pk=pk) : id = pk
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, "photo_detail.html", {"photo":photo})

    # form 사용 시
    # form = PhotoForm(instance=photo)
    # return render(request, "photo_detail.html", {"form":form})

def remove(request, pk):
    # pk에 해당하는 이미지 찾은 후 삭제
    # delete from photo where id=pk;
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    
    # 이미지 삭제 성공 시 리스트로 이동
    return redirect("/photo/")

def edit(request, pk):
    # pk에 해당하는 이미지 찾은 후 가져가기
    photo = get_object_or_404(Photo, pk=pk)

    # get(사용자가 요청하는 이미지 보여주기) / post (수정)
    # 일반 방식
    # if request.method == "POST":
    #     photo.price = request.POST["price"]
    #     photo.save()
    #     return redirect("/photo/{}/".format(photo.pk))
    # return render(request, "photo_edit.html", {"photo":photo})

    # 폼 사용방식
    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save()
            return redirect("detail", pk=photo.pk)
    else:
        form = PhotoForm(instance=photo)
    
    return render(request, "photo_edit.html", {"form":form, "pk":pk})

@api_view(['GET'])
def serialize_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    serializer = PhotoSerializer(photo)
    photo_serializer = serializer.data

    return render(request, 'photo_detail.html', {'photo':photo_serializer})
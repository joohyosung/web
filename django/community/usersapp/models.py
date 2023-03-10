from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, PermissionsMixin

# AbstracUser
# AbstractBaseUser 상속
# username, first_name, last_name, email, password
# is_staff, is_active, date_joined

# AbstractBaseUser
#  password, last_login, is_active

# user 객체
# 속성 - username, password, email(필수요소 아님), first_name, last_name


# 프로젝트에 필요한 user
# email 필드 == id 개념 == username
# gender 필드(필수는 아님)
# password
# name 필수

class UserManager(BaseUserManager):
    def _create_user(self, email, password, name, phone, **extra_fields):
        """
        Create and save a user with the given email, password, name.
        """
        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)

        user = self.model(email=email, name=name, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, name, phone, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, name, phone, **extra_fields)

    def create_superuser(self, email, password, name, **extra_fields):
        """
        admin 계정에 성별 필요없음
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, name, phone=None, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User 생성 : AbstractUser or AbstractBaseUser 상속
    필드 추가 : email, password, name, phone

    권한 여부 추가
    """

    # null = True 지정하지 않으면 not null + unique ==> pk 속성
    email = models.EmailField(verbose_name="이메일", max_length=255, unique=True)
    password = models.CharField(verbose_name="비밀번호", max_length=128)
    name = models.CharField(verbose_name="이름", max_length=64)
    # phone : 비어있거나 null 허용(선택적 입력)
    phone = models.CharField(verbose_name="전화번호", max_length=50, blank=True, null=True)

    is_staff = models.BooleanField(verbose_name="관리자여부", default=False)

    # CustomUser 를 기반으로 user 생성을 도와줄 매니저 클래스 등록
    objects = UserManager()  # User.objects.create_user() 생성

    # username(아이디) 으로 사용할 필드 지정
    USERNAME_FIELD = "email"

    # email, password 요소 외에 사용자 생성 시 꼭 받아야하는 필드 작성
    REQUIRED_FIELDS = ["name"]

    def __str__(self) -> str:
        return "<%s>" % (self.email)

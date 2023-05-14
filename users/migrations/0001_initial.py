# Generated by Django 4.1.7 on 2023-05-13 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "user_name",
                    models.CharField(
                        error_messages={"unique": "이미 사용 중이거나 탈퇴한 사용자의 아이디입니다!"},
                        max_length=30,
                        unique=True,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        error_messages={"unique": "이미 사용 중이거나 탈퇴한 사용자의 이메일입니다!"},
                        max_length=255,
                        unique=True,
                        verbose_name="EMAIL",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="계정 생성일"),
                ),
                (
                    "last_password_changed",
                    models.DateTimeField(auto_now=True, verbose_name="비밀번호 마지막 변경일"),
                ),
                (
                    "withdraw",
                    models.BooleanField(default=False, verbose_name="회원 비활성화"),
                ),
                ("withdraw_at", models.DateTimeField(null=True, verbose_name="계정 탈퇴일")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        default="default_profile_pic.jpg",
                        upload_to="profile_pics",
                        verbose_name="PROFILE IMAGE",
                    ),
                ),
                (
                    "nickname",
                    models.CharField(
                        error_messages={"unique": "이미 사용 중이거나 탈퇴한 사용자의 닉네임입니다!"},
                        max_length=10,
                        null=True,
                        unique=True,
                        verbose_name="NICKNAME",
                    ),
                ),
                ("age", models.IntegerField(null=True, verbose_name="AGE")),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("MALE", "male"),
                            ("FEMALE", "female"),
                            ("OTHER", "other"),
                        ],
                        max_length=6,
                        null=True,
                        verbose_name="GENDER",
                    ),
                ),
                ("introduction", models.TextField(default="안녕하세요!", null=True)),
                (
                    "review_cnt",
                    models.PositiveIntegerField(default=0, verbose_name="Review cnt"),
                ),
                (
                    "followings",
                    models.ManyToManyField(
                        blank=True, related_name="followers", to="users.userprofile"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_profile",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="USER",
                    ),
                ),
            ],
        ),
    ]

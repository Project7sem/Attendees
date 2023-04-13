from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator

#manager for our custom model 
class MyAccountManager(BaseUserManager):
    # Method for  creating new user
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an Emaill address")
        if not username :
            raise ValueError("Users must have an Username")
        user  = self.model(
                email=self.normalize_email(email),
                username=username,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user
    # Method for creating super user.
    def create_superuser(self, email, username, password):
        user = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username,
            )
        user.is_admin = True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class Institute(models.Model):
    name=models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

class User(AbstractBaseUser):    
    class Roles(models.TextChoices):
        ADMIN= 'ADMIN', 'Admin'
        STUDENT = 'STUDENT','Student'
        TEACHER = 'TEACHER','Teacher'  

    role =  models.CharField(max_length=100, choices=Roles.choices, default=Roles.ADMIN)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=100,unique=True)
    institute = models.ForeignKey("Institute",on_delete=models.CASCADE,blank=True, null=True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)

    #Defines email is in username field.
    USERNAME_FIELD = ('email')

    #Username is required
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label ):
        return True





class InstituteManager(models.Manager):
    def get_queryset(self,*args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.ADMIN)

class AdminUser(User):
    obj  = InstituteManager()
    objects = MyAccountManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Roles.ADMIN
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.username






class TeacherManager(models.Manager):
    def get_queryset(self,*args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.TEACHER)


class Teacher(User):
    obj = TeacherManager()
    objects = MyAccountManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Roles.TEACHER
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.username





class StudentManager(models.Manager):
    def get_queryset(self,*args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.STUDENT)

class Student(User):
    obj = StudentManager()
    objects = MyAccountManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Roles.STUDENT
        return super().save(*args,**kwargs)
    
    def __str__(self):
        return self.username




class Faculty(models.Model):
    name = models.CharField(max_length=50)   

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey("Faculty", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name

class Semester(models.Model):
    sem_name = models.CharField(max_length=100)
    faculty = models.ForeignKey("Faculty", on_delete=models.CASCADE)
    courses = models.ManyToManyField("Courses")

    def __str__(self):
        return self.sem_name


class AdminProfile(models.Model):
    user = models.OneToOneField("AdminUser", on_delete=models.CASCADE)
    def __str__(self):
        return self.admin.email + "-profile"


class StudentProfile(models.Model):
    symbol_no = models.CharField(max_length=50)
    student = models.OneToOneField('Student', related_name='student', on_delete=models.CASCADE)
    bio_info =  models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', height_field=170, width_field=170,blank=True, null= True)
    faculty = models.ForeignKey('Faculty', related_name='faculty', on_delete=models.CASCADE,blank=True, null=True)
    Batch =models.CharField(max_length=50)
    sem = models.ForeignKey("Semester", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.student.email + "- profile"

class TeacherProfile(models.Model):
    teacher = models.OneToOneField("Teacher", on_delete=models.CASCADE)
    courses = models.ManyToManyField("Courses")
    bio_info =  models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', height_field=170, width_field=170,blank=True, null=True)
    
    def __str__(self):
        return self.teacher.email + "- profile"






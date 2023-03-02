from django.db import models

from helpers.models import BaseModel


class Category(BaseModel):
    """Kategoriyalar uchun model"""

    name = models.CharField("Nomi", max_length=100)
    slug = models.SlugField('Slug', max_length=100)
    avatar = models.ImageField('Rasmi', upload_to='category/avatars/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
                                                      

class Article(BaseModel):
    """Maqolalar uchun model"""

    ARTICLE_TYPES = (
        ('New', 'Yangi'),
        ('Draft', 'Qoralama'),
        ('Popular', 'Mashhur'),
        ('Actual', 'Dolzarb'),
    )

    author_id = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Muallif')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Karegoriya')
    title = models.CharField('Sarlavhasi', max_length=200)
    slug = models.SlugField('Slugi', max_length=200)
    slider = models.ImageField('Rasmi', upload_to='article/sliders/')
    short_description = models.CharField('Qisqa tevsif', max_length=250)
    description = models.TextField('Maqola matni')
    type = models.CharField('Maqola turi', max_length=20, choices=ARTICLE_TYPES, default='New')
    tags = models.ManyToManyField('Tag')
    time_to_read = models.PositiveIntegerField('O`qish uchun vaqt', default=1, help_text='Minutlarda kiriting')
    views_count = models.PositiveIntegerField('Ko`rishlar soni', default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'


class Tag(BaseModel):
    """Teglar uchun model"""

    name = models.CharField('Nomi', max_length=100)
    slug = models.SlugField('Slugi', max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Teg'
        verbose_name_plural = 'Teglar'


class Author(BaseModel):
    """Mualliflar uchun model"""

    full_name = models.CharField('F.I.SH.', max_length=100)
    avatar = models.ImageField('Rasmi', upload_to='author/avatar/')
    bio = models.TextField('Muallif haqida ma`lumot')
    subscribers = models.ManyToManyField('Subscriber')
    professions = models.ManyToManyField('Profession')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Muallif'
        verbose_name_plural = 'Mualliflar'


class Subscriber(BaseModel):
    """Obunachilar uchun model"""

    full_name = models.CharField('F.I.SH.', max_length=150)
    email = models.EmailField("Elektron poschta", max_length=100)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Obunachi'
        verbose_name_plural = 'Obunachilar'


class Profession(BaseModel):
    """Kasblar uchun model"""

    title = models.CharField('Nomi', max_length=100)
    slug = models.SlugField("Slug", max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Kasb'
        verbose_name_plural = 'Kasblar'


class Comment(BaseModel):
    """Izohlar uchun model"""

    subscriber_id = models.ForeignKey(Subscriber, on_delete=models.CASCADE, verbose_name='Muallifi')
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Maqola')
    text = models.CharField('Izoh matni', max_length=250)

    def __str__(self):
        return f"Muallif: {self.subscriber_id.full_name} \n Maqola id: {self.article_id.pk} \n Text: {self.text}"
   
    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'  


class Social_network_profile(BaseModel):
    """Mualliflarning ijtimoiy tarmoqdagi sahifalari uchun model"""

    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Muallif')
    social_network_type_id = models.ForeignKey('Social_network_type', on_delete=models.CASCADE)
    nickname = models.CharField('Foydalanuvchi nomi', max_length=150)
    profile_link = models.CharField('Profil uchun link', max_length=200)

    def __str__(self):
        return f"{self.nickname} -> {self.social_network_type_id.name}"
    
    class Meta:
        verbose_name = 'Ijtimoiy tarmoq sahifasi'
        verbose_name_plural = 'Ijtimoiy tarmoq sahifalari'  
    

class Social_network_type(BaseModel):
    """Ijtimoiy tarmoq turlari uchun model"""

    name = models.CharField('Nomi', max_length=50)
    logo = models.ImageField('Rasmi', upload_to='social_network/logo/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ijtimoiy tarmoq turi'
        verbose_name_plural = 'Ijtimoiy tarmoq turlari' 


class Message(BaseModel):
    """Xabarlar uchun model"""

    name = models.CharField('Ismi', max_length=100)
    email = models.EmailField('Elektron pochta', max_length=100)
    subject = models.CharField('Mavzusi', max_length=150)
    text = models.TextField('Xabar matni')

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'Xabar'
        verbose_name_plural = 'Xabarlar'
    





from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from model_utils.managers import InheritanceManager




# ______________Общие параметры_____________

class Country(models.Model):
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    name = models.CharField(max_length=255, verbose_name="Страна")

    def __str__(self):
        return self.name


class Color(models.Model):
    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

    name = models.CharField(max_length=255, verbose_name="Цвет")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название категории")
    image = models.ImageField(upload_to='categories')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products', kwargs={'slug': self.slug})


class Item(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    name = models.CharField(max_length=255, verbose_name="Полное название товара")
    price = models.PositiveIntegerField(verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="Категория")
    avaliable = models.BooleanField(verbose_name="В продаже", default=True)
    objects = InheritanceManager()

    def get_absolute_url(self):
        return reverse('single-product', kwargs={'pk': self.pk})


class Manufacturer(models.Model):
    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    name = models.CharField(max_length=255, verbose_name="Страна")

    def __str__(self):
        return self.name


# _______________________TV____________________
class TVOuts(models.Model):
    class Meta:
        verbose_name = "Выход ТВ"
        verbose_name_plural = "Выходы ТВ"

    name = models.CharField(max_length=255, verbose_name="Название (HDMI/AV/...)")

    def __str__(self):
        return self.name


class TVOS(models.Model):
    class Meta:
        verbose_name = "Операционная система ТВ"
        verbose_name_plural = "Операционные системы ТВ"

    name = models.CharField(max_length=255, verbose_name="Операционная система")

    def __str__(self):
        return self.name


class TVresolution(models.Model):
    class Meta:
        verbose_name = "Разрешение экрана ТВ"
        verbose_name_plural = "Разрешения экранов ТВ"

    width = models.PositiveIntegerField(verbose_name="Ширина")
    height = models.PositiveIntegerField(verbose_name="Высота")

    def __str__(self):
        return f'{self.width} x {self.height}'


class TVPhoto(models.Model):
    class Meta:
        verbose_name = "Фото ТВ"
        verbose_name_plural = "Фото ТВ"

    name = models.CharField(max_length=255, verbose_name="Название фотографии")
    img = models.ImageField(upload_to='tvs', verbose_name="Фото")

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe(u'<Img src="%s" width="150" height="150"/>' % escape(self.img.url))

    image_tag.short_description = 'Фото'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name


class TV(Item):
    class Meta:
        verbose_name = "Телевизор"
        verbose_name_plural = "Телевизоры"

    model_name = models.CharField(max_length=255, verbose_name="Модель")
    image = models.ManyToManyField(TVPhoto, verbose_name="Фото")
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, verbose_name="Цвет")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Страна-производитель")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING,
                                     verbose_name="Производитель")
    diag = models.PositiveIntegerField(verbose_name="Диагональ экрана в дюймах")
    resolution = models.ForeignKey(TVresolution, on_delete=models.DO_NOTHING, verbose_name="Разрешение матрицы")
    outputs = models.CharField(max_length=255, verbose_name="Выходы для переферии")
    smart = models.BooleanField(verbose_name="Смарт-ТВ", default=True)
    year = models.PositiveIntegerField(verbose_name="Год выхода", blank=True, null=True)
    os = models.ForeignKey(TVOS, on_delete=models.DO_NOTHING, verbose_name="Операционная система")

    def __str__(self):
        return self.model_name


# _______________________Стиральные машины______________________

class WMPhoto(models.Model):
    class Meta:
        verbose_name = "Фото стиральной машины"
        verbose_name_plural = "Фото стиральных машин"

    name = models.CharField(max_length=255, verbose_name="Название фотографии")
    img = models.ImageField(upload_to='wms', verbose_name="Фото")

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe(u'<Img src="%s" width="150" height="150"/>' % escape(self.img.url))

    image_tag.short_description = 'Фото'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name


class WM(Item):
    class Meta:
        verbose_name = "Стиральная машина"
        verbose_name_plural = "Стиральные машины"

    model_name = models.CharField(max_length=255, verbose_name="Модель")
    image = models.ManyToManyField(WMPhoto, verbose_name="Фото")
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, verbose_name="Цвет")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Страна-производитель")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING,
                                     verbose_name="Производитель")
    mods = models.PositiveIntegerField(verbose_name="Количество режимов")
    power = models.PositiveIntegerField(verbose_name="Мощность Вт")
    kg = models.PositiveIntegerField(verbose_name="Максимальная загрузка Кг")
    dry = models.BooleanField(verbose_name="Отжим", default=True)
    year = models.PositiveIntegerField(verbose_name="Год выхода", blank=True, null=True)

    def __str__(self):
        return self.model_name


# ______________________Fridge______________________


class FridgePhoto(models.Model):
    class Meta:
        verbose_name = "Фото холодильника"
        verbose_name_plural = "Фото холодильников"

    name = models.CharField(max_length=255, verbose_name="Название фотографии")
    img = models.ImageField(upload_to='fridges', verbose_name="Фото")

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe(u'<Img src="%s" width="150" height="150"/>' % escape(self.img.url))

    image_tag.short_description = 'Фото'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name


class Fridge(Item):
    class Meta:
        verbose_name = "Холодильник"
        verbose_name_plural = "Холодильники"

    model_name = models.CharField(max_length=255, verbose_name="Модель")
    image = models.ManyToManyField(WMPhoto, verbose_name="Фото")
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, verbose_name="Цвет")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Страна-производитель")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING,
                                     verbose_name="Производитель")
    containers = models.PositiveIntegerField(verbose_name="Количество отсеков")
    power = models.CharField(max_length=255, verbose_name="Энергоэффективность Вт")
    liters = models.PositiveIntegerField(verbose_name="Объём в литрах")
    freeze = models.BooleanField(verbose_name="Режим заморозки", default=True)
    year = models.PositiveIntegerField(verbose_name="Год выхода", blank=True, null=True)

    def __str__(self):
        return self.model_name


# _________________Oven____________

class OvenPhoto(models.Model):
    class Meta:
        verbose_name = "Фото духовки"
        verbose_name_plural = "Фото духовок"

    name = models.CharField(max_length=255, verbose_name="Название фотографии")
    img = models.ImageField(upload_to='ovens', verbose_name="Фото")

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe(u'<Img src="%s" width="150" height="150"/>' % escape(self.img.url))

    image_tag.short_description = 'Фото'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name


class Oven(Item):
    class Meta:
        verbose_name = "Духовка"
        verbose_name_plural = "Духовкки"

    model_name = models.CharField(max_length=255, verbose_name="Модель")
    image = models.ManyToManyField(OvenPhoto, verbose_name="Фото")
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, verbose_name="Цвет")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Страна-производитель")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING,
                                     verbose_name="Производитель")
    effectivity = models.PositiveIntegerField(verbose_name="Энергоэффективность Вт")
    power = models.PositiveIntegerField(verbose_name="Мощность Вт")
    liters = models.PositiveIntegerField(verbose_name="Объём в литрах")
    freeze = models.BooleanField(verbose_name="Режим разморозки", default=True)
    year = models.PositiveIntegerField(verbose_name="Год выхода", blank=True, null=True)

    def __str__(self):
        return self.model_name


# _________________Посудомойки_______________

class DishWasherPhoto(models.Model):
    class Meta:
        verbose_name = "Фото посудомоечной машины"
        verbose_name_plural = "Фото посудомоечных машин"

    name = models.CharField(max_length=255, verbose_name="Название фотографии")
    img = models.ImageField(upload_to='dishwashers', verbose_name="Фото")

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe(u'<Img src="%s" width="150" height="150"/>' % escape(self.img.url))

    image_tag.short_description = 'Фото'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name


class DishWasher(Item):
    class Meta:
        verbose_name = "Посудомоечная машина"
        verbose_name_plural = "Посудомоечные машины"

    model_name = models.CharField(max_length=255, verbose_name="Модель")
    image = models.ManyToManyField(DishWasherPhoto, verbose_name="Фото")
    into = models.BooleanField(verbose_name="Встраивается", default=True)
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, verbose_name="Цвет")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Страна-производитель")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING,
                                     verbose_name="Производитель")
    effectivity = models.PositiveIntegerField(verbose_name="Энергоэффективность Вт")
    power = models.PositiveIntegerField(verbose_name="Мощность Вт")
    liters = models.PositiveIntegerField(verbose_name="Объём в литрах")
    spend = models.PositiveIntegerField(verbose_name="Расход воды в литрах")
    year = models.PositiveIntegerField(verbose_name="Год выхода", blank=True, null=True)

    def __str__(self):
        return self.model_name


# _________________Пылесосы_______________

class VacumCleanerPhoto(models.Model):
    class Meta:
        verbose_name = "Фото пылесоса"
        verbose_name_plural = "Фото пылесосов"

    name = models.CharField(max_length=255, verbose_name="Название фотографии")
    img = models.ImageField(upload_to='vacum', verbose_name="Фото")

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe(u'<Img src="%s" width="150" height="150"/>' % escape(self.img.url))

    image_tag.short_description = 'Фото'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name


class Vacum(Item):
    class Meta:
        verbose_name = "Пылесос"
        verbose_name_plural = "Пылесосы"

    model_name = models.CharField(max_length=255, verbose_name="Модель")
    image = models.ManyToManyField(VacumCleanerPhoto, verbose_name="Фото")
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, verbose_name="Цвет")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Страна-производитель")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING,
                                     verbose_name="Производитель")
    effectivity = models.PositiveIntegerField(verbose_name="Энергоэффективность Вт")
    power = models.PositiveIntegerField(verbose_name="Мощность Вт")
    mods = models.PositiveIntegerField(verbose_name="Количество режимов работы")
    cord_len = models.PositiveIntegerField(verbose_name="Длина шнура")
    year = models.PositiveIntegerField(verbose_name="Год выхода", blank=True, null=True)

    def __str__(self):
        return self.model_name


# _________________Сушилка_______________

class DryPhoto(models.Model):
    class Meta:
        verbose_name = "Фото сушилки"
        verbose_name_plural = "Фото сушилок"

    name = models.CharField(max_length=255, verbose_name="Название фотографии")
    img = models.ImageField(upload_to='dry', verbose_name="Фото")

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe(u'<Img src="%s" width="150" height="150"/>' % escape(self.img.url))

    image_tag.short_description = 'Фото'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name


class DryMashine(Item):
    class Meta:
        verbose_name = "Сушильная машина"
        verbose_name_plural = "Сушильные машины"

    model_name = models.CharField(max_length=255, verbose_name="Модель")
    image = models.ManyToManyField(DryPhoto, verbose_name="Фото")
    into = models.BooleanField(verbose_name="Встраивается", default=True)
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, verbose_name="Цвет")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Страна-производитель")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING,
                                     verbose_name="Производитель")
    effectivity = models.PositiveIntegerField(verbose_name="Энергоэффективность Вт")
    power = models.PositiveIntegerField(verbose_name="Мощность Вт")
    mods = models.PositiveIntegerField(verbose_name="Количество режимов работы")
    cord_len = models.PositiveIntegerField(verbose_name="Длина шнура")
    year = models.PositiveIntegerField(verbose_name="Год выхода", blank=True, null=True)

    def __str__(self):
        return self.model_name


# _________________Микроволновка_______________

class MicrowavePhoto(models.Model):
    class Meta:
        verbose_name = "Фото сушилки"
        verbose_name_plural = "Фото сушилок"

    name = models.CharField(max_length=255, verbose_name="Название фотографии")
    img = models.ImageField(upload_to='microwave', verbose_name="Фото")

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe(u'<Img src="%s" width="150" height="150"/>' % escape(self.img.url))

    image_tag.short_description = 'Фото'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name


class Microwave(Item):
    class Meta:
        verbose_name = "Микроволновка"
        verbose_name_plural = "Микроволновки"

    model_name = models.CharField(max_length=255, verbose_name="Модель")
    image = models.ManyToManyField(MicrowavePhoto, verbose_name="Фото")
    into = models.BooleanField(verbose_name="Встраивается", default=True)
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, verbose_name="Цвет")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Страна-производитель")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING,
                                     verbose_name="Производитель")
    effectivity = models.PositiveIntegerField(verbose_name="Энергоэффективность Вт")
    power = models.PositiveIntegerField(verbose_name="Мощность Вт")
    mods = models.PositiveIntegerField(verbose_name="Количество режимов работы")
    defrost = models.BooleanField(verbose_name="Режим разморозки", default=True)
    year = models.PositiveIntegerField(verbose_name="Год выхода", blank=True, null=True)

    def __str__(self):
        return self.model_name


# _________________Мультиварка_______________

class CookerPhoto(models.Model):
    class Meta:
        verbose_name = "Фото мультиварки"
        verbose_name_plural = "Фото мультиварок"

    name = models.CharField(max_length=255, verbose_name="Название фотографии")
    img = models.ImageField(upload_to='cooker', verbose_name="Фото")

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe(u'<Img src="%s" width="150" height="150"/>' % escape(self.img.url))

    image_tag.short_description = 'Фото'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name


class Cooker(Item):
    class Meta:
        verbose_name = "мультиварка"
        verbose_name_plural = "мультиварка"

    model_name = models.CharField(max_length=255, verbose_name="Модель")
    image = models.ManyToManyField(CookerPhoto, verbose_name="Фото")
    into = models.BooleanField(verbose_name="Встраивается", default=True)
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, verbose_name="Цвет")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Страна-производитель")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING,
                                     verbose_name="Производитель")
    effectivity = models.PositiveIntegerField(verbose_name="Энергоэффективность Вт")
    power = models.PositiveIntegerField(verbose_name="Мощность Вт")
    mods = models.PositiveIntegerField(verbose_name="Количество режимов работы")
    defrost = models.BooleanField(verbose_name="Режим разморозки", default=True)
    year = models.PositiveIntegerField(verbose_name="Год выхода", blank=True, null=True)

    def __str__(self):
        return self.model_name


class Cart(models.Model):
    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
    session_id = models.CharField(max_length=255)
    items = models.ManyToManyField(Item, verbose_name="Содержимое")
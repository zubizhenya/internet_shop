# Generated by Django 4.0.7 on 2023-06-14 13:10

import app_shop.models
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "name",
                    models.CharField(
                        db_index=True, max_length=200, verbose_name="Название"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=200, unique=True, verbose_name="Псевдоним для url"
                    ),
                ),
                (
                    "icon",
                    models.FileField(
                        blank=True,
                        upload_to="category/",
                        validators=[app_shop.models.validate_svg],
                        verbose_name="Иконка",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="category/", verbose_name="Изображение"
                    ),
                ),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="children",
                        to="app_shop.category",
                        verbose_name="Родительская категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                    "name",
                    models.CharField(
                        db_index=True, max_length=200, verbose_name="Название"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=200, verbose_name="Псевдоним для url"),
                ),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Цена"
                    ),
                ),
                ("stock", models.PositiveIntegerField(verbose_name="Остаток")),
                (
                    "available",
                    models.BooleanField(default=True, verbose_name="Активен"),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создан"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлен"),
                ),
                (
                    "manufacturer",
                    models.CharField(
                        db_index=True, max_length=50, verbose_name="Производитель"
                    ),
                ),
                (
                    "limited",
                    models.BooleanField(
                        default=False, verbose_name="Ограниченная серия"
                    ),
                ),
                (
                    "category",
                    mptt.fields.TreeForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="category",
                        to="app_shop.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
                "ordering": ("price",),
            },
        ),
        migrations.CreateModel(
            name="PropertyName",
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
                    "name",
                    models.CharField(
                        db_index=True, max_length=255, verbose_name="характеристика"
                    ),
                ),
            ],
            options={
                "verbose_name": "Имя характеристики",
                "verbose_name_plural": "Имена характеристик",
            },
        ),
        migrations.CreateModel(
            name="PropertyValue",
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
                ("value", models.CharField(max_length=255, verbose_name="значение")),
            ],
            options={
                "verbose_name": "Значение характеристики",
                "verbose_name_plural": "Значение характеристик",
            },
        ),
        migrations.CreateModel(
            name="Property",
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
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property",
                        to="app_shop.product",
                        verbose_name="товар",
                    ),
                ),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property",
                        to="app_shop.propertyname",
                        verbose_name="название",
                    ),
                ),
                (
                    "value",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property",
                        to="app_shop.propertyvalue",
                        verbose_name="значение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Характеристика",
                "verbose_name_plural": "Характеристики",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="option",
            field=models.ManyToManyField(
                through="app_shop.Property", to="app_shop.propertyname"
            ),
        ),
        migrations.CreateModel(
            name="Gallery",
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
                ("image", models.ImageField(upload_to="products/%Y/%m/%d")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="image",
                        to="app_shop.product",
                        verbose_name="изображение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Изображение",
                "verbose_name_plural": "Изображения",
            },
        ),
        migrations.AlterIndexTogether(
            name="product",
            index_together={("id", "slug")},
        ),
    ]

from django.db import models


class Advertisement(models.Model):

    #Заголовок
    #Небольшое текстовое поле
    title = models.CharField("Заголовок", max_length=128)
 
    #Описание
    #Большое текстовое поле
    description = models.TextField("Описание")

    #Цена
    #Число с фиксированной точностью
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)

    #Уместен ли торг
    #Логическое значение
    auction = models.BooleanField("Торг", help_text="Отметьте, если хотите торговаться")

    #Дата создания
    created_at = models.DateField(auto_now_add=True)

    #Дата изменения
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = "advertisements"
    #Изображение

    #Адрес

    #Отзыв/рейтинг продавца

    #Контакты продавца

    #Похожие товары

    


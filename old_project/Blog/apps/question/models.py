from django.db import models

# Create your models here.
class question(models.Model):
    money = 'Финансы'
    sales = 'Продажи'
    marketing = 'Маркетинг'
    TOPICS = [(money,'Финансы'), (sales,"Продажи"),(marketing, "Маркетинг")]
    question_quest = models.CharField('Вопрос', max_length=200)
    question_answer = models.CharField('Ответ',max_length=200)
    question_topic = models.CharField('Тема',max_length=200, choices=TOPICS)

    def __str__(self):
        return self.question_quest

    class Meta:
        verbose_name = 'Вопросик'
        verbose_name_plural = 'Вопросики'


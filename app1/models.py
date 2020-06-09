from django.db import models
from django.forms import ModelForm

# Create your models here.
class feedback(models.Model):
    topic = models.TextField()
    ques = models.TextField()
    ans = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        return self.topic,self.ques,self.ans

class PickForm(ModelForm):
    class Meta:
        model = feedback
        fields = "__all__"
from datetime import timezone

from haystack import indexes
from .models import Car



class CarIndex(indexes.SearchIndex, indexes.Indexable):
    name = indexes.CharField(document=True, use_template=False)
    color = indexes.CharField(model_attr="color")
    description = indexes.CharField(model_attr="description")

    def get_model(self):
        return Car

    def index_queryset(self, using=None):
        return self.get_model().objects.f(
            created__lte=timezone.now()
        )



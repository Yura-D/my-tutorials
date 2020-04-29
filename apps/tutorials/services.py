from .models import Tutorial, Category


TUTORIAL_TUPLE = (
    'name',
    'link',
    'category__name',
    'comment'
)

def get_all():
    ''' Return list of all article '''
    tutorial_list = Tutorial.objects.values_list(*TUTORIAL_TUPLE).order_by(
        'category')

    return tutorial_list


def get_by_category(category):
    tutorials_list = Tutorial.objects.filter(
        category__name=category).values_list(*TUTORIAL_TUPLE).order_by(
            'created')


def get_all_categories():
    return Category.objects.all().values_list(
        'name', flat=True).order_by('name')


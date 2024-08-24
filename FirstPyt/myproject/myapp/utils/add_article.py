from myapp.models import  Article

article = Article (title='Заголовок статьи', author='Имя автора', content='Текст статьи')
article.save()
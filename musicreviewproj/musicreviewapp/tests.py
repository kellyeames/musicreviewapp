from django.test import TestCase
from .models import GenreType, Album, Review
from .views import index, gettypes, getalbums
from django.urls import reverse
from django.contrib.auth.models import User
import datetime
from .forms import AlbumForm

# Create your tests here.
class GenreTypeTest(TestCase):
    def test_string(self):
        type=GenreType(typename="Alternative")
        self.assertEqual(str(type), type.typename)
    
    def test_table(self):
        self.assertEqual(str(GenreType._meta.db_table), 'genretype')

class ReviewTest(TestCase):
    def test_string(self):
        rev=Review(reviewtitle="Beastie Boys Review")
        self.assertEqual(str(rev), rev.reviewtitle)
    
    def test_table(self):
        self.assertEqual(str(Review._meta.db_table), 'review')

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetTypesTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('types'))
        self.assertEqual(response.status_code, 200)

class New_Album_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='Sadie2009')
        self.type=GenreType.objects.create(typename='pop')
        self.alb = Album.objects.create(albumname='album1', albumgenretype=self.type, user=self.test_user, albumreviewentrydate='2019-04-02', albumurl= 'http:www.pop.com')
    
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newalbum'))
        self.assertRedirects(response, '/accounts/login/?next=/musicreviewapp/newAlbum/')
    
    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='Sadie2009')
        response=self.client.get(reverse('newalbum'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'musicreviewapp/newalbum.html')

class AlbumFormTest(TestCase):
    def setUp(self):
        self.user2=User.objects.create(username='user2', password='Sadie2009')
        self.type2=GenreType.objects.create(typename='type1')

    def test_albumForm(self):
        data={
            'albumname' : 'album1',
            'albumgenretype' : self.type2,
            'user' : self.user2,
            'albumname' : 'new album',
            'albumreview' : 'good album',
            'albumreviewentrydate' : datetime.date(2019,5,28),
        }
        form = AlbumForm(data=data)
        self.assertFalse(form.is_valid())






from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import CommentForm
from .models import Post, Comment


class TestBlogViews(TestCase):

    def setUp(self):
        """Create a superuser and a blog post"""
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post(title="Blog title", author=self.user,
                         slug="blog-title", excerpt="Blog excerpt",
                         content="Blog content", status=1)
        self.post.save()

    def test_render_post_detail_page_with_comment_form(self):
        """Verifies a single blog post containing a comment form is returned"""
        response = self.client.get(reverse('post_detail', args=['blog-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(
            reverse('post_detail', args=['blog-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Comment submitted and awaiting approval',
                      response.content)

    def test_comment_edit(self):
        """Test for editing a comment on a post"""
        self.client.login(username="myUsername", password="myPassword")
        comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body="Original comment",
            approved=True
        )
        post_data = {
            'body': 'Updated comment.'
        }
        url = reverse('comment_edit', args=['blog-title', comment.id])
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, 302)
        comment.refresh_from_db()
        self.assertEqual(comment.body, 'Updated comment.')
        self.assertFalse(comment.approved)

    def test_comment_delete(self):
        """Test for deleting a comment on a post"""
        self.client.login(username="myUsername", password="myPassword")
        comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body="Comment to be deleted",
            approved=True
        )
        response = self.client.post(
            reverse('comment_delete', args=['blog-title', comment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(id=comment.id).exists())
        self.client.login(username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(
            reverse('post_detail', args=['blog-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Comment submitted and awaiting approval',
                      response.content)

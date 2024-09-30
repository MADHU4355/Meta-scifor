from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Ebook, Poster, BusinessCard
from .forms import EbookForm, PosterForm, BusinessCardForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.template.loader import render_to_string


def home(request):
    ebooks = Ebook.objects.all()  
    posters = Poster.objects.all()  
    context = {
        'ebooks': ebooks,
        'posters': posters,
    }
    return render(request, 'home.html', context)

def upload_business_card(request):
    if request.method == 'POST':
        form = BusinessCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BusinessCardForm()
    return render(request, 'upload_business_card.html', {'form': form})

def index(request):
    context = {
        'ebooks': [
            {'title': 'Nectar_of_Devotion', 'file': r'Downloads\Nectar_of_Devotion.pdf'},
            {'title': 'Janmashtami-Vrata-Manual', 'file': r'Downloads\English-Janmashtami-Vrata-Manual_1.pdf'},
        ],
        'posters': [
            {'title': 'Hare Krishna Maha Mantra', 'image': 'Downloads\chant hk.jpg'},
            {'title': 'Chant and Be Happy', 'image': 'Downloads\chant-and-be-happy-srila-prabhupada-2022-10-25-21-55.jpg'},
        ],
    }
    return render(request, 'index.html', context)

def nectar_of_devotion(request):
    return render(request, 'nectar_of_devotion.html')
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('login')  # Redirect to login after successful signup

    return render(request, 'signup.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')

    return render(request, 'login.html')



"""def create_ebook_and_poster(request):
    # Create an ebook instance
    ebook_instance = Ebook.objects.create(
        title="The Great Adventure",
        author="Jane Doe",
        description="A thrilling tale of adventure and discovery.",
        publication_date="2024-01-01",
        cover_image="covers/great_adventure_cover.jpg",  # Path to the cover image
        file="ebooks/great_adventure.epub"  # Path to the ebook file
    )

    # Create a poster instance associated with the ebook
    poster_instance = Poster.objects.create(
        ebook=ebook_instance,
        poster_image="posters/great_adventure_poster.jpg",  # Path to the poster image
        dimensions="24x36 inches"  # Dimensions of the poster
    )

    # Optional: Print to verify in the console (or you can log this)
    print(ebook_instance)
    print(poster_instance)

    # Render a template and pass the created instances
    return render(request, 'create.html', {
        'ebook': ebook_instance,
        'poster': poster_instance
    })
"""




@login_required
def upload_ebook(request):
    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ebook uploaded successfully!')
            return redirect('home')
    else:
        form = EbookForm()
    return render(request, 'upload_ebook.html', {'form': form})

@login_required
def upload_poster(request):
    if request.method == 'POST':
        form = PosterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Poster uploaded successfully!')
            return redirect('home')
    else:
        form = PosterForm()
    return render(request, 'upload_poster.html', {'form': form})

@login_required
def uploaded_list(request):
    ebooks = Ebook.objects.all()
    posters = Poster.objects.all()
    return render(request, 'uploaded_list.html', {'ebooks': ebooks, 'posters': posters})

@login_required
def ebook_detail(request, id):
    ebook = get_object_or_404(Ebook, id=id)
    return render(request, 'ebook_detail.html', {'ebook': ebook})
    #return render(request, 'ebook_detail.html')

@login_required
def poster_detail(request, id):
    poster = get_object_or_404(Poster, id=id)
    return render(request, 'poster_detail.html', {'poster': poster})

"""def download(request):
    ebooks = Ebook.objects.all()
    posters = Poster.objects.all()
    return render(request, 'download.html', {'ebooks': ebooks, 'posters': posters})"""

@login_required
def download(request, id):
    # Example for Ebook
    try:
        ebook = Ebook.objects.get(id=id)
        response = HttpResponse(ebook.file, content_type='application/pdf')  # Adjust content_type as needed
        response['Content-Disposition'] = f'attachment; filename="{ebook.title}.pdf"'
        return response
    except Ebook.DoesNotExist:
        return HttpResponse("E-book not found", status=404)

def change_password(request):
    return render(request, 'change_password.html')

#def reset_password(request):
    return render(request, 'reset_password.html')

def reset_password(request):
    if request.method == "POST":
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            subject = "Password Reset Requested"
            email_template_name = "password_reset_email.html"
            context = {
                "email": user.email,
                'domain': 'your-domain.com',
                'site_name': 'Ebook Platform',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                'token': default_token_generator.make_token(user),
                'protocol': 'http',
            }
            email_body = render_to_string(email_template_name, context)
            send_mail(subject, email_body, 'your_email@example.com', [user.email], fail_silently=False)

            # Add a success message
            messages.success(request, "A password reset link has been sent to your email address.")
        except User.DoesNotExist:
            messages.error(request, "This email address is not registered.")  # Optional error message
    return render(request, 'reset_password.html')

def user_logout(request):
    logout(request)
    return render(request, 'logout.html')

def forget_password(request):
    return render(request, 'forget_password.html')

def about(request):
    if request.method == 'POST':
        pass
    return render(request, 'about.html')

def contact(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        success = True 
    return render(request, 'contact_us.html', {'success': success})

def create_account(request):
    return render(request, 'create_account.html')













"""from django.shortcuts import render, redirect
from .models import Ebook, Poster
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def upload_ebook(request):
    if request.method == 'POST' and request.FILES['file']:
        ebook = Ebook(
            title=request.POST['title'],
            author=request.POST['author'],
            file=request.FILES['file']
        )
        ebook.save()
        return redirect('home')
    return render(request, 'upload_ebook.html')

def upload_poster(request):
    if request.method == 'POST' and request.FILES['image']:
        poster = Poster(
            title=request.POST['title'],
            image=request.FILES['image']
        )
        poster.save()
        return redirect('home')
    return render(request, 'upload_poster.html')

def download(request):
    ebooks = Ebook.objects.all()
    posters = Poster.objects.all()
    return render(request, 'download.html', {'ebooks': ebooks, 'posters': posters})

def change_password(request):
    return render(request, 'change_password.html')

def reset_password(request):
    return render(request, 'reset_password.html')

def forget_password(request):
    return render(request, 'forget_password.html')

def about(request):
    return render(request, 'about.html')

def create_account(request):
    return render(request, 'create_account.html')
"""
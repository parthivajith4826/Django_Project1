from django.shortcuts import render,get_object_or_404,redirect
from .models import Book,Users,Category
from .forms import BookForm,SignupForm,CategoryForm
import hashlib

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request,'booksapp/book_list.html',{'books':books})



def book_detail(request,book_id):

    book = get_object_or_404(Book,id = book_id)
    return render(request,'booksapp/book_details.html',{'book':book})




def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print(form.is_valid)
        if form.is_valid():
            # print(form.clean_email)
            print("hello")
            form.save()
            # email = form.cleaned_data['email']


            # request.session['email'] = email


            return redirect('/booksapp/list/')
    
    else :
        form = SignupForm()
    
    return render(request,'booksapp/signup.html',{'form':form})
        


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email','').strip()
        password = request.POST.get('password','').strip()
        
            

        if not Users.objects.filter(email=email).exists():
            return render(request,'booksapp/login.html',{'error':'No account found with this email.'})
        
        
        password = hashlib.sha256(password.encode()).hexdigest()

        if not Users.objects.filter(password=password).exists():
            return render(request, 'booksapp/login.html', {'error': 'Incorrect password.'})
        
        user  = Users.objects.filter(email=email,password=password).first()
    
        
        if user.admin:
            return redirect('/booksapp/list_admin_login/')
        else :
            return redirect('/booksapp/list_login/')
        
    
    return render(request,'booksapp/login.html')



def book_list_login(request):
    categories = Category.objects.all() 
    return render(request, 'booksapp/book_list_login.html', {'categories': categories})


def book_list_admin_login(request):
    categories = Category.objects.all() 
    return render(request, 'booksapp/admin_list_login.html', {'categories': categories})


def book_create(request):
    form1 = BookForm()
    form2 = CategoryForm()


    if request.method == 'POST':
        if 'Book_submit' in request.POST:
            book_form = BookForm(request.POST)
            if book_form.is_valid():
                book_form.save()
        elif 'Category_submit' in request.POST:
            category_form = CategoryForm(request.POST)
            if category_form.is_valid():
                category_form.save()
        
        else :
            return redirect('/booksapp/add/')
        
    return render(request,'booksapp/book_form.html',{'form1':form1,'form2':form2})


def book_update_s(request):
    books = Book.objects.all()
    return render(request,'booksapp/book_update_s.html',{'books':books})
    


def book_update_f(request,id):
    book = get_object_or_404(Book, id = id)

    if request.method == 'POST':
        form = BookForm(request.POST,instance = book)
        if form.is_valid():
            form.save()
            return redirect('/booksapp/update_s/')

    else :
        form = BookForm(instance=book) 
    return render(request,'booksapp/book_update_f.html',{'form1':form})





def book_remove_s(request):
    books = Book.objects.all()
    return render(request,'booksapp/book_remove_s.html',{'books':books})
    


def book_remove_f(request,id):
    book = get_object_or_404(Book, id = id)

    if request.method == 'POST':
        book.delete()
        return redirect('/booksapp/remove_s/')

    else :
        form = BookForm(instance=book) 
    return render(request,'booksapp/book_remove_f.html',{'form1':form})
    


    

        






            
             
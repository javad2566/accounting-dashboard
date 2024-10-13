from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.views.generic import TemplateView,DetailView
# Create your views here.
from .models import Customer
from django.contrib import messages
class ListCustomerView(View):
    def get(slf,request):
        customers = Customer.objects.filter(user=request.user)
        search_customer =request.GET.get("search_customer")
        available = request.GET.get("available")
        unavailable = request.GET.get("unavailable")
        if available:
            customers = Customer.objects.filter(user=request.user).filter(is_paid=True)
        if unavailable:
            customers = Customer.objects.filter(user=request.user).filter(is_paid=False)
        if search_customer:
            customers = Customer.objects.filter(user=request.user).filter(fullname__contains=search_customer)
        return render(request,"customer/list.html" ,{"customers":customers ,"available":available,"unavailable":unavailable,"search_customer":search_customer})
    

    def post(self,request):
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        discription = request.POST.get("discription")
        if fullname and phone:
            if Customer.objects.filter(user=request.user).filter(fullname__contains=fullname) or Customer.objects.filter(user=request.user).filter(phone=phone) :
                messages.error(request,"این مشتری در سایت وجود دارد !")
                return redirect("/customer/list")
            else:
                Customer.objects.create(user=request.user,fullname=fullname,phone=phone,is_paid=True,discription=discription)
                messages.success(request,"مشتری جدید اضافه شد ")
                return redirect("/customer/list")
        else:
            messages.error(request,"اطلاعات ناقس هست ")
            return redirect("/product/list")
        

class DetailCustomerView(View):
    def get(self,request,*args,**kwargs):
        customers = Customer.objects.filter(user=request.user)
        customer = get_object_or_404(customers,id=kwargs["id"])
        return render(request,"customer/detail.html",{"customer":customer})
    

    def post(self,request,*args,**kwargs):
        customers = Customer.objects.filter(user=request.user)
        customer = get_object_or_404(customers,id=kwargs["id"])       
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        discription = request.POST.get("discription")
        customer.fullname = fullname
        customer.phone = phone
        customer.discription = discription
        customer.save()
        messages.success(request,f"مشتری {customer.fullname} ویرایش شد  ")
        return redirect("/customer/list/")
    

class DeleteCustomerView(View):
    def get(self,request,*args,**kwargs):
        customers = Customer.objects.filter(user=request.user)
        customer = get_object_or_404(customers,id=kwargs["id"])
        messages.success(request,f"مشتری {customer.fullname} حذف شد !")
        customer.delete()
        return redirect("/customer/list")
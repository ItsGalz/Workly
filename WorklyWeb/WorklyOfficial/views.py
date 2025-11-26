from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    """Página principal - Login"""
    if request.method == 'POST':
        # Obtener datos del formulario
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        print(f"🔐 Intento de login: {email}")
        
        # Validaciones básicas
        if not email or not password:
            messages.error(request, 'Todos los campos son obligatorios.')
            return render(request, 'WorklyOfficial/login.html')  # ✅ Ruta corregida
        
        # Simulación de login exitoso (para pruebas)
        messages.success(request, f'¡Bienvenido a WORKLY, {email}! (Modo prueba)')
        return redirect('home')
    
    return render(request, 'WorklyOfficial/login.html')  # ✅ Ruta corregida

def home(request):
    """Página de inicio después del login"""
    return render(request, 'WorklyOfficial/home.html')  # ✅ Ruta corregida

def register_view(request):
    """Página de registro"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        
        print(f"📧 Registro intentado: {email}")
        
        # Validaciones
        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'WorklyOfficial/register.html')  # ✅ Ruta corregida
        
        if len(password) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres.')
            return render(request, 'WorklyOfficial/register.html')  # ✅ Ruta corregida
        
        # Simulación de registro exitoso
        messages.success(request, f'¡Cuenta creada para {email}! (Modo prueba)')
        messages.info(request, 'Ahora puedes iniciar sesión')
        
        # Redirigir al login después del registro
        return redirect('login')
    
    return render(request, 'WorklyOfficial/register.html')  # ✅ Ruta corregida

def logout_view(request):
    """Cerrar sesión (simulado)"""
    messages.info(request, 'Has cerrado sesión (Modo prueba)')
    return redirect('login')

def profile_view(request):
    """Página de perfil del usuario"""
    return render(request, 'WorklyOfficial/profile.html')  # ✅ Ruta corregida

def memberships_view(request):
    """Página de membresías"""
    return render(request, 'WorklyOfficial/memberships.html')  # ✅ Ruta corregida


def publicarme_view(request):
    """Página para publicar servicios"""
    return render(request, 'WorklyOfficial/publicarme.html')  # ✅ Nueva vista

def payment_page(request):
    """Página de pago - Sin verificación de autenticación Django"""
    # Obtener el ID de la membresía
    membership_id = request.GET.get('id')
    
    if not membership_id:
        # Si no hay ID, redirigir a membresías
        return redirect('memberships')
    
    context = {
        'membership_id': membership_id,
    }
    
    return render(request, 'WorklyOfficial/payment.html', context)
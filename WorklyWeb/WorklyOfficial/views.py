from django.shortcuts import render, redirect
from django.contrib import messages

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
            return render(request, 'WorklyOfficial/login.html')
        
        # Simulación de login exitoso (para pruebas)
        # En una versión real aquí iría la autenticación real
        messages.success(request, f'¡Bienvenido a WORKLY, {email}! (Modo prueba)')
        return redirect('home')  # Redirigir al home después del "login"
    
    # GET request - mostrar formulario de login
    return render(request, 'WorklyOfficial/login.html')

def home(request):
    """Página de inicio después del login"""
    return render(request, 'WorklyOfficial/home.html')

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
            return render(request, 'WorklyOfficial/register.html')
        
        if len(password) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres.')
            return render(request, 'WorklyOfficial/register.html')
        
        # Simulación de registro exitoso
        messages.success(request, f'¡Cuenta creada para {email}! (Modo prueba)')
        messages.info(request, 'Ahora puedes iniciar sesión')
        
        # Redirigir al login después del registro
        return redirect('login')
    
    return render(request, 'WorklyOfficial/register.html')

def logout_view(request):
    """Cerrar sesión (simulado)"""
    messages.info(request, 'Has cerrado sesión (Modo prueba)')
    return redirect('login')

def profile_view(request):
    return render(request, 'profile.html')
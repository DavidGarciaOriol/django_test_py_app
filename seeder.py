import os
import django
import random
from faker import Faker

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User
from marcador.models import Proyecto, Tarea  # Asumiendo que la app se llama 'tasks'

fake = Faker()

def create_demo_data():
    # 1. Asegurarnos de que hay usuarios
    if User.objects.count() < 3:
        print("Creando usuarios de prueba...")
        for name in ['profe_admin', 'alumno_1', 'alumno_2']:
            User.objects.get_or_create(username=name, email=f"{name}@ejemplo.com")

    users = list(User.objects.all())

# Crear Proyectos

    print("Generando proyectos...")
    for _ in range(5):
        owner = random.choice(users)
        project = Proyecto.objects.create(
            titulo=fake.catch_phrase(),
            descripcion=fake.paragraph(nb_sentences=3),
            fecha_limite=fake.future_date(random.randint(7,21)),
            owner=owner
        )
        # Añadir colaboradores aleatorios (que no sean el dueño)
        others = [u for u in users if u != owner]
        project.colaboradores.set(random.sample(others, k=random.randint(1, len(others))))

        # 3. Crear Tareas para cada proyecto
        print(f"  Añadiendo tareas al proyecto: {project.titulo}")
        for _ in range(random.randint(5, 10)):
            Tarea.objects.create(
                project=project,
                title=fake.bs().capitalize(),
                status=random.choice(['TODO', 'INPROG', 'DONE']),
                priority=random.choice(['L', 'M', 'H']),
                assigned_to=random.choice(users)
            )

    print("--- ¡Base de Datos Aiven/MySQL poblada con éxito! ---")

if __name__ == '__main__':
    create_demo_data()
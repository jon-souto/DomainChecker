import dns.resolver
import string
from tabulate import tabulate
from tqdm import tqdm  # Importar tqdm para la barra de progreso

# Función para obtener los posibles dominios homográficos
def homoglyphs(domain):
    homoglyphs = []
    for c in domain:
        # Comprobar si el carácter tiene homóglifos
        if c.lower() in string.ascii_lowercase:
            homoglyphs.extend([c.upper(), c.lower()])
    return homoglyphs

# Función para obtener los posibles dominios parecidos
def typosquatting(domain):
    typos = []
    for i in range(len(domain)):
        # Sustituir cada carácter por un carácter parecido
        for c in string.ascii_lowercase:
            if c != domain[i].lower():
                typo = domain[:i] + c + domain[i+1:]
                typos.append(typo)
    return typos

# Solicitar el dominio al usuario
domain = input("Ingrese el dominio a comprobar: ")

# Obtener los posibles dominios homográficos
homoglyph_domains = homoglyphs(domain)

# Obtener los posibles dominios parecidos
typo_domains = typosquatting(domain)

# Obtener los dominios regionales

# Crear una lista para almacenar los resultados
results = []

# Comprobar si los dominios están activos
for d in tqdm(homoglyph_domains + typo_domains, desc="Progreso", unit="dominio"):  # Agregar tqdm para la barra de progreso
    try:
        ip = dns.resolver.resolve(d, 'A')[0].to_text()
        # Si se resuelve correctamente, agregar a la lista de resultados
        results.append([d, "Activo", ip])
    except:
        pass

# Mostrar los resultados en una tabla
table_headers = ["Dominio", "Estado", "Dirección IP"]
print(tabulate(results, headers=table_headers, tablefmt="grid"))





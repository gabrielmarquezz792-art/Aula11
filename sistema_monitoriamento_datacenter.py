import datetime
import hashlib
import os

def  avaliar_temperatura(temp: float) -> str:
    if temp < 20:
        return 'Frio'
    elif 40 > temp >= 20:
        return 'Ideal'
    elif 70 > temp >= 40:
        return 'Alerta'
    return 'Risco critíco'

def  avaliar_cpu(uso: float) -> str:
    if uso < 40:
        return 'Normal'
    elif 80 >= uso >= 40:
        return 'Alta'
    return 'Sobrecarga'

def avaliar_memoria(mem: float) -> str:
    if mem < 50:
        return 'Confortável'
    elif 85 > mem >= 50:
        return 'Monitorar'
    return 'Crítica'

def classificar_latencia(lat: float) -> str:
    if lat < 10:
        return 'Excelente'
    elif 40 > lat >= 10:
        return 'Boa'
    elif 100 > lat >= 40:
        return 'Regular'
    return 'Ruim'

def avaliar_disco(espaco_livre: float) -> str:
    if espaco_livre >= 40:
        return 'Seguro'
    elif 40 > espaco_livre >= 20:
        return 'Atenção'
    return 'Crítico'

# CORREÇÃO: a função estava usando a variável 'dias_restantes' sem calculá-la
def validar_certificado(data_emissao: str, anos: int) -> str:
    data = datetime.datetime.strptime(data_emissao, "%d/%m/%Y").date()
    validade = data.replace(year=data.year + anos)
    dias_restantes = (validade - datetime.date.today()).days

    if dias_restantes < 0:
        return 'Certificado expirado'
    elif dias_restantes <= 30:
        return 'Certificado expira em breve'
    return 'Certificado válido'


def prever_armazenamento(inicial: float, taxa: float = 0, anos: int = 0) -> tuple:
    armazenamento_final = inicial * ((1 + taxa / 100) ** anos)

    if armazenamento_final < 500:
        status = 'Seguro'
    elif armazenamento_final < 2000:
        status = 'Monitorar'
    else:
        status = 'Upgrade necessário'

    return armazenamento_final, status


def analisar_trafego(r1, r2=None, r3=None) -> tuple:
    if r2 is None and r3 is None:
        media = r1
    else:
        media = (r1 + r2 + r3) / 3

    if media < 100:
        status = 'Baixo tráfego'
    elif media < 500:
        status = 'Tráfego moderado'
    else:
        status = 'Tráfego alto'

    return media, status


def gerar_id_evento(nome_servidor: str, timestamp: str) -> str:
    texto = nome_servidor + timestamp
    return hashlib.sha256(texto.encode()).hexdigest()


def identificar_so(nome_so=None) -> str:
    if nome_so is None:
        nome_so = os.name

    if nome_so == 'nt':
        return 'Windows'
    elif nome_so == 'posix':
        return 'Linux/Unix'
    return 'Outro sistema'


# CORREÇÃO: condição era 'temp >= 70' mas o enunciado e o teste exigem 'temp > 70'
def avaliar_datacenter(temp=0, cpu=0, mem=0, lat=0, disco=100) -> str:
    if temp > 70 or cpu > 90 or mem > 90 or disco < 10:
        return 'Servidor crítico'

    if lat > 100 or temp > 40:
        return 'Servidor em alerta'

    return 'Servidor estável'
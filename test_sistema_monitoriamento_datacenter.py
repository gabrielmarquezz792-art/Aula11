import sistema_monitoriamento_datacenter as si
import datetime
import hashlib

#Item 1
def test_status_frio_temperatura():
    assert si.avaliar_temperatura(19.99) == 'Frio'

def test_status_ideal_temperatura():
    assert si.avaliar_temperatura(20) == 'Ideal'
    assert si.avaliar_temperatura(39.99) == 'Ideal'
    
def test_status_alerta_temperatura():
    assert si.avaliar_temperatura(40) == 'Alerta'
    assert si.avaliar_temperatura(69.99) == 'Alerta'

def test_status_risco_critico_temperatura():
    assert si.avaliar_temperatura(70) == 'Risco critíco'

#Item 2
def test_status_normal_avaliar_cpu():
    assert si.avaliar_cpu(39.99) == 'Normal'

def test_status_alta_avaliar_cpu():
    assert si.avaliar_cpu(40) == 'Alta'
    assert si.avaliar_cpu(80) == 'Alta'
    
def test_status_sobrecarga_avaliar_cpu():
    assert si.avaliar_cpu(80.01) == 'Sobrecarga'

#Item 3
def test_status_confortavel_avaliar_memoria():
    assert si.avaliar_memoria(49.99) == 'Confortável'
    
def test_status_monitorar_avaliar_memoria():
    assert si.avaliar_memoria(50) == 'Monitorar'
    assert si.avaliar_memoria(84.99) == 'Monitorar'
    
def test_status_critica_avaliar_memoria():
    assert si.avaliar_memoria(85) == 'Crítica'

#Item 4
def test_retorno_excelente_classificar_latencia():
    assert si.classificar_latencia(9.99) == 'Excelente'
    
def test_retorno_boa_classificar_latencia():
    assert si.classificar_latencia(10) == 'Boa'
    assert si.classificar_latencia(39.99) == 'Boa'

def test_retorno_regular_classificar_latencia():
    assert si.classificar_latencia(40) == 'Regular'
    assert si.classificar_latencia(99.99) == 'Regular'

def test_retorno_ruim_classificar_latencia():
    assert si.classificar_latencia(100) == 'Ruim'

#Item 5
def test_retorno_seguro_avaliar_disco():
    assert si.avaliar_disco(40) == 'Seguro'

def test_retorno_atencao_avaliar_disco():
    assert si.avaliar_disco(20) == 'Atenção'
    assert si.avaliar_disco(39.99) == 'Atenção'

def test_retorno_critico_avaliar_disco():
    assert si.avaliar_disco(19.99) == 'Crítico'

#Item 6
# CORREÇÃO: datetime.date recebe (ano, mês, dia), não (dia, mês, ano)
def test_retorno_certificado_expirado():
    data_emissao = datetime.date(2020, 1, 1)
    emissao_str = data_emissao.strftime("%d/%m/%Y")
    assert si.validar_certificado(emissao_str, 1) == "Certificado expirado"

def test_retorno_certificado_expira_brevemente():
    data_emissao = datetime.date(2025, 6, 12)
    emissao_str = data_emissao.strftime("%d/%m/%Y")
    assert si.validar_certificado(emissao_str, 1) == "Certificado expira em breve"
    
def test_retorno_certificado_valido():
    data_emissao = datetime.date(2025, 6, 12)
    emissao_str = data_emissao.strftime("%d/%m/%Y")
    assert si.validar_certificado(emissao_str, 2) == "Certificado válido"

#Item 7
# CORREÇÃO: prever_armazenamento retorna uma tupla (valor, status); o teste deve comparar a tupla
def test_status_seguro():
    armazenamento_final = 499.99
    _, status = si.prever_armazenamento(armazenamento_final)
    assert status == 'Seguro'
    
def test_status_monitorar_prever_armazenamento():
    _, status = si.prever_armazenamento(500)
    assert status == 'Monitorar'
    _, status = si.prever_armazenamento(1999.99)
    assert status == 'Monitorar'

def test_status_upgrade():
    _, status = si.prever_armazenamento(2000)
    assert status == 'Upgrade necessário'

#Item 8
# CORREÇÃO: analisar_trafego retorna uma tupla (media, status); o teste deve comparar a tupla
def test_status_baixo_trafego_analisar_trafego():
    _, status = si.analisar_trafego(99.99)
    assert status == 'Baixo tráfego'
    
def test_status_trafego_moderado_analisar_trafego():
    _, status = si.analisar_trafego(100)
    assert status == 'Tráfego moderado'
    _, status = si.analisar_trafego(499.99)
    assert status == 'Tráfego moderado'

def test_status_trafego_alto_analisar_trafego():
    _, status = si.analisar_trafego(500)
    assert status == 'Tráfego alto'
    
#Item 9
def test_gerar_hash_sha256_hexadecimal():
    nome = 'server01'
    timestamp = '2026-05-13 14:00'

    esperado = hashlib.sha256((nome + timestamp).encode()).hexdigest()
    assert si.gerar_id_evento(nome, timestamp) == esperado

#Item 10
def test_windows_identificar_so():
    assert si.identificar_so('nt') == 'Windows'
    
def test_linux_identificar_so():
    assert si.identificar_so('posix') == 'Linux/Unix'

def test_outro_valor_identificar_so():
    assert si.identificar_so('outro valor') == 'Outro sistema'

#Item 11
def test_servidor_critico_avaliar_datacenter():
    assert si.avaliar_datacenter(temp=70.01) == 'Servidor crítico'
    assert si.avaliar_datacenter(cpu=90.01) == 'Servidor crítico'
    assert si.avaliar_datacenter(mem=90.01) == 'Servidor crítico'
    assert si.avaliar_datacenter(disco=9.99) == 'Servidor crítico'

def test_servidor_critico_alerta_avaliar_datacenter():
    assert si.avaliar_datacenter(lat=100.01) == 'Servidor em alerta'
    assert si.avaliar_datacenter(temp=40.01) == 'Servidor em alerta'
    
def test_servidor_nenhuma_avaliar_datacenter():
    assert si.avaliar_datacenter(temp=30) == 'Servidor estável'
    assert si.avaliar_datacenter(cpu=90) == 'Servidor estável'
    assert si.avaliar_datacenter(mem=90) == 'Servidor estável'
    assert si.avaliar_datacenter(disco=10) == 'Servidor estável'
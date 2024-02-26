import streamlit as st
import pandas as pd
from api_receita import consulta_cnpj

def pageOperacional():
     ##############################################################################################################################################
     #INCLUINDO O LOGO DA EMPRESA
     # URL da imagem do site
     url_imagem = 'https://www.stangdistribuidora.com.br/static/media/LOGO_STANG.daa8c5bd.svg'

     # Exibir a imagem do site
     st.image(url_imagem, width=200)

     ##############################################################################################################################################
     #PRODUTO - TRANSPORTE OU OPERACIONAL
     st.subheader("Produto - RC Ambiental Operacional")

     st.write("---") #Pular Linha     

     st.subheader("QAR - Questionário de Avaliação de Risco")

     ##############################################################################################################################################
     #CRIA O DICIONÁRIO COM AS RELATIVIDADES DE OPERACIONAL
     ml_intercepto= {"chave": [1],
                    "modelo": ['rc_ambiental_operacional'],
                    "intercepto":[15041.96]}

     import_coef_uf  = {"chave": [1,1,1,1],
                    "UF_DESC_RSC":['PR','RS','SC','SP'],
                    "coef_uf":[0.989832206, 1.000000, 0.959944069, 0.939888138]}

     import_coef_bonus = {"chave": [1,1,1,1,1,1,1,1,1,1,1],
                         "BONUS": [0,1,2,3,4,5,6,7,8,9,10],
                         "coef_bonus":[0.998655, 0.989231, 0.979616, 0.968847, 0.958463, 0.948078, 0.938270, 1.000000, 0.929423, 0.919039, 0.909808,]}

     import_coef_tipseg = {"chave": [1,1,1],
                         "QAR_DESC_TIP_SEG": ['Novo', 'Renovação','Renovação Congênere'],
                         "coef_tipseg":[1.000000, 0.909505, 0.859752]}

     import_coef_tipempresa = {"chave": [1,1,1,1,1,1],
                              "QAR_DESC_TIP_EMPRESA": ['Empresa de Responsabilidade Limitada', 'Joint Venture', 'Outras', 'Parceira', 'Sociedade Anônima','Não Informado'],
                              "coef_tipempresa":[1.000000, 0.989579, 0.939158, 0.959368, 0.979789, 1.020000]}

     import_coef_LMI = {"chave": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    "LMI_OPERACIONAL": [ '1.000.000,00',  '2.000.000,00',  '3.000.000,00',  '4.000.000,00',  '5.000.000,00',  '6.000.000,00',  '7.000.000,00',  '8.000.000,00', '9.000.000,00',
                                             '10.000.000,00', '15.000.000,00', '20.000.000,00', '25.000.000,00', '30.000.000,00', '35.000.000,00', '40.000.000,00', '45.000.000,00', '50.000.000,00',
                                             '60.000.000,00', '70.000.000,00', '80.000.000,00', '90.000.000,00', '100.000.000,00'],
                    "coef_lmi":[1.055887, 1.076845, 1.034930, 1.048901, 1.000000, 1.052394, 1.013972, 1.066366, 1.059380, 1.027944, 1.010479, 1.041916, 1.069859, 1.017465,
                                   1.073352, 1.062873, 1.031437, 1.020958, 1.069859, 1.045408, 1.038423, 1.024451, 1.034930]}

     import_coef_tipTanque = {"chave": [1,1], "QAR_DESC_TIP_TANQUE": ['De Superfície', 'Subterrâneo'], "coef_tipTanque":[1.000000, 1.061210]}

     import_coef_matConstTubulacao = {"chave": [1,1,1,1,1,1,1],
                    "QAR_DESC_MAT_CONST_TUBULACAO": ['ASM. Material Sintético Aprovado',
                                                       'CPSA. Proteção Catódica por Anodo de Sacrifício ou por Corrente Impressa',
                                                       'DW. Parede Dupla',
                                                       'EPC. Revestimento Protetor Externo',
                                                       'F. Fibra de vidro',
                                                       'OED. Outros Materiais para Tubulação Aprovados pela EPA/DEP',
                                                       'S Aço'],
                    "coef_mat_const_tubulacao":[1.06529, 1.043527, 1.032645, 1.000000, 1.054408, 1.010882, 1.021763]}

     import_coef_matConstrucaoTanque = {"chave": [1,1,1,1,1,1,1,1,1,1,1,1,1],
               "QAR_DESC_MATERIAL_CONST_TANQUE": ['C. Concreto',
                                                  'CPIC. Proteção Catódica por Corrente Impressa',
                                                  'CPSA. Proteção Catódica por Anodo de Sacrifícii',
                                                  'DWDM. Parede Dupla (DW)-Material Duplo',
                                                  'DWPU. Tanque Subterrâneo DW sem Tubulação e com Contenção Secundária',
                                                  'DWSL. Revestimento Sintético DW na Construção do Tanque',
                                                  'DWSM. Parede Dupla (DW)-Um Só Material',
                                                  'F. Fibra de vidro',
                                                  'FCS. Aço Cladeado com Resina Epóxi Reforçada com Fibra de Vidro',
                                                  'ILS. Revestimento Interno do STI. STI-P3',
                                                  'OED. Outras soluções aprovadas pela EPA / DEP',
                                                  'P. Polietileno',
                                                  'S Aço'],
                    "coef_matConstrucaoTanque":[0.98954, 0.979671, 0.939211, 0.899474, 0.999803, 0.999277, 0.999934, 0.999637, 0.999605, 0.979342, 0.969408, 0.989737, 1.000000]}

     import_coef_conteudoTanque = {"chave": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               "QAR_DESC_CONTEUDO_TANQUE": ['AC. Composto de Amônia',
                                             'CC. Composto de Cloro',
                                             'D. Diesel',
                                             'FO. Óleo Combustível',
                                             'G. Gasolina com álcool',
                                             'GBO. Óleos Combustíveis Marítimos Graus 5 e 6',
                                             'GG. Gasolina Genérica',
                                             'HS. Substância Perigosa (Lei ambiental americana CERCLA)',
                                             'K. Querosene',
                                             'MA. Ácidos Minerais',
                                             'MPB. Produtos Diversos à Base de Petróleo',
                                             'O. Outros, Identificar',
                                             'P. Pesticida',
                                             'PBA Aditivo à base de petróleo',
                                             'UG Gasolina sem chumbo',
                                             'WO Óleo usado/descartável'],
          "coef_conteudoTanque":[1.007381, 1.018451, 1.003690, 1.015991, 1.004920, 1.006150, 1.001230, 1.012301, 1.013531, 1.011071, 1.002460, 1.017221, 1.000000, 1.098407, 1.086106, 1.024761]}

     import_coef_protTransbordamento = {"chave": [1,1,1,1,1,1,1],
          "QAR_DESC_PROTECAO_CONTRA_TRANSB":   ['BCV. Válvula Esférica de Retenção',
                                                  'FS. Registro de Corte da Vazão',
                                                  'LG. Indicadores de Nível, Alarmes de Nível Alto',
                                                  'OED. Outros Métodos de Proteção Aprovados pela EPA / DEP',
                                                  'SCB. Bacia de Contenção de Derramamentos',
                                                  'TF. Conexão Hermética',
                                                  'Não Existe'],
                    "coef_protTransbordamento":[0.999848, 0.999924, 1.000000, 0.999772, 0.999696, 0.999620, 1.050000]}

     import_coef_detectaVazTubulacao = {"chave": [1,1,1,1,1,1,1],
               "QAR_DESC_DETECTA_VAZ_TUBULACAO": ['ELL. Detector Eletrônico de Vazamento pela Linha com Bloqueio de Vazão',
                                                  'EM. Monitoramento Externo',
                                                  'IM. Monitoramento Intersticial - Filtro na Tubulação',
                                                  'IMDW. Monitoramento Intersticial de Tubulações de Paredes Duplas',
                                                  'MLL. Detector Mecânico de Vazamentos pela Linha',
                                                  'SP Válvula de Retenção da Bomba de Sucção',
                                                  'Não Existe'],
                    "coef_detectaVazTubulacao":[0.999789, 0.988945, 0.979367, 1.000000, 0.989156, 0.969578, 1.150000]}

     import_coef_detectaVazTanque = {"chave": [1,1,1,1,1,1,1,1,1,1,1,1,1],
               "QAR_DESC_DETECTA_VAZ_TANQUE": ['ATG. Sistema Automático de Indicadores de Tanque (Enterrado)',
                                             'ATT. Teste Anual de Estanqueidade com Inventário (Enterado)',
                                             'GMW. Poços de Monitoramento do Lençol Freático',
                                             'IM. Monitoramento Intersticial',
                                             'IMA. Monitoramento Intersticial do Fundo de Tanques Aéreos',
                                             'ISDW. Espaço Intersticial-Tanque de Parede Dupla',
                                             'MTG. Indicadores Manuais de Tanques-Enterrados',
                                             'OED. Outros Aprovados pela EPA / DEP',
                                             'SIR. Reconciliação Estatística do Inventário (Enterrados)',
                                             'SPA. Plano SPCC-Tanques Aéreos',
                                             'VIA. Inspeções Visuais de Sistemas Aéreos',
                                             'VMW. Poços de Monitoramento de Vapores',
                                             'Não Existe'],
                    "coef_detectaVazTanque":[0.999878, 0.999514, 0.999696, 0.999575, 0.999818, 0.999392, 1.000000, 0.999635, 0.999453, 0.999332, 0.999757, 0.999939, 1.150000]}

     import_coef_contencaoTanque = {"chave": [1,1,1,1],
               "QAR_DESC_BACIA_CONTENCAO_TANQUE_SUP": ['CSM. Concreto, Material Sintético, Argilas',
                                                       'DE. Poeira / Terra',
                                                       'OED. Outros Sistemas Secundários de Contenção Aprovados pela EPA / DEP',
                                                       'Não Existe'],
                              "coef_contencaoTanque": [1.000000, 0.999201, 0.968403, 1.150000]}

     import_coef_controleTanqueAereo = {"chave": [1,1], "QAR_DESC_CONTROLE_TANQUES_AEREO" : ['Sim', 'Não'], "coef_controleTanqueAereo" :[0.970000, 1.061107]}
     import_coef_brigadaIncendio     = {"chave": [1,1], "QAR_DESC_BRIGADA_INCENDIO"       : ['Sim', 'Não'], "coef_brigadaIncendio"     :[0.950000, 1.099846]}
     import_coef_sujeitoAlagamento   = {"chave": [1,1], "QAR_DESC_SUJEITO_ALAGAMENTO"     : ['Sim', 'Não'], "coef_sujeitoAlagamento"   :[1.035630, 1.000000]}
     import_coef_EteLocalRisco       = {"chave": [1,1], "QAR_DESC_ETE_LOCAL_RSC"          : ['Sim', 'Não'], "coef_EteLocalRisco"       :[0.989800, 1.000000]}
     import_coef_lodoEte             = {"chave": [1,1], "QAR_DESC_LODO_ETE"               : ['Sim', 'Não'], "coef_lodoEte"             :[1.029381, 1.000000]}
     import_coef_sinistroUltAno      = {"chave": [1,1], "QAR_DESC_SIN_ULTIMO_ANO"         : ['Sim', 'Não'], "coef_sinistroUltAno"      :[1.099916, 1.000000]}


     #LOADS DE AGRAVO/DESCONTO
     import_load_da              = {"chave": [1], "coef_load_DA":                     [1.250000]}
     import_load_do              = {"chave": [1], "coef_load_DO":                     [1.100000]}
     import_load_lucro           = {"chave": [1], "coef_load_lucro":                  [1.100000]}
     import_load_impostos        = {"chave": [1], "coef_load_impostos":               [1.350000]}
     import_load_ibnr            = {"chave": [1], "coef_load_ibnr":                   [1.030000]}
     import_load_tendencia       = {"chave": [1], "coef_load_tendencia":              [1.000000]}
     import_load_salvado         = {"chave": [1], "coef_load_salvado":                [1.000000]}
     import_load_ressarcimento   = {"chave": [1], "coef_load_ressarcimento":          [1.000000]}
     import_load_iof             = {"chave": [1], "coef_load_iof":                    [1.070000]}
     import_load_inflacaoSin     = {"chave": [1], "coef_load_inflacao_sinistro":      [1.000000]}
     import_load_sinistroJud     = {"chave": [1], "coef_load_sinistro_judicial":      [1.000000]}
     import_load_carregamentoSeg = {"chave": [1], "coef_load_carregamento_seguranca": [1.010000]}
     import_load_comCorretor     = {"chave": [1], "coef_load_comissao_corretor":      [1.010000]}
     import_load_franquia        = {"chave": [1], "coef_load_franquia":               [0.800000]}


     ##############################################################################################################################################
     #TRANSFORMA OS ARQUIVOS DO DICIONÁRIO EM DATAFRAME
     ml_intercepto                   = pd.DataFrame(ml_intercepto)
     import_coef_uf                  = pd.DataFrame(import_coef_uf)
     import_coef_tipseg              = pd.DataFrame(import_coef_tipseg)
     import_coef_bonus               = pd.DataFrame(import_coef_bonus)
     import_coef_LMI                 = pd.DataFrame(import_coef_LMI)
     import_coef_tipempresa          = pd.DataFrame(import_coef_tipempresa)
     import_coef_tipTanque           = pd.DataFrame(import_coef_tipTanque)
     import_coef_matConstTubulacao   = pd.DataFrame(import_coef_matConstTubulacao)
     import_coef_matConstrucaoTanque = pd.DataFrame(import_coef_matConstrucaoTanque)
     import_coef_conteudoTanque      = pd.DataFrame(import_coef_conteudoTanque)
     import_coef_protTransbordamento = pd.DataFrame(import_coef_protTransbordamento)
     import_coef_detectaVazTubulacao = pd.DataFrame(import_coef_detectaVazTubulacao)
     import_coef_detectaVazTanque    = pd.DataFrame(import_coef_detectaVazTanque)
     import_coef_contencaoTanque     = pd.DataFrame(import_coef_contencaoTanque)
     import_coef_controleTanqueAereo = pd.DataFrame(import_coef_controleTanqueAereo)
     import_coef_brigadaIncendio     = pd.DataFrame(import_coef_brigadaIncendio)
     import_coef_sujeitoAlagamento   = pd.DataFrame(import_coef_sujeitoAlagamento)
     import_coef_EteLocalRisco       = pd.DataFrame(import_coef_EteLocalRisco)
     import_coef_lodoEte             = pd.DataFrame(import_coef_lodoEte)
     import_coef_sinistroUltAno      = pd.DataFrame(import_coef_sinistroUltAno)

     import_load_da              = pd.DataFrame(import_load_da)
     import_load_do              = pd.DataFrame(import_load_do)
     import_load_lucro           = pd.DataFrame(import_load_lucro)
     import_load_impostos        = pd.DataFrame(import_load_impostos)
     import_load_ibnr            = pd.DataFrame(import_load_ibnr)
     import_load_tendencia       = pd.DataFrame(import_load_tendencia)
     import_load_salvado         = pd.DataFrame(import_load_salvado)
     import_load_ressarcimento   = pd.DataFrame(import_load_ressarcimento)
     import_load_iof             = pd.DataFrame(import_load_iof)
     import_load_inflacaoSin     = pd.DataFrame(import_load_inflacaoSin)
     import_load_sinistroJud     = pd.DataFrame(import_load_sinistroJud)
     import_load_carregamentoSeg = pd.DataFrame(import_load_carregamentoSeg)
     import_load_comCorretor     = pd.DataFrame(import_load_comCorretor)
     import_load_franquia        = pd.DataFrame(import_load_franquia)


     ##############################################################################################################################################
     #INICIO DO QAR-QUESTIONÁRIO DE AVALIAÇÃO DE RISCO - OPERACIONAL
     #st.subheader("Tipo de Seguro")
     distinct_tipseg = import_coef_tipseg['QAR_DESC_TIP_SEG'].unique().tolist()
     response_tipseg= st.selectbox('Qual o Tipo de Seguro?',distinct_tipseg, index=None, placeholder="Selecione uma Opção")
     coef_tipseg = import_coef_tipseg[import_coef_tipseg['QAR_DESC_TIP_SEG']==response_tipseg]

     #st.subheader("Selecione o Tipo de Empresa")
     distinct_tipempresa = import_coef_tipempresa['QAR_DESC_TIP_EMPRESA'].unique().tolist()
     response_tipempresa= st.selectbox('Selecione o Tipo de Empresa',distinct_tipempresa, index=None, placeholder="Selecione uma Opção")
     coef_tipempresa = import_coef_tipempresa[import_coef_tipempresa['QAR_DESC_TIP_EMPRESA']==response_tipempresa]

     #st.subheader("Selecione a UF")
     distinct_uf = import_coef_uf['UF_DESC_RSC'].unique().tolist()
     response_uf= st.selectbox('UF do Risco',distinct_uf, index=None, placeholder="Selecione uma Opção")
     coef_uf = import_coef_uf[import_coef_uf['UF_DESC_RSC']==response_uf]

     #st.subheader("Selecione a Classe de Bônus")
     distinct_BONUS = import_coef_bonus['BONUS'].unique().tolist()
     response_bonus= st.selectbox('Classe de Bônus',distinct_BONUS, index=None, placeholder="Selecione uma Opção")
     coef_bonus = import_coef_bonus[import_coef_bonus['BONUS']==response_bonus]

     #st.subheader("Limite Maxímo de Indenização")
     distinct_LMItransp = import_coef_LMI['LMI_OPERACIONAL'].unique().tolist()
     response_LMI = st.selectbox('LMI',distinct_LMItransp, index=None, placeholder="Selecione uma Opção")
     coef_LMI = import_coef_LMI[import_coef_LMI['LMI_OPERACIONAL']==response_LMI]

     #st.subheader("Tipo de Tanque")
     distinct_tipTanque = import_coef_tipTanque['QAR_DESC_TIP_TANQUE'].unique().tolist()
     response_tipTanque= st.selectbox('Tipo de Tanque',distinct_tipTanque, index=None, placeholder="Selecione uma Opção")
     coef_tipTanque = import_coef_tipTanque[import_coef_tipTanque['QAR_DESC_TIP_TANQUE']==response_tipTanque]

     #st.subheader("Material De Construção Da Tubulação")
     distinct_matConstTubulacao = import_coef_matConstTubulacao['QAR_DESC_MAT_CONST_TUBULACAO'].unique().tolist()
     response_matConstTubulacao= st.selectbox('Material De Construção Da Tubulação',distinct_matConstTubulacao, index=None, placeholder="Selecione uma Opção")
     coef_matConstTubulacao = import_coef_matConstTubulacao[import_coef_matConstTubulacao['QAR_DESC_MAT_CONST_TUBULACAO']==response_matConstTubulacao]

     #st.subheader("Material De Construção Do Tanque")
     distinct_matConstrucaoTanque = import_coef_matConstrucaoTanque['QAR_DESC_MATERIAL_CONST_TANQUE'].unique().tolist()
     response_matConstrucaoTanque= st.selectbox('Material De Construção Do Tanque',distinct_matConstrucaoTanque, index=None, placeholder="Selecione uma Opção")
     coef_matConstrucaoTanque = import_coef_matConstrucaoTanque[import_coef_matConstrucaoTanque['QAR_DESC_MATERIAL_CONST_TANQUE']==response_matConstrucaoTanque]

     #st.subheader("Conteudo do Tanque")
     distinct_conteudoTanque = import_coef_conteudoTanque['QAR_DESC_CONTEUDO_TANQUE'].unique().tolist()
     response_conteudoTanque= st.selectbox('Conteudo do Tanque',distinct_conteudoTanque, index=None, placeholder="Selecione uma Opção")
     coef_conteudoTanque = import_coef_conteudoTanque[import_coef_conteudoTanque['QAR_DESC_CONTEUDO_TANQUE']==response_conteudoTanque]

     #st.subheader("Proteção Contra Transbordamento / Derramamento")
     distinct_protTransbordamento = import_coef_protTransbordamento['QAR_DESC_PROTECAO_CONTRA_TRANSB'].unique().tolist()
     response_protTransbordamento= st.selectbox('Extiste Proteção Contra Transbordamento / Derramamento?',distinct_protTransbordamento, index=None, placeholder="Selecione uma Opção")
     coef_protTransbordamento = import_coef_protTransbordamento[import_coef_protTransbordamento['QAR_DESC_PROTECAO_CONTRA_TRANSB']==response_protTransbordamento]

     #st.subheader("Tem Detecção De Vazamento Pela Tubulação")
     distinct_detectaVazTubulacao = import_coef_detectaVazTubulacao['QAR_DESC_DETECTA_VAZ_TUBULACAO'].unique().tolist()
     response_detectaVazTubulacao= st.selectbox('Tem Detecção De Vazamento Pela Tubulação?',distinct_detectaVazTubulacao, index=None, placeholder="Selecione uma Opção")
     coef_detectaVazTubulacao = import_coef_detectaVazTubulacao[import_coef_detectaVazTubulacao['QAR_DESC_DETECTA_VAZ_TUBULACAO']==response_detectaVazTubulacao]

     #st.subheader("Tem Detecção De Vazamentos Do Tanque")
     distinct_detectaVazTanque = import_coef_detectaVazTanque['QAR_DESC_DETECTA_VAZ_TANQUE'].unique().tolist()
     response_detectaVazTanque= st.selectbox('Tem Detecção De Vazamentos Do Tanque?',distinct_detectaVazTanque, index=None, placeholder="Selecione uma Opção")
     coef_detectaVazTanque = import_coef_detectaVazTanque[import_coef_detectaVazTanque['QAR_DESC_DETECTA_VAZ_TANQUE']==response_detectaVazTanque]

     #st.subheader("Construção De Bacia De Contenção E Base Para Tanque De Superfície")
     distinct_contencaoTanque = import_coef_contencaoTanque['QAR_DESC_BACIA_CONTENCAO_TANQUE_SUP'].unique().tolist()
     response_contencaoTanque= st.selectbox('Construção De Bacia De Contenção E Base Para Tanque De Superfície',distinct_contencaoTanque, index=None, placeholder="Selecione uma Opção")
     coef_contencaoTanque = import_coef_contencaoTanque[import_coef_contencaoTanque['QAR_DESC_BACIA_CONTENCAO_TANQUE_SUP']==response_contencaoTanque]

     #st.subheader("Exite Controle dos Tanques Áereo?")
     distinct_controleTanqueAereo = import_coef_controleTanqueAereo['QAR_DESC_CONTROLE_TANQUES_AEREO'].unique().tolist()
     response_controleTanqueAereo= st.selectbox('Exite Controle dos Tanques Áereo?',distinct_controleTanqueAereo, index=None, placeholder="Selecione uma Opção")
     coef_controleTanqueAereo = import_coef_controleTanqueAereo[import_coef_controleTanqueAereo['QAR_DESC_CONTROLE_TANQUES_AEREO']==response_controleTanqueAereo]

     #st.subheader("Brigada de Incêndio")
     distinct_brigadaIncendio = import_coef_brigadaIncendio['QAR_DESC_BRIGADA_INCENDIO'].unique().tolist()
     response_brigadaIncendio= st.selectbox('Existe Brigada de Incêndio?',distinct_brigadaIncendio, index=None, placeholder="Selecione uma Opção")
     coef_brigadaIncendio = import_coef_brigadaIncendio[import_coef_brigadaIncendio['QAR_DESC_BRIGADA_INCENDIO']==response_brigadaIncendio]

     #st.subheader("Área Sujeito a Alagamento")
     distinct_sujeitoAlagamento = import_coef_sujeitoAlagamento['QAR_DESC_SUJEITO_ALAGAMENTO'].unique().tolist()
     response_sujeitoAlagamento= st.selectbox('Área Sujeito a Alagamento?',distinct_sujeitoAlagamento, index=None, placeholder="Selecione uma Opção")
     coef_sujeitoAlagamento = import_coef_sujeitoAlagamento[import_coef_sujeitoAlagamento['QAR_DESC_SUJEITO_ALAGAMENTO']==response_sujeitoAlagamento]

     #st.subheader("ETE (Estação Tratamento Efluentes)")
     distinct_EteLocalRisco = import_coef_EteLocalRisco['QAR_DESC_ETE_LOCAL_RSC'].unique().tolist()
     response_EteLocalRisco= st.selectbox('Há ETE no local de risco? (ETE-Estação Tratamento Efluentes)',distinct_EteLocalRisco, index=None, placeholder="Selecione uma Opção")
     coef_EteLocalRisco = import_coef_EteLocalRisco[import_coef_EteLocalRisco['QAR_DESC_ETE_LOCAL_RSC']==response_EteLocalRisco]

     #st.subheader("Há Lodo ETE?")
     distinct_lodoEte = import_coef_lodoEte['QAR_DESC_LODO_ETE'].unique().tolist()
     response_lodoEte= st.selectbox('Há Lodo ETE? (ETE-Estação Tratamento Efluentes)',distinct_lodoEte, index=None, placeholder="Selecione uma Opção")
     coef_lodoEte = import_coef_lodoEte[import_coef_lodoEte['QAR_DESC_LODO_ETE']==response_lodoEte]

     #st.subheader("Ouve Sinistro no último Ano?")
     distinct_sinistroUltAno = import_coef_sinistroUltAno['QAR_DESC_SIN_ULTIMO_ANO'].unique().tolist()
     response_sinistroUltAno= st.selectbox('Ouve Sinistro no Último Ano ?',distinct_sinistroUltAno, index=None, placeholder="Selecione uma Opção")
     coef_sinistroUltAno = import_coef_sinistroUltAno[import_coef_sinistroUltAno['QAR_DESC_SIN_ULTIMO_ANO']==response_sinistroUltAno]

     ##############################################################################################################################################
     #FAZ O MERGE DAS TABELAS QAR COM INTERCEPTO 
     ml_1 = pd.merge(ml_intercepto, coef_tipseg,       on='chave', how='left')

     ml_1 = pd.merge(ml_1,  coef_tipempresa,           on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_uf,                   on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_LMI,                  on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_bonus,                on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_tipTanque,            on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_matConstTubulacao,    on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_matConstrucaoTanque,  on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_conteudoTanque,       on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_protTransbordamento,  on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_detectaVazTubulacao,  on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_detectaVazTanque,     on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_contencaoTanque,      on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_controleTanqueAereo,  on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_brigadaIncendio,      on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_sujeitoAlagamento,    on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_EteLocalRisco,        on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_lodoEte,              on='chave', how='left')
     ml_1 = pd.merge(ml_1,  coef_sinistroUltAno,       on='chave', how='left')

     # MERGE DOS LOADS DE CARREGAMENTO
     ml_1 = pd.merge(ml_1, import_load_da,              on='chave', how='left')
     ml_1 = pd.merge(ml_1, import_load_do,              on='chave', how='left')
     ml_1 = pd.merge(ml_1, import_load_lucro,           on='chave', how='left')
     ml_1 = pd.merge(ml_1, import_load_impostos,        on='chave', how='left')
     ml_1 = pd.merge(ml_1, import_load_ibnr,            on='chave', how='left')
     ml_1 = pd.merge(ml_1, import_load_tendencia,       on='chave', how='left')
     ml_1 = pd.merge(ml_1, import_load_salvado,         on='chave', how='left')
     ml_1 = pd.merge(ml_1, import_load_ressarcimento,   on='chave', how='left')
     ml_1 = pd.merge(ml_1, import_load_iof,             on='chave', how='left')
     ml_1 = pd.merge(ml_1, import_load_inflacaoSin,     on='chave', how='left')
     ml_1 = pd.merge(ml_1, import_load_sinistroJud,     on='chave', how='left')
     ml_1 = pd.merge(ml_1, import_load_carregamentoSeg, on='chave', how='left')
     ml_1 = pd.merge(ml_1, import_load_comCorretor,     on='chave', how='left')
     ml_1 = pd.merge(ml_1, import_load_franquia,        on='chave', how='left')


     ##############################################################################################################################################
     #CALCULO DAS RELATIVIDADES DO QAR OPERACIONAL E INTERCEPTO DA MODELAGEM  - PRÊMIO DE RISCO SEM CARREGAMENTOS

     ml_1['prRisco_0'] = ml_1['intercepto']*ml_1['coef_tipseg']*ml_1['coef_tipempresa']*ml_1['coef_uf']*ml_1['coef_tipTanque']*ml_1['coef_mat_const_tubulacao']*ml_1['coef_matConstrucaoTanque']*ml_1['coef_lmi']*ml_1['coef_conteudoTanque']*ml_1['coef_protTransbordamento']*ml_1['coef_detectaVazTubulacao']*ml_1['coef_detectaVazTanque']*ml_1['coef_contencaoTanque']*ml_1['coef_controleTanqueAereo']*ml_1['coef_brigadaIncendio']*ml_1['coef_sujeitoAlagamento']*ml_1['coef_EteLocalRisco']*ml_1['coef_lodoEte']*ml_1['coef_sinistroUltAno']*ml_1['coef_bonus']*ml_1['coef_load_franquia']
     pr_risco = pd.DataFrame(ml_1)

     #PRÊMIO DE RISCO COM A INCLUSÃO DOS LOAD'S "INFLAÇÃO DE SINISTRO" - "TENDENCIA" e "IBNR" - CARREGAMENTO 01
     pr_risco['prRisco_1'] = pr_risco['prRisco_0']*pr_risco['coef_load_inflacao_sinistro']*pr_risco['coef_load_tendencia']*pr_risco['coef_load_ibnr']

     #PRÊMIO DE RISCO COM A INCLUSÃO DOS LOAD'S - "SALVADO" e "RESSARCIMENTO" - "SINISTRO JUDICIAL" - CARREGAMENTO 02
     pr_risco['prRisco_2'] = pr_risco['prRisco_1']*pr_risco['coef_load_salvado']*pr_risco['coef_load_ressarcimento']*pr_risco['coef_load_sinistro_judicial']

     ##############################################################################################################################################
     #PRÊMIO PURO COM A INCLUSÃO DO LOAD "INFLAÇÃO DE SINISTRO" - "CARREGAMENTO DE SEGURANÇA" - CARREGAMENTO 03
     pr_puro = pd.DataFrame(pr_risco)
     pr_puro['prPuro'] = pr_puro['prRisco_2']*pr_puro['coef_load_carregamento_seguranca']


     ##############################################################################################################################################
     #PRÊMIO LIQUIDO COM A INCLUSÃO DOS LOADS "COMISSÃO" - "DO" - "DA" - "IMPOSTOS" - "LUCRO" - (OBS: COMISSÃO ESTÁ FULL EM 1%)
     pr_liquido = pd.DataFrame(pr_puro)
     pr_liquido['prLiquido'] = pr_liquido['prPuro']*pr_liquido['coef_load_comissao_corretor']*pr_liquido['coef_load_DO']*pr_liquido['coef_load_DA']*pr_liquido['coef_load_impostos']*pr_liquido['coef_load_lucro']

     #print(pr_liquido)

     ##############################################################################################################################################
     #PRÊMIO TOTAL COM INCLUSÃO DO "IOF"
     pr_total = pd.DataFrame(pr_liquido)
     pr_total['prTotal'] = pr_total['prLiquido']*pr_total['coef_load_carregamento_seguranca']

     #SELECIONA APENAS O PRÊMIO FINAL
     pr_total = (pr_total['prTotal'])

     st.write("---") #Pular Linha    

     #print(pr_total)

     ##############################################################################################################################################
     #DADOS DO SEGURADO
     st.subheader("Dados do Segurado")

     cnpj = st.text_input(label='Digite o CNPJ do Segurado')
     st.markdown('**Digite o CNPJ e clique em Calcular**')
     st.markdown('OBS: Esta consulta permite 3 CNPJ por minuto (**API Pública**)')
     st.markdown('Caso ocorra algum erro, por favor, aguarde 1 minuto para calcular.')

     if cnpj == '':
          st.subheader('')
     else: 
          campos = consulta_cnpj(cnpj)

          col1, col2 = st.columns(2)
          with col2:st.write("**Situação:**",campos[0])
          with col1:st.write("**Nome Segurado:**",campos[1])

          col11, col12, col13 = st.columns(3)
          with col11:st.write("**Porte:**",campos[2])
          with col12:st.write("**Logradouro:**",campos[3])
          with col13:st.write("**Número:**",campos[4])

          col21, col22, col23, col24 = st.columns(4)
          with col21:st.write("**Municipio:**",campos[5])
          with col22:st.write("**Bairro:**",campos[6])
          with col23:st.write("**UF:**",campos[7])
          with col24:st.write("**CEP:**",campos[8].replace('.','').replace('-','').replace(')',''))

          col31, col32, col33 = st.columns(3)
          with col31:st.write("**E-mail:**",campos[9])
          with col32:st.write("**Telefone:**",campos[10])
          with col33:st.write("**Status:**",campos[11])

     st.write("---") #Pular Linha    


     ##############################################################################################################################################
     #DADOS DO CORRETOR
     st.subheader("Dados do Corretor")
     st.markdown('Código-23867')
     st.markdown('Nome: LOJACORR S/A REDE DE CORRETORES DE SEGUROS')
     #load_comissao = st.number_input('Comissão do Corretor', min_value=0, max_value=50)

     st.write("---") #Pular Linha    

     ##############################################################################################################################################
     #FORMATAR VALOR
     with pd.option_context('display.float_format','R$ {:_.2f}'.format):
          
          #Retirando o Indice do arquivo de Risco
          serie = pr_total.to_string(index=False) 

     serie = serie.replace(".",",").replace("_",".")

     #print(serie)


     ##############################################################################################################################################
     #BOTÃO CALCULAR
     if st.button("Calcular"):
          st.write("**Prêmio Total (Com Carregamentos)**",serie)
          st.write("---") #Pular Linha   
          st.subheader("Carregamentos:")

     ##############################################################################################################################################
     #MOSTRAR CARREGAMENTOS NO MOTOR
          import_load_da              = ((import_load_da              ['coef_load_DA']-1)*100)
          import_load_do              = ((import_load_do              ['coef_load_DO']-1)*100)
          import_load_lucro           = ((import_load_lucro           ['coef_load_lucro']-1)*100)
          import_load_impostos        = ((import_load_impostos        ['coef_load_impostos']-1)*100)
          import_load_ibnr            = ((import_load_ibnr            ['coef_load_ibnr']-1)*100)
          import_load_iof             = ((import_load_iof             ['coef_load_iof']-1)*100)
          import_load_carregamentoSeg = ((import_load_carregamentoSeg ['coef_load_carregamento_seguranca']-1)*100)
          import_load_comCorretor     = ((import_load_comCorretor     ['coef_load_comissao_corretor']-1)*100)
          import_load_franquia        = ((import_load_franquia        ['coef_load_franquia']-1)*100)

          import_load_da              = import_load_da.to_string(index=False) 
          import_load_do              = import_load_do.to_string(index=False) 
          import_load_lucro           = import_load_lucro.to_string(index=False) 
          import_load_impostos        = import_load_impostos.to_string(index=False) 
          import_load_ibnr            = import_load_ibnr.to_string(index=False) 
          import_load_iof             = import_load_iof.to_string(index=False) 
          import_load_carregamentoSeg = import_load_carregamentoSeg.to_string(index=False) 
          import_load_comCorretor     = import_load_comCorretor.to_string(index=False) 
          import_load_franquia        = import_load_franquia.to_string(index=False)

          st.write("**Despesa Administrativa:**",      import_load_da,"%")
          st.write("**Despesa Operacional:**",         import_load_do,"%")
          st.write("**Lucro:**",                       import_load_lucro,"%")
          st.write("**Impostos:**",                    import_load_impostos,"%")
          st.write("**IBNR:**",                        import_load_ibnr,"%")
          st.write("**IOF:**",                         import_load_iof,"%")
          st.write("**Carregamento de Segurança:**",   import_load_carregamentoSeg,"%")
          st.write("**Comissão do Corretor (FULL):**", import_load_comCorretor,"%")
          #st.write("**Franquia:**",                   import_load_franquia,"%")
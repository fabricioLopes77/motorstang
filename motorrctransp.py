import streamlit as st
import pandas as pd
from api_receita import consulta_cnpj

def pageTransporte():
     ##############################################################################################################################################
     #INCLUINDO O LOGO DA EMPRESA
     # URL da imagem do site
     url_imagem = 'https://www.stangdistribuidora.com.br/static/media/LOGO_STANG.daa8c5bd.svg'

     # Exibir a imagem do site
     st.image(url_imagem, width=200)

     ##############################################################################################################################################
     #PRODUTO - TRANSPORTE OU OPERACIONAL
     st.subheader("Produto - RC Ambiental Transporte")

     st.write("---") #Pular Linha     

     st.subheader("QAR - Questionário de Avaliação de Risco")

     ##############################################################################################################################################
     #CRIA O DICIONÁRIO COM AS RELATIVIDADES DE TRANSPORTE
     ml_intercepto = {"chave": [1],
                    "modelo": ['rc_ambiental_transpote'],
                    "intercepto":[22.69]}

     import_coef_uf  = {"chave": [1,1,1,1],
                    "UF_DESC_RSC":['RS', 'SC', 'SP', 'PR'],
                    "coef_uf":[1.000000, 1.001733, 1.003466, 1.005200]}

     import_coef_bonus = {"chave": [1,1,1,1,1,1,1,1,1,1,1],
                         "BONUS": [0,1,2,3,4,5,6,7,8,9,10],
                         "coef_bonus":[1.000000, 0.935427, 0.870853, 0.80628, 0.741707, 0.677134, 0.61256, 0.547987, 0.483414, 0.418841, 0.354267]}

     import_coef_tipseg = {"chave": [1,1,1],
                         "QAR_DESC_TIP_SEG": ['Novo', 'Renovação','Renovação Congênere'],
                         "coef_tipseg":[1.000000, 0.991833, 0.983666]}

     import_coef_tipempresa = {"chave": [1,1,1,1,1,1],
                              "QAR_DESC_TIP_EMPRESA": ['Empresa de Responsabilidade Limitada', 'Joint Venture', 'Outras', 'Parceira', 'Sociedade Anônima','Não Informado'],
                              "coef_tipempresa":[1.000000, 0.977743, 0.985162, 0.970324, 0.992581, 1.020000]}

     import_coef_LMI = {"chave": [1,1,1,1,1,1,1,1,1,1,],
                    "LMI_TRANSP": ['100.000,00', '200.000,00','300.000,00','400.000,00','500.000,00','600.000,00','700.000,00','800.000,00','900.000,00','1.000.000,00'],
                    "coef_lmi":[1.000000, 1.150803, 1.301605, 1.452408, 1.60321, 1.754013, 1.904815, 2.055618, 2.206421, 2.357223]}

     import_coefprod_perig = {"chave": [1,1],
                              "QAR_DESC_CLASSIF_PROD_PERIGOSO": ['Sim', 'Não'],
                              "coef_prodperigoso":[1.000000, 1.014716]}

     import_coef_classeprod = {"chave": [1,1,1,1,1,1,1,1,1,1],
                              "QAR_DESC_CLASSE_PRODUTO": ['Classe 1 - Explosivos',
                                                       'Classe 2 - Gases',
                                                       'Classe 3 - Líquidos Inflamáveis',
                                                       'Classe 4 - Sólidos Inflamáveis, Substâncias Sujeitas A Combustão Espontânea, Substâncias Que, Em Contato Com Água, Emitem Gases Inflamáveis',
                                                       'Classe 5 - Substâncias Oxidantes E Peróxidos Orgânicos',
                                                       'Classe 6 - Substâncias Tóxicas E Substâncias Infectantes',
                                                       'Classe 7 - Materiais Radioativos',
                                                       'Classe 8 - Substâncias Corrosivas',
                                                       'Classe 9 - Substâncias E Artigos Perigosos Diversos',
                                                       'Substâncias Não Classificadas Acima Que Tenham Potencial De Causar Dano Ou Risco À Saúde ou Meio Ambiente'],
                              "coef_classeprod":[1.896927, 1.448464, 1.000000, 1.149488, 1.3086123, 1.747440, 2.046415, 1.597952, 1.298976, 2.195903]}

     import_coef_perfmotorista = {"chave": [1,1,1,1],
                              "QAR_DESC_PERFIL_MOTORISTA": ['Transportadora','Agregado','Frota Própria','Autônomo'],
                              "coef_perfmotorista":[1.000000, 0.998907, 0.997813, 0.99672]}

     import_coef_modais = {"chave": [1,1,1],
                         "QAR_DESC_MODAIS_UTILIZADO": ['Rodoviário','Rodo-Fluvial','Cabotagem'],
                         "coef_modais":[1.000000, 0.955996, 0.911992]}

     import_coef_certificacao = {"chave": [1,1,1,1,1,1],
                              "QAR_DESC_CERTIFICACOES": ['Certificação ISSO 14.0001',
                                                            'Certificação Mopp Para Motoristas',
                                                            'Certificação Prodir -Associquim',
                                                            'Certificação Sassmaq - Abiquim',
                                                            'Programa De Gerenciamento De Risco',
                                                            'Não Possui'],
                              "coef_certificacao":[0.99324, 0.97296, 1.000000, 0.97972, 0.98648, 1.100000]}

     import_coef_emergencia = {"chave": [1,1,1,1,1,1],
                              "QAR_DESC_PLANO_EMERGENCIA": ['Geo Ambiental', 'ATMO HAZMAT', 'SUATRANS - COTEC' ,'WGRA', 'Outras', 'Não Possui'],
                              "coef_emergencia":[1.000000, 1.006025, 1.012050, 1.018075, 1.024100, 1.100000]}

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
     ml_intercepto             = pd.DataFrame(ml_intercepto)
     import_coef_uf            = pd.DataFrame(import_coef_uf)
     import_coef_tipseg        = pd.DataFrame(import_coef_tipseg)
     import_coef_bonus         = pd.DataFrame(import_coef_bonus)
     import_coef_LMI           = pd.DataFrame(import_coef_LMI)
     import_coefprod_perig     = pd.DataFrame(import_coefprod_perig)
     import_coef_tipempresa    = pd.DataFrame(import_coef_tipempresa)
     import_coef_classeprod    = pd.DataFrame(import_coef_classeprod)
     import_coef_modais        = pd.DataFrame(import_coef_modais)
     import_coef_perfmotorista = pd.DataFrame(import_coef_perfmotorista)
     import_coef_certificacao  = pd.DataFrame(import_coef_certificacao)
     import_coef_emergencia    = pd.DataFrame(import_coef_emergencia)

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
     #INICIO DO QAR-QUESTIONÁRIO DE AVALIAÇÃO DE RISCO - TRANSPORTE
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
     response_uf= st.selectbox('UF de Circulação da Carga',distinct_uf, index=None, placeholder="Selecione uma Opção")
     coef_uf = import_coef_uf[import_coef_uf['UF_DESC_RSC']==response_uf]

     #st.subheader("Selecione a Classe de Bônus")
     distinct_BONUS = import_coef_bonus['BONUS'].unique().tolist()
     response_bonus= st.selectbox('Classe de Bônus',distinct_BONUS, index=None, placeholder="Selecione uma Opção")
     coef_bonus = import_coef_bonus[import_coef_bonus['BONUS']==response_bonus]

     #st.subheader("Limite Maxímo de Indenização")
     distinct_LMItransp = import_coef_LMI['LMI_TRANSP'].unique().tolist()
     response_LMI = st.selectbox('LMI',distinct_LMItransp, index=None, placeholder="Selecione uma Opção")
     coef_LMI = import_coef_LMI[import_coef_LMI['LMI_TRANSP']==response_LMI]

     #st.subheader("Informações de Embarques")
     distinct_prodPerig = import_coefprod_perig['QAR_DESC_CLASSIF_PROD_PERIGOSO'].unique().tolist()
     response_prod_perig  = st.selectbox('Produto Classificado como Perigosos',distinct_prodPerig, index=None, placeholder="Selecione uma Opção")
     coef_prod_perig = import_coefprod_perig[import_coefprod_perig['QAR_DESC_CLASSIF_PROD_PERIGOSO']==response_prod_perig]

     #st.write("---") #Pular Linha
     #st.subheader("Valor Embarcado por Viagem")
     #response_vlrEmbarque = st.number_input('Valor Embarcado Por Viagem R$', min_value=0.00) 
     #st.write("---") #Pular Linha

     #st.subheader("Quantidade de Embarques")
     qtdEmbarque = st.number_input('Quantidade de Embarques por Mês', min_value=0)

     #st.subheader("Classe dos Produtos")
     distinct_classeProd = import_coef_classeprod['QAR_DESC_CLASSE_PRODUTO'].unique().tolist()
     response_classeProd= st.selectbox('Tipo de Classe',distinct_classeProd, index=None, placeholder="Selecione uma Opção")
     coef_classeprod = import_coef_classeprod[import_coef_classeprod['QAR_DESC_CLASSE_PRODUTO']==response_classeProd]

     #st.subheader("Perfil do Motorista")
     distinct_perfmotorista = import_coef_perfmotorista['QAR_DESC_PERFIL_MOTORISTA'].unique().tolist()
     response_perfmotorista= st.selectbox('Perfil',distinct_perfmotorista, index=None, placeholder="Selecione uma Opção")
     coef_perfmotorista = import_coef_perfmotorista[import_coef_perfmotorista['QAR_DESC_PERFIL_MOTORISTA']==response_perfmotorista]

     #st.subheader("Modais Utilizados")
     distinct_modais = import_coef_modais['QAR_DESC_MODAIS_UTILIZADO'].unique().tolist()
     response_modais = st.selectbox('Tipo de Transporte',distinct_modais, index=None, placeholder="Selecione uma Opção")
     coef_modais = import_coef_modais[import_coef_modais['QAR_DESC_MODAIS_UTILIZADO']==response_modais]

     #st.subheader("Certificações")
     distinct_certificacao = import_coef_certificacao['QAR_DESC_CERTIFICACOES'].unique().tolist()
     response_certificacao= st.selectbox('O Cliente Possui alguma Certificação?',distinct_certificacao, index=None, placeholder="Selecione uma Opção")
     coef_certificacao = import_coef_certificacao[import_coef_certificacao['QAR_DESC_CERTIFICACOES']==response_certificacao]

     #st.subheader("Plano de Atendimento a Emergências")
     distinct_emergencia = import_coef_emergencia['QAR_DESC_PLANO_EMERGENCIA'].unique().tolist()
     response_emergencia= st.selectbox('O Segurado Possui Plano de Atendimento a Emergências-PAE?',distinct_emergencia, index=None, placeholder="Selecione uma Opção")
     coef_emergencia = import_coef_emergencia[import_coef_emergencia['QAR_DESC_PLANO_EMERGENCIA']==response_emergencia]


     ##############################################################################################################################################
     #FAZ O MERGE DAS TABELAS QAR COM INTERCEPTO 
     ml_1 = pd.merge(ml_intercepto, coef_tipseg,        on='chave', how='left')
     ml_1 = pd.merge(ml_1,          coef_tipempresa,    on='chave', how='left')
     ml_1 = pd.merge(ml_1,          coef_uf,            on='chave', how='left')
     ml_1 = pd.merge(ml_1,          coef_classeprod,    on='chave', how='left')
     ml_1 = pd.merge(ml_1,          coef_certificacao,  on='chave', how='left')
     ml_1 = pd.merge(ml_1,          coef_prod_perig,    on='chave', how='left')
     ml_1 = pd.merge(ml_1,          coef_LMI,           on='chave', how='left')
     ml_1 = pd.merge(ml_1,          coef_modais,        on='chave', how='left')
     ml_1 = pd.merge(ml_1,          coef_perfmotorista, on='chave', how='left')
     ml_1 = pd.merge(ml_1,          coef_emergencia,    on='chave', how='left')
     ml_1 = pd.merge(ml_1,          coef_bonus,         on='chave', how='left')

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

     #print(ml_1)

     ##############################################################################################################################################
     #CALCULO DAS RELATIVIDADES DO QAR TRANSPORTE E INTERCEPTO DA MODELAGEM  - PRÊMIO DE RISCO SEM CARREGAMENTOS
     ml_1['prRisco_0'] = ml_1['intercepto']*ml_1['coef_tipseg']*ml_1['coef_tipempresa']*ml_1['coef_uf']*ml_1['coef_classeprod']*ml_1['coef_certificacao']*ml_1['coef_prodperigoso']*ml_1['coef_lmi']*ml_1['coef_modais']*ml_1['coef_perfmotorista']*ml_1['coef_emergencia']*ml_1['coef_bonus']*ml_1['coef_load_franquia']
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


     ##############################################################################################################################################
     #PRÊMIO TOTAL COM INCLUSÃO DO "IOF"
     pr_total = pd.DataFrame(pr_liquido)
     pr_total['prTotal'] = pr_total['prLiquido']*pr_total['coef_load_carregamento_seguranca']

     #PRÊMIO DE RISCO PELA QUANTIDADE DE VIAGENS
     pr_total = (pr_total['prTotal']*qtdEmbarque)

     st.write("---") #Pular Linha    

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

     ##############################################################################################################################################
     #BOTÃO CALCULAR
     if st.button("Calcular"):
          st.write("**Prêmio Total (Com Carregamentos)**",serie)
          st.write("---") #Pular Linha   
          st.subheader("Carregamentos:")

     ##############################################################################################################################################
     #MOSTRAR CARREGAMENTOS NO MOTOR
          import_load_da              = ((import_load_da['coef_load_DA']-1)*100)
          import_load_do              = ((import_load_do['coef_load_DO']-1)*100)
          import_load_lucro           = ((import_load_lucro['coef_load_lucro']-1)*100)
          import_load_impostos        = ((import_load_impostos['coef_load_impostos']-1)*100)
          import_load_ibnr            = ((import_load_ibnr['coef_load_ibnr']-1)*100)
          import_load_iof             = ((import_load_iof['coef_load_iof']-1)*100)
          import_load_carregamentoSeg = ((import_load_carregamentoSeg['coef_load_carregamento_seguranca']-1)*100)
          import_load_comCorretor     = ((import_load_comCorretor['coef_load_comissao_corretor']-1)*100)
          import_load_franquia        = ((import_load_franquia['coef_load_franquia']-1)*100)

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
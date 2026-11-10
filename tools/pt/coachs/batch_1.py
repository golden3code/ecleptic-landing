# -*- coding: utf-8 -*-
# Adaptation en portugais du Brésil (« você ») des guides coachs, lot 1.
# Base : tools/en/coachs/batch_1.py. Droit, seuils et organismes : tools/intl/_faits-ue.md et
# tools/intl/_faits-pt.md (BR-F au Brésil, PT-F et U au Portugal). Le PAR-Q+ n'est jamais reproduit.

ENTRIES = [
    {
        "fr": "fiche-client-coach-sportif",
        "slug": "ficha-do-aluno-personal-trainer",
        "title": "Ficha do aluno para personal trainer: o que incluir",
        "description": "Ficha do aluno para personal trainer: as seções que incluir, o que conta como dado de saúde pela LGPD e pelo RGPD, o que não anotar e por quanto tempo guardar.",
        "body": """
<p>A resposta curta: a <strong>ficha do aluno para personal trainer</strong> cabe em sete seções: contato, logística, objetivo, histórico de treino, saúde, medidas e acompanhamento. Assim que ela registra uma lesão, um histórico médico ou as respostas de um questionário, passa a conter dados de saúde, que têm proteção especial pela LGPD, no Brasil, e pelo RGPD, em Portugal. Anote só o que você precisa, peça o consentimento do aluno e mantenha a seção de saúde separada.</p>

<h2>O que colocar na ficha do aluno?</h2>
<p>Veja um exemplo de estrutura. A última coluna mostra como tratar cada seção, porque saber se algo é dado de saúde depende de cada caso.</p>
<div class="tablewrap"><table>
<caption>Seções sugeridas como exemplo, com uma leitura prudente da LGPD e do RGPD.</caption>
<thead><tr><th>Seção</th><th>O que você anota</th><th>Tipo de dado</th></tr></thead>
<tbody>
<tr><td>Contato</td><td>Nome, e-mail, telefone, contato de emergência</td><td>Dado pessoal comum</td></tr>
<tr><td>Logística</td><td>Horários, local, equipamento, pacote, data de início</td><td>Dado pessoal comum</td></tr>
<tr><td>Objetivo</td><td>As palavras do próprio aluno, prazo, motivação</td><td>Comum, a menos que revele uma condição de saúde</td></tr>
<tr><td>Histórico de treino</td><td>Atividade atual, passado esportivo, preferências, intensidade desejada</td><td>Comum, avaliar caso a caso</td></tr>
<tr><td>Saúde</td><td>Respostas do questionário, desconfortos relatados, parecer médico pedido</td><td>Dado de saúde</td></tr>
<tr><td>Medidas</td><td>Peso, cintura, frequência cardíaca, sono</td><td>Tratar como dado de saúde</td></tr>
<tr><td>Acompanhamento</td><td>Testes, treinos, cargas, como o aluno se sentiu, decisões tomadas</td><td>Sensível quando cruzado com as medidas</td></tr>
</tbody>
</table></div>
<p>Guarde as palavras exatas do aluno para o objetivo. «Subir até o meu apartamento sem parar no segundo andar» vai servir mais do que «cardio» na hora de escolher um teste ou medir o progresso.</p>

<h2>O que conta como dado de saúde na ficha do aluno?</h2>
<p>Na União Europeia, e portanto em Portugal, dados de saúde são os dados sobre a saúde física ou mental de uma pessoa que revelam informações sobre o estado de saúde dela, passado, presente ou futuro, seja qual for a fonte. No Brasil, a LGPD coloca o dado referente à saúde entre os dados pessoais sensíveis. Histórico médico, doenças, tratamentos e deficiências entram por natureza. Uma lesão também diz algo sobre a saúde física, então registre-a junto com o resto. Trate da mesma forma as respostas de um <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">questionário de saúde</a>.</p>
<p>O peso depende do contexto. Um peso alto pode revelar obesidade, e o peso cruzado com a contagem de passos ou com as calorias ingeridas pode virar dado de saúde. Frequência cardíaca, peso e altura também podem ser sensíveis, principalmente quando vêm de um aparelho conectado. Não encontrei nenhuma classificação escrita dos dados de sono, então trate-os como dados de saúde, por segurança. A sua ficha reúne todas essas medidas no mesmo lugar: aplique a regra mais protetora ao conjunto.</p>
<p>Para guardar esses dados, peça um consentimento à parte do contrato, depois de explicar o que você coleta e por quê. No Brasil, se a base for o consentimento, a LGPD pede que ele seja específico e destacado, para uma finalidade clara, e a autoridade responsável é a ANPD (Agência Nacional de Proteção de Dados). Em Portugal, o RGPD pede um consentimento explícito, para finalidades específicas, que o aluno pode retirar a qualquer momento, com a mesma facilidade com que o deu, e a autoridade é a CNPD (Comissão Nacional de Proteção de Dados). E, no Brasil, para orientar treinos como Profissional de Educação Física, você precisa estar registrado no CREF.</p>

<h2>O que não escrever nas anotações do aluno?</h2>
<ul>
<li><strong>Um diagnóstico.</strong> Escreva, por exemplo: «dor no joelho direito ao subir escada, relatada em 12 de janeiro, encaminhamento ao médico». Não acrescente um nome de doença por conta própria. Você não interpreta os dados de saúde do aluno: assim que um sinal levanta uma dúvida, você encaminha ao médico.</li>
<li><strong>Detalhe médico de que você não precisa.</strong> Você precisa saber que existe um parecer médico e quais limites ele impõe. Cópia de receita ou de laudo não tem lugar na sua ficha.</li>
<li><strong>Um julgamento sobre a pessoa.</strong> O aluno pode pedir para ver os dados dele. No Brasil, você pode responder na hora, de forma simplificada, ou entregar uma declaração completa em até 15 dias. Em Portugal, você responde sem demora e no máximo em um mês; se o pedido for complexo, pode prorrogar o prazo por até mais dois meses, desde que avise o aluno no primeiro mês e explique o motivo. Escreva cada linha como se ele fosse ler.</li>
<li><strong>Tudo o que não muda nada no seu treino.</strong> Para cada campo, pergunte o que você faria de diferente com aquela informação. Se não tiver resposta, apague o campo.</li>
</ul>

<h2>Por quanto tempo guardar a ficha do aluno, e onde?</h2>
<p>Defina o seu próprio prazo de guarda, informe o aluno e apague a seção de saúde quando não precisar mais dela, normalmente no fim do acompanhamento. Recibos e notas fiscais seguem regras próprias: no Brasil, a lei não fixa um número de anos e manda guardar os comprovantes até a prescrição dos tributos, com prazos de 5 anos que começam a contar em datas diferentes; em Portugal, guarde faturas e recibos por 10 anos. Por isso, mantenha a parte administrativa separada da ficha de treino: assim você apaga uma sem mexer na outra.</p>
<p>Trabalhar sozinho não dispensa o registro do que você faz com os dados dos alunos. Em Portugal, como em toda a União Europeia, a dispensa do registro das atividades de tratamento para empresas com menos de 250 trabalhadores não vale se você trata dados de forma não ocasional, como num acompanhamento regular, ou se trata dados de saúde: nesse caso, você mantém o registro, pelo menos para esses tratamentos. No Brasil, a LGPD também exige um registro dos dados que você trata; como profissional autônomo, você pode fazê-lo de forma simplificada, desde que o tratamento não seja de alto risco. Atenção: o uso de dados de saúde já preenche um dos critérios de alto risco, e basta somar um critério geral, como o tratamento em larga escala, para perder essa facilidade.</p>
<p>Para o armazenamento, dados de saúde pedem uma segurança proporcional à sensibilidade deles, e uma conversa de WhatsApp ou um arquivo sem proteção não estão à altura.</p>

<h2>Como manter a ficha do aluno atualizada?</h2>
<p>Abra a ficha na <a href="/coachs/bilan-forme-premier-rendez-vous.html">primeira avaliação física</a> e, depois de cada treino, acrescente três coisas: o que foi feito, como o aluno se sentiu e o que você vai mudar na próxima vez. Registre também os resultados dos <a href="/coachs/tests-physiques-nouveau-client.html">testes físicos</a>, com as condições em que foram feitos.</p>
<p>Mostre esses números ao aluno. Uma meta-análise de 138 ensaios e 19.951 pessoas (Harkin, 2016) indica que acompanhar o progresso ajuda a atingir os objetivos, com um efeito maior quando o resultado é registrado fisicamente ou tornado público. Ela não trata só de exercício, então use-a como referência.</p>
<p>Releia a seção de saúde sempre que a situação mudar. Uma dor nova leva você de volta à mesma regra: você anota, não interpreta e encaminha.</p>
<p>Este guia é apenas informativo e não substitui o conselho de um advogado ou de um encarregado de proteção de dados.</p>

<h2>Em resumo</h2>
<ul>
<li>Sete seções bastam, e cada campo precisa mudar alguma coisa no seu treino.</li>
<li>Lesões, histórico médico e respostas do questionário são dados de saúde. Por segurança, trate peso e sono da mesma forma.</li>
<li>Registre fatos sem interpretá-los, separe a saúde da cobrança e defina um prazo de guarda.</li>
</ul>
""",
        "faq": [
            {"q": "Como fazer uma ficha de aluno de personal trainer?", "a": "Monte sete seções: contato, logística, objetivo, histórico de treino, saúde, medidas e acompanhamento. Anote só o que você precisa e mantenha a seção de saúde separada, porque ela tem proteção especial pela LGPD, no Brasil, e pelo RGPD, em Portugal. Uma planilha com senha ou um software servem, desde que o acesso seja seguro."},
            {"q": "A ficha do aluno tem dados de saúde?", "a": "Quase sempre. Lesões, histórico médico e respostas do questionário são dados de saúde, e peso e sono também podem ser, principalmente cruzados com outras medidas. Na dúvida, trate-os assim e peça um consentimento à parte do contrato: específico e destacado no Brasil, explícito em Portugal."},
            {"q": "Por quanto tempo o personal deve guardar a ficha do aluno?", "a": "Defina o seu próprio prazo, informe o aluno e apague a seção de saúde quando não precisar mais dela, normalmente no fim do acompanhamento. Recibos e notas seguem regras fiscais: no Brasil, guarde até a prescrição dos tributos; em Portugal, por 10 anos."},
        ],
        "sources": [
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychol Bull</em>. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
            {"t": "Lei nº 13.709, de 14 de agosto de 2018 (Lei Geral de Proteção de Dados Pessoais), norma atualizada. Câmara dos Deputados.", "u": "https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-normaatualizada-pl.html"},
            {"t": "ANPD. Resolução CD/ANPD nº 2, de 27 de janeiro de 2022 (agentes de tratamento de pequeno porte).", "u": "https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022"},
            {"t": "Lei nº 9.696, de 1º de setembro de 1998 (regulamentação da profissão de Educação Física), norma atualizada. Câmara dos Deputados.", "u": "https://www2.camara.leg.br/legin/fed/lei/1998/lei-9696-1-setembro-1998-374623-normaatualizada-pl.html"},
            {"t": "Lei nº 5.172, de 25 de outubro de 1966 (Código Tributário Nacional), norma atualizada. Câmara dos Deputados.", "u": "https://www2.camara.leg.br/legin/fed/lei/1960-1969/lei-5172-25-outubro-1966-358971-normaatualizada-pl.html"},
            {"t": "Regulamento (UE) 2016/679 do Parlamento Europeu e do Conselho, de 27 de abril de 2016 (Regulamento Geral sobre a Proteção de Dados). EUR-Lex.", "u": "https://eur-lex.europa.eu/legal-content/PT/TXT/HTML/?uri=CELEX:32016R0679"},
            {"t": "Lei n.º 58/2019, de 8 de agosto (execução do Regulamento Geral sobre a Proteção de Dados). Diário da República.", "u": "https://diariodarepublica.pt/dr/detalhe/lei/58-2019-123815982"},
            {"t": "Código do IVA, artigo 52.º. Portal das Finanças.", "u": "https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva52.aspx"},
        ],
    },
    {
        "fr": "bilan-forme-premier-rendez-vous",
        "slug": "primeira-avaliacao-fisica-aluno-novo",
        "title": "Primeira avaliação física: como conduzir com um aluno novo",
        "description": "Primeira avaliação física com um aluno novo: como se preparar, o que perguntar, o que fazer diante de um sinal de alerta de saúde e como encerrar o encontro.",
        "body": """
<p>A resposta curta: uma boa <strong>primeira avaliação física</strong> segue quatro etapas: ouvir o objetivo, identificar o que pede um parecer médico, medir um ponto de partida simples e propor um plano claro. Não encontrei nenhuma norma que defina o conteúdo ou a duração dela. Ela ajuda você a decidir se pode começar, com que intensidade e em que direção. Você não faz nenhum diagnóstico.</p>

<h2>O que preparar antes da primeira avaliação física?</h2>
<p>Três coisas enviadas com antecedência evitam que você perca metade do encontro:</p>
<ul>
<li><strong>O <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">questionário de saúde</a></strong>, para preencher antes de vir, com uma explicação do que você faz com os dados e um pedido de consentimento.</li>
<li><strong>Os detalhes práticos:</strong> local, roupa, água, duração do encontro.</li>
<li><strong>O formato do encontro:</strong> gratuito ou pago, você avisa desde o início. O guia sobre <a href="/coachs/seance-essai-coach-sportif.html">aula experimental</a> trata dessa questão.</li>
</ul>
<p>Chame de avaliação física, nunca de check-up de saúde: essa expressão cria uma expectativa que você não pode cumprir.</p>

<h2>Como fazer uma avaliação física em uma hora?</h2>
<p>Não encontrei nenhuma recomendação que fixe uma duração. Veja um exemplo de divisão em 60 minutos, para adaptar:</p>
<ol>
<li><strong>5 minutos, a abertura.</strong> Você explica o que vai acontecer e com o que o aluno vai sair.</li>
<li><strong>20 minutos, a escuta.</strong> Objetivo, histórico de treino, restrições, preferências.</li>
<li><strong>5 minutos, a segurança.</strong> Vocês revisam o questionário juntos.</li>
<li><strong>20 minutos, o movimento.</strong> Dois ou três testes simples, com aquecimento se o protocolo pedir.</li>
<li><strong>10 minutos, os próximos passos.</strong> Você resume e faz a sua proposta.</li>
</ol>
<p>Os <a href="/coachs/tests-physiques-nouveau-client.html">testes físicos</a> definem um ponto de partida. Eles esperam se o questionário ou a conversa levantar uma questão de saúde. Na primeira avaliação, deixe margem: nada máximo com alguém que você acabou de conhecer, e nenhum teste que caiba a um médico. A Haute Autorité de Santé (HAS), autoridade nacional de saúde da França, lembra que o teste de esforço com análise de gases (ergoespirometria) é feito em estruturas especializadas, com médicos capacitados.</p>

<h2>O que perguntar a um aluno novo?</h2>
<p>Perguntas abertas, e um aluno que fala mais do que você:</p>
<ul>
<li><strong>«Por que você decidiu começar agora?»</strong> O motivo do momento muitas vezes diz mais do que o objetivo declarado.</li>
<li><strong>«Como você vai saber que deu certo?»</strong> Você ganha um critério concreto, nas palavras do aluno.</li>
<li><strong>«O que você já tentou antes, e o que fez você parar?»</strong> Você identifica os obstáculos antes que eles voltem.</li>
<li><strong>«Quantos treinos cabem de verdade na sua semana?»</strong> O programa se constrói sobre essa resposta.</li>
<li><strong>«O que você gosta de fazer, e o que você se recusa a fazer?»</strong> O aluno mantém o controle de parte das escolhas.</li>
</ul>
<p>Esse último ponto conta. Uma revisão de 66 estudos (Teixeira, 2012) mostra uma relação consistente entre as formas autônomas de motivação e o exercício, e a motivação intrínseca prevê melhor a adesão a longo prazo. A maioria desses estudos é descritiva: eles estabelecem uma relação, não uma causa. O guia da HAS vai no mesmo sentido para a entrevista motivacional: identificar os obstáculos e definir objetivos realistas com a pessoa.</p>

<h2>O que fazer se o aluno relatar um problema de saúde?</h2>
<p>Desde 2015, a triagem do American College of Sports Medicine (ACSM) se apoia em três fatores: a atividade atual, os sinais ou a doença cardiovascular, metabólica ou renal conhecida, e a intensidade desejada. Essa atualização respondeu a um excesso: encaminhamentos desnecessários demais ao médico, que podem desestimular as pessoas a se mexer. A OMS também considera que, sem contraindicação, uma liberação médica prévia em geral não é necessária para uma atividade leve a moderada que não vá além de uma caminhada rápida.</p>
<p>A HAS indica o que fazer em caso de dúvida:</p>
<ul>
<li><strong>Uma resposta positiva no questionário:</strong> recomenda-se um parecer médico antes de começar.</li>
<li><strong>Sinais que sugerem uma doença:</strong> a pessoa adia a atividade, qualquer que seja a intensidade, e procura o médico.</li>
<li><strong>45 anos ou mais, sem exercício intenso regular e com um plano perto do esforço máximo:</strong> aconselha-se um parecer médico.</li>
</ul>
<p>Nos três casos, você não interpreta nada. Você repete o que ouviu, explica que a decisão cabe a um médico, anota a data e adia a parte de movimento. Se o aluno tiver dor no peito ou um desmaio na sua frente, ligue 192 (SAMU) no Brasil ou 112 em Portugal. Diagnóstico é trabalho de médico, então uma frase como «deve ser a sua pressão» não tem lugar numa avaliação física.</p>

<h2>Como encerrar a avaliação física?</h2>
<p>Resuma em três frases o que você entendeu, o que mediu e o que propõe. Depois, dê um objetivo com data, o ritmo dos treinos e a data da próxima reavaliação. Coloque as condições e o preço por escrito antes de qualquer compromisso: no Brasil, o Código de Ética do CONFEF pede que as condições sejam combinadas antes do início, de preferência por contrato escrito.</p>
<p>Não prometa um resultado em números, porque você não pode nem garanti-lo nem prová-lo. Diga o que vai medir, e quando. No Brasil, para orientar treinos, na academia, na casa do aluno ou online, você precisa estar registrado no CREF da sua região. Em Portugal, numa academia (ginásio), você precisa do título profissional de técnico de exercício físico, emitido pelo IPDJ, e a academia precisa ter seguro e afixar essa informação em local visível; a Lei 39/2012, que traz essas regras, trata das instalações de fitness e não diz nada sobre o treino em casa, ao ar livre ou online. Na mesma noite, passe o essencial para a <a href="/coachs/fiche-client-coach-sportif.html">ficha do aluno</a>, enquanto as palavras exatas dele ainda estão frescas.</p>

<h2>Em resumo</h2>
<ul>
<li>Envie o questionário antes do encontro e faça da escuta a parte mais longa.</li>
<li>Ao menor sinal de alerta de saúde, adie o movimento e encaminhe ao médico, sem interpretar.</li>
<li>Termine com um objetivo com data e condições por escrito, sem prometer resultado.</li>
</ul>
""",
        "faq": [
            {"q": "O que acontece na avaliação física com o personal trainer?", "a": "O personal ouve o objetivo e o histórico de treino, revisa o questionário de saúde, faz dois ou três testes simples se nada impedir e depois propõe um plano. Esse encontro avalia a forma física. Ele não substitui uma consulta médica."},
            {"q": "Quanto tempo dura uma avaliação física?", "a": "Não encontrei nenhuma recomendação que fixe uma duração. Uma hora é um formato prático: um terço para a escuta, um terço para o movimento e o resto para a abertura, a segurança e os próximos passos. Adapte ao aluno e aos testes previstos."},
            {"q": "O que perguntar ao aluno na primeira avaliação?", "a": "Por que ele decidiu começar agora, como vai saber que deu certo, o que já tentou, quanto tempo tem de verdade, do que gosta e o que se recusa a fazer. Acrescente o questionário de saúde e encaminhe ao médico assim que uma resposta pedir."},
        ],
        "sources": [
            {"t": "HAS. Consultation et prescription médicale d'activité physique à des fins de santé chez l'adulte. Guide. 2022 (em francês).", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2018-10/guide_aps_vf.pdf"},
            {"t": "Riebe D, Franklin BA, Thompson PD, et al. Updating ACSM's Recommendations for Exercise Preparticipation Health Screening. <em>Med Sci Sports Exerc</em>. 2015.", "u": "https://doi.org/10.1249/MSS.0000000000000664"},
            {"t": "Bull FC, Al-Ansari SS, Biddle S, et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. <em>Br J Sports Med</em>. 2020.", "u": "https://doi.org/10.1136/bjsports-2020-102955"},
            {"t": "Teixeira PJ, Carraça EV, Markland D, et al. Exercise, physical activity, and self-determination theory: a systematic review. <em>Int J Behav Nutr Phys Act</em>. 2012.", "u": "https://doi.org/10.1186/1479-5868-9-78"},
            {"t": "Lei nº 9.696, de 1º de setembro de 1998 (regulamentação da profissão de Educação Física), norma atualizada. Câmara dos Deputados.", "u": "https://www2.camara.leg.br/legin/fed/lei/1998/lei-9696-1-setembro-1998-374623-normaatualizada-pl.html"},
            {"t": "CREF12/PE. Código de Ética Profissional de Educação Física (Resolução CONFEF nº 508/2023).", "u": "https://www.cref12.org.br/codigo-de-etica/"},
            {"t": "Ministério da Saúde. SAMU 192.", "u": "https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/s/samu-192"},
            {"t": "Lei n.º 39/2012 (atividades desportivas em ginásios, academias e clubes de saúde), versão consolidada. Diário da República.", "u": "https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2012-155873811"},
        ],
    },
    {
        "fr": "questionnaire-sante-avant-le-sport-client",
        "slug": "questionario-de-saude-antes-do-treino",
        "title": "Questionário de saúde antes do treino: o que perguntar ao aluno",
        "seo_title": "Questionário de saúde (PAR-Q): o que perguntar ao aluno",
        "description": "Questionário de saúde antes do treino: o que o personal pode perguntar, a lei do PAR-Q em São Paulo, o uso do PAR-Q+ e o que fazer quando o aluno diz sim.",
        "body": """
<p>A resposta curta: um <strong>questionário de saúde antes do treino</strong> pergunta sobre a atividade atual, as doenças conhecidas, os sintomas novos e a intensidade desejada. Ser obrigatório ou não depende do lugar onde você trabalha, mas a ferramenta é útil de qualquer forma. A Haute Autorité de Santé (HAS), autoridade nacional de saúde da França, recomenda um questionário de autoavaliação para quem quer começar ou aumentar uma atividade de intensidade pelo menos moderada, e diz que um profissional do exercício pode aplicá-lo. Se o aluno responder «sim», você não interpreta: encaminha ao médico antes de começar.</p>

<h2>O personal trainer precisa aplicar questionário ou pedir atestado médico?</h2>
<p>A resposta muda de um lugar para outro. No Brasil, não encontrei lei federal sobre isso. No estado de São Paulo, a Lei estadual 10.848/2001, alterada pela Lei 16.724/2018, exige que alunos de 15 a 69 anos respondam ao PAR-Q na matrícula da academia; quem responder «sim» a alguma pergunta assina um termo de responsabilidade. Essa lei trata das academias e de outros estabelecimentos de prática esportiva, não do treino na casa do aluno nem online, e não verifiquei os outros estados. Em Portugal, a Lei 39/2012, que regula as academias, não fala de questionário, e não verifiquei outros textos. Onde nada obriga, em geral você ainda pode incluir um questionário ou um atestado médico no seu contrato com o aluno.</p>

<h2>PAR-Q+ ou questionário próprio: qual usar?</h2>
<div class="tablewrap"><table>
<caption>Fonte: HAS 2022 e os termos e condições do PAR-Q+, lidos em 31 de outubro de 2026.</caption>
<thead><tr><th>Opção</th><th>Uso</th><th>O que saber</th></tr></thead>
<tbody>
<tr><td>PAR-Q+</td><td>Triagem antes da atividade, de 15 a 69 anos</td><td>7 perguntas, texto protegido</td></tr>
<tr><td>Seu próprio questionário</td><td>O que muda o seu treino</td><td>Escreva você mesmo, sem copiar o PAR-Q+</td></tr>
</tbody>
</table></div>
<p>O PAR-Q+ pede cuidado. Os termos de uso exigem autorização prévia por escrito para modificá-lo ou integrá-lo a um app, site, software ou formulário online. Citar a fonte não vale como autorização. As versões oficiais sem modificação são, hoje, gratuitas para certos usos individuais, clínicos, educacionais e de pesquisa não comercial. Os termos não citam os personal trainers, embora o site ofereça recursos para profissionais do exercício, e o uso comercial pode ser cobrado. Na dúvida, escreva para o detentor dos direitos.</p>
<p>O caminho mais simples: convide o aluno a preenchê-lo ele mesmo no site oficial, eparmedx.com. Encontrar o texto reproduzido em outro lugar não dá permissão para copiá-lo no seu formulário.</p>

<h2>O que perguntar num questionário de saúde?</h2>
<p>Para o seu próprio questionário, parta da lógica do American College of Sports Medicine (ACSM), que se resume a três fatores, e acrescente o que serve ao seu treino:</p>
<ul>
<li><strong>Atividade atual.</strong> Quantos treinos por semana, de quanto tempo, com que intensidade.</li>
<li><strong>O que já se sabe.</strong> Uma doença cardiovascular, metabólica ou renal diagnosticada. Sim ou não basta.</li>
<li><strong>O que é novo.</strong> Um sinal incomum, em repouso ou no esforço.</li>
<li><strong>Intensidade desejada.</strong> O que o aluno quer fazer, e em que nível.</li>
<li><strong>O que limita o movimento.</strong> Desconforto, cirurgia recente, gravidez: tudo o que obriga você a adaptar um exercício.</li>
</ul>
<p>Passe cada pergunta pelo mesmo filtro: o que você muda no treino se a resposta for «sim»? Se nada muda, corte a pergunta.</p>
<p>A HAS acrescenta dois marcos de idade. A partir de 45 anos, sem atividade intensa regular e com um plano perto do esforço máximo, aconselha-se um parecer médico. A partir de 70 anos, ele é recomendado para uma atividade de intensidade pelo menos alta. No estado de São Paulo, a lei vai além na matrícula da academia: a partir de 70 anos, exige um atestado médico de aptidão com o nome e o CRM do médico.</p>

<h2>O que fazer se o aluno responder sim?</h2>
<p>A HAS é clara. Uma resposta positiva: recomenda-se um parecer médico antes de começar. Sinais ou sintomas que sugerem uma doença: a pessoa adia a atividade e procura o médico. Tudo negativo: ela pode ficar mais ativa, com as precauções de sempre.</p>
<p>O seu papel para aí. Você não avalia a gravidade e não tranquiliza. Anota a data, espera o aluno confirmar o parecer recebido e os eventuais limites, e depois adapta. Aplique o questionário de novo sempre que a situação mudar.</p>

<h2>Como tratar as respostas do questionário?</h2>
<p>As respostas de um questionário de saúde são dados de saúde. No Brasil, a LGPD as trata como dados sensíveis: se a base for o consentimento, ele precisa ser específico e destacado, para uma finalidade clara. Em Portugal, vale o RGPD: tratar dados de saúde é proibido em princípio, salvo exceções, e a primeira é o consentimento explícito do aluno para finalidades específicas, que ele pode retirar a qualquer momento. Peça esse consentimento à parte do contrato, depois de dizer o que você coleta e por quê. Um ponto continua em aberto: o consentimento só vale se a pessoa puder recusar de verdade, então recusar um aluno que deixa o formulário em branco não é uma questão resolvida. Guarde as respostas na seção de saúde da <a href="/coachs/fiche-client-coach-sportif.html">ficha do aluno</a>.</p>
<p>Este guia é apenas informativo e não substitui o conselho de um médico ou de um advogado.</p>

<h2>Em resumo</h2>
<ul>
<li>A obrigação depende do lugar (no Brasil, só a encontrei numa lei do estado de São Paulo, para academias), mas a HAS recomenda um questionário antes de começar.</li>
<li>O PAR-Q+ não pode ser copiado num formulário sem autorização por escrito.</li>
<li>Quando o aluno responde «sim», você não interpreta: encaminha ao médico antes de começar.</li>
</ul>
""",
        "faq": [
            {"q": "O PAR-Q é obrigatório?", "a": "No Brasil, não encontrei lei federal que o imponha, mas uma lei do estado de São Paulo exige o PAR-Q na matrícula da academia, para alunos de 15 a 69 anos. Em Portugal, a lei das academias (Lei 39/2012) não trata disso. Em todo caso, os termos do PAR-Q+ proíbem modificá-lo ou integrá-lo a uma ferramenta online sem autorização por escrito."},
            {"q": "O personal trainer pode pedir atestado médico?", "a": "Sim, em geral você pode colocar essa condição no seu contrato. No estado de São Paulo, a lei já exige atestado médico na matrícula da academia a partir de 70 anos. Se as respostas do aluno pedirem um parecer médico, espere esse parecer antes de começar."},
            {"q": "O que fazer quando o aluno responde sim no questionário de saúde?", "a": "Não interprete a resposta e não tranquilize. Recomenda-se um parecer médico antes de começar, e um aluno com sinais ou sintomas que sugerem uma doença adia a atividade e procura o médico. Anote a data e adapte quando o aluno confirmar o parecer e os eventuais limites."},
        ],
        "sources": [
            {"t": "HAS. Consultation et prescription médicale d'activité physique à des fins de santé chez l'adulte. Guide. 2022 (em francês).", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2018-10/guide_aps_vf.pdf"},
            {"t": "Riebe D, Franklin BA, Thompson PD, et al. Updating ACSM's Recommendations for Exercise Preparticipation Health Screening. <em>Med Sci Sports Exerc</em>. 2015.", "u": "https://doi.org/10.1249/MSS.0000000000000664"},
            {"t": "PAR-Q+ Collaboration. Terms and Conditions. 2026 (em inglês).", "u": "https://eparmedx.com/terms-and-conditions/"},
            {"t": "Lei estadual nº 10.848, de 6 de julho de 2001, compilação. Assembleia Legislativa do Estado de São Paulo.", "u": "https://www.al.sp.gov.br/repositorio/legislacao/lei/2001/compilacao-lei-10848-06.07.2001.html"},
            {"t": "Lei nº 13.709, de 14 de agosto de 2018 (Lei Geral de Proteção de Dados Pessoais), norma atualizada. Câmara dos Deputados.", "u": "https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-normaatualizada-pl.html"},
            {"t": "Regulamento (UE) 2016/679 do Parlamento Europeu e do Conselho, de 27 de abril de 2016 (Regulamento Geral sobre a Proteção de Dados). EUR-Lex.", "u": "https://eur-lex.europa.eu/legal-content/PT/TXT/HTML/?uri=CELEX:32016R0679"},
            {"t": "Lei n.º 39/2012 (atividades desportivas em ginásios, academias e clubes de saúde), versão consolidada. Diário da República.", "u": "https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2012-155873811"},
        ],
    },
    {
        "fr": "tests-physiques-nouveau-client",
        "slug": "testes-fisicos-aluno-novo",
        "title": "Testes físicos para aluno novo: quais escolher?",
        "description": "Testes físicos para aluno novo: quais escolher para cada perfil, como aplicá-los de forma confiável, como ler os resultados e o que pensar do teste de Ruffier.",
        "body": """
<p>A resposta curta: não encontrei nenhuma bateria oficial de <strong>testes físicos para aluno novo</strong>. Escolha três ou quatro testes ligados ao objetivo: um de resistência aeróbia, um de membros inferiores, um de membros superiores e um de equilíbrio, se o perfil pedir. Eles comparam o aluno com ele mesmo. Não fazem diagnóstico.</p>

<h2>Quais testes físicos escolher para cada aluno?</h2>
<p>A Haute Autorité de Santé (HAS), autoridade nacional de saúde da França, detalha os testes de campo mais comuns e lembra que nenhum teste sozinho mede a força ou a flexibilidade do corpo inteiro. A tabela combina as referências dela com alguns estudos.</p>
<div class="tablewrap"><table>
<caption>Fonte: HAS 2022; Holland 2014; Jones 1999; Penry 2011.</caption>
<thead><tr><th>Capacidade</th><th>Teste</th><th>Perfil</th><th>O que saber</th></tr></thead>
<tbody>
<tr><td>Resistência aeróbia</td><td>Caminhada de 6 minutos</td><td>Iniciante, idoso, retorno ao exercício</td><td>Validação clínica, não esportiva</td></tr>
<tr><td>Resistência aeróbia</td><td>Corrida de 12 minutos</td><td>Adulto jovem já ativo</td><td>Esforço intenso, cautela com a estimativa de VO2 máx</td></tr>
<tr><td>Pernas</td><td>Sentar e levantar da cadeira em 30 segundos</td><td>Idoso, iniciante</td><td>Cadeira sem braços, sem usar as mãos. Validado depois dos 60 anos</td></tr>
<tr><td>Membros superiores</td><td>Flexões de braço sem parar</td><td>Adulto sem desconforto no ombro</td><td>Mistura força e resistência</td></tr>
<tr><td>Força</td><td>Teste de 10 a 15 repetições máximas</td><td>Iniciante, idoso, retorno ao exercício</td><td>Específico de cada exercício</td></tr>
<tr><td>Flexibilidade</td><td>Sentar e alcançar</td><td>Aluno sem dor nas costas</td><td>Sobretudo os isquiotibiais</td></tr>
<tr><td>Equilíbrio</td><td>Apoio unipodal de olhos fechados</td><td>Idoso</td><td>Três tentativas, vale o melhor tempo. Fique ao lado, perto de um apoio</td></tr>
</tbody>
</table></div>
<p>Dois exemplos de escolha. Para uma pessoa sedentária de 55 anos que volta ao exercício: caminhada de 6 minutos, sentar e levantar da cadeira, apoio unipodal. Para um aluno ativo de 30 anos que busca força: corrida de 12 minutos, flexões de braço e um teste de 8 repetições máximas em dois exercícios que ele domina, divididos em dois treinos.</p>
<p>Antes de qualquer teste, releia o <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">questionário de saúde</a>. Se ele pedir um parecer médico, o teste espera.</p>

<h2>Como aplicar os testes físicos sem distorcer os resultados?</h2>
<p>Um teste só vale se você puder repeti-lo de forma idêntica. A norma técnica da European Respiratory Society e da American Thoracic Society (ERS/ATS; Holland, 2014) considera os testes de caminhada válidos, confiáveis e sensíveis à mudança nas doenças respiratórias crônicas, e insiste em como eles reagem a pequenas diferenças de método. Ela recomenda duas tentativas na caminhada de 6 minutos, com pelo menos 30 minutos de intervalo, para ter uma linha de base estável.</p>
<ul>
<li><strong>Mesmo cenário.</strong> Mesmo lugar, mesmo percurso, mesmo horário, mesmo tênis, mesma cadeira. A HAS descreve a caminhada de 6 minutos em volta de dois cones a 30 m um do outro. A norma ERS/ATS pede uma superfície plana e pelo menos 30 m: num percurso mais curto, esqueça as normas.</li>
<li><strong>Mesmas palavras.</strong> Escreva as suas instruções e leia em voz alta. Para a caminhada, a norma prevê uma frase padrão a cada minuto, e nada mais. Se o aluno parar, o cronômetro continua.</li>
<li><strong>Mesma preparação.</strong> Para a caminhada de 6 minutos, nada de aquecimento e nenhum esforço intenso nas 2 horas anteriores, segundo essa norma. Para os outros testes, mantenha o mesmo aquecimento.</li>
<li><strong>Um registro escrito.</strong> Anote as condições ao lado do resultado, ou você vai acabar comparando duas coisas diferentes.</li>
</ul>
<p>Se o aluno relatar dor, mal-estar, falta de ar incomum ou cãibras, ou se ele cambalear ou ficar pálido, interrompa o teste e encaminhe ao médico. Em caso de dor no peito ou desmaio, coloque a pessoa sentada ou deitada e ligue 192 (SAMU) no Brasil ou 112 em Portugal.</p>

<h2>Um aluno novo pode fazer um teste máximo?</h2>
<p>Não na primeira avaliação, a menos que seja um aluno treinado que já conhece o teste. A HAS descreve o teste de 1RM como um indicador confiável da força, e os testes de 4RM ou 8RM como uma estimativa confiável. Ela considera os testes de 10 a 15 repetições máximas mais seguros para pessoas mais velhas, descondicionadas ou que vivem com uma doença crônica. Mesmo com 4 ou 8 repetições, espere a técnica estar limpa. A corrida de 12 minutos já exige um esforço sustentado, então reserve-a para um aluno acostumado à intensidade.</p>
<p>Não confunda esses testes com um teste ergométrico clínico, feito com eletrocardiograma e controle da pressão arterial em ambiente clínico.</p>

<h2>O teste de Ruffier é confiável?</h2>
<p>Ele continua sendo um marcador simples, pouco preciso para estimar a aptidão cardiorrespiratória. Num estudo com 81 adultos saudáveis (Sartor, 2016), o índice de Ruffier-Dickson teve uma correlação de -0,40 com a aptidão medida e explicou 15% da variabilidade. Ele não aparece na tabela de testes da HAS. Se o seu aluno fizer questão dele, compare os resultados dele entre si e não tire dele um VO2 máx.</p>

<h2>Como ler os resultados, e quando refazer os testes?</h2>
<p>Compare o aluno com ele mesmo: é isso que significa uma <a href="/methode/ligne-de-base.html">linha de base</a>. As normas descrevem outras populações. Para a caminhada de 6 minutos, Enright (1998) encontrou uma mediana de 576 m nos homens e de 494 m nas mulheres, entre 290 adultos saudáveis de 40 a 80 anos, e as equações explicam cerca de 40% da variância. Para a corrida de 12 minutos, Penry (2011) relata uma boa confiabilidade em adultos jovens, mas pede cautela ao tirar dela um VO2 máx.</p>
<p>Uma diferença em relação a uma norma não permite concluir nada sobre a saúde do aluno. Se um resultado surpreender você, encaminhe ao médico sem comentar. O teste de sentar e levantar, por sua vez, foi validado em 76 adultos com mais de 60 anos (Jones, 1999): os valores dele não servem para um aluno de 30 anos.</p>
<p>Não encontrei nenhuma frequência oficial para refazer os testes. O mais lógico é refazê-los ao fim de um bloco do <a href="/coachs/creer-programme-personnalise-client.html">programa</a>, nas mesmas condições, e depois mostrar a evolução no <a href="/coachs/bilan-mensuel-client-coaching.html">relatório mensal</a>.</p>

<h2>Em resumo</h2>
<ul>
<li>Três ou quatro testes ligados ao objetivo bastam, escolhidos conforme o perfil.</li>
<li>Use sempre o mesmo protocolo, anote as condições e compare o aluno com ele mesmo.</li>
<li>Um teste não faz diagnóstico: ao menor sinal de alerta, pare e encaminhe ao médico.</li>
</ul>
""",
        "faq": [
            {"q": "Qual teste físico fazer com um aluno iniciante?", "a": "A caminhada de 6 minutos para a resistência aeróbia, o teste de sentar e levantar da cadeira em 30 segundos para as pernas e, se precisar, um teste de 10 a 15 repetições máximas. Esses testes são fáceis de dosar. Releia sempre o questionário de saúde antes de começar."},
            {"q": "O teste de Ruffier é confiável?", "a": "É um marcador simples, pouco preciso para estimar a aptidão cardiorrespiratória. Num estudo com 81 adultos saudáveis, ele explicou 15% da variabilidade. Ele não aparece na tabela de testes da HAS, a autoridade nacional de saúde da França."},
            {"q": "De quanto em quanto tempo refazer a avaliação física do aluno?", "a": "Não encontrei nenhuma frequência oficial. O mais lógico é refazer os testes ao fim de um bloco de treino, nas mesmas condições, para comparar o aluno com ele mesmo."},
        ],
        "sources": [
            {"t": "HAS. Guide des connaissances sur l'activité physique et la sédentarité. 2022 (em francês).", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2022-08/guide_connaissance_ap_sedentarite_vf.pdf"},
            {"t": "Holland AE, Spruit MA, Troosters T, et al. An official European Respiratory Society/American Thoracic Society technical standard: field walking tests in chronic respiratory disease. <em>Eur Respir J</em>. 2014.", "u": "https://doi.org/10.1183/09031936.00150314"},
            {"t": "Enright PL, Sherrill DL. Reference equations for the six-minute walk in healthy adults. <em>Am J Respir Crit Care Med</em>. 1998.", "u": "https://doi.org/10.1164/ajrccm.158.5.9710086"},
            {"t": "Jones CJ, Rikli RE, Beam WC. A 30-s chair-stand test as a measure of lower body strength in community-residing older adults. <em>Res Q Exerc Sport</em>. 1999.", "u": "https://doi.org/10.1080/02701367.1999.10608028"},
            {"t": "Penry JT, Wilcox AR, Yun J. Validity and reliability analysis of Cooper's 12-minute run and the multistage shuttle run in healthy adults. <em>J Strength Cond Res</em>. 2011.", "u": "https://doi.org/10.1519/JSC.0b013e3181cc2423"},
            {"t": "Sartor F, Bonato M, Papini G, et al. A 45-Second Self-Test for Cardiorespiratory Fitness: Heart Rate-Based Estimation in Healthy Individuals. <em>PLoS One</em>. 2016.", "u": "https://doi.org/10.1371/journal.pone.0168154"},
            {"t": "Ministério da Saúde. SAMU 192.", "u": "https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/s/samu-192"},
            {"t": "gov.pt. Contactos de emergência em Portugal. 2026.", "u": "https://www.gov.pt/guias/contactos-de-emergencia-em-portugal"},
        ],
    },
    {
        "fr": "creer-programme-personnalise-client",
        "slug": "como-montar-treino-personalizado-aluno",
        "title": "Como montar um treino personalizado para o aluno: o método",
        "description": "Como montar um treino personalizado para o aluno: da primeira avaliação à progressão, com as referências da OMS e do ACSM para cada objetivo de treino.",
        "body": """
<p>A resposta curta: um <strong>treino personalizado</strong> parte da avaliação do aluno, nunca de um modelo pronto. Comece pelo objetivo, pelo tempo que ele tem de verdade e pelo nível dele. Defina o volume e a intensidade, escolha uma divisão que ele vá manter, escreva uma regra de progressão e ajuste pelo que ele relata. O posicionamento do American College of Sports Medicine (ACSM) publicado em 2026 mostra que poucas variáveis mudam de fato os resultados, então concentre-se nelas.</p>

<h2>O que saber antes de montar o treino do aluno?</h2>
<p>Cinco informações decidem quase tudo. Elas saem da <a href="/coachs/bilan-forme-premier-rendez-vous.html">primeira avaliação física</a> e dos <a href="/coachs/tests-physiques-nouveau-client.html">testes físicos</a>:</p>
<ul>
<li><strong>O objetivo</strong>, nas palavras do aluno, com prazo.</li>
<li><strong>O tempo disponível de verdade:</strong> o número de treinos que ele vai manter numa semana cheia.</li>
<li><strong>O nível:</strong> o que ele faz hoje, e o que já fez antes.</li>
<li><strong>O local e o equipamento.</strong></li>
<li><strong>Os limites:</strong> desconfortos relatados, parecer médico pendente ou limites definidos por um médico.</li>
</ul>
<p>Se houver um parecer médico pendente, o treino também espera. Se o aluno recebeu limites, aplique-os como estão, sem reinterpretá-los.</p>

<h2>Como definir o volume e a intensidade do treino?</h2>
<p>Duas referências bastam para os parâmetros: a OMS, para a saúde, e o ACSM, para o treino de força, com 137 revisões sistemáticas e mais de 30.000 participantes, todos adultos saudáveis.</p>
<div class="tablewrap"><table>
<caption>Fonte: OMS 2020; ACSM 2026; Schoenfeld 2017. Adultos saudáveis.</caption>
<thead><tr><th>Objetivo</th><th>Referência</th><th>Fonte</th></tr></thead>
<tbody>
<tr><td>Saúde, retorno ao exercício</td><td>150 a 300 min de atividade moderada por semana, ou 75 a 150 min de atividade vigorosa, mais fortalecimento de todos os grandes grupos musculares em 2 dias ou mais</td><td>OMS</td></tr>
<tr><td>Idosos</td><td>Dentro desse volume, atividade variada com foco em equilíbrio e força, 3 dias ou mais por semana</td><td>OMS</td></tr>
<tr><td>Força</td><td>80% de 1RM ou mais, 2 a 3 séries, 2 treinos ou mais por semana</td><td>ACSM</td></tr>
<tr><td>Hipertrofia</td><td>10 séries ou mais por semana, por grupo muscular. Mais volume, mais ganho (15 estudos)</td><td>ACSM, Schoenfeld</td></tr>
<tr><td>Potência</td><td>30 a 70% de 1RM, fase concêntrica rápida</td><td>ACSM</td></tr>
</tbody>
</table></div>
<p>Esses números descrevem o destino, muito além da primeira semana. A OMS aconselha quem está longe deles a começar com pouco e depois aumentar aos poucos a frequência, a intensidade e a duração. Comparado a não treinar, o treino de força já melhora a força, a massa muscular e o equilíbrio. Para um iniciante, um primeiro programa simples basta.</p>
<p>Outros parâmetros pesam menos do que se pensa. Segundo o ACSM, treinar até a falha muscular ou mudar o tipo de equipamento não mudou os resultados de forma consistente. Um aluno sem academia pode seguir um programa de verdade, desde que a carga ou as repetições possam subir.</p>

<h2>Como dividir os treinos na semana?</h2>
<p>Escolha a partir da agenda do aluno. Uma meta-análise de 14 estudos e 392 pessoas (Ramos-Campo, 2024) não encontrou diferença significativa de força ou de massa muscular entre o treino de corpo inteiro (full body) e o treino dividido, com o mesmo volume. Os autores concluem que a escolha pode seguir as preferências.</p>
<p>Veja um exemplo de lógica, para ajustar:</p>
<ul>
<li><strong>2 treinos:</strong> corpo inteiro nas duas vezes.</li>
<li><strong>3 treinos:</strong> corpo inteiro, ou uma alternância entre membros superiores e inferiores.</li>
<li><strong>4 treinos ou mais:</strong> um treino dividido passa a ser possível, se o aluno mantiver de verdade esses dias.</li>
</ul>
<p>Pense na semana em que um treino cai: o treino dividido deixa um grupo muscular para trás, e o corpo inteiro não. Para um objetivo de força, coloque o exercício prioritário no começo do treino, como lembra o ACSM.</p>

<h2>Como fazer a progressão do treino?</h2>
<p>Escreva a regra no próprio programa, para o aluno saber o que dispara a etapa seguinte. Exemplo: quando todas as séries chegarem a 12 repetições bem feitas, a carga sobe e as repetições voltam para 8.</p>
<p>Você tem várias alavancas. Um ensaio com praticantes treinados (Plotkin, 2022, 43 no início, 38 no fim) mostra que acrescentar repetições ou acrescentar carga dá adaptações comparáveis em 8 semanas, com uma leve vantagem da carga para a força máxima. Isso ajuda em casa, quando a carga disponível chega ao limite. O estudo é curto e trata só do quadríceps e das panturrilhas.</p>
<p>Mude uma variável de cada vez, para saber o que produziu o quê. Segundo o ACSM, a periodização não mudou os resultados de forma consistente: reserve os planos complexos para um aluno avançado e reveja <a href="/articles/periodisation-entrainement-bases.html">as bases da periodização</a> se precisar.</p>

<h2>Quando ajustar o treino, e onde termina o seu papel?</h2>
<p>Depois de cada treino, colete o esforço percebido, os eventuais desconfortos e o que ficou de fora. Se o aluno faltar duas vezes seguidas ao mesmo tipo de treino, mude o programa antes de falar de motivação.</p>
<p>Três limites não mudam:</p>
<ul>
<li><strong>A saúde.</strong> Segundo a OMS, quem desenvolve sintomas novos ao aumentar a atividade deve procurar um profissional de saúde. Você pausa, encaminha e não interpreta.</li>
<li><strong>A nutrição.</strong> Você pode passar orientações gerais. Quanto mais pessoal o conselho, maior o risco, principalmente quando há uma condição médica envolvida.</li>
<li><strong>As regras da profissão.</strong> No Brasil, para orientar treinos, na academia, na casa do aluno ou online, você precisa estar registrado no CREF, e o Código de Ética do CONFEF vale tanto no trabalho presencial quanto em ambiente virtual. Em Portugal, numa academia, você precisa do título profissional de técnico de exercício físico, emitido pelo IPDJ, e planeja e prescreve o treino sob a coordenação e a supervisão do diretor técnico; a academia, por sua vez, precisa ter seguro. A Lei 39/2012, que traz essas regras, trata das instalações de fitness e não diz nada sobre o treino em casa, ao ar livre ou online.</li>
</ul>

<h2>Em resumo</h2>
<ul>
<li>O treino nasce da avaliação: objetivo, tempo real, nível, equipamento, limites.</li>
<li>Defina poucas variáveis, com uma regra de progressão escrita e uma divisão que o aluno vá manter.</li>
<li>Sintomas novos, nutrição e regras da profissão: esses limites vêm antes do programa.</li>
</ul>
""",
        "faq": [
            {"q": "Como montar um treino de força personalizado para o aluno?", "a": "Parta da avaliação: objetivo, tempo disponível de verdade, nível, equipamento e limites. Depois defina o volume e a intensidade conforme o objetivo, escolha uma divisão que ele vá manter, escreva uma regra de progressão e ajuste pelo retorno dele."},
            {"q": "Quantos treinos por semana o programa deve ter?", "a": "A OMS recomenda fortalecimento de todos os grandes grupos musculares em 2 dias ou mais por semana, e o ACSM, 2 treinos ou mais para a força. Para um iniciante, dois treinos de corpo inteiro são um bom começo. O número certo é o que o aluno mantém numa semana cheia."},
            {"q": "O personal trainer pode passar dieta para o aluno?", "a": "Você pode passar orientações gerais, sem se apresentar como nutricionista. A fronteira com o conselho individual não é nítida: quanto mais pessoal o conselho, maior o risco, principalmente com uma condição médica. Nesse caso, encaminhe o aluno a um médico ou nutricionista."},
        ],
        "sources": [
            {"t": "Currier BS, D'Souza AC, Singh MAF, et al. American College of Sports Medicine Position Stand. Resistance Training Prescription for Muscle Function, Hypertrophy, and Physical Performance in Healthy Adults: An Overview of Reviews. <em>Med Sci Sports Exerc</em>. 2026.", "u": "https://doi.org/10.1249/MSS.0000000000003897"},
            {"t": "Schoenfeld BJ, Ogborn D, Krieger JW. Dose-response relationship between weekly resistance training volume and increases in muscle mass: A systematic review and meta-analysis. <em>J Sports Sci</em>. 2017.", "u": "https://doi.org/10.1080/02640414.2016.1210197"},
            {"t": "Bull FC, Al-Ansari SS, Biddle S, et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. <em>Br J Sports Med</em>. 2020.", "u": "https://doi.org/10.1136/bjsports-2020-102955"},
            {"t": "Ramos-Campo DJ, Benito-Peinado PJ, Andreu-Caravaca L, et al. Efficacy of Split Versus Full-Body Resistance Training on Strength and Muscle Growth: A Systematic Review With Meta-Analysis. <em>J Strength Cond Res</em>. 2024.", "u": "https://doi.org/10.1519/JSC.0000000000004774"},
            {"t": "Plotkin D, Coleman M, Van Every D, et al. Progressive overload without progressing load? The effects of load or repetition progression on muscular adaptations. <em>PeerJ</em>. 2022.", "u": "https://doi.org/10.7717/peerj.14142"},
            {"t": "Lei nº 9.696, de 1º de setembro de 1998 (regulamentação da profissão de Educação Física), norma atualizada. Câmara dos Deputados.", "u": "https://www2.camara.leg.br/legin/fed/lei/1998/lei-9696-1-setembro-1998-374623-normaatualizada-pl.html"},
            {"t": "CREF12/PE. Código de Ética Profissional de Educação Física (Resolução CONFEF nº 508/2023).", "u": "https://www.cref12.org.br/codigo-de-etica/"},
            {"t": "Lei n.º 39/2012 (atividades desportivas em ginásios, academias e clubes de saúde), versão consolidada. Diário da República.", "u": "https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2012-155873811"},
        ],
    },
    {
        "fr": "fideliser-clients-coaching-sportif",
        "slug": "fidelizar-alunos-personal-trainer",
        "title": "Por que seus alunos desistem: como fidelizar alunos de personal",
        "seo_title": "Como fidelizar alunos de personal trainer: por que desistem",
        "description": "Como fidelizar alunos de personal trainer: por que eles desistem, o que os estudos de abandono mostram de verdade e como calcular a sua taxa de retenção.",
        "body": """
<p>A resposta curta: para <strong>fidelizar alunos como personal trainer</strong>, comece medindo quem sai e por quê, porque nenhuma estatística vai fazer isso por você. Não encontrei nenhuma taxa de abandono específica de personal trainers autônomos. A pesquisa apoia sobretudo três alavancas simples: um objetivo escrito, um progresso registrado e um retorno regular. O resto está na sua própria lista de alunos.</p>

<h2>Quantos alunos desistem de verdade?</h2>
<p>O único número sólido que guardei vem de uma academia do Rio de Janeiro. Sperandei e colegas acompanharam 5.240 matriculados: 63% tinham desistido antes do terceiro mês, e menos de 4% passaram de doze meses de atividade contínua. O estudo, publicado em 2016, trata de uma única academia, usa os dados de matrícula dela e foi feito num contexto sem supervisão, como diz o título. Ele não vale, portanto, nem para todas as academias nem para um aluno que treina com personal. Desconfie das porcentagens de abandono que circulam sem referência.</p>
<p>O seu número real leva dez minutos para calcular. Pegue os seus alunos ativos no início de um trimestre e conte quantos continuam no fim, sem somar os novos. Exemplo de cálculo: 12 alunos em 1º de janeiro, 9 ainda ativos em 31 de março, ou seja, 9 ÷ 12 = 75% de retenção em três meses. Com tão poucos alunos, uma única saída pesa mais de 8 pontos. Leia essa taxa ao longo do ano e olhe, sobretudo, os motivos.</p>

<h2>Por que os alunos de personal desistem?</h2>
<p>Nenhum dos estudos citados aqui responde a isso para o aluno de um personal autônomo. A sua melhor fonte continua sendo os seus ex-alunos. Esta grade de trabalho, sem valor estatístico, ajuda a classificar cada saída:</p>
<ul>
<li><strong>Saída planejada:</strong> o objetivo foi atingido, ou o aluno agora sabe treinar sozinho. É um sucesso, e talvez uma futura indicação.</li>
<li><strong>Saída forçada:</strong> mudança de cidade, orçamento, novo horário de trabalho, nascimento de um filho, saúde. Às vezes você pode oferecer um formato mais leve ou a consultoria online.</li>
<li><strong>Saída evitável:</strong> progresso invisível, treinos todos iguais, objetivo nunca revisto, horário que deixou de funcionar, relação que se desgastou.</li>
</ul>
<p>Faça três perguntas a cada aluno que sai: o que fez você tomar a decisão, o que teria feito você ficar, o que você diria a alguém pensando em começar? Anote as respostas palavra por palavra. «Não tenho mais como pagar» também pode querer dizer «não vejo mais o que ganho com isso». Se o mesmo motivo aparecer várias vezes no ano, você encontrou a sua prioridade número um.</p>

<h2>O que faz um aluno ficar a longo prazo?</h2>
<p>Os trabalhos que selecionei não tratam do atendimento individual de um personal autônomo, mas dão uma direção.</p>
<ul>
<li><strong>Acompanhe o progresso.</strong> A meta-análise de Harkin e colegas (2016, 138 ensaios, 19.951 pessoas) encontra um efeito médio de 0,40 sobre o alcance dos objetivos, maior quando o resultado é registrado ou compartilhado. Ela não se limita ao exercício.</li>
<li><strong>Vá além do automonitoramento.</strong> Em 122 avaliações e 44.747 pessoas, Michie e colegas (2009) mostram que as intervenções que o combinam com outra técnica da teoria do controle chegam a um efeito de 0,42, contra 0,26 nas outras.</li>
<li><strong>Acerte o contexto.</strong> A síntese de 55 revisões de Collado-Mateo (2021) lista, entre outros fatores, a supervisão, o retorno, o acompanhamento do progresso, os objetivos, o apoio social e o prazer. Ela trata de pacientes com doença crônica e de idosos, não de todo aluno que um personal atende.</li>
</ul>
<p>Na prática: o aluno registra, você responde, e vocês revisam o objetivo juntos. Um <a href="/coachs/bilan-mensuel-client-coaching.html">relatório mensal de uma página</a> basta para dar esse ritmo.</p>

<h2>Quando agir para não perder o aluno?</h2>
<p>Não espere o aluno anunciar que vai sair. Quatro momentos pedem ação:</p>
<ul>
<li><strong>As primeiras semanas.</strong> Na academia do Rio, o abandono veio cedo, e <a href="/articles/combien-de-temps-pour-prendre-une-habitude.html">um hábito leva tempo para se formar</a>. Marque uma conversa rápida por volta da terceira semana: o que funciona, o que não funciona.</li>
<li><strong>O fim de um pacote.</strong> Fale do que vem depois duas ou três aulas antes da última, com o relatório na mão. <a href="/coachs/packs-abonnement-seance-coach-sportif.html">O plano que você oferece</a> também pesa nesse momento.</li>
<li><strong>Objetivo atingido.</strong> Definam juntos o próximo, ou prepare uma saída bem feita, com o que ele precisa para continuar sozinho.</li>
<li><strong>Faltas repetidas.</strong> Aplique a <a href="/coachs/seance-annulee-regles-coach.html">sua política de cancelamento</a> e depois pergunte o que mudou na semana dele.</li>
</ul>
<p>Não conte com o contrato para segurar ninguém. Antes de escrever para um ex-aluno, confirme que você tem esse direito e ofereça, em cada mensagem, um jeito simples de recusar. Em Portugal, se o plano renova automaticamente, o prazo para o aluno avisar que não quer renovar não pode ficar longe demais do fim do contrato; e, como em toda a União Europeia, e-mails e SMS comerciais exigem o consentimento prévio da pessoa, salvo para clientes cujo contato você obteve ao vender um serviço, que podem receber mensagens sobre serviços seus semelhantes se tiverem, desde a coleta dos dados e em cada mensagem, um jeito simples e gratuito de recusar. No Brasil, confira também as regras de renovação automática e de mensagens comerciais antes de usá-las.</p>

<h2>Em resumo</h2>
<ul>
<li>Nenhuma taxa geral de abandono descreve o seu negócio: calcule a sua retenção com os seus próprios alunos e anote cada motivo de saída.</li>
<li>Objetivo escrito, progresso registrado, retorno regular: essas alavancas têm o melhor apoio, mesmo que os estudos não tratem de personal autônomo.</li>
<li>Aja antes da saída: primeiras semanas, fim de pacote, objetivo atingido, faltas repetidas.</li>
</ul>
""",
        "faq": [
            {"q": "Como fidelizar alunos de personal trainer?", "a": "Defina um objetivo escrito, registre o progresso, faça reavaliações regulares e fale do que vem depois antes de o pacote acabar. Pergunte também a cada aluno que sai o que o teria feito ficar: os seus próprios motivos de saída vão ensinar mais do que uma estatística geral."},
            {"q": "Qual é a taxa de desistência nas academias?", "a": "Não encontrei nenhum número geral confiável. Numa academia do Rio de Janeiro estudada com 5.240 matriculados, 63% tinham desistido antes do terceiro mês. Esse resultado vem de uma única academia, num contexto sem supervisão, e não vale nem para todas as academias nem para um aluno que treina com personal."},
            {"q": "Como calcular a taxa de retenção de alunos?", "a": "Pegue os seus alunos ativos no início de um trimestre e conte quantos continuam no fim, sem somar os novos. Por exemplo, 12 alunos em 1º de janeiro e 9 ainda ativos em 31 de março dão 9 ÷ 12 = 75% em três meses. Com poucos alunos, leia a taxa ao longo do ano."},
        ],
        "sources": [
            {"t": "Sperandei S, Vieira MC, Reis AC. Adherence to physical activity in an unsupervised setting: Explanatory variables for high attrition rates among fitness center members. <em>J Sci Med Sport</em>. 2016.", "u": "https://doi.org/10.1016/j.jsams.2015.12.522"},
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychol Bull</em>. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
            {"t": "Michie S, Abraham C, Whittington C, McAteer J, Gupta S. Effective techniques in healthy eating and physical activity interventions: a meta-regression. <em>Health Psychol</em>. 2009.", "u": "https://doi.org/10.1037/a0016136"},
            {"t": "Collado-Mateo D, Lavín-Pérez AM, Peñacoba C, et al. Key Factors Associated with Adherence to Physical Exercise in Patients with Chronic Diseases and Older Adults: An Umbrella Review. <em>Int J Environ Res Public Health</em>. 2021.", "u": "https://doi.org/10.3390/ijerph18042023"},
            {"t": "Decreto-Lei n.º 446/85 (cláusulas contratuais gerais), versão consolidada. Diário da República.", "u": "https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/1985-34436475"},
            {"t": "Diretiva 2002/58/CE do Parlamento Europeu e do Conselho, de 12 de julho de 2002 (privacidade e comunicações eletrónicas), versão consolidada. EUR-Lex.", "u": "https://eur-lex.europa.eu/legal-content/PT/TXT/HTML/?uri=CELEX:02002L0058-20091219"},
        ],
    },
    {
        "fr": "bilan-mensuel-client-coaching",
        "slug": "relatorio-mensal-evolucao-aluno",
        "title": "Relatório mensal de evolução do aluno: o que mostrar",
        "description": "Relatório mensal de evolução do aluno: que medidas mostrar, como compará-las, como conduzir a reavaliação e como tratar os dados de saúde do aluno.",
        "body": """
<p>A resposta curta: um <strong>relatório mensal de evolução do aluno</strong> cabe numa página e responde a quatro perguntas: como está o objetivo, o que vocês fizeram, o que mudou e o que muda no mês seguinte. Mostre de três a cinco medidas, sempre comparadas com o próprio aluno, e termine com uma decisão por escrito. O ritmo mensal é uma escolha prática, que os estudos citados aqui não fixam.</p>

<h2>Por que fazer uma reavaliação todo mês?</h2>
<p>De um treino para o outro, o aluno tem dificuldade de ver o próprio progresso. O relatório o torna visível. A meta-análise de Harkin e colegas (2016, 138 ensaios, 19.951 pessoas) mostra que acompanhar o progresso ajuda a atingir os objetivos, com um efeito maior quando o resultado é registrado ou compartilhado. Ela não se limita ao exercício, mas um relatório cumpre as duas condições: fica por escrito e é compartilhado com você.</p>
<p>Ele também ajuda você a tomar uma decisão em vez de repetir o mesmo programa, e dá uma base para <a href="/coachs/fideliser-clients-coaching-sportif.html">manter um aluno a longo prazo</a>. Um mês já dá material sobre frequência e cargas. Um teste de campo pode esperar dois ou três meses.</p>

<h2>O que colocar no relatório mensal do aluno?</h2>
<p>Escolha conforme o objetivo do aluno. Esta grade cobre a maioria dos casos:</p>
<div class="tablewrap"><table>
<caption>Fonte: grade de trabalho deste guia, para adaptar a cada aluno.</caption>
<thead><tr><th>Medida</th><th>O que você mostra</th><th>Cuidado</th></tr></thead>
<tbody>
<tr><td>Frequência</td><td>Treinos feitos sobre treinos previstos</td><td>Separe as faltas inevitáveis das outras</td></tr>
<tr><td>Carga</td><td>Esforço percebido multiplicado pela duração, semana a semana</td><td>Compare com o próprio aluno, nunca com outra pessoa</td></tr>
<tr><td>Desempenho</td><td>Dois ou três exercícios de referência: carga, repetições, tempo</td><td>Mantenha o mesmo exercício e as mesmas instruções</td></tr>
<tr><td>Teste de campo</td><td>Um teste só, se ele servir ao objetivo</td><td>Mesmas condições a cada vez</td></tr>
<tr><td>Como ele se sente</td><td>Energia, sono, prazer, com notas de 1 a 5</td><td>Orienta a conversa e não diagnostica nada</td></tr>
<tr><td>Peso, medidas</td><td>Só se for o objetivo dele e ele concordar</td><td>Nunca a única medida de sucesso</td></tr>
</tbody>
</table></div>
<p>Para a carga, o método mais simples continua sendo a PSE da sessão (percepção subjetiva de esforço): uma nota de esforço multiplicada pela duração. Foster e colegas avaliaram o método em 2001 em comparação com um método baseado na frequência cardíaca e o consideraram válido para esforços variados. A escolha dos testes está no nosso guia sobre <a href="/coachs/tests-physiques-nouveau-client.html">testes físicos para aluno novo</a>.</p>

<h2>Como comparar os resultados do aluno sem erro?</h2>
<p>A única comparação útil coloca o aluno diante dele mesmo, em condições iguais: mesmo exercício, mesmas instruções, mesmo horário, mesmo aquecimento. Esse rigor conta. Para a caminhada de 6 minutos, a norma europeia e americana de 2014 lembra que os resultados são sensíveis a pequenas diferenças de método e recomenda duas tentativas. Esse teste foi validado em doenças respiratórias crônicas: com um aluno saudável, ele só serve para comparar o aluno com ele mesmo.</p>
<p>Desconfie também dos testes que prometem demais. No estudo de Sartor e colegas (2016, 81 adultos saudáveis), o índice de Ruffier-Dickson explica só 15% da variabilidade da aptidão cardiorrespiratória. Use-o como um marcador simples e não tire dele um VO2 máx. Leia qualquer diferença ao longo de vários meses: uma queda isolada pode vir de uma semana cheia, de uma viagem ou de um resfriado.</p>

<h2>Como conduzir a reavaliação com o aluno?</h2>
<p>De quinze a vinte minutos bastam, durante um treino ou por videochamada. Um roteiro possível:</p>
<ol>
<li>Comece perguntando como foi o mês, antes de mostrar qualquer número.</li>
<li>Mostre o que melhorou, com o número de partida ao lado.</li>
<li>Apresente o que estagnou como fatos: «6 treinos de 8», sem comentário sobre força de vontade.</li>
<li>Procurem a causa juntos: agenda, sono, programa ambicioso demais, objetivo desatualizado.</li>
<li>Decidam de uma a três mudanças e anote o objetivo do mês seguinte.</li>
</ol>
<p>Trate um mês ruim da mesma forma. Se o aluno não consegue manter três treinos por semana, adapte o programa à semana real dele. Não prometa nenhum resultado para o mês seguinte. Se ele mencionar um sintoma novo, uma doença ou um transtorno alimentar, você não interpreta: encaminha a um médico ou nutricionista.</p>

<h2>O que fazer com os dados do relatório?</h2>
<p>Um relatório costuma ter dados sensíveis. Histórico médico, doenças e tratamentos são dados de saúde por natureza, e o peso também pode virar dado de saúde, principalmente cruzado com a contagem de passos ou com as calorias. No Brasil, a LGPD coloca as informações de saúde entre os dados sensíveis: se a base for o consentimento, ele precisa ser específico e destacado, para uma finalidade clara, e a autoridade é a ANPD (Agência Nacional de Proteção de Dados). Em Portugal, como em toda a União Europeia, os dados de saúde têm proteção especial; a autoridade é a CNPD, e esses dados só devem ser acessados por quem realmente precisa deles. Peça o consentimento à parte do contrato e guarde esses documentos num espaço protegido.</p>
<p>O relatório fica entre você e o aluno. Compartilhe com um médico, um fisioterapeuta, outro personal ou um familiar só com o acordo dele. O mais simples: entregue o relatório a ele, e ele compartilha se quiser. Antes de publicar uma foto de antes e depois em que ele possa ser reconhecido, peça uma autorização por escrito que diga o meio, a finalidade e a duração: nem no Brasil nem em Portugal a lei exige a forma escrita, mas o documento serve de prova. Concordar em ser fotografado não basta. Em Portugal, o aluno pode, além disso, retirar o consentimento depois.</p>

<h2>Em resumo</h2>
<ul>
<li>Uma página, de três a cinco medidas, uma decisão por escrito: o relatório existe para mudar algo no mês seguinte.</li>
<li>Compare o aluno com ele mesmo, em condições iguais, e leia as diferenças ao longo de vários meses.</li>
<li>Os dados do relatório pertencem ao aluno: consentimento à parte, espaço protegido, nada de compartilhar sem o acordo dele.</li>
</ul>
""",
        "faq": [
            {"q": "O que colocar no relatório mensal do aluno de personal?", "a": "O objetivo de partida, a frequência, duas ou três medidas de desempenho, como o aluno se sente e as mudanças decididas para o mês seguinte. Uma página basta. Compare cada número com o próprio aluno, nunca com uma média ou com outro aluno."},
            {"q": "Devo pesar o aluno em toda reavaliação?", "a": "Só se o peso corresponder ao objetivo dele e ele concordar. Esse número nunca deve ser a única medida de sucesso, e ele pode contar como dado de saúde. Se o aluno mencionar um transtorno alimentar ou uma doença, encaminhe a um médico ou nutricionista."},
            {"q": "O personal pode mandar o relatório do aluno para o médico ou o fisioterapeuta?", "a": "Só com o acordo do aluno. O mais simples é entregar o relatório a ele, para que ele mesmo o repasse. Sem esse acordo, não envie a ninguém, nem a um profissional de saúde."},
        ],
        "sources": [
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychol Bull</em>. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
            {"t": "Foster C, Florhaug JA, Franklin J, et al. A new approach to monitoring exercise training. <em>J Strength Cond Res</em>. 2001.", "u": "https://pubmed.ncbi.nlm.nih.gov/11708692/"},
            {"t": "Holland AE, Spruit MA, Troosters T, et al. An official European Respiratory Society/American Thoracic Society technical standard: field walking tests in chronic respiratory disease. <em>Eur Respir J</em>. 2014.", "u": "https://doi.org/10.1183/09031936.00150314"},
            {"t": "Sartor F, Bonato M, Papini G, et al. A 45-Second Self-Test for Cardiorespiratory Fitness: Heart Rate-Based Estimation in Healthy Individuals. <em>PLoS One</em>. 2016.", "u": "https://doi.org/10.1371/journal.pone.0168154"},
            {"t": "Lei nº 13.709, de 14 de agosto de 2018 (Lei Geral de Proteção de Dados Pessoais), norma atualizada. Câmara dos Deputados.", "u": "https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-normaatualizada-pl.html"},
            {"t": "Lei nº 10.406, de 10 de janeiro de 2002 (Código Civil), norma atualizada. Câmara dos Deputados.", "u": "https://www2.camara.leg.br/legin/fed/lei/2002/lei-10406-10-janeiro-2002-432893-normaatualizada-pl.html"},
            {"t": "Lei n.º 58/2019, de 8 de agosto (execução do Regulamento Geral sobre a Proteção de Dados). Diário da República.", "u": "https://diariodarepublica.pt/dr/detalhe/lei/58-2019-123815982"},
            {"t": "Código Civil (Decreto-Lei n.º 47344/66), versão consolidada. Diário da República.", "u": "https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/1966-34509075"},
        ],
    },
    {
        "fr": "lire-etat-de-forme-client",
        "slug": "prontidao-do-aluno-antes-do-treino",
        "title": "Sono, cansaço, carga de treino: como avaliar o aluno antes do treino",
        "seo_title": "Prontidão do aluno: como avaliar antes do treino",
        "description": "Prontidão do aluno para o treino: o que perguntar antes, o que uma noite curta muda, como acompanhar a carga e o que relógios e VFC dizem de verdade.",
        "body": """
<p>A resposta curta: para avaliar a <strong>prontidão do aluno para o treino</strong>, faça três perguntas antes do aquecimento, compare as respostas com o que é normal para aquele aluno e ajuste o treino quando vários sinais apontam na mesma direção. Nenhum marcador sozinho basta: nem o sono, nem a variabilidade da frequência cardíaca, nem a nota de um relógio inteligente. Essas medidas ajudam a dosar um esforço. Não fazem diagnóstico.</p>

<h2>O que perguntar ao aluno antes do treino?</h2>
<p>Dois minutos bastam. Mantenha as mesmas perguntas e a mesma escala de 1 a 5:</p>
<ul>
<li>Como você dormiu, comparado com o normal?</li>
<li>Quanta energia você tem hoje, contando o estresse?</li>
<li>Você tem alguma dor ou desconforto novo?</li>
</ul>
<p>A revisão de Saw e colegas (2016, 56 estudos) mostra que as medidas subjetivas e as objetivas concordam pouco, e que as subjetivas refletem melhor a carga de treino. Ela trata de atletas, então aplique com cautela. Anote cada resposta, porque só a diferença em relação ao normal do aluno diz alguma coisa. Um 2 de um aluno que sempre responde 4 pesa mais do que um 2 de quem responde 2 com frequência.</p>

<h2>Uma noite mal dormida deve mudar o treino?</h2>
<p>Não necessariamente. A meta-análise de Craven e colegas (2022, 69 publicações, 959 participantes, 89% deles homens) encontra um desempenho 7,56% menor, em média, depois de 6 horas de sono ou menos, com uma heterogeneidade muito alta entre os estudos. Duas nuances ajudam na prática:</p>
<ul>
<li><strong>O tipo de noite.</strong> Os efeitos só foram consistentes depois de uma noite em claro ou de um despertar cedo, não depois de dormir tarde. A queda chegava então a cerca de 0,4% por hora acordado antes do exercício.</li>
<li><strong>O horário do treino.</strong> Os esforços à tarde e à noite foram afetados, os da manhã muito pouco.</li>
</ul>
<p>Um aluno que acordou às 5h e chega às 19h não está na mesma situação que outro que foi dormir tarde e chega às 8h. Essas médias também não preveem o treino dele: veja como ele responde ao aquecimento antes de mudar qualquer coisa.</p>

<h2>Como acompanhar a carga de treino sem equipamento?</h2>
<p>Peça ao aluno uma nota de 0 a 10 para o esforço depois do treino e multiplique essa nota pela duração: é a PSE da sessão (percepção subjetiva de esforço). Exemplo de cálculo: 60 minutos com nota 7 dão 420 unidades. Foster e colegas avaliaram o método em 2001 em comparação com um método baseado na frequência cardíaca e o consideraram válido para esforços variados. Some os treinos, incluindo o exercício feito sem você, e compare as semanas entre si.</p>
<p>Essa nota descreve o que o aluno sentiu. As suas cargas, séries e distâncias descrevem o que ele fez. Para o mesmo trabalho, um esforço percebido que sobe ao longo de vários treinos merece uma pergunta. Deixe de lado, porém, a razão entre carga aguda e crônica (ACWR) para prevenir lesões: Impellizzeri e colegas concluíram em 2020 que nenhuma evidência apoia esse uso.</p>

<h2>Relógios inteligentes e VFC são confiáveis?</h2>
<p>Leia esses dados como tendências, com limites conhecidos.</p>
<ul>
<li><strong>Sono.</strong> Em Chinoy e colegas (2021), sete aparelhos de consumo da época, usados no corpo ou colocados perto da cama e comparados com a polissonografia em 34 adultos jovens saudáveis, detectaram bem o sono (sensibilidade de pelo menos 0,93) e pior a vigília (especificidade de 0,18 a 0,54). As fases do sono foram inconsistentes, e as noites agitadas foram medidas pior. Ignore o número de «sono profundo» de uma noite.</li>
<li><strong>Variabilidade da frequência cardíaca (VFC).</strong> Segundo a meta-análise de Bellenger e colegas (2016, 27 estudos), ela sobe em repouso quando a adaptação é positiva e muda pouco com o overreaching (excesso de treino de curto prazo). Um valor baixo não prova overtraining, e um valor normal não o descarta. Esses estudos tratam de atletas de resistência, longe do aluno médio.</li>
<li><strong>Medição.</strong> A <a href="/methode/variabilite-cardiaque.html">variabilidade da frequência cardíaca</a> depende do sensor, da forma de usar o relógio, de batimentos irregulares ou de um remédio que diminui a frequência cardíaca. Você não pode compará-la de um aparelho para outro.</li>
<li><strong>Referência.</strong> Só a <a href="/methode/ligne-de-base.html">linha de base</a> do próprio aluno, construída ao longo de várias semanas, quer dizer alguma coisa. Ela mostra se ele está se afastando dos próprios hábitos, sem dizer se esses hábitos são bons, e um desvio lento pode passar despercebido.</li>
<li><strong>Notas de recuperação.</strong> Elas resumem esses sinais, com os mesmos limites. Uma nota baixa não proíbe nada, e uma nota alta não autoriza nada.</li>
</ul>
<p>Esses dados pertencem ao aluno. Ele os mostra a você se quiser, com o consentimento explícito dele, e você não os repassa a ninguém sem ele. Nunca faça o treino depender desse compartilhamento. No Brasil, essas informações de saúde são dados sensíveis pela LGPD: se a base for o consentimento, ele precisa ser específico e destacado. Em Portugal, como em toda a União Europeia, os dados de saúde têm proteção especial.</p>

<h2>Quando ajustar o treino, e quando encaminhar ao médico?</h2>
<p>Busque a convergência: diante de um sinal isolado, você observa; diante de vários, você age.</p>
<div class="tablewrap"><table>
<caption>Fonte: referências prudentes deste guia, sem valor diagnóstico.</caption>
<thead><tr><th>O que você observa</th><th>Decisão possível</th></tr></thead>
<tbody>
<tr><td>Noite curta, energia razoável, bom aquecimento</td><td>Treino previsto</td></tr>
<tr><td>Noite curta e pouca energia, treino à tarde ou à noite</td><td>Menos volume, nenhuma carga máxima</td></tr>
<tr><td>Esforço percebido subindo ao longo de vários treinos</td><td>Semana mais leve, procurar a causa com o aluno</td></tr>
<tr><td>Dor que muda o movimento</td><td>Tirar o exercício, parecer médico se persistir</td></tr>
<tr><td>Cansaço incomum que dura apesar de uma carga mais leve</td><td>Encaminhar ao médico</td></tr>
<tr><td>Mal-estar, dor no peito, falta de ar anormal, palpitações</td><td>Parar na hora, procurar um médico e, em emergência, ligar 192 (SAMU) no Brasil ou 112 em Portugal</td></tr>
</tbody>
</table></div>
<p>Você não precisa dar nome ao que está acontecendo. «Overtraining» e «deficiência nutricional» são conclusões médicas. Descreva o que observa, sugira uma consulta e leve as tendências para o seu <a href="/coachs/bilan-mensuel-client-coaching.html">relatório mensal</a>.</p>

<h2>Em resumo</h2>
<ul>
<li>Três perguntas com nota a cada treino já dão o essencial: a diferença em relação ao normal do aluno.</li>
<li>Sono, carga, relógio e variabilidade da frequência cardíaca se leem juntos e como tendência. Nenhum basta sozinho.</li>
<li>Você ajusta o treino e não diagnostica: um sintoma novo ou um cansaço que dura é assunto de médico.</li>
</ul>
""",
        "faq": [
            {"q": "Como saber se o aluno está cansado demais para treinar?", "a": "Pergunte como ele dormiu, quanta energia tem e se tem dor nova, depois observe como ele responde ao aquecimento. Se vários sinais caírem, alivie o treino. Se o cansaço durar ou vier com sintomas, encaminhe ao médico."},
            {"q": "Devo cancelar o treino depois de uma noite mal dormida?", "a": "Não necessariamente. Uma noite curta reduz o desempenho em média, sobretudo à tarde ou à noite e depois de um despertar cedo, mas a resposta varia de pessoa para pessoa. Mantenha o treino se o aluno responder bem ao aquecimento e, se não, reduza o volume ou a intensidade."},
            {"q": "VFC baixa significa overtraining?", "a": "Não. Os resultados são contraditórios e, segundo uma meta-análise de 2016 com atletas de resistência, a VFC de repouso muda pouco com o overreaching. Uma queda isolada pode vir de uma noite ruim ou de uma medição menos limpa. Leia a tendência, junto com o que o aluno sente."},
        ],
        "sources": [
            {"t": "Saw AE, Main LC, Gastin PB. Monitoring the athlete training response: subjective self-reported measures trump commonly used objective measures: a systematic review. <em>Br J Sports Med</em>. 2016.", "u": "https://doi.org/10.1136/bjsports-2015-094758"},
            {"t": "Craven J, McCartney D, Desbrow B, et al. Effects of Acute Sleep Loss on Physical Performance: A Systematic and Meta-Analytical Review. <em>Sports Med</em>. 2022.", "u": "https://doi.org/10.1007/s40279-022-01706-y"},
            {"t": "Foster C, Florhaug JA, Franklin J, et al. A new approach to monitoring exercise training. <em>J Strength Cond Res</em>. 2001.", "u": "https://pubmed.ncbi.nlm.nih.gov/11708692/"},
            {"t": "Impellizzeri FM, Tenan MS, Kempton T, Novak A, Coutts AJ. Acute:Chronic Workload Ratio: Conceptual Issues and Fundamental Pitfalls. <em>Int J Sports Physiol Perform</em>. 2020.", "u": "https://doi.org/10.1123/ijspp.2019-0864"},
            {"t": "Chinoy ED, Cuellar JA, Huwa KE, et al. Performance of seven consumer sleep-tracking devices compared with polysomnography. <em>Sleep</em>. 2021.", "u": "https://doi.org/10.1093/sleep/zsaa291"},
            {"t": "Bellenger CR, Fuller JT, Thomson RL, et al. Monitoring Athletic Training Status Through Autonomic Heart Rate Regulation: A Systematic Review and Meta-Analysis. <em>Sports Med</em>. 2016.", "u": "https://doi.org/10.1007/s40279-016-0484-2"},
            {"t": "Lei nº 13.709, de 14 de agosto de 2018 (Lei Geral de Proteção de Dados Pessoais), norma atualizada. Câmara dos Deputados.", "u": "https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-normaatualizada-pl.html"},
            {"t": "Ministério da Saúde. SAMU 192.", "u": "https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/s/samu-192"},
        ],
    },
]

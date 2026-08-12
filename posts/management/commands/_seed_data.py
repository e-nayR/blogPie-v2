# -*- coding: utf-8 -*-
"""Biblioteca de conteudo para o seed de posts (modelagem de busca semantica).

O conteudo e real e agrupado por categoria/tema. O gerador em ``seed_posts.py``
recombina temas e fatos em artigos longos e coerentes. Cada tema traz:

- ``name``: sintagma nominal usado em titulos e cabecalhos de secao.
- ``subtitles``: opcoes de subtitulo para o post.
- ``lead``: frase de abertura da secao.
- ``facts``: sentencas concretas que compoem os paragrafos.
"""

# ---------------------------------------------------------------------------
# Blocos genericos de moldura (compartilhados entre todas as categorias)
# ---------------------------------------------------------------------------

INTRO_FRAMES = [
    "Poucos assuntos dentro de {categoria} despertam tanto debate quanto {tema}.",
    "Compreender {tema} exige olhar para alem das aparencias e reconstruir seu contexto.",
    "Este artigo percorre {tema}, situando-o no panorama mais amplo de {categoria}.",
    "Ao tratar de {tema}, e preciso reunir historia, teoria e observacao atenta do presente.",
    "{tema} ocupa um lugar central em qualquer discussao seria sobre {categoria}.",
    "Ha muito a dizer sobre {tema}, e o percurso a seguir tenta organizar esse debate.",
]

CONNECTORS = [
    "Alem disso,",
    "Nesse sentido,",
    "Por outro lado,",
    "Vale lembrar que",
    "Nao por acaso,",
    "Como consequencia,",
    "Em paralelo,",
    "Convem destacar que",
    "Ao mesmo tempo,",
    "Em contrapartida,",
]

ELABORATIONS = [
    "O fenomeno nao pode ser compreendido de forma isolada, pois se conecta a processos mais amplos.",
    "As implicacoes desse quadro se estendem muito alem do que uma leitura apressada sugere.",
    "Ha aqui uma tensao produtiva entre continuidade e ruptura que merece atencao.",
    "Especialistas divergem sobre o peso relativo de cada fator envolvido nessa dinamica.",
    "O tema resiste a simplificacoes e recompensa quem se dispoe a examina-lo com cuidado.",
    "Essa dinamica ganha contornos proprios quando observada ao longo do tempo.",
    "Trata-se de um debate em aberto, sujeito a revisoes a luz de novas evidencias.",
    "Reconhecer a complexidade envolvida e o primeiro passo para uma analise honesta.",
    "Os efeitos praticos aparecem tanto no cotidiano quanto nas grandes decisoes coletivas.",
]

CONCLUSION_FRAMES = [
    "Em sintese, {tema} revela como {categoria} esta longe de ser um territorio estavel ou consensual.",
    "Ao final deste percurso, fica claro que {tema} continuara a alimentar debates dentro de {categoria}.",
    "Mais do que respostas definitivas, {tema} oferece um convite permanente a reflexao.",
    "O balanco de {tema} sugere que ainda ha muito a investigar e a discutir.",
    "Retomar {tema} com rigor ajuda a enxergar {categoria} com outros olhos.",
]

TITLE_STYLES = [
    "{tema}",
    "Entenda {tema}",
    "{tema}: um panorama",
    "Ensaio sobre {tema}",
    "Notas sobre {tema}",
    "Um olhar sobre {tema}",
    "{tema} em perspectiva",
    "O que esta em jogo em {tema}",
    "{tema}: historia e debates",
    "Repensando {tema}",
    "Guia para entender {tema}",
]

TITLE_ANGLES = [
    "",
    ": uma introducao",
    ": debates atuais",
    ": historia e legado",
    ": o que esta em jogo",
    ": leituras contemporaneas",
    ": mitos e realidades",
    ": um balanco",
    ": origens e desdobramentos",
]

# ---------------------------------------------------------------------------
# Conteudo por categoria
# ---------------------------------------------------------------------------

CATEGORIES = {
    "Literatura": [
        {
            "name": "o Romantismo na literatura brasileira",
            "subtitles": [
                "Do indianismo de Alencar a poesia de Goncalves Dias",
                "Como o Romantismo ajudou a inventar uma identidade nacional",
            ],
            "lead": "O Romantismo brasileiro floresceu no seculo XIX e associou a construcao da nacao a uma literatura de forte apelo emocional.",
            "facts": [
                "O movimento ganhou impulso apos a independencia de 1822, quando escritores buscaram temas e paisagens genuinamente brasileiros.",
                "Jose de Alencar consolidou o romance indianista com obras como O Guarani e Iracema, idealizando o indio como heroi nacional.",
                "Goncalves Dias eternizou a saudade da patria na Cancao do Exilio, um dos poemas mais citados do idioma.",
                "A prosa urbana de Alencar, em Senhora e LucIola, retratou os costumes e os interesses da sociedade do Segundo Reinado.",
                "Castro Alves ficou conhecido como o poeta dos escravos, levando a causa abolicionista para dentro dos versos.",
                "O ultrarromantismo de Alvares de Azevedo cultivou o gosto pela melancolia, pela morte e pelo amor idealizado.",
            ],
        },
        {
            "name": "o Realismo e a obra de Machado de Assis",
            "subtitles": [
                "A ironia que desmontou a sociedade do Segundo Reinado",
                "Por que Machado continua atual",
            ],
            "lead": "O Realismo deslocou o foco do sentimentalismo romantico para a analise critica e ironica da sociedade.",
            "facts": [
                "Memorias Postumas de Bras Cubas, de 1881, inaugurou uma nova fase ao ser narrado por um defunto autor.",
                "Machado de Assis criou em Dom Casmurro a ambiguidade insoluvel sobre a suposta traicao de Capitu.",
                "A ironia machadiana expoe o egoismo, a hipocrisia e as convencoes da elite carioca do seculo XIX.",
                "Quincas Borba satiriza o oportunismo social por meio da filosofia ficticia do Humanitismo.",
                "Machado foi o primeiro presidente da Academia Brasileira de Letras, fundada em 1897.",
                "Sua prosa influenciou geracoes e e hoje estudada em universidades de todo o mundo.",
            ],
        },
        {
            "name": "o Modernismo e a Semana de 22",
            "subtitles": [
                "A ruptura estetica que sacudiu Sao Paulo",
                "Antropofagia, verso livre e a cara nova do Brasil",
            ],
            "lead": "A Semana de Arte Moderna de 1922 marcou a virada estetica que buscou uma expressao artistica autenticamente brasileira.",
            "facts": [
                "Realizada no Teatro Municipal de Sao Paulo, a Semana reuniu Mario de Andrade, Oswald de Andrade e Anita Malfatti.",
                "Macunaima, de Mario de Andrade, e um heroi sem nenhum carater que sintetiza a diversidade cultural do pais.",
                "O Manifesto Antropofago de Oswald propos devorar as influencias estrangeiras para criar algo novo e proprio.",
                "O verso livre e a linguagem coloquial romperam com o rigor formal do Parnasianismo.",
                "A segunda fase modernista consagrou o romance regionalista e a poesia madura de Drummond.",
                "O movimento reverberou nas artes plasticas, na musica e no design das decadas seguintes.",
            ],
        },
        {
            "name": "a poesia brasileira do seculo XX",
            "subtitles": [
                "De Drummond a Cecilia Meireles",
                "As muitas vozes do verso moderno",
            ],
            "lead": "A poesia brasileira do seculo XX combinou experimentacao formal e profunda investigacao da condicao humana.",
            "facts": [
                "Carlos Drummond de Andrade fez do cotidiano e da ironia materia de uma poesia densa e reflexiva.",
                "No meio do caminho tinha uma pedra tornou-se simbolo da poetica drummondiana e de sua fortuna critica.",
                "Cecilia Meireles cultivou um lirismo fluido, marcado pela musicalidade e pela meditacao sobre o tempo.",
                "Joao Cabral de Melo Neto buscou o rigor construtivo e a secura mineral em Morte e Vida Severina.",
                "Manuel Bandeira transformou a doenca e a memoria em versos de aparente simplicidade.",
                "O Concretismo dos anos 1950 explorou a dimensao visual e espacial da palavra na pagina.",
            ],
        },
        {
            "name": "o romance regionalista de 1930",
            "subtitles": [
                "A seca, o sertao e a denuncia social",
                "Graciliano, Rachel e Jose Lins do Rego",
            ],
            "lead": "A geracao de 1930 voltou o olhar para o interior do Brasil e para as tensoes sociais do campo.",
            "facts": [
                "Vidas Secas, de Graciliano Ramos, acompanha uma familia de retirantes em prosa seca e economica.",
                "O drama da seca nordestina tornou-se materia central de denuncia da desigualdade.",
                "Rachel de Queiroz estreou aos vinte anos com O Quinze, sobre a estiagem de 1915 no Ceara.",
                "Jose Lins do Rego retratou a decadencia dos engenhos de cana no ciclo da cana-de-acucar.",
                "Jorge Amado deu voz ao cacau, aos coroneis e a vida popular da Bahia.",
                "O romance de 30 uniu ambicao estetica e consciencia dos problemas do pais.",
            ],
        },
        {
            "name": "a literatura brasileira contemporanea",
            "subtitles": [
                "Novas vozes e novos temas depois de 1980",
                "A cidade, a periferia e a memoria",
            ],
            "lead": "A literatura brasileira das ultimas decadas ampliou vozes, formas e territorios antes pouco representados.",
            "facts": [
                "A ficcao urbana passou a explorar a violencia, a solidao e a experiencia das grandes cidades.",
                "A chamada literatura marginal ou periferica trouxe autores e perspectivas das quebradas para o centro do debate.",
                "Autoras como Conceicao Evaristo elaboraram a nocao de escrevivencia, ligando escrita e experiencia afrodescendente.",
                "O conto ganhou forca como forma agil e adequada aos ritmos da vida contemporanea.",
                "A autoficcao borrou as fronteiras entre relato pessoal e invencao literaria.",
                "Premios e feiras literarias ampliaram a circulacao de novos nomes junto ao publico.",
            ],
        },
        {
            "name": "o realismo magico e a literatura fantastica",
            "subtitles": [
                "Quando o extraordinario invade o cotidiano",
                "De Garcia Marquez a Murilo Rubiao",
            ],
            "lead": "O realismo magico apresenta o sobrenatural como parte natural do mundo, sem espanto por parte das personagens.",
            "facts": [
                "Cem Anos de Solidao, de Gabriel Garcia Marquez, tornou-se o marco maior da corrente na America Latina.",
                "No realismo magico, prodigios convivem com a rotina sem romper a logica interna da narrativa.",
                "Jorge Luis Borges explorou labirintos, espelhos e bibliotecas infinitas em contos filosoficos.",
                "No Brasil, Murilo Rubiao antecipou o insolito em contos de atmosfera kafkiana.",
                "O fantastico costuma usar a hesitacao entre explicacao racional e sobrenatural para gerar efeito.",
                "A vertente dialoga com o mito, o folclore e a tradicao oral dos povos.",
            ],
        },
        {
            "name": "os grandes romances da literatura russa",
            "subtitles": [
                "Dostoievski, Tolstoi e a alma humana",
                "Culpa, fe e historia no romance russo",
            ],
            "lead": "A literatura russa do seculo XIX levou o romance a um patamar de profundidade psicologica e moral raramente igualado.",
            "facts": [
                "Crime e Castigo, de Dostoievski, investiga a culpa e a redencao de um estudante que comete um assassinato.",
                "Os Irmaos Karamazov encena o embate entre fe, duvida e liberdade em torno de um parricidio.",
                "Guerra e Paz, de Tolstoi, entrelaca destinos individuais a invasao napoleonica da Russia.",
                "Anna Karenina abre com uma das frases mais celebres sobre familias felizes e infelizes.",
                "O romance russo uniu ambicao filosofica a um realismo minucioso dos costumes.",
                "Sua influencia alcanca a psicologia moderna e a ficcao ocidental ate hoje.",
            ],
        },
        {
            "name": "a traducao literaria e a circulacao de obras",
            "subtitles": [
                "O oficio invisivel que aproxima culturas",
                "O que se ganha e se perde ao traduzir",
            ],
            "lead": "A traducao literaria e a ponte que permite a uma obra atravessar linguas, epocas e fronteiras.",
            "facts": [
                "Traduzir envolve escolhas de ritmo, tom e sentido que reescrevem a obra em outra lingua.",
                "Toda traducao e tambem uma interpretacao, condicionada pelo tempo e pela cultura do tradutor.",
                "Classicos ganham novas traducoes a cada geracao, refletindo mudancas no gosto e na lingua.",
                "O tradutor literario costuma permanecer invisivel, apesar do peso de suas decisoes.",
                "Grandes escritores tambem foram tradutores, como Machado de Assis e Haroldo de Campos.",
                "A circulacao internacional de uma literatura depende de tradutores e editoras dispostos ao risco.",
            ],
        },
        {
            "name": "o romance como forma literaria",
            "subtitles": [
                "Uma breve teoria do genero mais popular",
                "Do folhetim ao romance moderno",
            ],
            "lead": "O romance e a forma literaria mais plastica e ambiciosa, capaz de absorver quase todos os assuntos e registros.",
            "facts": [
                "O genero se firmou na modernidade como espelho da vida privada e da sociedade burguesa.",
                "O narrador onisciente do seculo XIX cedeu espaco a experimentos com ponto de vista e fluxo de consciencia.",
                "O folhetim popularizou a leitura por meio de capitulos publicados em jornais.",
                "O romance moderno fragmentou o tempo e a personagem, como em Joyce e Virginia Woolf.",
                "A tensao entre enredo e digressao e uma das forcas motrizes da forma.",
                "Mesmo diante de novas midias, o romance segue reinventando seus recursos.",
            ],
        },
    ],

    "Historia": [
        {
            "name": "a Antiguidade classica grega e romana",
            "subtitles": [
                "As raizes da politica, da filosofia e do direito ocidental",
                "De Atenas a Roma",
            ],
            "lead": "A Antiguidade classica lancou as bases da politica, da filosofia e do direito que ainda estruturam o Ocidente.",
            "facts": [
                "A democracia ateniense do seculo V a.C. inaugurou a participacao direta dos cidadaos nas decisoes da cidade.",
                "Socrates, Platao e Aristoteles fundaram tradicoes filosoficas que atravessaram milenios.",
                "A Republica Romana desenvolveu instituicoes como o Senado e a nocao de lei escrita.",
                "O Imperio Romano unificou o Mediterraneo e difundiu lingua, direito e engenharia.",
                "O direito romano permanece na base dos sistemas juridicos de muitos paises.",
                "A queda do Imperio Romano do Ocidente, em 476, e um marco tradicional do fim da Antiguidade.",
            ],
        },
        {
            "name": "a Idade Media e o mundo feudal",
            "subtitles": [
                "Alem dos cliches sobre a idade das trevas",
                "Feudalismo, Igreja e cidades",
            ],
            "lead": "A Idade Media foi um periodo longo e diverso, muito mais dinamico do que sugere a imagem de idade das trevas.",
            "facts": [
                "O feudalismo organizou poder e terra em relacoes de vassalagem entre senhores e servos.",
                "A Igreja Catolica exerceu enorme influencia cultural, politica e economica no periodo.",
                "O renascimento das cidades e do comercio, a partir do seculo XI, transformou a vida europeia.",
                "As universidades medievais preservaram e desenvolveram o saber classico e arabe.",
                "As catedrais goticas expressaram avancos tecnicos e uma nova sensibilidade religiosa.",
                "A Peste Negra do seculo XIV dizimou parte da populacao e abalou as estruturas sociais.",
            ],
        },
        {
            "name": "o Renascimento e o humanismo",
            "subtitles": [
                "A redescoberta do homem e da Antiguidade",
                "Arte, ciencia e um novo olhar sobre o mundo",
            ],
            "lead": "O Renascimento reabilitou a cultura classica e colocou o ser humano no centro da reflexao e da arte.",
            "facts": [
                "O movimento comecou nas cidades italianas dos seculos XIV e XV, como Florenca e Veneza.",
                "O humanismo valorizou o estudo dos textos antigos e a capacidade criativa do individuo.",
                "Leonardo da Vinci e Michelangelo simbolizam a fusao de arte, tecnica e ciencia.",
                "A perspectiva revolucionou a pintura ao criar a ilusao de profundidade.",
                "A imprensa de Gutenberg, por volta de 1450, acelerou a circulacao do conhecimento.",
                "O periodo preparou terreno para a revolucao cientifica e para a modernidade.",
            ],
        },
        {
            "name": "a Revolucao Francesa",
            "subtitles": [
                "Liberdade, igualdade e o fim do Antigo Regime",
                "1789 e a invencao da politica moderna",
            ],
            "lead": "A Revolucao Francesa de 1789 derrubou o Antigo Regime e difundiu ideais que moldaram a politica moderna.",
            "facts": [
                "A tomada da Bastilha, em 14 de julho de 1789, tornou-se simbolo da insurreicao popular.",
                "A Declaracao dos Direitos do Homem e do Cidadao proclamou principios universais de liberdade e igualdade.",
                "O periodo do Terror, sob Robespierre, revelou a face violenta do processo revolucionario.",
                "A revolucao aboliu privilegios feudais e reorganizou o Estado e a sociedade.",
                "Napoleao Bonaparte ascendeu ao poder e difundiu parte do legado revolucionario pela Europa.",
                "Os ideais de 1789 inspiraram movimentos por direitos e independencia no mundo todo.",
            ],
        },
        {
            "name": "a Revolucao Industrial",
            "subtitles": [
                "A maquina que mudou o trabalho e a vida",
                "Da Inglaterra ao mundo",
            ],
            "lead": "A Revolucao Industrial transformou radicalmente a producao, o trabalho e a organizacao das cidades.",
            "facts": [
                "Iniciada na Inglaterra no fim do seculo XVIII, apoiou-se na maquina a vapor e na industria textil.",
                "A producao fabril substituiu o trabalho artesanal e concentrou operarios nas cidades.",
                "O crescimento urbano trouxe problemas de moradia, saude e jornadas de trabalho extenuantes.",
                "Surgiram novas classes sociais e os primeiros movimentos operarios e sindicatos.",
                "A segunda revolucao industrial acrescentou eletricidade, aco e petroleo ao processo.",
                "As transformacoes tecnicas redefiniram o comercio mundial e as relacoes de poder.",
            ],
        },
        {
            "name": "o Brasil colonial",
            "subtitles": [
                "Acucar, ouro e trabalho escravizado",
                "Tres seculos que formaram o pais",
            ],
            "lead": "O periodo colonial estruturou a economia, a sociedade e as desigualdades que marcariam o Brasil.",
            "facts": [
                "A economia acucareira do Nordeste sustentou a colonia nos primeiros seculos.",
                "A escravizacao de africanos foi a base da forca de trabalho por mais de trezentos anos.",
                "A descoberta de ouro em Minas Gerais, no seculo XVIII, deslocou o eixo economico para o interior.",
                "As missoes jesuiticas atuaram na catequese e na organizacao do trabalho indigena.",
                "Revoltas como a Inconfidencia Mineira expressaram tensoes contra o dominio metropolitano.",
                "O pacto colonial subordinava a producao da colonia aos interesses de Portugal.",
            ],
        },
        {
            "name": "a Independencia e o Imperio do Brasil",
            "subtitles": [
                "De 1822 a proclamacao da Republica",
                "Um imperio nos tropicos",
            ],
            "lead": "A independencia de 1822 e o periodo imperial definiram as fronteiras e as instituicoes do Brasil moderno.",
            "facts": [
                "Dom Pedro I proclamou a independencia em 7 de setembro de 1822, as margens do Ipiranga.",
                "O Brasil adotou a monarquia, caso singular em meio as republicas latino-americanas.",
                "O Segundo Reinado, sob Dom Pedro II, foi periodo de relativa estabilidade e expansao do cafe.",
                "A escravidao so foi abolida em 1888, com a Lei Aurea, ultima do continente.",
                "A Guerra do Paraguai mobilizou o pais e teve efeitos duradouros sobre o Exercito.",
                "A Republica foi proclamada em 1889, encerrando quase sete decadas de imperio.",
            ],
        },
        {
            "name": "as Grandes Navegacoes",
            "subtitles": [
                "A era das descobertas e seus efeitos globais",
                "Caravelas, especiarias e novos mundos",
            ],
            "lead": "As Grandes Navegacoes dos seculos XV e XVI conectaram continentes e inauguraram a primeira globalizacao.",
            "facts": [
                "Portugal liderou a expansao maritima com o apoio da Escola de Sagres e de novas tecnicas.",
                "A chegada de Colombo a America, em 1492, mudou a historia dos dois lados do Atlantico.",
                "Vasco da Gama alcancou a India em 1498, abrindo a rota das especiarias.",
                "O encontro entre europeus e povos americanos teve consequencias demograficas devastadoras.",
                "O comercio atlantico articulou Europa, Africa e America, inclusive pelo trafico de escravizados.",
                "A troca de plantas, animais e doencas ficou conhecida como intercambio colombiano.",
            ],
        },
        {
            "name": "a Guerra Fria",
            "subtitles": [
                "Meio seculo de tensao entre duas superpotencias",
                "Do Muro de Berlim a corrida espacial",
            ],
            "lead": "A Guerra Fria dividiu o mundo em dois blocos e definiu a geopolitica da segunda metade do seculo XX.",
            "facts": [
                "O conflito opos os Estados Unidos e a Uniao Sovietica sem confronto militar direto entre eles.",
                "A corrida armamentista nuclear criou o equilibrio do terror entre as superpotencias.",
                "A construcao do Muro de Berlim, em 1961, materializou a divisao da Europa.",
                "A corrida espacial levou a Uniao Sovietica ao primeiro satelite e os EUA a Lua.",
                "Guerras como a do Vietna e a da Coreia foram conflitos por procuracao entre os blocos.",
                "A queda do Muro, em 1989, anunciou o fim da ordem bipolar.",
            ],
        },
        {
            "name": "a historiografia e a construcao da memoria",
            "subtitles": [
                "Como o passado e escrito e reescrito",
                "Fontes, versoes e disputas",
            ],
            "lead": "A historia nao e um relato neutro do passado, mas uma construcao feita a partir de fontes, metodos e perguntas.",
            "facts": [
                "Toda narrativa historica depende das fontes disponiveis e das perguntas do historiador.",
                "A escola dos Annales ampliou o objeto da historia para o cotidiano, a economia e as mentalidades.",
                "A memoria coletiva e disputada por grupos que reivindicam versoes do passado.",
                "Monumentos, datas e museus participam da construcao de uma memoria oficial.",
                "A historia oral valoriza depoimentos de testemunhas antes ignoradas pelos documentos.",
                "Revisar interpretacoes faz parte do metodo, e nao um sinal de fragilidade da disciplina.",
            ],
        },
    ],

    "Noticia": [
        {
            "name": "a cobertura jornalistica de eleicoes",
            "subtitles": [
                "Como a imprensa acompanha o processo democratico",
                "Pesquisas, debates e apuracao",
            ],
            "lead": "A cobertura de eleicoes e um dos momentos mais exigentes do jornalismo, em que velocidade e precisao precisam caminhar juntas.",
            "facts": [
                "A imprensa acompanha campanhas, debates e propostas para informar o eleitor antes do voto.",
                "Pesquisas de intencao de voto medem tendencias, mas trazem margem de erro que precisa ser explicada.",
                "A apuracao exige rigor para evitar a divulgacao de resultados incorretos ou precipitados.",
                "A checagem de propostas e declaracoes ajuda a conter a desinformacao no periodo eleitoral.",
                "A cobertura equilibrada busca dar espaco proporcional aos diferentes candidatos.",
                "Transparencia sobre metodos e fontes fortalece a confianca do publico na informacao.",
            ],
        },
        {
            "name": "o jornalismo ambiental e a crise climatica",
            "subtitles": [
                "Reportar a maior historia do nosso tempo",
                "Do desmatamento aos eventos extremos",
            ],
            "lead": "O jornalismo ambiental traduz dados cientificos complexos em informacao util sobre a crise climatica.",
            "facts": [
                "Reportagens sobre clima precisam articular ciencia, economia e politica de forma acessivel.",
                "Eventos extremos, como secas e enchentes, ganham cada vez mais espaco no noticiario.",
                "O desmatamento e as emissoes de gases de efeito estufa estao entre os temas centrais.",
                "A cobertura de conferencias do clima acompanha compromissos e cobra resultados dos paises.",
                "Dados de institutos de pesquisa dao base a reportagens sobre tendencias de longo prazo.",
                "O desafio e informar sem paralisar, mostrando tanto riscos quanto solucoes possiveis.",
            ],
        },
        {
            "name": "tecnologia e sociedade no noticiario",
            "subtitles": [
                "Quando a inovacao vira pauta cotidiana",
                "Plataformas, dados e privacidade",
            ],
            "lead": "A tecnologia deixou de ser um caderno especializado para ocupar o centro da cobertura sobre economia, politica e cultura.",
            "facts": [
                "A ascensao das grandes plataformas digitais reorganizou o consumo de informacao.",
                "Debates sobre privacidade e uso de dados pessoais tornaram-se pauta recorrente.",
                "A inteligencia artificial levanta questoes sobre trabalho, criacao e responsabilidade.",
                "A cobertura tecnologica precisa distinguir promessas de mercado de avancos concretos.",
                "Falhas de seguranca e vazamentos de dados afetam milhoes de usuarios.",
                "Regulacao e concorrencia no setor digital ganharam atencao de governos e da imprensa.",
            ],
        },
        {
            "name": "a cobertura de saude publica",
            "subtitles": [
                "Informar sem alarmar em tempos de crise",
                "Do SUS as emergencias sanitarias",
            ],
            "lead": "O jornalismo de saude tem a responsabilidade de informar com precisao sobre riscos, tratamentos e politicas publicas.",
            "facts": [
                "Emergencias sanitarias exigem informacao rapida, checada e baseada em evidencias.",
                "A cobertura de vacinas precisa combater mitos e explicar dados de eficacia e seguranca.",
                "Reportagens sobre o sistema de saude acompanham filas, financiamento e acesso a tratamentos.",
                "Fontes cientificas e autoridades sanitarias sao essenciais para a credibilidade das materias.",
                "O excesso de alarmismo pode ser tao prejudicial quanto a falta de informacao.",
                "Dados de mortalidade e incidencia ajudam a dimensionar problemas de forma responsavel.",
            ],
        },
        {
            "name": "a economia nas paginas dos jornais",
            "subtitles": [
                "Traduzir numeros em vida cotidiana",
                "Juros, inflacao e emprego",
            ],
            "lead": "O jornalismo economico traduz indicadores abstratos em efeitos concretos sobre a vida das pessoas.",
            "facts": [
                "Indicadores como inflacao, juros e desemprego pautam boa parte da cobertura economica.",
                "Explicar o impacto de decisoes do banco central no bolso do cidadao e um desafio constante.",
                "A cobertura de mercados precisa evitar o exagero diante de oscilacoes de curto prazo.",
                "Reportagens sobre desigualdade mostram a distribuicao desigual do crescimento.",
                "Dados oficiais e de institutos de pesquisa embasam analises confiaveis.",
                "O bom jornalismo economico conecta macroeconomia e experiencias concretas.",
            ],
        },
        {
            "name": "o jornalismo esportivo",
            "subtitles": [
                "Muito alem do placar",
                "Paixao, negocio e sociedade",
            ],
            "lead": "O jornalismo esportivo combina a emocao da competicao com a analise de um setor que movimenta bilhoes.",
            "facts": [
                "A cobertura vai do relato ao vivo a analise tatica e ao noticiario de bastidores.",
                "O esporte de alto rendimento envolve grandes contratos, patrocinios e direitos de transmissao.",
                "Temas sociais, como racismo e inclusao, ganharam espaco na cobertura esportiva.",
                "Grandes eventos, como Copas e Olimpiadas, mobilizam audiencias globais.",
                "A tecnologia mudou a forma de assistir, com estatisticas e recursos de video.",
                "O jornalismo investigativo tambem alcanca a gestao e as financas do esporte.",
            ],
        },
        {
            "name": "a cobertura de seguranca publica",
            "subtitles": [
                "Entre o fato, o dado e a sensacao de medo",
                "Crime, policia e politicas de prevencao",
            ],
            "lead": "A cobertura de seguranca publica precisa equilibrar a apuracao dos fatos com a contextualizacao dos dados de criminalidade.",
            "facts": [
                "Reportagens responsaveis evitam reforcar estigmas e o sensacionalismo em torno do crime.",
                "Dados de criminalidade ajudam a distinguir percepcao de inseguranca de tendencias reais.",
                "A cobertura acompanha politicas de prevencao, policiamento e sistema prisional.",
                "O respeito a presuncao de inocencia e um principio central nesse tipo de materia.",
                "Fontes oficiais e independentes ajudam a checar versoes divergentes dos fatos.",
                "Investigacoes jornalisticas expoem falhas e abusos em orgaos de seguranca.",
            ],
        },
        {
            "name": "o noticiario sobre educacao",
            "subtitles": [
                "A pauta que molda o futuro",
                "Da sala de aula as politicas nacionais",
            ],
            "lead": "A cobertura de educacao acompanha desde o cotidiano das escolas ate as grandes politicas que definem o futuro do pais.",
            "facts": [
                "Avaliacoes nacionais e internacionais medem o desempenho dos estudantes ao longo do tempo.",
                "Reportagens sobre desigualdade educacional mostram diferencas de acesso e qualidade.",
                "O debate sobre financiamento e valorizacao docente e recorrente no setor.",
                "A tecnologia na educacao acelerou-se e trouxe novos desafios pedagogicos.",
                "A cobertura acompanha reformas curriculares e seus efeitos praticos.",
                "Historias de escolas e professores dao rosto humano aos dados educacionais.",
            ],
        },
        {
            "name": "a divulgacao cientifica no jornalismo",
            "subtitles": [
                "Aproximar a ciencia do grande publico",
                "Descobertas, metodo e ceticismo",
            ],
            "lead": "A divulgacao cientifica traduz descobertas complexas para o publico e ajuda a fortalecer o pensamento critico.",
            "facts": [
                "Boas reportagens explicam nao so o resultado, mas o metodo por tras da ciencia.",
                "A cobertura precisa distinguir estudos preliminares de consensos consolidados.",
                "Descobertas em saude, espaco e meio ambiente costumam ganhar grande repercussao.",
                "O ceticismo saudavel ajuda a evitar promessas exageradas e pseudociencia.",
                "Entrevistar pesquisadores e checar fontes dao solidez as materias cientificas.",
                "A ciencia avanca por revisao e erro, o que precisa ser comunicado ao publico.",
            ],
        },
        {
            "name": "a checagem de fatos e a desinformacao",
            "subtitles": [
                "A linha de frente contra as fake news",
                "Como o jornalismo verifica o que circula",
            ],
            "lead": "A checagem de fatos tornou-se peca central do jornalismo diante da avalanche de desinformacao nas redes.",
            "facts": [
                "Agencias de checagem verificam declaracoes, imagens e conteudos virais.",
                "A desinformacao se espalha mais rapido que a correcao, o que exige agilidade.",
                "Transparencia sobre metodo e fontes e essencial para a credibilidade da checagem.",
                "A alfabetizacao midiatica ajuda o publico a identificar conteudos suspeitos.",
                "Imagens e videos manipulados exigem ferramentas especificas de verificacao.",
                "O combate a desinformacao envolve plataformas, jornalistas e usuarios.",
            ],
        },
    ],

    "Politica": [
        {
            "name": "a democracia representativa",
            "subtitles": [
                "Como o povo governa por meio de representantes",
                "Virtudes e limites do modelo",
            ],
            "lead": "A democracia representativa organiza o governo do povo por meio de representantes eleitos periodicamente.",
            "facts": [
                "Eleicoes livres e periodicas sao o mecanismo central de escolha dos governantes.",
                "A representacao busca conciliar a vontade popular com a necessidade de decisoes tecnicas.",
                "A alternancia de poder e um sinal de saude das democracias.",
                "O voto universal ampliou-se ao longo do tempo para incluir mulheres e grupos excluidos.",
                "A qualidade da representacao depende de partidos e instituicoes funcionais.",
                "Criticas apontam a distancia entre eleitores e representantes como um problema persistente.",
            ],
        },
        {
            "name": "a separacao dos poderes",
            "subtitles": [
                "Freios e contrapesos no Estado moderno",
                "Executivo, Legislativo e Judiciario",
            ],
            "lead": "A separacao dos poderes distribui a autoridade do Estado para evitar a concentracao e o abuso de poder.",
            "facts": [
                "A ideia foi sistematizada por Montesquieu no seculo XVIII.",
                "O Executivo administra, o Legislativo elabora leis e o Judiciario as interpreta.",
                "O sistema de freios e contrapesos permite que um poder controle os excessos do outro.",
                "A independencia entre os poderes e condicao do Estado de Direito.",
                "Tensoes entre os poderes fazem parte do funcionamento normal da democracia.",
                "A erosao desses limites e um sinal de alerta para regimes democraticos.",
            ],
        },
        {
            "name": "os sistemas eleitorais",
            "subtitles": [
                "Como votos viram cadeiras",
                "Majoritario, proporcional e suas consequencias",
            ],
            "lead": "Os sistemas eleitorais definem as regras que transformam votos em mandatos e moldam o sistema partidario.",
            "facts": [
                "O sistema majoritario elege quem obtem mais votos em cada distrito.",
                "O sistema proporcional distribui cadeiras conforme a votacao de cada partido.",
                "Cada modelo produz efeitos diferentes sobre o numero e o tamanho dos partidos.",
                "Clausulas de barreira buscam reduzir a fragmentacao partidaria.",
                "As regras eleitorais influenciam a governabilidade e a representatividade.",
                "Nao existe sistema perfeito, apenas escolhas com vantagens e custos.",
            ],
        },
        {
            "name": "os partidos politicos",
            "subtitles": [
                "As engrenagens da representacao",
                "Da mobilizacao ao governo",
            ],
            "lead": "Os partidos politicos organizam a disputa pelo poder e conectam a sociedade as instituicoes de governo.",
            "facts": [
                "Partidos agregam interesses, formulam programas e selecionam candidatos.",
                "Eles estruturam o trabalho legislativo por meio de bancadas e liderancas.",
                "A fidelidade partidaria e a coerencia programatica variam entre paises.",
                "A crise de confianca nos partidos e um fenomeno global.",
                "Novas formas de mobilizacao digital desafiam os partidos tradicionais.",
                "Sem partidos, a democracia representativa dificilmente funciona em larga escala.",
            ],
        },
        {
            "name": "o federalismo e a divisao do poder",
            "subtitles": [
                "Uniao, estados e municipios",
                "Autonomia e cooperacao",
            ],
            "lead": "O federalismo distribui competencias entre diferentes niveis de governo, equilibrando unidade e autonomia.",
            "facts": [
                "Em uma federacao, uniao, estados e municipios possuem atribuicoes proprias.",
                "A repartir competencias, o modelo aproxima decisoes das realidades locais.",
                "Conflitos de competencia entre niveis de governo sao comuns e precisam de arbitragem.",
                "A distribuicao de recursos entre entes e tema central do debate federativo.",
                "O federalismo pode acomodar diversidades regionais dentro de um mesmo pais.",
                "O equilibrio entre autonomia e cooperacao e sempre delicado.",
            ],
        },
        {
            "name": "a Constituicao e o Estado de Direito",
            "subtitles": [
                "As regras do jogo democratico",
                "Direitos, limites e legitimidade",
            ],
            "lead": "A Constituicao estabelece as regras fundamentais do Estado e submete governantes e governados a lei.",
            "facts": [
                "O Estado de Direito significa que ninguem esta acima da lei.",
                "Constituicoes definem direitos fundamentais e limites ao poder.",
                "O controle de constitucionalidade protege a hierarquia das normas.",
                "Direitos fundamentais funcionam como barreira contra abusos das maiorias.",
                "A estabilidade constitucional favorece a previsibilidade e a confianca.",
                "Reformas constitucionais exigem procedimentos mais rigorosos que leis comuns.",
            ],
        },
        {
            "name": "a opiniao publica e a midia na politica",
            "subtitles": [
                "Como se forma a agenda do debate",
                "Das velhas as novas midias",
            ],
            "lead": "A opiniao publica e a midia influenciam quais temas entram na agenda politica e como sao percebidos.",
            "facts": [
                "Os meios de comunicacao ajudam a definir a agenda do debate publico.",
                "As redes sociais fragmentaram o espaco de informacao e ampliaram vozes antes marginais.",
                "Bolhas e camaras de eco podem reforcar visoes ja existentes.",
                "Pesquisas de opiniao medem, mas tambem influenciam, o clima politico.",
                "A relacao entre governos e imprensa e marcada por tensao permanente.",
                "A qualidade do debate depende do acesso a informacao confiavel.",
            ],
        },
        {
            "name": "o populismo na politica contemporanea",
            "subtitles": [
                "Um conceito disputado",
                "Povo, elites e lideranca",
            ],
            "lead": "O populismo e um dos conceitos mais debatidos e disputados da ciencia politica contemporanea.",
            "facts": [
                "O populismo costuma opor um povo puro a uma elite corrupta.",
                "Lideres populistas reivindicam falar em nome direto do povo.",
                "O fenomeno aparece em diferentes posicoes do espectro ideologico.",
                "Criticos alertam para o risco de erosao das instituicoes de controle.",
                "Contextos de crise economica e de representacao favorecem o populismo.",
                "O termo e usado tanto como analise quanto como acusacao politica.",
            ],
        },
        {
            "name": "as politicas publicas",
            "subtitles": [
                "Do problema social a acao do Estado",
                "Como decisoes viram programas",
            ],
            "lead": "As politicas publicas sao as respostas organizadas do Estado a problemas coletivos.",
            "facts": [
                "O ciclo de politicas inclui formulacao, implementacao e avaliacao.",
                "Boas politicas dependem de diagnostico correto e de dados confiaveis.",
                "A implementacao costuma ser tao dificil quanto a formulacao.",
                "A avaliacao de resultados permite corrigir rumos e justificar gastos.",
                "Politicas sociais buscam reduzir desigualdades e ampliar direitos.",
                "A coordenacao entre orgaos e niveis de governo e um desafio constante.",
            ],
        },
        {
            "name": "a participacao e a sociedade civil",
            "subtitles": [
                "Democracia alem do voto",
                "Movimentos, conselhos e engajamento",
            ],
            "lead": "A participacao da sociedade civil amplia a democracia para alem do momento eleitoral.",
            "facts": [
                "Movimentos sociais pressionam por direitos e colocam temas na agenda.",
                "Conselhos e conferencias abrem canais de participacao em politicas publicas.",
                "O associativismo fortalece a vida democratica e o capital social.",
                "A participacao digital criou novas formas de mobilizacao coletiva.",
                "O engajamento civico depende de confianca nas instituicoes.",
                "Sem sociedade civil ativa, a democracia tende a se esvaziar.",
            ],
        },
    ],

    "Geopolitica": [
        {
            "name": "a ordem mundial e a transicao para a multipolaridade",
            "subtitles": [
                "O fim do momento unipolar",
                "Um mundo com varios centros de poder",
            ],
            "lead": "A ordem internacional caminha de um momento unipolar para um cenario mais multipolar e disputado.",
            "facts": [
                "Apos a Guerra Fria, os Estados Unidos viveram um periodo de hegemonia relativa.",
                "A ascensao de novas potencias redistribui o poder no sistema internacional.",
                "A multipolaridade aumenta a complexidade e a incerteza das relacoes globais.",
                "Instituicoes criadas no pos-guerra enfrentam pressao por reformas.",
                "A competicao entre grandes potencias se estende a tecnologia e a economia.",
                "A ordem emergente ainda nao tem contornos definidos.",
            ],
        },
        {
            "name": "a ascensao da China",
            "subtitles": [
                "De fabrica do mundo a potencia global",
                "Economia, tecnologia e influencia",
            ],
            "lead": "A ascensao da China e um dos fenomenos geopoliticos mais importantes das ultimas decadas.",
            "facts": [
                "As reformas iniciadas em 1978 abriram a economia chinesa ao mercado.",
                "A China tornou-se a segunda maior economia do mundo e centro industrial global.",
                "A Iniciativa do Cinturao e Rota expandiu sua influencia em infraestrutura.",
                "O pais investe pesado em tecnologia, energia e inovacao.",
                "A relacao com os Estados Unidos combina interdependencia e rivalidade.",
                "Seu peso demografico e economico reorganiza cadeias produtivas globais.",
            ],
        },
        {
            "name": "a Russia e seu entorno estrategico",
            "subtitles": [
                "Historia, territorio e poder",
                "Energia e influencia regional",
            ],
            "lead": "A Russia articula seu peso geopolitico a partir de territorio, recursos energeticos e presenca militar.",
            "facts": [
                "A Russia e o maior pais do mundo em extensao territorial.",
                "Recursos de gas e petroleo sao instrumentos de influencia economica e politica.",
                "As relacoes com o Ocidente oscilam entre cooperacao e confronto.",
                "A seguranca de suas fronteiras e um tema central de sua estrategia.",
                "O pais mantem forte capacidade militar e arsenal nuclear.",
                "Sua politica externa busca preservar influencia em seu entorno regional.",
            ],
        },
        {
            "name": "os Estados Unidos e a projecao de poder",
            "subtitles": [
                "A superpotencia diante de novos desafios",
                "Poder militar, economico e cultural",
            ],
            "lead": "Os Estados Unidos permanecem a principal potencia global, embora diante de novos desafios a sua lideranca.",
            "facts": [
                "O pais combina poder militar, economico, tecnologico e cultural.",
                "O dolar ocupa posicao central no sistema financeiro internacional.",
                "Sua rede de aliancas amplia o alcance de sua influencia.",
                "Debates internos afetam a consistencia de sua politica externa.",
                "A competicao com a China marca sua agenda estrategica atual.",
                "O chamado poder brando difunde valores e cultura pelo mundo.",
            ],
        },
        {
            "name": "a Uniao Europeia e a integracao regional",
            "subtitles": [
                "Um projeto de paz e prosperidade",
                "Conquistas e tensoes internas",
            ],
            "lead": "A Uniao Europeia e a mais ambiciosa experiencia de integracao regional da historia moderna.",
            "facts": [
                "O projeto europeu nasceu para evitar novas guerras no continente.",
                "O mercado unico permite a livre circulacao de bens, servicos e pessoas.",
                "O euro unificou a moeda de grande parte dos paises-membros.",
                "A ampliacao do bloco incorporou paises do Leste apos a Guerra Fria.",
                "Crises economicas e migratorias testaram a coesao interna.",
                "A saida do Reino Unido revelou tensoes sobre soberania e integracao.",
            ],
        },
        {
            "name": "o Oriente Medio e suas disputas",
            "subtitles": [
                "Petroleo, religiao e geopolitica",
                "Uma regiao no centro das tensoes globais",
            ],
            "lead": "O Oriente Medio concentra recursos estrategicos e disputas historicas que reverberam em todo o sistema internacional.",
            "facts": [
                "A regiao detem parte significativa das reservas mundiais de petroleo.",
                "Conflitos historicos e disputas territoriais marcam sua geopolitica.",
                "Diferentes tradicoes religiosas e etnicas convivem e por vezes se chocam.",
                "Potencias externas disputam influencia sobre a regiao.",
                "A instabilidade tem efeitos sobre precos de energia e fluxos migratorios.",
                "Iniciativas de paz enfrentam obstaculos profundos e recorrentes.",
            ],
        },
        {
            "name": "o comercio internacional e as cadeias globais",
            "subtitles": [
                "Como o mundo produz de forma integrada",
                "Interdependencia e vulnerabilidade",
            ],
            "lead": "O comercio internacional e as cadeias globais de valor tornaram as economias profundamente interdependentes.",
            "facts": [
                "Produtos modernos reunem componentes fabricados em varios paises.",
                "A interdependencia amplia a eficiencia, mas tambem as vulnerabilidades.",
                "Tensoes comerciais podem interromper cadeias de suprimento globais.",
                "Acordos e organismos buscam regular o comercio entre nacoes.",
                "Crises revelaram os riscos de depender de poucos fornecedores.",
                "Muitos paises passaram a discutir a diversificacao de suas cadeias.",
            ],
        },
        {
            "name": "a geopolitica da energia e dos recursos",
            "subtitles": [
                "Quem controla a energia controla o poder",
                "Da era do petroleo a transicao verde",
            ],
            "lead": "O controle de fontes de energia e de recursos estrategicos e um dos motores da geopolitica.",
            "facts": [
                "Petroleo e gas influenciaram guerras, aliancas e o preco de tudo.",
                "A transicao energetica desloca o poder para novos recursos e tecnologias.",
                "Minerais criticos tornaram-se disputados na era das baterias e eletronicos.",
                "A seguranca energetica e prioridade estrategica dos Estados.",
                "A dependencia de importacoes cria vulnerabilidades politicas.",
                "Energias renovaveis podem redesenhar o mapa do poder global.",
            ],
        },
        {
            "name": "os organismos internacionais",
            "subtitles": [
                "Governanca global em xeque",
                "Da ONU as instituicoes economicas",
            ],
            "lead": "Os organismos internacionais buscam coordenar a acao dos Estados diante de problemas que ultrapassam fronteiras.",
            "facts": [
                "A ONU foi criada em 1945 para promover paz e cooperacao entre nacoes.",
                "O Conselho de Seguranca concentra poder em seus membros permanentes.",
                "Instituicoes economicas influenciam politicas de desenvolvimento e credito.",
                "Criticas apontam deficit de representatividade e de eficacia.",
                "A cooperacao multilateral e testada por crises e rivalidades.",
                "Reformar essas instituicoes e um debate recorrente e dificil.",
            ],
        },
        {
            "name": "o Sul global e os novos arranjos",
            "subtitles": [
                "Vozes emergentes na ordem internacional",
                "BRICS e a busca por autonomia",
            ],
            "lead": "O chamado Sul global reivindica maior participacao na governanca e busca reduzir dependencias historicas.",
            "facts": [
                "Paises emergentes pressionam por reformas na governanca global.",
                "Arranjos como os BRICS buscam ampliar a autonomia economica e politica.",
                "A cooperacao Sul-Sul propoe alternativas as dependencias tradicionais.",
                "Recursos naturais e demografia dao peso a essas economias.",
                "Interesses internos diversos dificultam posicoes plenamente comuns.",
                "O tema expressa a insatisfacao com uma ordem vista como desigual.",
            ],
        },
    ],

    "Economia": [
        {
            "name": "a inflacao e a politica monetaria",
            "subtitles": [
                "Por que os precos sobem e como controla-los",
                "O papel dos juros",
            ],
            "lead": "A inflacao corroi o poder de compra e seu controle e um dos principais objetivos da politica economica.",
            "facts": [
                "Inflacao e o aumento generalizado e continuo dos precos ao longo do tempo.",
                "Bancos centrais usam a taxa de juros para conter ou estimular a demanda.",
                "Juros mais altos tendem a reduzir o consumo e frear a alta de precos.",
                "A inflacao alta prejudica sobretudo os mais pobres e quem tem renda fixa.",
                "Metas de inflacao ancoram expectativas de empresas e consumidores.",
                "O desafio e conter precos sem sufocar o crescimento e o emprego.",
            ],
        },
        {
            "name": "o mercado de trabalho",
            "subtitles": [
                "Emprego, renda e transformacoes",
                "Da industria a economia de servicos",
            ],
            "lead": "O mercado de trabalho conecta crescimento economico, renda das familias e coesao social.",
            "facts": [
                "A taxa de desemprego mede a parcela da forca de trabalho sem ocupacao.",
                "A informalidade e um desafio persistente em muitas economias.",
                "A automacao transforma profissoes e exige requalificacao dos trabalhadores.",
                "A produtividade influencia salarios e competitividade.",
                "A economia de plataformas criou novas formas de trabalho e de vinculo.",
                "Educacao e qualificacao afetam diretamente as chances no mercado.",
            ],
        },
        {
            "name": "o comercio internacional e as vantagens comparativas",
            "subtitles": [
                "Por que os paises trocam entre si",
                "Ganhos e perdas da abertura",
            ],
            "lead": "O comercio internacional permite que paises se especializem e ampliem o bem-estar, embora gere ganhadores e perdedores.",
            "facts": [
                "A teoria das vantagens comparativas explica os ganhos da especializacao.",
                "A abertura comercial reduz precos e amplia a variedade de produtos.",
                "Setores expostos a concorrencia externa podem sofrer perdas.",
                "Politicas de protecao buscam abrigar industrias nacionais.",
                "Acordos comerciais reduzem barreiras e integram mercados.",
                "Distribuir os ganhos do comercio e um desafio politico.",
            ],
        },
        {
            "name": "a desigualdade economica",
            "subtitles": [
                "Como a renda se distribui",
                "Causas, medidas e consequencias",
            ],
            "lead": "A desigualdade economica afeta o crescimento, a coesao social e a propria estabilidade das democracias.",
            "facts": [
                "O indice de Gini e uma das medidas mais usadas de desigualdade de renda.",
                "Educacao, herancas e mercado de trabalho influenciam a distribuicao.",
                "Desigualdade extrema pode limitar a mobilidade social.",
                "Politicas tributarias e sociais afetam a concentracao de renda.",
                "O debate opoe visoes sobre eficiencia e justica.",
                "Reduzir desigualdades exige combinar crescimento e redistribuicao.",
            ],
        },
        {
            "name": "o crescimento economico e a produtividade",
            "subtitles": [
                "O que faz uma economia prosperar",
                "Capital, trabalho e inovacao",
            ],
            "lead": "O crescimento sustentado depende, sobretudo, de ganhos de produtividade ao longo do tempo.",
            "facts": [
                "O crescimento resulta de mais capital, mais trabalho e melhor tecnologia.",
                "A produtividade mede quanto se produz por unidade de recurso empregado.",
                "Inovacao e educacao sao motores de ganhos de produtividade.",
                "Infraestrutura e instituicoes solidas favorecem o investimento.",
                "Crescimento sem produtividade tende a ser fragil e passageiro.",
                "O desafio e crescer de forma sustentavel e inclusiva.",
            ],
        },
        {
            "name": "o sistema financeiro",
            "subtitles": [
                "Como o dinheiro circula na economia",
                "Bancos, credito e risco",
            ],
            "lead": "O sistema financeiro intermedeia poupanca e investimento e e essencial ao funcionamento da economia.",
            "facts": [
                "Bancos captam depositos e concedem credito a familias e empresas.",
                "O credito viabiliza consumo e investimento, mas amplia riscos.",
                "Crises financeiras podem se espalhar rapidamente pela economia real.",
                "A regulacao busca conter riscos sistemicos e proteger poupadores.",
                "Mercados de capitais permitem financiar projetos de longo prazo.",
                "A confianca e o ativo mais precioso do sistema financeiro.",
            ],
        },
        {
            "name": "a politica fiscal e o papel do Estado",
            "subtitles": [
                "Gastos, impostos e divida publica",
                "Como o orcamento molda a economia",
            ],
            "lead": "A politica fiscal, feita de gastos e impostos, e um dos principais instrumentos de acao economica do Estado.",
            "facts": [
                "O governo arrecada tributos e financia servicos e investimentos.",
                "O deficit ocorre quando os gastos superam as receitas.",
                "A divida publica cresce quando deficits se acumulam ao longo do tempo.",
                "A politica fiscal pode estimular a economia em periodos de crise.",
                "A sustentabilidade da divida e condicao para a estabilidade.",
                "Escolhas fiscais expressam prioridades politicas e sociais.",
            ],
        },
        {
            "name": "a moeda e os bancos centrais",
            "subtitles": [
                "O que da valor ao dinheiro",
                "Independencia e credibilidade",
            ],
            "lead": "A moeda e a base das trocas modernas, e os bancos centrais zelam por sua estabilidade.",
            "facts": [
                "A moeda cumpre funcoes de meio de troca, unidade de conta e reserva de valor.",
                "Bancos centrais controlam a oferta de moeda e a taxa basica de juros.",
                "A credibilidade da autoridade monetaria ancora as expectativas.",
                "A independencia do banco central busca isolar decisoes de pressoes politicas.",
                "Moedas digitais de bancos centrais estao em estudo em varios paises.",
                "A confianca na moeda e essencial para o funcionamento da economia.",
            ],
        },
        {
            "name": "a economia digital",
            "subtitles": [
                "Dados, plataformas e novos mercados",
                "A transformacao dos negocios",
            ],
            "lead": "A economia digital reorganiza mercados, empregos e a propria nocao de valor.",
            "facts": [
                "Plataformas digitais conectam oferta e demanda em escala global.",
                "Dados tornaram-se um insumo economico de enorme valor.",
                "Efeitos de rede tendem a concentrar mercados em poucas empresas.",
                "A economia digital cria novos servicos e tambem novos desafios regulatorios.",
                "A inteligencia artificial promete ganhos de produtividade e disrupcao.",
                "A tributacao de gigantes digitais e um debate internacional.",
            ],
        },
        {
            "name": "o desenvolvimento sustentavel",
            "subtitles": [
                "Crescer sem comprometer o futuro",
                "Economia, sociedade e meio ambiente",
            ],
            "lead": "O desenvolvimento sustentavel busca conciliar crescimento economico, justica social e preservacao ambiental.",
            "facts": [
                "O conceito articula dimensoes economica, social e ambiental.",
                "A transicao energetica e central para reduzir emissoes de carbono.",
                "Investimentos verdes ganham espaco no mercado financeiro.",
                "O custo da inacao climatica tende a superar o da transicao.",
                "Metas globais orientam politicas de sustentabilidade.",
                "Conciliar crescimento e limites ambientais e o grande desafio do seculo.",
            ],
        },
    ],

    "Cultura": [
        {
            "name": "o cinema como arte e industria",
            "subtitles": [
                "Entre a bilheteria e a autoria",
                "Uma linguagem de pouco mais de um seculo",
            ],
            "lead": "O cinema e, ao mesmo tempo, uma das artes mais jovens e uma das industrias culturais mais poderosas.",
            "facts": [
                "O cinema surgiu no fim do seculo XIX e rapidamente se tornou fenomeno de massa.",
                "A linguagem cinematografica se constroi com montagem, enquadramento e som.",
                "Grandes estudios convivem com um cinema autoral e independente.",
                "Festivais consagram obras e revelam novos cineastas.",
                "O streaming transformou a producao e o consumo de filmes.",
                "O cinema reflete e molda imaginarios coletivos.",
            ],
        },
        {
            "name": "a musica popular brasileira",
            "subtitles": [
                "Do samba a bossa nova e ao que veio depois",
                "A trilha sonora de um pais",
            ],
            "lead": "A musica popular brasileira e um dos patrimonios culturais mais ricos e reconhecidos do pais.",
            "facts": [
                "O samba consolidou-se no inicio do seculo XX como simbolo da identidade nacional.",
                "A bossa nova, nos anos 1950, renovou a harmonia e conquistou o mundo.",
                "A Tropicalia misturou generos e provocou o debate cultural nos anos 1960.",
                "Nomes como Tom Jobim e Joao Gilberto influenciaram a musica global.",
                "O pais abriga enorme diversidade regional de ritmos e tradicoes.",
                "A MPB dialoga com a poesia, a politica e a vida cotidiana.",
            ],
        },
        {
            "name": "as artes visuais e seus movimentos",
            "subtitles": [
                "Da tradicao a arte contemporanea",
                "Como olhamos para a imagem",
            ],
            "lead": "As artes visuais acompanham e desafiam as formas como cada epoca enxerga o mundo.",
            "facts": [
                "Movimentos como impressionismo e cubismo romperam com a representacao tradicional.",
                "A arte moderna questionou as fronteiras entre obra, objeto e experiencia.",
                "A arte contemporanea incorpora video, instalacao e performance.",
                "Bienais e museus articulam a circulacao internacional das obras.",
                "O mercado de arte movimenta cifras expressivas e gera polemicas.",
                "A imagem tornou-se central na cultura visual contemporanea.",
            ],
        },
        {
            "name": "o teatro e as artes cenicas",
            "subtitles": [
                "A arte do encontro ao vivo",
                "Da tragedia grega a cena atual",
            ],
            "lead": "O teatro e a arte do encontro presente entre atores e publico, viva ha milenios.",
            "facts": [
                "O teatro ocidental nasceu na Grecia antiga, com a tragedia e a comedia.",
                "Shakespeare ampliou as possibilidades dramaticas na virada para a modernidade.",
                "O teatro moderno experimentou novas formas de encenacao e de relacao com o publico.",
                "As artes cenicas incluem danca, performance e teatro fisico.",
                "O carater efemero e ao vivo distingue o teatro de outras artes.",
                "Grupos e festivais mantem viva a cena teatral contemporanea.",
            ],
        },
        {
            "name": "a cultura pop e a era do streaming",
            "subtitles": [
                "Como consumimos entretenimento hoje",
                "Series, plataformas e fandom",
            ],
            "lead": "A cultura pop e o streaming redefiniram a forma como o mundo consome entretenimento.",
            "facts": [
                "As plataformas de streaming mudaram o ritmo de lancamento e consumo de series.",
                "Franquias e universos ficcionais organizam boa parte da industria do entretenimento.",
                "Comunidades de fas influenciam a producao cultural contemporanea.",
                "O algoritmo passou a mediar o que o publico descobre e assiste.",
                "A cultura pop dialoga com identidade, memoria e pertencimento.",
                "A abundancia de conteudo trouxe novos desafios de atencao e curadoria.",
            ],
        },
        {
            "name": "o patrimonio cultural e a memoria",
            "subtitles": [
                "O que escolhemos preservar",
                "Bens materiais e imateriais",
            ],
            "lead": "O patrimonio cultural reune aquilo que uma sociedade decide preservar como parte de sua identidade.",
            "facts": [
                "O patrimonio pode ser material, como edificios, ou imaterial, como saberes e festas.",
                "Politicas de tombamento protegem bens de valor historico e artistico.",
                "A preservacao envolve escolhas sobre o que merece ser lembrado.",
                "O patrimonio imaterial inclui musicas, culinaria e tradicoes orais.",
                "A destruicao de patrimonio representa perda irreparavel de memoria.",
                "Comunidades reivindicam voz sobre o proprio patrimonio.",
            ],
        },
        {
            "name": "a cultura digital e a internet",
            "subtitles": [
                "Novas formas de criar e compartilhar",
                "Memes, redes e criacao coletiva",
            ],
            "lead": "A cultura digital transformou a forma como as pessoas criam, compartilham e se relacionam com o conteudo.",
            "facts": [
                "A internet ampliou a producao cultural feita por qualquer pessoa.",
                "Memes tornaram-se uma linguagem propria da cultura em rede.",
                "Plataformas moldam o que se produz e o que ganha visibilidade.",
                "A criacao coletiva e o remix desafiam nocoes tradicionais de autoria.",
                "A cultura digital acelera tendencias e encurta ciclos culturais.",
                "Novas formas de expressao surgem e desaparecem em ritmo acelerado.",
            ],
        },
        {
            "name": "as festas populares e o folclore",
            "subtitles": [
                "A cultura que vive nas ruas",
                "Tradicao, fe e celebracao",
            ],
            "lead": "As festas populares e o folclore expressam a diversidade e a criatividade da cultura brasileira.",
            "facts": [
                "O Carnaval e uma das maiores manifestacoes culturais do pais.",
                "As festas juninas celebram tradicoes rurais e religiosas.",
                "O folclore reune lendas, personagens e saberes transmitidos oralmente.",
                "Manifestacoes como o maracatu e o frevo carregam heranca afro-brasileira.",
                "As festas populares combinam fe, musica, danca e culinaria.",
                "Essas tradicoes fortalecem identidades e lacos comunitarios.",
            ],
        },
        {
            "name": "os museus e a curadoria",
            "subtitles": [
                "Espacos de memoria e de debate",
                "O que expor e como narrar",
            ],
            "lead": "Os museus deixaram de ser depositos de objetos para se tornarem espacos vivos de memoria e debate.",
            "facts": [
                "A curadoria define quais objetos sao expostos e como sao narrados.",
                "Museus contemporaneos buscam dialogo com diferentes publicos.",
                "A digitalizacao de acervos ampliou o acesso ao patrimonio.",
                "Debates sobre restituicao de bens culturais ganharam forca.",
                "Exposicoes podem provocar e nao apenas celebrar.",
                "O museu e tambem um espaco de disputa sobre a memoria.",
            ],
        },
        {
            "name": "a identidade e a diversidade cultural",
            "subtitles": [
                "Muitas culturas, um mesmo mundo",
                "Pertencimento e reconhecimento",
            ],
            "lead": "A diversidade cultural e uma riqueza das sociedades contemporaneas e tambem fonte de debates sobre identidade.",
            "facts": [
                "A cultura molda identidades individuais e coletivas.",
                "O reconhecimento da diversidade amplia direitos e representatividade.",
                "A globalizacao aproxima culturas e tambem gera tensoes.",
                "Culturas tradicionais reivindicam preservacao e protagonismo.",
                "O dialogo intercultural enriquece as sociedades.",
                "Respeitar a diferenca e um dos desafios do mundo contemporaneo.",
            ],
        },
    ],
}

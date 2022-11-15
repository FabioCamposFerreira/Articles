# Redes de Computadores 

## Introdução

**Internet**: a ligação entre diversos computadores espalhados pelo mundo. Realiza a troca de mensagens, imagens, arquivos etc.

**Rede**: é um conjunto de equipamentos que podem se comunicar e trocar informações. Permitindo a comunicação e compartilhar recursos.

**Rede de computadores**: conexão entre dois ou mais computadores. Conexão por meio de cabos e conexão sem fio, também chamada de wireless.

## Tipos de Redes

### Rede Local (LAN)

 São interconexão de equipamentos em **espaço normalmente limitado**. Usado em residências, empresas, escolas etc.

| ![Rede LAN](imgs/lan.gif) |
| :-----------------------: |
|        *Rede LAN*         |


### Rede metropolitana (MAN)

Interligam computadores em grandes centros urbanos, em áreas maiores do que as redes locais.

| ![Rede MAN](imgs/man.png) |
| :-----------------------: |
|        *Rede MAN*         |

### Rede geograficamente distribuída (WAN - *Wide Area Network*)

 Conectar computadores próximos ou muito distantes, sem limitação de distância. Cidades distantes ou até mesmo em outros países e continentes

| ![Rede wan](imgs/wan.png) |
| :-----------------------: |
|        *Rede WAN*         |

## Tipos de Conexão

* **Dial-Up** (acesso discado):  usa a rede pública de telefonia para acessar a internet. Era caro e lento;

* **Banda Larga**: pode ser oferecido: 

    * **ADSL** :  por uma operadora de telefonia fixa;
    * **Cable Modem** :  por uma operadora de telefonia fixa;
    * **Rádio e Satélite**:   por uma operadora de rádio.

* **Sem fio**: rádios e satélites e faz uso das redes baseadas em ondas eletromagnéticas. baseadas em redes celulares 3G/4G.

 Os cabos, os fios, as antenas e as ondas eletromagnéticas levam/transportam as informações nas redes.

 * **Largura de banda**:  limite na comunicação entre equipamentos. Quanto mais larga, maior será a capacidade de transmissão.

## Meios de transmissão Guiados

* **Par trançado**: mais utilizado e antigo.  é composto de pares de fios de cobre entrelaçados. Eles apresentam baixo custo de manutenção.
 | ![](imgs/) |
 | :--------: |
 |     **     |

* **Cabo Coaxial**: é um fio de cobre esticado, na parte central do cabo, recoberto por um material isolante
| ![Cabo Coaxial](imgs/coaxial.jpg) |
| :-------------------------------: |
|          *Cabo Coaxial*           |

* **Fibras ópticas**:sistema mais moderno de transmissão de dados. O sistema é formado por uma fonte de luz, um meio de transmissão e um detector (componente eletrônico capaz de detectar a luz)
| ![](imgs/) |
| :--------: |
|     **     |

### Fibra Óptica
Um sistema de transmissão de dados em apenas uma direção (unidirecional) é formado de  uma fonte de luz em uma de suas extremidades e um detector na outra. Recebe um sinal elétrico, converte esse sinal e o transmite na forma de pulsos de luz. Na extremidade de recepção, a saída é reconvertida em um sinal elétrico.

As fibras ópticas são feitas de vidro bastante transparente. Essa propriedade é que permite a transmissão da luz.

cabos de fibra óptica são bem parecidos com os cabos coaxiais. No centro, fica o núcleo de vidro ( com espessura de um fio de cabelo ) através do qual se propaga a luz. . Em volta há uma cobertura de plástico fino que protege o revestimento interno.

| ![Fibra](imgs/fibra.png) |
| :----------------------: |
|         *Fibra*          |

Os cabos de fibra terrestre são colocados no solo, a um metro da superfície. Em regiões litorâneas, são enterrados em trincheiras. Nos oceanos, eles são depositados no fundo.



A fibra óptica permite maior largura de banda, não desperdiça luz e os cabos dificilmente são danificados. Enquanto os fios de cobre precisam de repetidores, que ampliam a intensidade do sinal a cada 5 quilômetros, a fibra óptica só utiliza repetidores a cada 50 quilômetros.

A fibra óptica também tem a vantagem de não ser afetada por picos de voltagem, interferência eletromagnética ou quedas no fornecimento de energia, não sofre a ação corrosiva de alguns elementos químicos que pairam no ar, além de adaptar-se muito bem a ambientes industriais desfavoráveis.

A principal desvantagem da fibra óptica está no fato de ser uma tecnologia menos conhecida, que exige competência técnica que nem todos os engenheiros possuem. Também podem ser danificadas com facilidade se forem encurvadas demais.

As empresas telefônicas usam a fibra óptica por ser muito mais leve que o cobre e ocupar bem menos espaço. Outro ponto que facilita a transição entre cabos de cobre e a fibra, é que o cobre pode ser revendido para refinarias

## Meios de transmissão não guiados

Os  transmissão com fio possuem limitação física(tem limite do volume de informações que podem transportar).

Transmissão sem fio é feita por meio de antenas, como as de TV ou telefone celular. Essas antenas transmitem ondas eletromagnéticas no espaço livre (ar) para um receptor (localizado em um ponto distante)

* **Ondas de rádio**: ão fáceis de gerar, podem percorrer longas distâncias e adentrar facilmente nos prédios. É omnidirecional (transmitida por todas as direções), assim O transmissor e você não precisam estar alinhados.

* **Micro-ondas**:  ocorre em linha reta, é mais barato. Não atravessa muito bem limites físicos, como paredes de edifícios. é usado nos telefones celulares

* **Infravermelho**: é próprio para comunicação de curto alcance. É usado no controle remoto. Não atravessar objetos sólidos

* **Ondas de luz**:  utiliza raios laser, é fácil de ser instalada. Uma aplicação é instalar  para conectar LANs de dois predios com laser instalados no telhado

* **Satélites**: liga um ou mais transmissores fora da atmosfera a receptores na Terra. Existem dois tipos de satélites: os **geoestacionários** ficam a 36 mil quilômetros acima da superfície terrestre e estão parados em relação a um ponto na Terra; os **satélites de baixa altitude** ficam girando em torno do nosso Planeta.

# Formas de Transmissão de Dados 

As formas de transimssão tem o objetivo de aumentar a velocidade da transmissão dos dados e Maximizando o uso do canal.

* **Transmissão Simplex**: transmissão básica,  a transmissão pode ocorrer apenas em uma direção. Não há meios de verificar a recepção dos dados. Problemas na transmissão não são corrigidos. Um exemplo é a transmissão da TV aberta.

* **Transmissão Half-Duplex**: a transmissão pode ocorrer em ambas as direções, mas não ao mesmo tempo. A detecção de erros é possível. Exemplo: *walkie-talkies*.

* **Transmissão Full-Duplex**: melhor forma de transmissão. Os dados podem ser transmitidos e recebidos simultaneamente. Exemplos: TV a cabo que possui internet internet.

# LANS

LANs são rede localizadas em um único edficio (casa, escritorios, etc)

## Topologia 

Topologia pe a formas como os equipamentros estão conectados entre si.

### Topologia em Anel

Os computadoes estão ligados em anel. Cada computador esta ligado a somente dois outros. A desvantegem dasta topologia é que se uma maquina, toda a rede pode cair.

| ![Fibra](imgs/anel.png) |
| :---------------------: |
|   *Topologia em Anel*   |

### Topologia em Barramento

Nesta topologia todos os computadores estão conectados no mesmo ponto. A desvantangem desta topologia é que somente um computadore pode venviar informação por vez, ou seja, em quanto um fala os outros são barrados.

| ![Fibra](imgs/barramento.png) |
| :---------------------------: |
|   *Topologia em Barramento*   |

### Topologia em Estrela

Nesta tipo de rede todos os computadores estão conectados  a  um dispositivo chamado *switch* que tem a função de gerenciar a comunicação. Assim todos os computadores podem comunicar-se entre diretamente e com outros computadores remotos (em outra rede). A sua vantagem é que se um computador parar a rede não ira cair, por isso esta topologia é a mais usada.

| ![Fibra](imgs/estrela.png) |
| :------------------------: |
|   *Topologia em Estrela*   |

# Placa de Rede

| ![Fibra](imgs/placa_rede.png) |
| :---------------------------: |
|        *Placa de rede*        |
E um *hardware* que permite a troca de informações entre os conputadores, controlando o realizando o envia e recebimento de dados. As placas podem ser classificadas em função de três caracteristicas:
* Taxa de transmissão: 
  * Ethernet, com velocidades de 10Mbps ate 10.000 Mbps;
  * Token Ring, com velocidades de 4Mbps ate 300 Mbps;
  * Wi-Fi, com velocidades de 2Mbps ate 9,6 Gbps;
  * Fibra optica, com velocidades de 100 Mbps a 300 Mbps.
* Cabos de rede suportados:
  * Ehternet usão cabo par trançado e coaxial;
  * Token Ring usa par trançado;
  * Fibra óptica.
* Barramento:
  * ISA (*Industry Standard Architecture*);
  * PCI (*Peripheral Component Interconnect*);
  * PCI-X (*Peripheral Component Interconnect Extended*);
  * AGP (*Accelerated Graphics Port*);
  * PCI Express (mais comum atualmente);
  * AMR, CNR e ACR;
  * VESA (VESA *Loca Bus*);
  * MCA (*Micro Channel Architecture*);
  * EISA (*Extended Industry Standard Architecture*).


# Conectores

## *HUB* ou concentrador

É um ponto central que interliga diversos computadores. Ele permite que novos computadores sejam adicionados a rede sem que a mesma tenha que ser desligada. O hub é um componente antigo que tem como caracteristica negativa repassar um dado para todos os computadores da rede, gerando trafego e problemas de segurança. Usado em LANs.

## *Swith* ou comutador

Tem a mesma função do *hub*, mas ele repassa a informação somente para um computador (destinatário final). Alguns modelos de swith podem sete ate 48 portas. Usado em LANs.
| ![Fibra](imgs/switch.jpg) |
| :-----------------------: |
|   *Switch de 24 portas*   |

## Roteador

Tem a função de conetar grande redes, exercendo o mesmo papel do switch e com o adicinal de conseguir escolher a melhor rota de transmissão dos dados ate chegar no destinatario, aumentando a velocidade de comunicação e reduzindo a perca de dados.

## Repetidor de sinal

Sua função é receber pacotes (dados) e repetilos sem realizar qualquer gerenciamento, amplificando o sinal, permitindo alcançar grandes distânicas

## *Gateway*

O *gateway* tem a função de interpretar e fazer o intercanbio os diversos protocolos e arquiteturas que estão presentes na rede.

# Cabeamento

O cabeamento de um pedrio tem a função de disponibilizar pontoes de rede em todos os lacais em forem necessarios ao redor do predio. Estes pontos se encontraram em uum ponto central onde ficam os equipamentos de rede como roteadores e switches.

| ![Fibra](imgs/cabeamento_estruturado.png) |
| :-----------------------: |
|   *Cabeamento estruturado.png*   |

* Cabeamento vertical 
* Armário de telecomunicações
* Entrada do prédio
* Cabeamento horizontal
* Área de trabalho
* Sala de equipamentos
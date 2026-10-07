#Análise Analítica Forense e Computação Gráfica

**Aluno:** Guilherme Pimentel Nogueira dos Santos  
**Tema 8:** Bacias Hidrográficas, Rios e Corpos d'Água Interiores  

---

## 1. Processamento e Tratamento de Imagem

A renderização de corpos d'água interiores (rios, lagos e represas) através de fotogrametria e mosaicos de satélite impõe desafios computacionais específicos aos algoritmos de *stitching* (costura de imagens) e texturização:

* **Reflexo da Luz na Água (Glint / Especularidade):** O ângulo de incidência solar varia no momento da captura por diferentes satélites ou passagens temporais. Isso gera manchas brilhantes (*sun glint*) na água em algumas imagens e superfícies escuras em outras. O algoritmo precisa aplicar correções de iluminação e filtros de polarização digital para uniformizar o tom da água e evitar marcas visíveis de corte ("costura") no meio do leito dos rios.
* **Variação Dinâmica de Cor e Turbidez:** A cor da água varia drasticamente conforme a profundidade, carga de sedimentos, estações do ano e proliferação de algas. Unir imagens capturadas em períodos diferentes exige algoritmos avançados de equalização de histograma e alinhamento radiométrico para evitar descontinuidades abruptas nas superfícies hídricas.
* **Geometria Dinâmica de Margens:** Diferente de estruturas urbanas ou formações rochosas, a linha de costa/margem muda de formato com variações de maré ou cheias dos rios. O algoritmo de *mesh warping* precisa ajustar o Modelo Digital de Elevação (DEM) para que a água não pareça "subir" morros ou deformar relevos adjacentes.

---

## 2. Design de Interface e Leis da Gestalt

A interface do Google Earth utiliza princípios visuais clássicos da Psicologia da Gestalt para orientar o foco do usuário na exploração de redes hidrográficas:

1. **Lei da Continuidade:**
   * **Aplicação:** Os rios e canais d'água são representados como linhas contínuas e fluídas que cortam o terreno. Mesmo quando um rio passa sob uma ponte ou se ramifica em deltas, o cérebro humano e os vetores da interface (quando selecionada a camada de hidrografia) percebem o fluxo como um elemento único e ininterrupto.
   * **Navegação UI:** O usuário instintivamente segue a trajetória do curso d'água com o cursor do mouse ao deslizar o zoom (*pan/zoom*), facilitando o rastreamento da nascente até a foz.

2. **Lei da Figura-Fundo:**
   * **Aplicação:** A interface contrasta fortemente o tom azulado reflectivo dos corpos d'água (figura) em relação aos tons verdes, marrons ou cinzas da vegetação, solo e superfícies urbanas ao redor (fundo).
   * **Navegação UI:** Esse contraste imediato permite que o usuário identifique instantaneamente grandes massas hídricas ou rios delgados ao aproximar o zoom, concentrando a atenção nos detalhes do curso fluvial sem se perder nas texturas do terreno circundante.

---

## 3. Imagens / Evidências

![Mapeamento de Bacia Hidrográfica no Google Earth](https://via.placeholder.com/800x450.png?text=Inserir+Captura+de+Tela+do+Google+Earth+Aqui)

> **Instruções para o aluno:** Tire uma captura de tela (print screen) do Google Earth focada em uma bacia hidrográfica ou grande rio (ex.: Rio Amazonas, Rio Paraná ou Rio São Francisco), salve a imagem na pasta do seu projeto (ex.: `evidencia.png`) e substitua o link acima por `./evidencia.png`.

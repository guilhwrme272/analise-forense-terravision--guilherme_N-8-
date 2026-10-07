# ETAPA 2: COMPUTAÇÃO GRÁFICA & UX/UI

**Aluno:** Guilherme Pimentel Nogueira dos Santos  
**Tema 8:** Bacias Hidrográficas, Rios e Corpos d'Água Interiores  

---

## 1. Processamento e Tratamento de Imagem

A renderização de corpos d'água interiores (rios, lagos e represas) em sistemas de informação geográfica e fotogrametria de satélite apresenta desafios técnicos específicos para os algoritmos de *stitching* (costura de imagens), ajuste de textura e balanceamento de cores:

* **Reflexo da Luz na Água (*Sun Glint* / Especularidade):** O ângulo de incidência da luz solar varia conforme a hora da captura por diferentes sensores geostacionários ou orbitais. Isso causa manchas brancas e brilhantes de reflexo em algumas fotos e tom escuro em outras. O algoritmo precisa aplicar correções de iluminação e filtros de polarização digital para harmonizar a refletância da água e evitar linhas de corte ("costuras") artificiais no meio do leito fluvial.
* **Variação Dinâmica de Cor e Turbidez:** A tonalidade da água muda drasticamente de acordo com a profundidade, quantidade de sedimentos em suspensão, estação do ano (períodos de seca ou cheia) e proliferação de algas. A união de imagens tiradas em datas diferentes exige equalização de histograma e alinhamento radiométrico contínuo para evitar rupturas visuais na continuidade dos rios.
* **Geometria e Dinâmica de Margens (Modelo Digital de Elevação - DEM):** Ao contrário do relevo urbano ou rochoso, o nível da água e o contorno das margens flutuam. O algoritmo de *mesh warping* precisa ajustar com precisão os dados de altitude para evitar que corpos d'água pareçam "subir" morros ou distorcer a linha de costa/vegetação ciliar.

---

## 2. Design de Interface e Leis da Gestalt

A interface do Google Earth utiliza princípios da Psicologia da Gestalt para otimizar o fluxo de navegação e direcionar o foco visual durante a exploração de redes hidrográficas:

1. **Lei da Continuidade:**
   * **Aplicação na UI:** Os rios e redes de drenagem são percebidos pelo sistema visual como linhas fluídas e ininterruptas que cortam o mapa. Mesmo quando um rio passa sob pontes, por áreas de mata densa ou se ramifica em deltas, o cérebro preserva a percepção da trajetória linear contínua.
   * **Orientação ao Usuário:** Facilita o acompanhamento intuitivo do curso d'água com o cursor (operações de *pan/zoom*), permitindo navegar sem interrupção do leito principal até a nascente ou foz.

2. **Lei da Figura-Fundo:**
   * **Aplicação na UI:** A interface estabelece um forte contraste cromático entre o tom azul/escuro da água (*figura*) e a paleta de cores do terreno ao redor (*fundo* — tons verdes da vegetação, marrons do solo e cinzas urbanos).
   * **Orientação ao Usuário:** Permite a identificação imediata de represas, lagos e grandes rios ao aproximar o zoom, guiando o olhar diretamente para os detalhes do tema de estudo sem distração pela textura das áreas terrestres.

---

### Evidência 1: Mapeamento da Bacia Hidrográfica (LoD Médio/Baixo)
![Mapeamento da Bacia Hidrográfica do Rio Amazonas](https://tunesambiental.com/wp-content/uploads/amazon-5.png)  
*Figura 1: Mosaico regional exibindo a delimitação da bacia hidrográfica, a rede de drenagem e a calha principal do rio.*


## 3. Imagens / Evidências <img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/298999db-70b5-4825-8422-f3a51e0d8632" />





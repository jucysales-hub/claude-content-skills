---
name: carousel
description: Use this skill to create Instagram carousel content from scratch or by recycling existing ideas. Trigger whenever the user mentions "carrossel", "carousel", "slides", "criar carrossel", "montar carrossel", "reciclar carrossel", or asks for structured post content with multiple slides. Also trigger when the user provides a hook/gancho and asks to build content around it, or when they mention creating content for Instagram with a defined CTA. Always use this skill — even for simple carousel requests — because it handles hook selection, tone calibration, CTA alignment, and slide structure automatically.
user-invokable: true
argument-hint: "[nicho, tema, objetivo da CTA e tom]"
license: MIT
---

# Carousel Skill

Cria conteúdo completo para carrosséis de Instagram: do gancho até o CTA final.

---

## Fluxo de execução

### Passo 1 — Coleta de contexto

Pergunte ao usuário as 4 informações abaixo. Pode fazer tudo de uma vez, em formato de lista simples:

1. **Nicho/segmento** — Ex: marketing digital, saúde mental, nutrição, finanças pessoais
2. **Tema ou ideia central** — O que esse carrossel vai abordar?
3. **Objetivo da CTA final** — O que a pessoa deve fazer depois de ler? Ex: salvar o post, seguir o perfil, mandar DM com uma palavra-chave, clicar no link da bio
4. **Tom do conteúdo** — Ex: didático, direto, provocativo, empático, leve, técnico

---

### Passo 2 — Gancho

Depois de receber o contexto, pergunte:

> "Você já escolheu o gancho para esse carrossel?"

**Se a resposta for sim:** peça para inserir o gancho escolhido e use exatamente como fornecido, sem alterar nenhuma palavra.

**Se a resposta for não:** consulte o arquivo `references/ganchos.md` e sugira 3 opções de ganchos alinhados ao tema, nicho e tom informados. Peça para o usuário escolher um. Use o gancho escolhido exatamente como está no banco, sem alterar.

---

### Passo 3 — Geração do carrossel

Com o contexto e o gancho definidos, gere o carrossel completo seguindo as regras abaixo.

---

## Regras de estrutura

**Quantidade de slides:** mínimo 6, máximo 10. Ajuste conforme a profundidade do tema.

**Slide 1 — Capa (Gancho)**
- Usa o gancho escolhido, sem alterações
- Pode ter uma linha de apoio abaixo do gancho se necessário, mas o gancho é intocável

**Slides intermediários (2 até penúltimo)**
- Um conceito central por slide, mas pode ter múltiplos parágrafos para desenvolvê-lo
- Cada parágrafo tem no máximo 3 linhas — sem exceção
- O conteúdo pode e deve ter profundidade, desde que seja fácil de entender
- Linguagem acessível, topo de funil — qualquer pessoa do nicho precisa entender
- Progressão lógica: cada slide abre o próximo naturalmente
- Sem listas com bullets. Se precisar enumerar, escreva em linha corrida
- Sem travessões
- Sem estruturas de oposição semântica ("não é X, é Y")
- Tom alinhado ao que o usuário informou no contexto

**Último slide — CTA**
- Direto e específico, alinhado ao objetivo informado
- Uma instrução clara de ação
- Pode ter uma linha de reforço emocional antes da instrução, se fizer sentido

---

## Formato de entrega

Entregue o carrossel neste formato:

```
📌 SLIDE 1 — CAPA
[gancho]

📌 SLIDE 2
[conteúdo]

📌 SLIDE 3
[conteúdo]

...

📌 SLIDE [N] — CTA
[chamada para ação]
```

Depois do carrossel, adicione uma linha com o número total de slides gerados.

---

## Referências

- `references/ganchos.md` — Banco com 500 ganchos para carrosséis. Consulte sempre que o usuário não tiver um gancho definido. Filtre por alinhamento com nicho, tema e tom antes de sugerir.

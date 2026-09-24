# Site-Institucional-Matheus-Marques

Portfólio de sites institucionais — no ar em https://portfolio-matheusamarques.vercel.app

Cinco sites conceituais no mesmo padrão do [Marques & Peixer](https://marquesepeixer-matheusamarques.vercel.app/):
página única com Tailwind, assistente virtual de triagem, formulário com envio por e-mail (Web3Forms) ou WhatsApp,
política de privacidade (LGPD), dados estruturados para o Google e pré-visualização ao compartilhar o link.

| Pasta | Segmento | Destaques |
|---|---|---|
| `aurora-odontologia/` | Clínica odontológica (São Paulo/SP) | Jornada do paciente, fluxo de urgência para dor |
| `vertice-contabilidade/` | Contabilidade digital (Campinas/SP) | Tabela de planos, simulador que qualifica o lead |
| `atelier-lumen/` | Arquitetura e interiores (Curitiba/PR) | Layout editorial, galeria de projetos, briefing guiado |
| `amigo-fiel-vet/` | Clínica veterinária 24h (Belo Horizonte/MG) | Faixa de emergência, identificação de casos graves |
| `studio-equilibrio/` | Pilates e fisioterapia (Florianópolis/SC) | Grade de horários, planos por frequência |

`index.html` (na raiz) é uma vitrine que reúne os 6 projetos, incluindo o Marques & Peixer.

> Todas as empresas, profissionais, preços, telefones e depoimentos são **fictícios** (avisado no rodapé de cada site).
> Fotos: [Unsplash](https://unsplash.com/license), carregadas direto da CDN do Unsplash.

## Personalizar um site

No fim de cada `index.html` há um bloco `window.SITE`:

- `wa` / `waDisplay` — número do WhatsApp. Hoje são números fictícios (`90000-000X`); troque pelo seu para que
  quem testar o portfólio consiga enviar a mensagem de verdade.
- `web3formsKey` — cole uma chave do [web3forms.com](https://web3forms.com) para receber o formulário e o
  assistente por e-mail. Vazio = tudo vai pelo WhatsApp.
- `bot.steps` — perguntas do assistente. Cada opção pode ter `then` (sub-perguntas), `urgent`, `alert` e
  `urgentWa` (botão de WhatsApp imediato).

Também vale ajustar `og:url` e `og:image` no `<head>` depois de publicar.

## Assistente compartilhado

O motor do assistente e do formulário é o mesmo nos 5 sites e fica em `_ferramentas/assistente.html`.
Para alterar todos de uma vez, edite esse arquivo e rode:

```bash
python _ferramentas/montar.py
```

O script reinsere o motor em cada `index.html` e regenera as páginas `privacidade.html`.

## Publicar na Vercel

Cada pasta é um site estático independente: crie um projeto na Vercel apontando para a pasta
(Root Directory) ou publique a raiz inteira para ter a vitrine em `/` e cada site em `/<pasta>/`.

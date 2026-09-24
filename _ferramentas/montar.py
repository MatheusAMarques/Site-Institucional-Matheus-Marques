"""Monta os sites do portfolio.

Uso:  python _ferramentas/montar.py            (todos os sites)
      python _ferramentas/montar.py atelier-lumen

- Copia o motor do assistente virtual (_ferramentas/assistente.html) para dentro
  de cada index.html, substituindo a versao anterior.
- Gera a privacidade.html de cada site a partir dos dados abaixo.
"""
import pathlib, sys, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
ENGINE = (pathlib.Path(__file__).parent / "assistente.html").read_text(encoding="utf-8")
MARK = "<!-- @@ENGINE@@ -->"

# Dados de cada site para a página de privacidade
SITES = {
    "aurora-odontologia": dict(
        nome="Aurora Odontologia", curto="Aurora", dark="#0B3B3C", accent="#237565", bg="#F7FBFA", line="#DCEBE7",
        ft="DM+Serif+Display", fb="Manrope", fts='"DM Serif Display"', fbs="Manrope", tw="400", tl="letter-spacing:0",
        email="contato@auroraodontologia.com.br", end="Av. Ibirapuera, 2120, conj. 81 – Moema – São Paulo/SP – CEP 04028-001", wa="(11) 90000-0001",
        dados="nome, e-mail, telefone, tratamento de interesse, período preferido e as informações que você escrever na mensagem",
        uso="agendar consultas, responder às suas dúvidas e, havendo atendimento, prestar os serviços odontológicos",
        sigilo=("Sigilo profissional", "Todas as informações de saúde recebidas são tratadas com sigilo, conforme o Código de Ética Odontológica, e o prontuário clínico é mantido pelo prazo exigido pelo Conselho Federal de Odontologia."),
        icon=("A", "#7DD3C0", "16")),
    "vertice-contabilidade": dict(
        nome="Vértice Contabilidade", curto="Vértice", dark="#0E2A22", accent="#3B7A1E", bg="#F6F7F2", line="#E3E6DA",
        ft="Space+Grotesk", fb="Inter", fts='"Space Grotesk"', fbs="Inter", tw="700", tl="letter-spacing:-.02em",
        email="ola@verticecontabil.com.br", end="Rua Barão de Jaguara, 1481, 9º andar – Centro – Campinas/SP – CEP 13015-002", wa="(19) 90000-0002",
        dados="nome, e-mail, telefone, cidade, tipo de empresa, faixa de faturamento e as informações que você escrever na mensagem",
        uso="preparar propostas, responder às suas dúvidas e, havendo contratação, prestar os serviços contábeis",
        sigilo=("Sigilo profissional", "As informações recebidas são protegidas pelo sigilo profissional previsto no Código de Ética Profissional do Contador."),
        icon=("V", "#C6F432", "12")),
    "atelier-lumen": dict(
        nome="Atelier Lumen Arquitetura", curto="Atelier Lumen", dark="#1F1C1A", accent="#B4552F", bg="#F3EEE7", line="#E4DBCF",
        ft="Cormorant+Garamond", fb="Jost", fts='"Cormorant Garamond"', fbs="Jost", tw="600", tl="letter-spacing:0",
        email="projetos@atelierlumen.arq.br", end="Rua Comendador Araújo, 510, sala 1203 – Batel – Curitiba/PR – CEP 80420-000", wa="(41) 90000-0003",
        dados="nome, e-mail, telefone, cidade, tipo de projeto, metragem aproximada, faixa de investimento e as informações que você escrever na mensagem",
        uso="preparar propostas de projeto, agendar reuniões e, havendo contratação, desenvolver os serviços de arquitetura e interiores",
        sigilo=("Confidencialidade", "Plantas, fotos e informações sobre o seu imóvel são usadas exclusivamente para o seu projeto e não são divulgadas sem sua autorização expressa."),
        icon=("L", "#E9A27F", "4")),
    "amigo-fiel-vet": dict(
        nome="Amigo Fiel Clínica Veterinária", curto="Amigo Fiel", dark="#2E1A47", accent="#C4600C", bg="#FFF8EF", line="#F1E4D3",
        ft="Fraunces", fb="Nunito", fts="Fraunces", fbs="Nunito", tw="700", tl="letter-spacing:0",
        email="atendimento@amigofielvet.com.br", end="Rua Pernambuco, 1322 – Savassi – Belo Horizonte/MG – CEP 30130-151", wa="(31) 90000-0004",
        dados="seu nome, telefone, e-mail e bairro, além do nome, espécie e informações de saúde do seu animal que você escrever na mensagem",
        uso="agendar consultas, orientar atendimentos de urgência e, havendo atendimento, prestar os serviços veterinários",
        sigilo=("Sigilo profissional", "As informações recebidas são tratadas com sigilo, conforme o Código de Ética do Médico-Veterinário, e o prontuário do seu animal é mantido pelo prazo exigido pelo CFMV."),
        icon=("A", "#F28C28", "32")),
    "studio-equilibrio": dict(
        nome="Studio Equilíbrio Pilates & Fisioterapia", curto="Studio Equilíbrio", dark="#2F3A2C", accent="#8A5A3C", bg="#F5F1EA", line="#E5DED1",
        ft="Lora", fb="Outfit", fts="Lora", fbs="Outfit", tw="600", tl="letter-spacing:0",
        email="ola@studioequilibrio.com.br", end="Rua Bocaiúva, 2080 – Centro – Florianópolis/SC – CEP 88015-530", wa="(48) 90000-0005",
        dados="nome, e-mail, telefone, objetivo, histórico de dores ou lesões informado por você, horário preferido e as informações que você escrever na mensagem",
        uso="agendar a aula experimental ou avaliação, indicar a modalidade adequada e, havendo matrícula, prestar os serviços de pilates e fisioterapia",
        sigilo=("Sigilo profissional", "Informações sobre sua saúde são tratadas com sigilo, conforme o Código de Ética da Fisioterapia (COFFITO), e usadas apenas pela equipe responsável pelo seu atendimento."),
        icon=("E", "#C9D6B8", "32")),
}

PRIV = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Política de Privacidade | {nome_h}</title>
<meta name="robots" content="noindex">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='{ir}' fill='%23{dark_u}'/%3E%3Ctext x='32' y='43' text-anchor='middle' font-family='Georgia,serif' font-size='30' fill='%23{ic_u}'%3E{il}%3C/text%3E%3C/svg%3E">
<link href="https://fonts.googleapis.com/css2?family={ft}:wght@{tw}&amp;family={fb}:wght@400;600&amp;display=swap" rel="stylesheet">
<style>
  :root {{ --dark: {dark}; --accent: {accent}; --text: #3f4a4a; --line: {line}; --bg: {bg}; }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--bg); color: var(--text); font-family: {fbs}, system-ui, sans-serif; line-height: 1.7; }}
  header {{ background: #fff; border-bottom: 1px solid var(--line); padding: 1.5rem 1rem; }}
  header a {{ font-family: {fts}, Georgia, serif; color: var(--dark); font-weight: {tw}; font-size: 1.25rem; text-decoration: none; {tl}; }}
  main {{ max-width: 46rem; margin: 0 auto; padding: 3rem 1.25rem 5rem; }}
  h1 {{ font-family: {fts}, Georgia, serif; font-weight: {tw}; color: var(--dark); font-size: clamp(1.8rem, 5vw, 2.6rem); line-height: 1.2; margin: 0 0 .5rem; {tl}; }}
  h2 {{ font-family: {fts}, Georgia, serif; font-weight: {tw}; color: var(--dark); font-size: 1.3rem; margin: 2.5rem 0 .5rem; {tl}; }}
  .data {{ color: var(--accent); font-weight: 600; font-size: .85rem; margin-bottom: 2rem; }}
  a {{ color: var(--accent); }}
  .voltar {{ display: inline-block; margin-top: 3rem; font-weight: 600; }}
  .header-inner {{ max-width: 46rem; margin: 0 auto; }}
  .aviso {{ margin-top: 3rem; font-size: .75rem; color: #94a3b8; }}
</style>
</head>
<body>
<header><div class="header-inner"><a href="index.html">{curto_h}</a></div></header>
<main>
<h1>Política de Privacidade</h1>
<p class="data">Última atualização: setembro de 2026</p>

<p>Esta política explica como {nome_h} trata os dados pessoais das pessoas que acessam este site e entram em contato conosco, em conformidade com a Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018 – LGPD).</p>

<h2>Quais dados coletamos</h2>
<p>Coletamos apenas os dados que você nos fornece voluntariamente ao entrar em contato: {dados}. O assistente virtual não armazena suas respostas no site: elas só são transmitidas quando você confirma o envio. Para entender quantas pessoas visitam o site, usamos uma ferramenta de estatísticas (Vercel Web Analytics) que conta visitas de forma agregada e anônima, sem cookies e sem identificar quem você é. Este site não utiliza cookies de rastreamento nem ferramentas de publicidade.</p>

<h2>Para que usamos os dados</h2>
<p>Os dados são utilizados exclusivamente para {uso}. Não vendemos, alugamos nem compartilhamos seus dados com terceiros para fins comerciais.</p>

<h2>Como o contato é enviado</h2>
<p>As mensagens enviadas pelo formulário ou pelo assistente virtual podem ser encaminhadas ao nosso e-mail por meio do Web3Forms, um serviço de envio de formulários que apenas transmite a mensagem. Se você optar por enviar pelo WhatsApp, o tratamento dos dados segue também a política de privacidade do próprio WhatsApp.</p>

<h2>{sig_t}</h2>
<p>{sig_p}</p>

<h2>Por quanto tempo guardamos</h2>
<p>Os dados são mantidos pelo tempo necessário para atender à sua solicitação e cumprir obrigações legais aplicáveis, sendo descartados de forma segura após esse período.</p>

<h2>Seus direitos</h2>
<p>Você pode, a qualquer momento, solicitar confirmação da existência de tratamento, acesso, correção, anonimização ou eliminação dos seus dados, bem como revogar seu consentimento. Para isso, escreva para <a href="mailto:{email}">{email}</a>.</p>

<h2>Contato</h2>
<p>{nome_h}<br>
{end_h}<br>
WhatsApp: {wa}</p>

<a class="voltar" href="index.html">← Voltar ao site</a>
<p class="aviso">Projeto conceitual de portfólio — empresa e dados de contato fictícios.</p>
</main>
</body>
</html>
"""

only = sys.argv[1:] or list(SITES)
for slug in only:
    d = SITES[slug]
    folder = ROOT / slug
    idx = folder / "index.html"
    src = idx.read_text(encoding="utf-8")
    START, END = "ASSISTENTE VIRTUAL + FORMULÁRIO (motor compartilhado)", "<!-- FIM: assistente virtual + formulário -->"
    if MARK in src:
        src = src.replace(MARK, ENGINE.strip())
    elif START in src and END in src:
        a = src.rindex("<!--", 0, src.index(START)); b = src.index(END) + len(END)
        src = src[:a] + ENGINE.strip() + src[b:]
    else:
        raise SystemExit(slug + ": marker not found")
    idx.write_text(src, encoding="utf-8")
    print(slug, "engine injected")
    il, ic, ir = d["icon"]
    priv = PRIV.format(
        nome_h=html.escape(d["nome"]), curto_h=html.escape(d["curto"]), end_h=html.escape(d["end"]),
        dark_u=d["dark"][1:], ic_u=ic[1:], il=il, ir=ir, sig_t=d["sigilo"][0], sig_p=d["sigilo"][1], **d)
    (folder / "privacidade.html").write_text(priv, encoding="utf-8")
    print(slug, "privacidade.html ok")

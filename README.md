# ThermalEquity

Dashboard web que monitora a desigualdade térmica urbana em São Paulo, usando dados inspirados em imagens satelitais do Landsat (NASA).

Desenvolvido para a **FIAP Global Solution 2026** — Engenharia de Software 4º Ano.

---

## O problema

Favelas em São Paulo são até **15°C mais quentes** que bairros ricos vizinhos. Heliópolis chega a 44°C de temperatura de superfície enquanto Alphaville registra 28°C. Essa desigualdade é invisível para gestores públicos e não entra em nenhuma política habitacional.

**ODS relacionados:** ODS 10 (Redução de Desigualdades) · ODS 11 (Cidades Sustentáveis) · ODS 13 (Ação Climática)

---

## Stack

- **Backend:** Python 3.11 + Flask
- **Deploy:** Azure App Service
- **CI/CD:** GitHub Actions
- **Segurança:** Azure Key Vault + GitHub Secrets + IAM
- **Monitoramento:** Azure Application Insights

---

## Como rodar localmente

**1. Instalar dependências:**
```bash
py -m pip install flask
```

**2. Iniciar o servidor:**
```bash
py -m flask run
```

**3. Acessar:** http://localhost:5000

---

## Estrutura do projeto

```
thermalequity/
├── app.py                  # Aplicação Flask principal
├── requirements.txt        # Dependências (flask, gunicorn)
├── startup.txt             # Comando de inicialização no Azure
├── templates/
│   └── index.html          # Dashboard HTML
├── static/
│   └── style.css           # Estilos (tema escuro)
└── .github/
    └── workflows/
        └── deploy.yml      # Pipeline CI/CD para o Azure
```

---

## API Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Dashboard principal |
| GET | `/api/bairros` | Lista todos os bairros com dados de temperatura |
| GET | `/api/bairros/<nome>` | Dados de um bairro específico (nome com acento) |
| GET | `/health` | Status da aplicação |

**Exemplo:**
```
GET /api/bairros/Heliópolis

{
  "nome": "Heliópolis",
  "zona": "Sul",
  "temp_media": 44.2,
  "veg_pct": 8,
  "renda_media": 1200,
  "risco": "crítico"
}
```

---

## Deploy no Azure

O deploy é automático via GitHub Actions a cada `push` na branch `main`. Requer o secret `AZURE_WEBAPP_PUBLISH_PROFILE` configurado no repositório.

App Service: `https://thermalequity-app.azurewebsites.net`

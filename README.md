# 🧱 SDET Python Automation Core

Framework **core reutilizável** para automação de testes, projetado para cenários **SDET / QA Automation Engineering**, com foco em **arquitetura limpa, desacoplamento e reuso**.

Este projeto é consumido via **pip** por projetos de automação (ex: Robot Framework), sem cópia de código ou dependência manual.

---

## 🎯 Objetivo

Este framework tem como objetivo:

* Centralizar lógica técnica de automação (HTTP, contexto, configurações)
* Expor **libraries reutilizáveis** para ferramentas de teste
* Suportar projetos Robot Framework desacoplados
* Permitir versionamento e releases independentes
* Servir como base para automação de API e integrações futuras

---

## 🏗 Arquitetura do Framework

![Arquitetura do Automation Core](docs/architecture-diagram.png)

Este projeto representa o **core reutilizável de automação**, desacoplado de qualquer ferramenta de execução,
permitindo integração com Robot Framework, Pytest ou outros consumidores.

## 🧱 Arquitetura

```text
sdet-python-automation-core
│
├── src/
│   └── sdet_python_automation_core/
│       ├── core/
│       │   └── context/
│       │       └── execution_context.py
│       │
│       ├── services/
│       │   └── http/
│       │       ├── http_client.py
│       │       └── http_response.py
│       │
│       ├── libraries/
│       │   └── base_library.py
│       │
│       └── __init__.py
│
├── pyproject.toml
└── README.md
```

### 🔗 Responsabilidades por camada

| Camada      | Responsabilidade                                |
| ----------- | ----------------------------------------------- |
| `services`  | Implementação técnica (HTTP, integrações)       |
| `core`      | Contexto e controle de estado de execução       |
| `libraries` | Exposição de keywords para ferramentas de teste |

---

## 🌐 HttpClient

O `HttpClient` encapsula o uso do `requests` e fornece:

* Session reutilizável
* Retry automático (5xx)
* Timeout configurável
* Abstração de resposta (`HttpResponse`)

```python
client = HttpClient(base_url="https://api.example.com")
response = client.get("/health")
```

---

## 🤖 Integração com Robot Framework

A integração ocorre através da **BaseLibrary**, que expõe keywords reutilizáveis:

```robot
Create HTTP Client    https://api.example.com
GET                   /users
Status Should Be      200
```

A library mantém estado interno através do `ExecutionContext`, garantindo controle sobre:

* Cliente HTTP ativo
* Última resposta
* Expansão futura (auth, headers, ambientes)

---

## 📦 Instalação

### Via pip (GitHub)

```bash
pip install git+https://github.com/rftrombeta/sdet-python-automation-core.git@v0.0.1
```

### Durante desenvolvimento

```bash
pip install -e .
```

---

## 🔖 Versionamento

Este projeto segue **Semantic Versioning**:

```text
MAJOR.MINOR.PATCH
```

* `main` → versões estáveis
* `develop` → desenvolvimento contínuo

Releases são criadas via **GitHub Tags**.

---

## 🔗 Projetos que utilizam este core

* **SDET Robot Automation Project**
  [https://github.com/rftrombeta/sdet-robot-automation-project](https://github.com/rftrombeta/sdet-robot-automation-project)

---

## 🧠 Conceitos aplicados

* SDET Architecture
* Framework desacoplado
* Core versionado e reutilizável
* Integração via pip
* Separação entre testes e implementação

---

## 👤 Autor

**Rodrigo Trombeta**
QA SDET • Automação • IA

* LinkedIn: [https://www.linkedin.com/in/rodrigo-trombeta-21b89252](https://www.linkedin.com/in/rodrigo-trombeta-21b89252)
* GitHub: [https://github.com/rftrombeta](https://github.com/rftrombeta)

---

## 🚀 Próximos passos

* Config Loader (YAML + ENV)
* Autenticação (Bearer / OAuth)
* Logging estruturado
* Validações JSON como keywords

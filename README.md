# sdet-python-automation-core

Core reutilizável de automação para projetos SDET, desenvolvido em Python e
distribuído como pacote pip.  
Este projeto concentra regras de negócio, serviços, clientes HTTP e utilidades
que podem ser consumidas por diferentes frameworks de teste, como Robot Framework,
Pytest ou Playwright.

---

## 🎯 Objetivo

Separar a **orquestração de testes** da **implementação técnica**, permitindo:

- Reutilização entre múltiplos projetos
- Versionamento controlado
- Evolução independente do framework de testes
- Arquitetura limpa e desacoplada

---

## 🧱 Arquitetura

![Arquitetura de Automação SDET](docs/architecture-diagram.png)

### Visão geral

- **Automation Core**  
  Camada responsável por toda a lógica técnica e integração com serviços externos.

- **Services**
  Implementações reutilizáveis (HTTP Client, Response, validações, etc).

- **Config**
  Centralização de configurações e variáveis de ambiente.

- **Libraries**
  Pontes para frameworks de teste (ex: Robot Framework).

---

## 📦 Estrutura do projeto

src/
└── sdet_python_automation_core/
├── core/
│ └── config/
├── services/
│ └── http/
│ ├── http_client.py
│ └── http_response.py
├── libraries/
│ └── base_library.py

---

## 🚀 Instalação

```bash
pip install sdet-python-automation-core

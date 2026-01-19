# SDET Python Automation Core 🧠

Este repositório é o "coração" técnico do ecossistema de automação. Ele foi projetado como uma **Shared Library (Biblioteca Compartilhada)** em Python, focada em fornecer infraestrutura de dados, modelos de contrato e utilitários para projetos de teste.

O objetivo principal desta lib é garantir o **DRY (Don't Repeat Yourself)** e a consistência dos contratos de dados em múltiplos clientes de teste.

---

## 🏗️ Arquitetura e Tecnologias

Diferente de scripts de automação isolados, este projeto segue os padrões modernos de empacotamento Python:

* **Python 3.9+**: Base tecnológica da biblioteca.
* **Pyproject.toml (PEP 621)**: Gestão de dependências e metadados de forma centralizada e moderna, substituindo o antigo `setup.py`.
* **Pydantic**: Utilizado para a criação de **Models** que validam os contratos das APIs, garantindo que os dados trafegados estejam corretos.
* **Faker**: Integração para geração de massa de dados dinâmicos e aleatórios (e-mails, nomes, senhas).
* **Requests**: Cliente base para futuras abstrações de comunicação HTTP.

---

## 📁 Estrutura de Pastas

```text
sdet-python-automation-core/
├── automation_core/         # Pacote principal da biblioteca
│   ├── models/              # Definições de Schemas (Pydantic Models)
│   └── utils/               # Helpers, Faker integration e utilitários
├── pyproject.toml           # Configuração de build e dependências
└── README.md
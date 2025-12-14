# SDET Python Automation Core

Core de automação em Python projetado para ser reutilizável, desacoplado e
consumido por frameworks de testes como Robot Framework, Playwright ou testes
diretos em Python.

Este projeto representa a camada central de uma arquitetura SDET moderna,
onde a lógica técnica de automação não fica acoplada ao framework de testes.

---

## 🧠 Visão Geral da Arquitetura

![Arquitetura de Automação](docs/architecture-diagram.png)

A arquitetura é composta por três camadas principais:

- **Framework de Testes** (ex: Robot Framework)
- **Library de Keywords** (BaseLibrary)
- **Automation Core** (este repositório)

O core é responsável por:
- Comunicação HTTP
- Abstração de respostas
- Configuração centralizada
- Regras técnicas reutilizáveis

---

## 🎯 Objetivos do Projeto

- Separar lógica técnica do framework de testes
- Permitir reutilização entre múltiplos projetos
- Facilitar manutenção e evolução
- Suportar versionamento e distribuição via pip
- Seguir princípios SDET e Clean Architecture

---

## 📁 Estrutura do Projeto

src/
└── sdet_python_automation_core/
├── core/
│ └── config/
│ └── loader.py
├── services/
│ └── http/
│ ├── http_client.py
│ └── http_response.py
├── libraries/
│ └── base_library.py
└── init.py

---

## 📌 Descrição das Camadas

### **core**
Componentes fundamentais do projeto, como carregamento de configurações e
funcionalidades compartilhadas.

### **services**
Implementações técnicas reutilizáveis (ex: comunicação HTTP, parsing de resposta,
futuras integrações).

### **libraries**
Camada exposta para frameworks de testes como Robot Framework, traduzindo
funcionalidades do core em keywords.

---

## ⚙️ Configuração via YAML (Opcional)

O core suporta configuração externa via arquivos YAML para evitar valores
hardcoded no código e facilitar a reutilização entre ambientes.

📌 **O arquivo YAML não faz parte do core**  
📌 Ele normalmente fica no **projeto consumidor** (ex: projeto Robot Framework)

### Exemplo de arquivo YAML

```yaml
http:
  base_url: https://jsonplaceholder.typicode.com
  timeout: 30
  verify_ssl: true
Exemplo de carregamento no código
python
Copy code
from sdet_python_automation_core.core.config.loader import load_config

config = load_config("settings.yaml")
🧪 Testes
Este projeto contém testes unitários para validar os principais componentes do core.

Executar testes
bash
Copy code
pytest
📦 Instalação
Modo desenvolvimento
bash
Copy code
pip install -e .
Uso como dependência em outro projeto
bash
Copy code
pip install git+https://github.com/rftrombeta/sdet-python-automation-core.git@v0.1.0
🤖 Integração com Robot Framework
Este core foi projetado para ser consumido por Robot Framework através de uma
Library Python.

Exemplo de import no Robot Framework:

robot
Copy code
Library    sdet_python_automation_core.libraries.base_library.BaseLibrary
A partir disso, as keywords Python ficam disponíveis para os testes.

🧩 Exemplo de Uso em Python
python
Copy code
from sdet_python_automation_core.services.http.http_client import HttpClient

client = HttpClient(base_url="https://jsonplaceholder.typicode.com")
response = client.get("/posts/1")

print(response.status_code)
print(response.json())
🚀 Roadmap
 Versionamento semântico

 Publicação no PyPI

 Suporte a autenticação (OAuth / JWT)

 Observabilidade e logs

 Integração com outros protocolos

👨‍💻 Autor
Rodrigo Trombeta
QA SDET | Automação | Arquitetura de Testes

LinkedIn: https://www.linkedin.com/in/rodrigo-trombeta-21b89252/
GitHub: https://github.com/rftrombeta
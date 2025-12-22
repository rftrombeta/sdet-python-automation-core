# SDET Python Automation Core 🚀

Este projeto é uma biblioteca core de automação desenvolvida em Python, projetada para ser o motor técnico de projetos de teste. Ela fornece utilitários de rede, gerenciamento de configuração, geradores de massa de dados e integração facilitada com o **Robot Framework**.

## 🛠️ Tecnologias Principais

- **Python 3.9+**
- **Requests:** Comunicação HTTP.
- **PyYAML:** Gestão de configurações por ambiente.
- **Faker:** Geração de massa de dados aleatórios.
- **Robot Framework:** Orquestração de testes (opcional).

---

## 💻 Instalação e Configuração

Siga os passos abaixo para preparar seu ambiente de desenvolvimento após a formatação ou ao clonar o projeto.

### 1. Pré-requisitos

Certifique-se de ter o Python instalado. Verifique no terminal:

```bash
python --version
```

### 2. Criação do Ambiente Virtual (VENV)
Recomendamos o uso de um ambiente isolado para evitar conflitos de dependências:

Bash

# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente (Windows)
.\.venv\Scripts\activate

# Ative o ambiente (Linux/Mac)
source .venv/bin/activate

### 3. Instalação do Projeto
Para desenvolvedores que irão modificar o core, utilize a instalação em modo editável. Isso garante que suas alterações reflitam instantaneamente sem necessidade de reinstalação.

Bash

# Instala as dependências base, de dev e suporte ao Robot
pip install -e ".[dev,robot]"
🏗️ Estrutura do Projeto
O projeto segue uma arquitetura desacoplada:

src/sdet_core/utils: Componentes puros (HTTP Client, Config Loader, Data Generator).

src/sdet_core/services: Lógica de negócio (ex: integração com a API ServeRest).

src/sdet_core/bridge: Adaptadores que expõem as funções como Keywords para o Robot Framework.

🚀 Como Usar
Exemplo em Python Puro
Ideal para scripts utilitários ou integração com Pytest:

Python

from sdet_core.services.serverest_service import ServeRestService

service = ServeRestService()
service.autenticar_e_salvar_sessao("admin@serverest.com.br", "teste")
usuarios = service.listar_usuarios()
Exemplo no Robot Framework
Importe a biblioteca e utilize as keywords semânticas:

Snippet de código

*** Settings ***
Library    sdet_core.bridge.ServeRestKeywords

*** Test Cases ***
Cenário: Listagem de usuários
    Autenticar No Sistema    admin@serverest.com.br    teste
    ${lista}    Obter Lista De Usuarios
⚙️ Configuração de Ambientes
O core utiliza o arquivo config.yaml para alternar entre ambientes. Para mudar o alvo dos testes sem alterar o código, utilize variáveis de ambiente:

Bash

# No terminal antes de rodar os testes
export TEST_ENV=hml  # No Linux/Mac
set TEST_ENV=hml     # No Windows
```

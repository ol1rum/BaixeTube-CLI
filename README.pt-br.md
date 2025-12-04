<div align="center">
  <a href="README.md">🇺🇸 English</a> | <a href="README.pt-br.md">🇧🇷 Português</a>
</div>

<br />

# 🎥 BaixeTube CLI (v2.0)

> Ferramenta de linha de comando (CLI) moderna e interativa para download de vídeos e playlists do YouTube, construída com Python e arquitetura robusta.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![yt-dlp](https://img.shields.io/badge/Core-yt--dlp-red)
![License](https://img.shields.io/badge/License-MIT-green)

## 🧠 Sobre o Projeto

O **BaixeTube** é uma aplicação completa desenvolvida para demonstrar conceitos avançados de engenharia de software, focada em automação de downloads de mídia. Diferente de scripts simples, ele implementa:

* **Arquitetura Orientada a Objetos (OOP):** Separação clara entre Interface (CLI), Regra de Negócio (Downloader) e Persistência (ConfigManager).
* **Interface Interativa (TUI):** Menus navegáveis via teclado (usando `questionary`), eliminando a necessidade de digitar números ou comandos complexos.
* **Persistência de Dados:** Salva as preferências do usuário (pasta de download, qualidade, formato de áudio) em JSON para uso contínuo.

## ✨ Funcionalidades

- [x] **Downloads Inteligentes:** Suporte para Vídeo (MP4) e Áudio (MP3/M4A/WAV).
- [x] **Playlists:** Detecta automaticamente playlists e organiza os downloads em subpastas nomeadas.
- [x] **Metadados:** Adiciona automaticamente capa (thumbnail) e tags aos arquivos de áudio.
- [x] **Qualidade Selecionável:** De 4K a 480p (economia de dados).
- [x] **Configurações Persistentes:** Lembra sua pasta de download e preferências entre sessões.

## 🛠️ Tecnologias Utilizadas

* **Python 3.12**
* **yt-dlp:** O motor de download mais robusto e atualizado do mercado.
* **Questionary:** Para criação de menus CLI profissionais e interativos.
* **Mutagen:** Para manipulação de metadados de áudio.
* **Pathlib:** Para manipulação de caminhos de arquivos compatível com múltiplos sistemas (Windows/Linux/Mac).

## ⚙️ Instalação e Configuração

### Pré-requisitos
Para que o motor de download funcione corretamente, você precisa ter duas ferramentas instaladas no seu sistema e acessíveis via terminal (PATH):

1.  **FFmpeg:** Essencial para converter e unir vídeo/áudio.
2.  **Deno (ou Node.js):** Runtime necessário para o `yt-dlp` contornar as novas proteções do YouTube.

### Passo 1: Instalação das Ferramentas (Windows)
A maneira mais recomendada é usar o **Winget** no PowerShell:

    winget install Gyan.FFmpeg
    winget install DenoLand.Deno

*Reinicie o terminal após a instalação.*

### Passo 2: Instalação do Projeto

1.  Clone este repositório:
    
        git clone https://github.com/ol1rum/BaixeTube-CLI.git
        cd baixetube-cli

2.  Crie um ambiente virtual (recomendado):

        python -m venv venv
        .\venv\Scripts\activate  # No Windows
        # source venv/bin/activate  # No Linux/Mac

3.  Instale as dependências:

        pip install -r requirements.txt

## 🚀 Como Usar

Execute o arquivo principal a partir da raiz do projeto:

    python src/main.py

* **Navegação:** Use as setas `↑` e `↓` do teclado para navegar nos menus.
* **Seleção:** Pressione `Enter` para confirmar.
* **Configuração:** Acesse o menu de configurações na primeira execução para definir sua pasta de downloads preferida.

## ⚠️ Aviso Legal

Este software foi desenvolvido estritamente para **fins educacionais** (estudo de automação, manipulação de streams e interfaces CLI).
O usuário é o único responsável pelo respeito aos Termos de Serviço do YouTube e às leis de direitos autorais. Não utilize esta ferramenta para pirataria ou distribuição ilegal de conteúdo.

---
Desenvolvido por Murilo
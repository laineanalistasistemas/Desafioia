# -*- coding: utf-8 -*-
"""
Natural ou Fake Natty? - Projeto DIO
Arquivo principal para listar e salvar os conteúdos do desafio.
"""

import os
import typer
from rich.console import Console
from rich.table import Table

# Prompts e texto exemplo
PROMPTS = {
    "texto": (
        "Ele acorda às 5h, toma o pré-treino e segue para a academia. "
        "A rotina parece comum: alongamento, aquecimento e exercícios compostos. "
        "Mas cada detalhe foi criado por IA—do suor na pele à respiração entre séries. "
        "Natural ou Fake Natty?"
    ),
    "imagem": (
        "Um fisiculturista hiper-realista em uma academia moderna, luz dramática destacando músculos definidos, "
        "suor brilhando na pele, expressão determinada, estilo fotográfico 8K, ultra-detalhado, realismo cinematográfico."
    ),
    "audio": (
        "Narrador com voz firme e natural descrevendo a rotina do atleta: "
        "acorda às 5h, toma pré-treino, treina com foco em compostos, "
        "pausas controladas e técnica impecável. Tom inspirador, sem exageros, "
        "cadência de 110–120 palavras por minuto."
    ),
    "video": (
        "Clipe curto (10–15s) mostrando sequência de treino em academia moderna: "
        "entrada, aquecimento, execução de supino e remada, closes nos músculos com luz dramática, "
        "estilo cinematográfico, cores neutras, granulação leve. Transições suaves, câmera levemente "
        "na mão para realismo controlado."
    ),
}

app = typer.Typer(help="Natural ou Fake Natty? - Kit de prompts e conteúdo exemplo")
console = Console()

@app.command()
def listar():
    """
    Lista todos os prompts e o texto exemplo.
    """
    table = Table(title="Prompts e Conteúdo - Natural ou Fake Natty?")
    table.add_column("Tipo", style="cyan", no_wrap=True)
    table.add_column("Conteúdo", style="white")

    for tipo, conteudo in PROMPTS.items():
        table.add_row(tipo, conteudo)

    console.print(table)

@app.command()
def salvar(dest: str = typer.Option("./content", help="Diretório de saída")):
    """
    Salva os prompts e o texto exemplo em arquivos dentro do diretório especificado.
    """
    os.makedirs(dest, exist_ok=True)
    for tipo, conteudo in PROMPTS.items():
        fname = f"{tipo}_prompt.txt" if tipo != "texto" else "texto_exemplo.md"
        path = os.path.join(dest, fname)
        with open(path, "w", encoding="utf-8") as f:
            f.write(conteudo)
    console.print(f"[green]Arquivos salvos em[/green] {dest}")

if __name__ == "__main__":
    app()

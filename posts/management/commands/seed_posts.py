# -*- coding: utf-8 -*-
"""Popula o banco com muitos posts longos e tematicamente diversos.

Voltado a modelagem/testes de busca semantica: gera artigos extensos
(~1500-2500 palavras) agrupados por categoria, recombinando uma biblioteca
de conteudo real (``_seed_data.py``).

Exemplos:
    python manage.py seed_posts
    python manage.py seed_posts --per-category 30 --min-words 1500 --max-words 2500
    python manage.py seed_posts --clear            # apaga posts do autor de seed antes
    python manage.py seed_posts --per-category 10 --author blogbot
"""

import random
import re
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from categories.models import Category
from posts.models import Post

from ._seed_data import (
    CATEGORIES,
    CONCLUSION_FRAMES,
    CONNECTORS,
    ELABORATIONS,
    INTRO_FRAMES,
    TITLE_ANGLES,
    TITLE_STYLES,
)


def cap(text):
    """Capitaliza apenas o primeiro caractere, preservando o resto."""
    return text[:1].upper() + text[1:] if text else text


# Contracoes preposicao + artigo (de/em + o/a/os/as). Como os nomes de tema
# comecam com artigo, molduras como "de {tema}" gerariam "de o ..." (errado).
_CONTRACTIONS = [
    (re.compile(r"\bde o\b"), "do"), (re.compile(r"\bde a\b"), "da"),
    (re.compile(r"\bde os\b"), "dos"), (re.compile(r"\bde as\b"), "das"),
    (re.compile(r"\bem o\b"), "no"), (re.compile(r"\bem a\b"), "na"),
    (re.compile(r"\bem os\b"), "nos"), (re.compile(r"\bem as\b"), "nas"),
    (re.compile(r"\bDe o\b"), "Do"), (re.compile(r"\bDe a\b"), "Da"),
    (re.compile(r"\bEm o\b"), "No"), (re.compile(r"\bEm a\b"), "Na"),
]


def fix_contractions(text):
    for pattern, repl in _CONTRACTIONS:
        text = pattern.sub(repl, text)
    return text


def word_count(parts):
    return len(" ".join(parts).split())


def _paragraph(rng, facts):
    """Monta um paragrafo encadeando fatos com conectores e uma elaboracao."""
    sentences = []
    for idx, fact in enumerate(facts):
        sentence = fact
        if idx > 0 and rng.random() < 0.45:
            connector = rng.choice(CONNECTORS)
            sentence = connector + " " + sentence[:1].lower() + sentence[1:]
        sentences.append(sentence)
    paragraph = " ".join(sentences)
    if rng.random() < 0.7:
        paragraph += " " + rng.choice(ELABORATIONS)
    return paragraph


def build_paragraphs(rng, theme, n_paragraphs=2):
    """Gera 1 ou 2 paragrafos a partir dos fatos de um tema (sem repetir fato)."""
    facts = theme["facts"][:]
    rng.shuffle(facts)
    if n_paragraphs <= 1 or len(facts) < 4:
        return [_paragraph(rng, facts)]
    mid = (len(facts) + 1) // 2
    groups = [facts[:mid], facts[mid:]]
    return [_paragraph(rng, group) for group in groups if group]


def make_title(rng, theme, used_titles):
    """Cria um titulo unico e legivel para o tema."""
    name = theme["name"]
    for _ in range(25):
        base = cap(rng.choice(TITLE_STYLES).format(tema=name, categoria=""))
        # Evita dois-pontos duplicado quando o estilo ja traz um sufixo com ":".
        angle = "" if ":" in base else rng.choice(TITLE_ANGLES)
        title = fix_contractions((base + angle).strip())
        if title not in used_titles and len(title) <= 255:
            used_titles.add(title)
            return title
    # fallback: garante unicidade com sufixo numerico
    n = 2
    base = fix_contractions(cap(rng.choice(TITLE_STYLES).format(tema=name, categoria="")))
    while True:
        title = f"{base} (parte {n})"[:255]
        if title not in used_titles:
            used_titles.add(title)
            return title
        n += 1


def build_post(rng, category_name, themes, main_idx, target_words, used_titles):
    """Monta um artigo longo com tema principal + secoes relacionadas."""
    main = themes[main_idx]
    parts = []

    parts.append(cap(rng.choice(INTRO_FRAMES).format(tema=main["name"], categoria=category_name)))
    parts.append(main["lead"])
    parts.append("## " + cap(main["name"]))
    parts.extend(build_paragraphs(rng, main, n_paragraphs=2))

    others = [t for i, t in enumerate(themes) if i != main_idx]
    rng.shuffle(others)
    queue = list(others)
    guard = 0

    while word_count(parts) < target_words and guard < 40:
        guard += 1
        if queue:
            theme = queue.pop(0)
            remaining = target_words - word_count(parts)
            n_par = 2 if remaining > 300 else 1
            parts.append("## " + cap(theme["name"]))
            parts.append(theme["lead"])
            parts.extend(build_paragraphs(rng, theme, n_paragraphs=n_par))
        else:
            theme = rng.choice(others) if others else main
            parts.append("## Aprofundando: " + cap(theme["name"]))
            parts.extend(build_paragraphs(rng, theme, n_paragraphs=2))

    parts.append("## Consideracoes finais")
    parts.append(cap(rng.choice(CONCLUSION_FRAMES).format(tema=main["name"], categoria=category_name)))

    title = make_title(rng, main, used_titles)
    subtitle = rng.choice(main["subtitles"])
    text = fix_contractions("\n\n".join(parts))
    return title, subtitle, text


class Command(BaseCommand):
    help = "Popula o banco com muitos posts longos e diversos (para busca semantica)."

    def add_arguments(self, parser):
        parser.add_argument("--per-category", type=int, default=30,
                            help="Quantidade de posts por categoria (padrao: 30).")
        parser.add_argument("--min-words", type=int, default=1500,
                            help="Tamanho minimo do texto em palavras (padrao: 1500).")
        parser.add_argument("--max-words", type=int, default=2500,
                            help="Tamanho maximo do texto em palavras (padrao: 2500).")
        parser.add_argument("--author", type=str, default="seed_author",
                            help="Username do autor dos posts (padrao: seed_author).")
        parser.add_argument("--author-password", type=str, default="seedpass123",
                            help="Senha do autor de seed, caso seja criado.")
        parser.add_argument("--clear", action="store_true",
                            help="Apaga os posts do autor de seed antes de gerar.")
        parser.add_argument("--random-seed", type=int, default=2024,
                            help="Semente do gerador aleatorio (reprodutibilidade).")

    def handle(self, *args, **options):
        per_category = options["per_category"]
        min_words = options["min_words"]
        max_words = max(options["max_words"], min_words)
        rng = random.Random(options["random_seed"])

        User = get_user_model()
        author, created = User.objects.get_or_create(
            username=options["author"],
            defaults={
                "email": f"{options['author']}@seed.local",
                "first_name": "Autor",
                "last_name": "Seed",
            },
        )
        if created:
            author.set_password(options["author_password"])
            author.save()
            self.stdout.write(self.style.SUCCESS(
                f"Autor '{author.username}' criado (senha: {options['author_password']})."
            ))
        else:
            self.stdout.write(f"Usando autor existente '{author.username}'.")

        if options["clear"]:
            deleted, _ = Post.objects.filter(user=author).delete()
            self.stdout.write(self.style.WARNING(f"Removidos {deleted} registros do autor de seed."))

        used_titles = set(Post.objects.values_list("title", flat=True))
        word_stats = []
        created_count = 0

        with transaction.atomic():
            for category_name, themes in CATEGORIES.items():
                # Busca case-insensitive para nao duplicar categorias ja existentes.
                category = Category.objects.filter(name__iexact=category_name).first()
                if category is None:
                    category = Category.objects.create(name=category_name, created_by=author)
                    self.stdout.write(f"Categoria '{category_name}' criada.")

                for i in range(per_category):
                    main_idx = i % len(themes)
                    target = rng.randint(min_words, max_words)
                    title, subtitle, text = build_post(
                        rng, category_name, themes, main_idx, target, used_titles
                    )
                    post = Post.objects.create(
                        title=title[:255],
                        subtitle=subtitle[:255],
                        text=text,
                        user=author,
                        category=category,
                    )
                    # Espalha as datas nos ultimos ~2,5 anos (bypassa auto_now via update()).
                    when = timezone.now() - timedelta(
                        days=rng.randint(0, 900),
                        hours=rng.randint(0, 23),
                        minutes=rng.randint(0, 59),
                    )
                    Post.objects.filter(pk=post.pk).update(created_at=when, updated_at=when)

                    word_stats.append(len(text.split()))
                    created_count += 1

                self.stdout.write(self.style.SUCCESS(
                    f"  {category_name}: {per_category} posts gerados."
                ))

        avg = sum(word_stats) // len(word_stats) if word_stats else 0
        self.stdout.write(self.style.SUCCESS(
            f"\nConcluido: {created_count} posts em {len(CATEGORIES)} categorias.\n"
            f"Palavras por post -> min: {min(word_stats)}, max: {max(word_stats)}, media: {avg}.\n"
            f"Autor: {author.username} | Total de posts no banco: {Post.objects.count()}."
        ))

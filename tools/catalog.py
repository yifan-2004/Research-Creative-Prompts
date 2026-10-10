#!/usr/bin/env python3
"""Validate the source catalog and deterministically build its Markdown pages.

Python 3.10+; standard library only. No network access or model calls.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    'research-literature': ('科研选题与文献', 'Research & literature'),
    'academic-writing': ('论文写作与审稿回复', 'Academic writing'),
    'deep-learning': ('深度学习实验', 'Deep learning'),
    'image-generation': ('图像生成与编辑', 'Image generation'),
    'scientific-figures': ('科研图表与结果展示', 'Scientific figures'),
    'coding-agents': ('编程与个人 Agent', 'Coding & agents'),
    'startup-product': ('创业与产品验证', 'Startup & product'),
    'learning-communication': ('学习与技术表达', 'Learning & communication'),
}
FIELDS = {
    'id', 'category', 'slug', 'title', 'input_variables', 'template',
    'example_input', 'expected_output', 'suitability', 'limitations',
    'provenance', 'verification',
}
TOKEN = re.compile(r'\{\{([a-z][a-z0-9_]*)\}\}')
SLUG = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
VAR = re.compile(r'[a-z][a-z0-9_]*\Z')
LINK = re.compile(r'!?\[[^\]\n]*\]\(([^)\n]+)\)')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_and_validate():
    entries = json.loads((ROOT / 'data/prompts.json').read_text(encoding='utf-8'))
    require(isinstance(entries, list), 'Catalog must be a JSON array')
    require(len(entries) == 120, f'Expected 120 entries, found {len(entries)}')
    ids, titles, templates = set(), set(), set()
    counts = Counter()
    for entry in entries:
        require(isinstance(entry, dict), 'Each entry must be an object')
        require(set(entry) == FIELDS, f'Invalid fields in {entry.get("id", "unknown")}')
        ident = entry['id']
        category = entry['category']
        slug = entry['slug']
        require(category in CATEGORIES, f'{ident}: unknown category')
        require(isinstance(slug, str) and SLUG.fullmatch(slug), f'{ident}: invalid slug')
        require(ident == f'{category}/{slug}', f'{ident}: inconsistent ID')
        require(ident not in ids, f'{ident}: duplicate ID')
        ids.add(ident)
        counts[category] += 1
        for key in ('title', 'template', 'expected_output', 'suitability', 'limitations'):
            require(isinstance(entry[key], str) and entry[key].strip(), f'{ident}: empty {key}')
        require(entry['title'] not in titles, f'{ident}: duplicate title')
        titles.add(entry['title'])
        require(entry['template'] not in templates, f'{ident}: duplicate template')
        templates.add(entry['template'])
        require(len(entry['template']) >= 120, f'{ident}: template too short')
        variables = entry['input_variables']
        require(isinstance(variables, list) and len(variables) >= 2, f'{ident}: missing variables')
        names = set()
        for variable in variables:
            require(set(variable) == {'name', 'description'}, f'{ident}: invalid variable fields')
            name = variable['name']
            require(isinstance(name, str) and VAR.fullmatch(name), f'{ident}: invalid variable name')
            require(name not in names, f'{ident}: duplicate variable')
            names.add(name)
            require(isinstance(variable['description'], str) and variable['description'].strip(),
                    f'{ident}: empty variable description')
        require(set(TOKEN.findall(entry['template'])) == names, f'{ident}: template variable mismatch')
        require(set(entry['example_input']) == names, f'{ident}: example variable mismatch')
        for value in entry['example_input'].values():
            require(isinstance(value, str) and len(value.strip()) >= 2, f'{ident}: incomplete example')
            require('{{' not in value and '}}' not in value, f'{ident}: unresolved example variable')
        require(entry['provenance']['kind'] == 'original', f'{ident}: provenance mismatch')
        require(bool(entry['provenance']['note']), f'{ident}: missing provenance note')
        require(entry['verification']['status'] == 'untested', f'{ident}: unverified status claim')
        require(bool(entry['verification']['note']), f'{ident}: missing verification note')
    require(counts == Counter({category: 15 for category in CATEGORIES}),
            f'Expected 15 per category, found {dict(counts)}')
    return entries


def cell(text):
    return text.replace('|', '\\|').replace('\n', ' ')


def english_label(slug):
    terms = {'3d': '3D', 'api': 'API', 'cli': 'CLI', 'rag': 'RAG', 'mvp': 'MVP'}
    return ' '.join(terms.get(word, word.capitalize()) for word in slug.split('-'))


def generate(entries):
    files = {}
    for category, (zh, en) in CATEGORIES.items():
        selected = [entry for entry in entries if entry['category'] == category]
        rows = '\n'.join(
            f'| {index:02} | [{english_label(entry["slug"])}]({entry["slug"]}.md) |'
            for index, entry in enumerate(selected, 1)
        )
        files[Path('prompts') / category / 'README.md'] = (
            f'# {en}\n\n15 original, Chinese-language templates · All untested with models\n\n'
            '[Back to the main catalog](../../README.md)\n\n'
            'Choose a task, replace each `{{variable}}` with your materials, and copy the template. '
            'Individual prompt pages remain in Chinese and include examples, intended outputs, '
            'scope, limitations and provenance.\n\n'
            '| # | Template |\n| --- | --- |\n' + rows + '\n'
        )
        for entry in selected:
            variables = '\n'.join(
                f'| `{var["name"]}` | {cell(var["description"])} |'
                for var in entry['input_variables']
            )
            example = json.dumps(entry['example_input'], ensure_ascii=False, indent=2)
            files[Path('prompts') / category / (entry['slug'] + '.md')] = (
                f'# {entry["title"]}\n\n'
                f'[分类目录](README.md) · [总目录](../../README.md)\n\n'
                f'ID：`{entry["id"]}`  \n状态：**待验证 / untested**\n\n'
                '## 输入变量\n\n| 变量 | 填写说明 |\n| --- | --- |\n' + variables + '\n\n'
                '## 复制模板\n\n将下方变量替换为你的材料。不要将示例中的演示数据用于真实报告。\n\n'
                f'```text\n{entry["template"]}\n```\n\n'
                f'## 示例输入\n\n```json\n{example}\n```\n\n'
                f'## 预期输出\n\n{entry["expected_output"]}\n\n'
                f'## 适用与边界\n\n{entry["suitability"]}\n\n{entry["limitations"]}\n\n'
                f'## 来源与验证\n\n{entry["provenance"]["note"]}\n\n'
                f'{entry["verification"]["note"]}\n'
            )
    return files


def check_links():
    checked = 0
    for document in sorted(ROOT.rglob('*.md')):
        if any(part in {'.git', 'work'} for part in document.relative_to(ROOT).parts):
            continue
        text = document.read_text(encoding='utf-8')
        # Ignore examples and literal Markdown inside fenced code blocks.
        text = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.MULTILINE | re.DOTALL)
        for raw in LINK.findall(text):
            target = raw.strip().split(' "', 1)[0].strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            path = (document.parent / unquote(parsed.path)).resolve()
            require(path.is_relative_to(ROOT), f'{document}: link leaves repository: {target}')
            require(path.exists(), f'{document}: broken local link: {target}')
            checked += 1
    return checked


def check_english_readmes():
    documents = [ROOT / 'README.md'] + [ROOT / 'prompts' / category / 'README.md'
                                      for category in CATEGORIES]
    for document in documents:
        text = document.read_text(encoding='utf-8')
        require(not re.search(r'[\u3400-\u9fff]', text),
                f'{document}: README must use English; prompt pages may remain Chinese')
    return len(documents)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['build', 'check'])
    args = parser.parse_args()
    entries = load_and_validate()
    outputs = generate(entries)
    if args.command == 'build':
        for relative, text in outputs.items():
            destination = ROOT / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(text, encoding='utf-8')
    else:
        for relative, text in outputs.items():
            destination = ROOT / relative
            require(destination.is_file(), f'Missing generated page: {relative}')
            require(destination.read_text(encoding='utf-8') == text,
                    f'Stale generated page: {relative}; run build')
    expected = {ROOT / relative for relative in outputs}
    actual = set((ROOT / 'prompts').rglob('*.md'))
    require(actual == expected, 'Unexpected or missing generated Markdown pages')
    links = check_links()
    readmes = check_english_readmes()
    print(f'OK: {len(entries)} unique prompts; 8 categories × 15; '
          f'{len(outputs)} generated pages; {links} local links; {readmes} English READMEs; '
          'variables/examples/provenance/status consistent; all prompts untested.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError, json.JSONDecodeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        sys.exit(1)

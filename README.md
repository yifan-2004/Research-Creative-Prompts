# Research & Creative Prompts

**120 original, Chinese-language prompt templates for research, deep learning, image creation, personal agents and product validation.** Each template includes input variables, a complete example, intended output, scope and limitations.

The templates were authored for this collection with AI assistance; they were not copied from external prompt collections. **All templates are untested with models.** Catalog and link validation does not establish output quality. Copy a template into a suitable assistant; file reading, image generation and tool execution depend on your chosen platform.

## Choose a task

| Category | Templates | Suggested starting points |
| --- | --- | --- |
| [Research & literature](prompts/research-literature/README.md) | 15 | [Evidence matrix](prompts/research-literature/evidence-matrix.md), [Research gap validation](prompts/research-literature/gap-validation.md) |
| [Academic writing](prompts/academic-writing/README.md) | 15 | [Evidence-bound abstract](prompts/academic-writing/evidence-bound-abstract.md), [Reviewer response](prompts/academic-writing/reviewer-response.md) |
| [Deep learning](prompts/deep-learning/README.md) | 15 | [Low-light evaluation](prompts/deep-learning/low-light-evaluation.md), [Monocular 3D review](prompts/deep-learning/monocular-3d-review.md) |
| [Image generation](prompts/image-generation/README.md) | 15 | [Product hero image](prompts/image-generation/product-hero.md), [Localized editing](prompts/image-generation/localized-edit.md) |
| [Scientific figures](prompts/scientific-figures/README.md) | 15 | [Architecture specification](prompts/scientific-figures/architecture-spec.md), [3D box visualization](prompts/scientific-figures/3d-box-visualization.md) |
| [Coding & agents](prompts/coding-agents/README.md) | 15 | [Evidence-based knowledge-base answers](prompts/coding-agents/rag-evidence-answer.md), [Personal assistant memory](prompts/coding-agents/personal-assistant-memory.md) |
| [Startup & product](prompts/startup-product/README.md) | 15 | [MVP scope](prompts/startup-product/mvp-scope.md), [User interview guide](prompts/startup-product/interview-guide.md) |
| [Learning & communication](prompts/learning-communication/README.md) | 15 | [Study plan](prompts/learning-communication/study-plan.md), [Project introduction](prompts/learning-communication/project-introduction.md) |

## How to use

1. Open a template and read its scope and limitations.
2. Replace the `{{variables}}` with your real materials. The example input demonstrates what to provide.
3. Copy the complete template and attach any required files or reference images.
4. Review facts, citations, code and results. Keep missing evidence explicit rather than asking the model to invent it.

Prompt bodies, examples and individual prompt pages are in Chinese. Repository and category READMEs are in English. The templates are model-agnostic; use a model and platform that support the task and input language.

For example, the low-light evaluation template asks for your methods, paired or unpaired datasets, and evaluation priorities. It requests separate protocols and avoids full-reference PSNR for unpaired data. This describes the intended behavior; it has not been verified through model runs.

Image-generation templates first ask a text assistant to draft instructions, which can then be passed to an image tool. Editing requires an actual reference image. Network diagrams require the real architecture. Result figures and performance tables require real experimental data.

## Files and maintenance

- [data/prompts.json](data/prompts.json): the content source for all 120 templates, suitable for search or programmatic use.
- [prompts/](prompts/): generated category indexes and individual template pages; edit the JSON to change content.
- [tools/catalog.py](tools/catalog.py): deterministic generation and validation, using Python 3.10+ and the standard library only. No network or model calls.
- [CONTRIBUTING.md](CONTRIBUTING.md): contribution and verification guidance, currently in Chinese.

```bash
python3 tools/catalog.py build
python3 tools/catalog.py check
```

Validation covers category counts, unique IDs/titles/templates, matching variables and examples, provenance, untested status, generated-page consistency, local links and English README text. **It does not evaluate prompt effectiveness.** The current catalog contains eight categories with 15 templates each.

## License and provenance

Original templates, documentation and maintenance scripts are available under the [MIT License](LICENSE). The license does not grant rights to third-party papers, images, datasets, models or trademarks. Example data and fictional references are illustrative, not research evidence. Each entry records its original provenance and untested status.

# <project_name>

Prototype of using [va.landing.ai](https://va.landing.ai) locally with python scripts.

![Version](https://img.shields.io/badge/version-0.0.0-8A2BE2)
[![CodeFactor](https://www.codefactor.io/repository/github/qte77/VisAgent-Proto/badge)](https://www.codefactor.io/repository/github/qte77/VisAgent-Proto)
[![CodeQL](https://github.com/qte77/VisAgent-Proto/actions/workflows/codeql.yaml/badge.svg)](https://github.com/qte77/VisAgent-Proto/actions/workflows/codeql.yaml)
[![ruff](https://github.com/qte77/VisAgent-Proto/actions/workflows/ruff.yaml/badge.svg)](https://github.com/qte77/VisAgent-Proto/actions/workflows/ruff.yaml)
[![pytest](https://github.com/qte77/VisAgent-Proto/actions/workflows/pytest.yaml/badge.svg)](https://github.com/qte77/VisAgent-Proto/actions/workflows/pytest.yaml)
[![Link Checker](https://github.com/qte77/VisAgent-Proto/actions/workflows/links-fail-fast.yaml/badge.svg)](https://github.com/qte77/VisAgent-Proto/actions/workflows/links-fail-fast.yaml)
[![Deploy Docs](https://github.com/qte77/VisAgent-Proto/actions/workflows/generate-deploy-mkdocs-ghpages.yaml/badge.svg)](https://github.com/qte77/VisAgent-Proto/actions/workflows/generate-deploy-mkdocs-ghpages.yaml)
[![vscode.dev](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=vscode.dev&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://vscode.dev/github/qte77/VisAgent-Proto)

## Status

(DRAFT) (WIP) ----> Not fully implemented yet

For version history have a look at the [CHANGELOG](CHANGELOG.md).

## Examples

### Question

```sh
Can you perform object detection to identify the different sections of the conveyor belt system in the image, focusing on distinguishing between straight and curved parts?
```

<img src="assets/images/landing.ai_depositphotos_74665111-stock-photo-metal-roller-conveyor-system.jpg" alt="metal-roller-conveyor-system" title="metal-roller-conveyor-system" width="60%" />

### Answer

```sh
I've analyzed the image and detected the conveyor belt sections. Here are the results: - Curved sections detected: 5 - Straight sections detected: 0 - Total length of curved sections: 1668667.8016 (in pixel units squared) A visualization of the detected sections has been saved as 'conveyor_belt_detection.jpg'. Would you like to see this visualization or do you need any further analysis?

[{'straight_sections_count': 0,
  'curved_sections_count': 5,
  'total_straight_length': 0,
  'total_curved_length': 1668667.8016,
  'visualization_path': 'conveyor_belt_detection.jpg'}]
```

<img src="assets/images/answer-metal-roller-conveyor-system.png" alt="answer-metal-roller-conveyor-system" title="answer-metal-roller-conveyor-system" width="60%" />

### Deployment

This app has been deployed with the above question prompt as task. You can use [the streamlit app on landing.ai](https://qbwc15b-streamlit.sandbox.landing.ai?embed=True) or the following API request.

```sh
curl -X 'POST' \
  'https://qbwc15b-webendpoint.sandbox.landing.ai/inference' \
  -H "Content-Type: application/json" \
  -H 'Authorization: Basic {{your_api_key}}' \
  -d '{ "{{your_param_name}}": "{{image_url}}" }'
```

## Setup

`TODO`

## Usage

`TODO`

## Testing

Run tests using: `pytest tests/`

## Documentation

`TODO`

<!--
- **Project DSL**: See [docs/project_dsl.txt](docs/project_dsl.txt) for a high-level overview of the project structure and functionality.
- **PRD**: See [docs/PRD.md](docs/PRD.md) for detailed product requirements.
-->

### Architecture

`TODO`

<!--
<img src="assets/images/c4-arch.dark.png#gh-dark-mode-only" alt="C4-Arch" title="C4-Arch" width="60%" />
<img src="assets/images/c4-arch.light.png#gh-light-mode-only" alt="C4-Arch" title="C4-Arch" width="60%" />
-->

## Project Structure

```sh
TODO
```
## TODO


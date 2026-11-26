# BizBot

**A modular, multi-tenant business management platform built with Python.**

## Overview

BizBot is an open-source project designed to provide a shared foundation for managing multiple businesses through a modular architecture.

The platform aims to support different business types while keeping common business logic separate from business-specific functionality.

A central design principle is separating user identity from business membership, allowing a single user to be associated with multiple businesses with different roles and permissions.

## Core Concepts

- **Business:** Represents an individual business within the platform.
- **User:** Represents a standalone user identity.
- **Business Membership (Planned):** Connects users to businesses and manages their roles and access.
- **Business Modules (Planned):** Provide functionality specific to different business types.

## Current Implementation

The current development phase includes:

- Business domain model
- User domain model
- UUID-based identifiers
- Input validation
- Activation state management
- Custom domain exceptions
- Localization management
- Persian and English localization infrastructure
- Translation file validation and error handling
- Automated tests using Pytest

## Technology Stack

### Core

- Python 3.12+
- Setuptools
- Python Standard Library

### Development Tools

- Pytest
- Ruff

### Planned Integrations

- SQLite
- Telegram Bot API
- Bale messaging platform

## Project Structure

```text
BIZBOT/
├── src/
│   └── bizbot/
│       ├── __init__.py
│       ├── main.py
│       ├── business.py
│       ├── user.py
│       ├── exceptions/
│       │   ├── __init__.py
│       │   ├── domain.py
│       │   └── localization.py
│       └── localization/
│           ├── __init__.py
│           ├── manager.py
│           └── translations/
│               ├── en.json
│               └── fa.json
├── tests/
│   ├── __init__.py
│   ├── test_business.py
│   ├── test_user.py
│   └── test_manager.py
├── .gitignore
├── pyproject.toml
└── README.md
```

The project follows the `src`-based Python package layout.

## Getting Started

### Requirements

- Python 3.12 or later
- pip

### Installation

Clone the repository:

```bash
git clone https://github.com/sidzi-prog/BIZBOT.git
cd BIZBOT
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the project with development dependencies:

```bash
python -m pip install -e ".[dev]"
```

### Running Tests

Run the test suite:

```bash
python -m pytest -v
```

### Code Quality

Check code quality with Ruff:

```bash
ruff check .
```

Check formatting:

```bash
ruff format --check .
```

## Roadmap

### Core Architecture

- [x] Business domain model
- [x] User domain model
- [x] Input validation
- [x] UUID-based identifiers
- [x] Activation state management
- [x] Custom domain exceptions
- [x] Initial automated test coverage

### Localization and Error Handling

- [x] Localization manager
- [x] Persian and English translation files
- [x] Supported language validation
- [x] Translation file loading
- [x] Translation file error handling
- [x] Missing translation key handling

### Identity and Access Management

- [ ] UserAccount and authentication management
- [ ] UserIdentity for messaging platform integrations
- [ ] BusinessMembership for multi-business relationships
- [ ] Role-Based Access Control (RBAC)
- [ ] Contact information management

### Business Management

- [ ] Customer management
- [ ] Business-specific modules
- [ ] Request and order management
- [ ] Administrative reporting

### Infrastructure and Integrations

- [ ] Database integration
- [ ] SQLite support
- [ ] Telegram integration
- [ ] Bale integration

## Project Status

**Early Development**

BizBot is under active development. The current implementation establishes the initial domain models, custom error handling, localization infrastructure, and automated test foundation.

Planned features and integrations have not yet been implemented.

## License

License information will be added in a future release.

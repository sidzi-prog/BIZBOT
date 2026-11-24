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

The initial development phase includes:

- Business domain model
- User domain model
- UUID-based identifiers
- Basic input validation
- Activation state management
- Initial automated tests using Pytest

## Technology Stack

- Python 3.12+
- Setuptools
- Pytest

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
│       └── user.py
├── tests/
│   ├── __init__.py
│   ├── test_business.py
│   └── test_user.py
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

## Roadmap

### Core Architecture

- [x] Business domain model
- [x] User domain model
- [x] Initial input validation
- [x] UUID-based identifiers
- [x] Basic activation state management
- [x] Initial Pytest coverage

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

BizBot is under active development. The current version establishes the initial domain models and project structure. Planned features and integrations have not yet been implemented.

## License

License information will be added in a future release.

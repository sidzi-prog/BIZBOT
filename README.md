# Sixar

**A Modular Multi-Tenant Marketplace, Business Management, and Customer Relationship Platform**

Sixar is an open-source Python project designed to provide a shared foundation for a multi-tenant platform that connects businesses and customers through a modular architecture.

Sixar combines three complementary capabilities:

- **Marketplace:** A shared environment where customers can discover businesses and their services.
- **Business Management:** A modular platform that enables businesses to manage their profiles, services, and operations.
- **Customer Relationship Management:** A centralized customer experience for managing interactions, requests, notifications, and relationships across businesses.

The project is being developed with a focus on clean architecture, extensibility, maintainability, and long-term scalability.

---

## Core Concepts

### Multi-Tenancy

Each business operates within its own logical environment. Business-specific data and operations are designed to remain isolated from other tenants.

### Centralized User Identity

A user has a platform-level identity and can interact with multiple businesses without requiring a separate platform account for each one.

Business-specific roles and memberships are separate concepts from the user's global identity.

### Modular Architecture

Business functionality is organized into modules.

Default modules are determined by the business type. Additional modules can be requested and enabled after compatibility and conflict validation.

### Business Categories and Types

Business categories and types are managed by the platform.

- Each business type belongs to one business category.
- Platform administrators manage the official categories and types.
- Business owners select from the approved list.
- Users can suggest new business types for platform review.
- Changing an existing business's type requires a review process.

### Localization

Sixar is designed to support Persian and English from the beginning.

- Supported languages: `fa` and `en`
- Platform-managed interface text is localized.
- User language preference determines the language of the interface.
- User-generated content does not require duplicate entries in multiple languages.

---

## Architectural Principles

The project follows these principles:

- Separation of concerns
- Domain-driven design principles
- Explicit domain validation
- Modular and extensible architecture
- Clear separation between platform-level and business-level responsibilities
- UUID-based entity identification
- Maintainable package structure
- Automated testing

The architecture is intended to support future expansion without introducing unnecessary dependencies into the initial core.

---

## Current Implementation

The current implementation establishes the initial domain foundation.

Implemented components include:

- `Business` domain model
- `User` domain model
- UUID-based identifiers
- Domain validation
- Activation state management
- Custom domain exceptions
- Localization infrastructure
- Persian and English translation files
- Automated unit tests

The localization infrastructure currently supports `fa` and `en` through JSON translation files.

Missing translation keys raise `KeyError`; implicit fallback behavior is not used.

<text>**Current test status:** 40 passing tests at the latest verified checkpoint.</text>

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12+ | Core programming language |
| pytest | Automated testing |
| Ruff | Code quality and linting |
| JSON | Localization resources |
| Git | Version control |

---

## Project Structure

```text
SIXAR/
│
├── src/
│   └── sixar/
│       ├── __init__.py
│       ├── business.py
│       ├── user.py
│       ├── main.py
│       │
│       ├── exceptions/
│       │   ├── __init__.py
│       │   ├── domain.py
│       │   └── localization.py
│       │
│       └── localization/
│           ├── __init__.py
│           ├── manager.py
│           └── translations/
│               ├── en.json
│               └── fa.json
│
├── tests/
│   ├── test_business.py
│   ├── test_domain.py
│   ├── test_manager.py
│   └── test_user.py
│
├── .gitignore
├── pyproject.toml
└── README.md
```

---

## Getting Started

### Requirements

- Python 3.12 or newer
- Git

### Clone the Repository

```bash
git clone https://github.com/sidzi-prog/SIXAR.git
cd SIXAR
```

### Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate it:

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows**

```powershell
.venv\Scripts\activate
```

### Install the Project

```bash
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
```

### Run Ruff

```bash
ruff check .
```

---

## Roadmap

Sixar is under active development. The roadmap is organized around establishing a reliable domain foundation before expanding into application-level functionality.

### Core Domain

- [x] Initial Business model
- [x] Initial User model
- [x] Domain exception handling
- [x] Localization infrastructure
- [ ] BusinessCategory model
- [ ] BusinessType model
- [ ] BusinessTypeSuggestion model
- [ ] Business model integration with business categories and types

### Business Management

- [ ] Business membership and role management
- [ ] Business module management
- [ ] Module compatibility validation
- [ ] Business profile and service management

### Marketplace

- [ ] Public business discovery
- [ ] Business search and filtering
- [ ] Location-based business discovery
- [ ] Direct business access links

### Customer Relationships

- [ ] Centralized customer interaction history
- [ ] Customer requests
- [ ] Notification infrastructure
- [ ] Customer relationship features

### Platform Infrastructure

- [ ] Authentication and authorization
- [ ] Persistent storage
- [ ] API layer
- [ ] Application interfaces
- [ ] Payment infrastructure
- [ ] Internationalization and regional configuration

---

## Project Status

Sixar is currently in its early development stage.

The initial domain foundation, localization infrastructure, exception handling, and automated test foundation have been established.

The next development phase focuses on business categories and types, followed by their integration into the existing Business domain model.

Features listed in the roadmap are planned and should not be considered implemented unless explicitly marked as completed.

---

## License

The project license has not yet been finalized.

---

**Sixar — One Platform, Multiple Businesses, Connected Customers.**
